# Generated by Django 4.1.7 on 2023-03-18 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settingmain',
            name='logo',
            field=models.ImageField(default=1, upload_to='home/logo/', verbose_name='Логотип'),
            preserve_default=False,
        ),
    ]
