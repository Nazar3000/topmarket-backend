# Generated by Django 2.1.7 on 2019-04-08 15:22

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_pocket', models.CharField(blank=True, choices=[('BASE', 'Base'), ('FULL', 'Full'), ('NO', 'No')], default='BASE', max_length=10, null=True, verbose_name='Пакет услуг')),
                ('first_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Last name')),
                ('patronymic', models.CharField(blank=True, max_length=256, null=True, verbose_name='Patronymic')),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Is the user allowed to have access to the admin', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=False, help_text='Is the user account currently active', verbose_name='active')),
                ('username', models.CharField(blank=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, null=True, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='user_profiles/avatars')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ActivityAreas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=1095, verbose_name='Имя сферы деятельности')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cert_doc', models.ImageField(blank=True, null=True, upload_to='companies/documents/certificates', verbose_name='Свидетельство о регистрации или выписка с ЕГРПОУ')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название компании')),
                ('town', models.TextField(blank=True, max_length=30, null=True, verbose_name='Город')),
                ('address', models.TextField(blank=True, max_length=40, null=True, verbose_name='Адресс')),
                ('url', models.URLField(blank=True, null=True)),
                ('working_conditions', models.TextField(blank=True, max_length=100, null=True, verbose_name='Условия работы')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='users/company/logos', verbose_name='Лого компании')),
                ('web_site', models.URLField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Телефон')),
                ('who_see_contact', models.CharField(blank=True, max_length=200, null=True, verbose_name='Кому видны контактные данные?')),
                ('is_internet_shop', models.BooleanField(default=False, verbose_name='Интернет магазин')),
                ('is_offline_shop', models.BooleanField(default=False, verbose_name='Оффлайн-магазин')),
                ('retail_network', models.BooleanField(default=False, verbose_name='Розничная сеть')),
                ('distributor', models.BooleanField(default=False, verbose_name='Дистрибьютор')),
                ('manufacturer', models.BooleanField(default=False, verbose_name='ПРоизводитель')),
                ('importer', models.BooleanField(default=False, verbose_name='Импортер')),
                ('dealer', models.BooleanField(default=False, verbose_name='Дилер')),
                ('sub_dealer', models.BooleanField(default=False, verbose_name='Субдилер')),
                ('exporter', models.BooleanField(default=False, verbose_name='Експортер')),
                ('official_representative', models.BooleanField(default=False, verbose_name='Официальный представитель')),
                ('about_company', models.TextField(blank=True, max_length=500, null=True, verbose_name='Информация')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владецел компании')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyPitch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who_are_you', models.TextField(blank=True, max_length=30, null=True, verbose_name='Кто вы?')),
                ('guru', models.TextField(blank=True, max_length=100, null=True, verbose_name='В чем вы Гуру?')),
                ('for_whom', models.TextField(blank=True, max_length=50, null=True, verbose_name='Для кого работает ваша компания?')),
                ('difference', models.TextField(blank=True, max_length=100, null=True, verbose_name='Чем отличаетесь от конкурентов?')),
                ('good_partner', models.TextField(blank=True, max_length=100, null=True, verbose_name='Мы классные партнеры, потому что:')),
                ('future', models.TextField(blank=True, max_length=100, null=True, verbose_name='Какой будет Ваша компания через 5 лет?')),
                ('company', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Company')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=1095, verbose_name='Тип компании')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Company')),
            ],
        ),
        migrations.CreateModel(
            name='MyStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_subdomain', models.CharField(blank=True, choices=[('DM', 'Домен'), ('SD', 'Поддомен')], max_length=2, null=True)),
                ('domain_name', models.URLField(blank=True, null=True)),
                ('call_back', models.CharField(blank=True, choices=[('YES', 'Включена'), ('NO', 'Выключена')], max_length=3, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('top_sales', models.BooleanField(default=False, verbose_name='Топ продаж')),
                ('no_items', models.BooleanField(default=False, verbose_name='Без товара')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='users/company_logo')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navigation', models.CharField(blank=True, max_length=200, null=True)),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='navigations', to='users.MyStore')),
            ],
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_doc', models.ImageField(blank=True, null=True, upload_to='companies/documents/passports', verbose_name='Паспорт')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='passports', to='users.Company')),
            ],
        ),
        migrations.CreateModel(
            name='PayerCertificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payer_cert_doc', models.ImageField(blank=True, null=True, upload_to='companies/documents/payer_certificates', verbose_name='Cвидетельство плательщика единого налога')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payer_certificates', to='users.Company')),
            ],
        ),
        migrations.CreateModel(
            name='PayerRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payer_reg_doc', models.ImageField(blank=True, null=True, upload_to='companies/documents/payer_registers', verbose_name='Выписка из реестра плательщиков НДС')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payer_registers', to='users.Company')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=20, null=True)),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='users.MyStore')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceIndustry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=1095, verbose_name='Имя сферы услуг')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Company')),
            ],
        ),
        migrations.CreateModel(
            name='StoreSliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='users/company/store/slider', verbose_name='Картинка для слайдера')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slider_images', to='users.MyStore')),
            ],
        ),
        migrations.CreateModel(
            name='TaxPayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_doc', models.ImageField(blank=True, null=True, upload_to='companies/documents/tax_payers', verbose_name='Справка 4 Учета плательщика налогов')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tax_payers', to='users.Company')),
            ],
        ),
        migrations.CreateModel(
            name='UkraineStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uk_doc', models.ImageField(blank=True, null=True, upload_to='companies/documents/uk_statistics', verbose_name='Справка Государственного комитета статистики Украины')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ukraine_statistics', to='users.Company')),
            ],
        ),
        migrations.CreateModel(
            name='UserNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_order_email', models.BooleanField(default=False, verbose_name='Новый заказ (email)')),
                ('new_order_tel', models.BooleanField(default=False, verbose_name='Новый заказ (смс)')),
                ('ttn_change', models.BooleanField(default=False, verbose_name='Смена ТТН заказа')),
                ('order_paid', models.BooleanField(default=False, verbose_name='Получение счета на оплату')),
                ('sales_report', models.BooleanField(default=False, verbose_name='Sales report notification')),
                ('new_message', models.BooleanField(default=False, verbose_name='New message in internal mailing notification')),
                ('cancel_order', models.BooleanField(default=False, verbose_name='Cancel order notification')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User notification',
                'verbose_name_plural': 'User notifications',
            },
        ),
        migrations.AddField(
            model_name='certificate',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to='users.Company'),
        ),
        migrations.AddField(
            model_name='activityareas',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_areas', to='users.Company'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Company', verbose_name='Менеджер'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]