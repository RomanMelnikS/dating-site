# Generated by Django 3.2.9 on 2021-11-24 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='Аватарка'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='sex',
            field=models.CharField(blank=True, choices=[('м', 'Мужской'), ('ж', 'Женский')], max_length=20, verbose_name='Пол'),
        ),
    ]
