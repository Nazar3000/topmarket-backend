from django.conf import settings
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from users.constants import DOMEN, CALL_BACK, USER_ROLE
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_POCKET = (
        ('BASE', 'Base'),
        ('FULL', 'Full'),
        ('NO', 'No')
    )

    manager = models.ForeignKey(
        'Company',
        on_delete=models.SET_NULL,
        verbose_name=_('Менеджер'),
        null=True, blank=True,
    )

    role = models.CharField(
        max_length=10,
        choices=USER_ROLE,
    )
    user_pocket = models.CharField(
        max_length=10,
        choices=USER_POCKET,
        null=True, blank=True,
        default='BASE',
        verbose_name=_('Пакет услуг')
    )

    first_name = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name=_('Имя')
    )

    last_name = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name=_('Фамилия')
    )

    patronymic = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name=_('Отчество')
    )

    email = models.EmailField(unique=True, null=True, verbose_name=_('Емейл'))
    phone = models.CharField(
        max_length=50,
        null=True, blank=True,
        verbose_name=_('Телефон')
    )
    web_site = models.URLField(
        null=True, blank=True,
        verbose_name=_('Веб сайт (url)'),
    )
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата регистрации'))
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Is the user allowed to have access to the admin',
    )
    is_active = models.BooleanField(
        'active',
        default=False,
        help_text='Is the user account currently active',
    )
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        help_text='150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
        null=True,
        blank=True
    )
    avatar = models.ImageField(blank=True, null=True, upload_to='user_profiles/avatars')

    verified = models.BooleanField(default=False)

    rozetka_username = models.CharField(max_length=128, null=True, blank=True)
    rozetka_password = models.CharField(max_length=512, null=True, blank=True)

    rozetka_old_orders_imported = models.BooleanField(default=False)

    nova_poshta_api_key = models.CharField(max_length=64, null=True, blank=True)

    # Поля для ФОП
    organizational_legal_form_of_the_company = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        verbose_name=_('Организационно-правовая форма предприятия')
    )
    organization = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        verbose_name=_('Организация')
    )
    edpnou = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        verbose_name=_('ЕДРПОУ')
    )
    vat_payer_certificate = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        verbose_name=_('Свидетельства плательщика НДС')
    )
    bank_name = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        verbose_name=_('Название банка')
    )
    mfi = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        verbose_name=_('МФО')
    )
    checking_account = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        verbose_name=_('Рассчетный счет')
    )
    available_products_count = models.PositiveIntegerField(
        default=200
    )  # available products for contractor

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return '{} {}'.format(self.id, self.email)

    def get_full_name(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.patronymic)

    def get_short_name(self):
        return '{}'.format(self.first_name)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__pk = self.pk
        self.__verified = self.verified

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.__pk and self.role == 'PARTNER':
            Company.objects.get_or_create(user_id=self.pk)
            MyStore.objects.get_or_create(user_id=self.pk)

        if not self.__verified and self.verified:
            from_email = settings.DEFAULT_FROM_EMAIL
            message = render_to_string('account_verification_email.html', {
                'domain': settings.HOST_NAME,
            })
            data = {
                'to_emails': [self.email, ],
                'subject': "Ваш аккаунт верифицирован",
                'html_content': message,
            }

            message = Mail(
                from_email=from_email,
                **data
            )

            try:
                sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
                sg.send(message)
            except Exception as e:
                print(e.args)

    @property
    def products_count(self):
        return self.products.count()

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')


class UserNotificationEmail(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='email_notifications')
    new_order = models.BooleanField(default=False, verbose_name=_('Новый заказ (email)'))
    ttn_change = models.BooleanField(default=False, verbose_name=_('Смена ТТН заказа'))
    order_paid = models.BooleanField(default=False, verbose_name=_('Получение счета на оплату'))
    sales_report = models.BooleanField(default=False, verbose_name=_('Уведомление о продажах'))
    new_message = models.BooleanField(default=False, verbose_name=_('Новое сообщение во внутреннем почтовом уведомлении'))
    cancel_order = models.BooleanField(default=False, verbose_name=_('Уведомление об отмене заказа'))

    def __str__(self):
        return '{}'.format(self.user.get_full_name())

    class Meta:
        verbose_name = _('Уведомление пользователя(email)')
        verbose_name_plural = _('Увидемления пользователя(email)')


class UserNotificationPhone(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='phone_notifications')
    new_order = models.BooleanField(default=False, verbose_name=_('Новый заказ (смс)'))

    def __str__(self):
        return '{}'.format(self.user.get_full_name())

    class Meta:
        verbose_name = _('Уведомление пользователя(тел)')
        verbose_name_plural = _('Увидемления пользователя(тел)')


class Company(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name=_('Владецел компании'))

    name = models.CharField(
        max_length=255,
        null=True, blank=True,
        verbose_name=_('Название компании')
    )

    town = models.TextField(
        max_length=30,
        null=True, blank=True,
        verbose_name=_('Город')
    )

    address = models.TextField(
        max_length=40,
        null=True, blank=True,
        verbose_name=_('Адресс')
    )

    url = models.URLField(
        max_length=200,
        null=True, blank=True,
        verbose_name=_('URL-путь')
    )

    working_conditions = models.TextField(
        max_length=100,
        null=True, blank=True,
        verbose_name=_('Условия работы')
    )

    logo = models.ImageField(
        upload_to='users/company/logos',
        null=True, blank=True,
        verbose_name=_('Лого компании'),
    )

    web_site = models.URLField(
        max_length=200,
        null=True, blank=True,
        verbose_name=_('Веб-сайт')
    )

    phone = models.CharField(
        max_length=50,
        null=True, blank=True,
        verbose_name=_('Телефон')
    )

    email = models.EmailField(
        max_length=200,
        null=True, blank=True,
        verbose_name=_('Емейл')
    )

    who_see_contact = models.CharField(
        max_length=200,
        null=True, blank=True,
        verbose_name=_('Кому видны контактные данные?')
    )

    # Тип деятельности для розничной торговли

    is_internet_shop = models.BooleanField(
        verbose_name=_('Интернет магазин'),
        default=False
    )

    is_offline_shop = models.BooleanField(
        verbose_name=_('Оффлайн-магазин'),
        default=False
    )

    retail_network = models.BooleanField(
        verbose_name=_('Розничная сеть'),
        default=False
    )

    # Тип деятельности для оптовой торговли

    distributor = models.BooleanField(
        verbose_name=_('Дистрибьютор'),
        default=False
    )

    manufacturer = models.BooleanField(
        verbose_name=_('Производитель'),
        default=False
    )

    importer = models.BooleanField(
        verbose_name=_('Импортер'),
        default=False
    )

    dealer = models.BooleanField(
        verbose_name=_('Дилер'),
        default=False
    )

    sub_dealer = models.BooleanField(
        verbose_name=_('Субдилер'),
        default=False
    )

    exporter = models.BooleanField(
        verbose_name=_('Експортер'),
        default=False
    )

    official_representative = models.BooleanField(
        verbose_name=_('Официальный представитель'),
        default=False
    )

    # Страница компании

    about_company = models.TextField(
        max_length=500,
        null=True, blank=True,
        verbose_name=_('Информация')
    )

    activity_area = models.ForeignKey(
        'ActivityAreas',
        null=True, blank=True,
        related_name='activity_areas',
        on_delete=models.SET_NULL

        )

    service_industry = models.ForeignKey(
        'ServiceIndustry',
        null=True, blank=True,
        related_name='service_industries',
        on_delete=models.SET_NULL
    )

    company_type = models.ForeignKey(
        'CompanyType',
        null=True, blank=True,
        related_name='company_types',
        on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = _('Компания партнера')
        verbose_name_plural = _('Компании партнеров')

    def __str__(self):
        return '{} {}'.format(self.id, self.name)


class ActivityAreas(models.Model):

    name = models.TextField(
        max_length=1095,
        verbose_name=_('Имя сферы деятельности')
    )

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = _('Сфера деятельности')
        verbose_name_plural = _('Сферы деятельности')


class ServiceIndustry(models.Model):

    name = models.TextField(
        max_length=1095,
        verbose_name=_('Имя сферы услуг')
    )

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = _('Сфера услуг')
        verbose_name_plural = _('Сферы услуг')


class CompanyType(models.Model):

    name = models.TextField(
        max_length=1095,
        verbose_name=_('Тип компании')
    )

    class Meta:
        verbose_name = _('Тип компании')
        verbose_name_plural = _('Типы компаний')


# Документы
class Passport(models.Model):
    company = models.ForeignKey(
        'Company',
        related_name='passports',
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    pass_doc = models.ImageField(
        upload_to='companies/documents/passports',
        null=True, blank=True,
        verbose_name=_('Паспорт')
    )

    class Meta:
        verbose_name = _('Паспорт')
        verbose_name_plural = _('Паспорта')


class UkraineStatistic(models.Model):
    company = models.ForeignKey(
        'Company',
        related_name='ukraine_statistics',
        on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name=_('Компания')
        )
    uk_doc = models.FileField(
        upload_to='companies/documents/uk_statistics',
        null=True, blank=True,
        verbose_name=_('Справка Государственного комитета статистики Украины')
    )

    class Meta:
        verbose_name = _('Статистика (комитет статистики Украины)')
        verbose_name_plural = _('Статистика (комитет статистики Украины)')


class Certificate(models.Model):
    company = models.ForeignKey(
        'Company',
        related_name='certificates',
        on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name=_('Компания')
        )
    cert_doc = models.FileField(
        upload_to='companies/documents/certificates',
        null=True, blank=True,
        verbose_name=_('Свидетельство о регистрации или выписка с ЕГРПОУ')
    )

    class Meta:
        verbose_name = _('Свидетельсво')
        verbose_name_plural = _('Свидетельсва')


class TaxPayer(models.Model):
    company = models.ForeignKey(
        'Company',
        related_name='tax_payers',
        on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name=_('Компания')
        )
    tax_doc = models.FileField(
        upload_to='companies/documents/tax_payers',
        null=True, blank=True,
        verbose_name=_('Справка 4 Учета плательщика налогов')
    )

    class Meta:
        verbose_name = _('Плательщик налогов')
        verbose_name_plural = _('Плательщики налогов')


class PayerRegister(models.Model):
    company = models.ForeignKey(
        'Company',
        related_name='payer_registers',
        on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name=_('Компания')
        )
    payer_reg_doc = models.FileField(
        upload_to='companies/documents/payer_registers',
        null=True, blank=True,
        verbose_name=_('Выписка из реестра плательщиков НДС')
    )

    class Meta:
        verbose_name = _('Регистрация плательщика')
        verbose_name_plural = _('Регистрации плательщиков')


class PayerCertificate(models.Model):
    company = models.ForeignKey(
        'Company',
        related_name='payer_certificates',
        on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name=_('Компания')

    )
    payer_cert_doc = models.FileField(
        upload_to='companies/documents/payer_certificates',
        null=True, blank=True,
        verbose_name=_('Cвидетельство плательщика единого налога')
    )

    class Meta:
        verbose_name = _('Свидетельство плательщика ЕН')
        verbose_name_plural = _('Свидетельства плательщиков ЕН')

# Питч


class CompanyPitch(models.Model):
    company = models.OneToOneField(
        'Company',
        on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name=_('Компания')

    )
    who_are_you = models.TextField(
        max_length=30,
        null=True, blank=True,
        verbose_name=_('Кто вы?')
    )

    guru = models.TextField(
        max_length=100,
        null=True, blank=True,
        verbose_name=_('В чем вы Гуру?')
    )

    for_whom = models.TextField(
        max_length=50,
        null=True, blank=True,
        verbose_name=_('Для кого работает ваша компания?')
    )

    difference = models.TextField(
        max_length=100,
        null=True, blank=True,
        verbose_name=_('Чем отличаетесь от конкурентов?')
    )

    good_partner = models.TextField(
        max_length=100,
        null=True, blank=True,
        verbose_name=_('Мы классные партнеры, потому что:')
    )

    future = models.TextField(
        max_length=100,
        null=True, blank=True,
        verbose_name=_('Какой будет Ваша компания через 5 лет?')
    )

    class Meta:
        verbose_name = _('Питч компании')
        verbose_name_plural = _('Питчи компаний')


# Мой магазин

class MyStore(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    domain_subdomain = models.CharField(max_length=3, choices=DOMEN, blank=True, null=True, verbose_name=_('Домен/поддомен'))
    domain_name = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('Имя домена'))
    call_back = models.CharField(max_length=3, choices=CALL_BACK, null=True, blank=True, verbose_name=_('Функция Сall-back'))
    facebook = models.URLField(max_length=200, null=True, blank=True, verbose_name=_('Facebook'))
    instagram = models.URLField(max_length=200, null=True, blank=True, verbose_name=_('Instagram'))
    linkedin = models.URLField(max_length=200, null=True, blank=True, verbose_name=_('Linkedin'))
    top_sales = models.BooleanField(default=False, verbose_name='Топ продаж')
    no_items = models.BooleanField(default=False, verbose_name='Без товара')
    logo = models.ImageField(upload_to='users/company_logo', null=True, blank=True, verbose_name=_('Логотип'))

    @property
    def get_url(self):
        if self.domain_subdomain:
            return 'https://{}/'.format(self.domain_name)

    class Meta:
        verbose_name = _('Магазин партнера')
        verbose_name_plural = _('Магазины партнеров')

    def __str__(self):
        return '{} {}'.format(self.id, self.user)


class HeaderPhoneNumber(models.Model):

    store = models.ForeignKey('MyStore', on_delete=models.CASCADE, related_name='header_phones', null=True, blank=True)
    number = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Номер телефона для хедера'))


class FooterPhoneNumber(models.Model):

    store = models.ForeignKey('MyStore', on_delete=models.CASCADE, related_name='footer_phones', null=True, blank=True)
    number = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Номер телефона для футера'))


class Navigation(models.Model):
    store = models.ForeignKey('MyStore', on_delete=models.CASCADE, related_name='navigations', null=True, blank=True)
    navigation = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('Раздел навигации'))


class StoreSliderImage(models.Model):
    store = models.ForeignKey(MyStore, on_delete=models.CASCADE, related_name='slider_images')
    image = models.ImageField(upload_to='users/company/store/slider', verbose_name='Картинка для слайдера')
