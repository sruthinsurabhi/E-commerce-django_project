# Generated by Django 2.2 on 2023-02-18 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20230217_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='available',
            field=models.BooleanField(default='0'),
            preserve_default=False,
        ),
    ]