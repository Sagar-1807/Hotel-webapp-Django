# Generated by Django 3.2 on 2021-08-07 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_contact_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.TextField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.TextField(max_length=50),
        ),
    ]
