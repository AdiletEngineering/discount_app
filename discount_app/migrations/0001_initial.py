# Generated by Django 3.2.5 on 2021-08-05 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название категории')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название города')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название компании')),
                ('image', models.TextField(verbose_name='Ссылка на картинку компании')),
                ('description', models.TextField(verbose_name='Описание компании')),
                ('active', models.BooleanField(default=True, verbose_name='Компания активна?')),
                ('working_time', models.CharField(max_length=50, verbose_name='Режим работы')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Скидка активна?')),
                ('views_count', models.IntegerField(verbose_name='Количество просмотров')),
                ('value', models.IntegerField(verbose_name='Процент скидки')),
                ('terms', models.TextField(verbose_name='Условия скидки')),
                ('duration', models.DurationField(verbose_name='Длительность скидки')),
                ('max_coupons', models.IntegerField(verbose_name='максимальное количество купонов')),
                ('pin', models.CharField(max_length=4, verbose_name='Пин код для активации')),
                ('is_active_every_day', models.TextField(verbose_name='акция действует каждый день?')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='discounts', to='discount_app.category')),
                ('companies', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='discounts', to='discount_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название соц сети')),
                ('image', models.TextField(verbose_name='Ссылка на картинку социальной сети')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст отзыва')),
                ('discounts', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reviews', to='discount_app.discount')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reviews', to='discount_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('companies', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='phones', to='discount_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50, verbose_name='Статус купона')),
                ('start_time', models.DateField(auto_now_add=True)),
                ('deadline', models.DateField()),
                ('discounts', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='coupons', to='discount_app.discount')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='coupons', to='discount_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='CompanySocials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(verbose_name='Ссылка для перехода в текущую соц сеть')),
                ('companies', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='company_socials', to='discount_app.company')),
                ('socials', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='company_socials', to='discount_app.social')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('house', models.CharField(max_length=10, verbose_name='Дом')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('cities', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='addresses', to='discount_app.city')),
                ('companies', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='addresses', to='discount_app.company')),
            ],
        ),
    ]
