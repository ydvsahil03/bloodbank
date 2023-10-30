# Generated by Django 4.2.6 on 2023-10-07 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.IntegerField(default=9712203775, help_text='Enter 10 digits phone number', max_length=10, unique=True, verbose_name='Phone Number'),
            preserve_default=False,
        ),
    ]
