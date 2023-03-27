# Generated by Django 4.1.7 on 2023-03-27 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregister',
            name='u_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='userregister',
            name='u_phone',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
