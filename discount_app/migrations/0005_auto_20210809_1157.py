# Generated by Django 3.2.5 on 2021-08-09 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount_app', '0004_auto_20210806_1142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ('order_num',)},
        ),
        migrations.AlterModelOptions(
            name='discount',
            options={'ordering': ('order_num',)},
        ),
        migrations.AddField(
            model_name='city',
            name='order_num',
            field=models.IntegerField(default=0, verbose_name='Кастомный порядковый номер ГОРОДА'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='status',
            field=models.CharField(choices=[('RESERVED', 'reserved'), ('ACTIVATED', 'activated'), ('EXPIRED', 'expired')], max_length=50, verbose_name='Статус купона'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='order_num',
            field=models.IntegerField(default=0, verbose_name='Кастомный порядковый номер скидки'),
        ),
    ]
