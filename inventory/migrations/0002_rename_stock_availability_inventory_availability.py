# Generated by Django 3.2.7 on 2021-12-08 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='stock_availability',
            new_name='availability',
        ),
    ]
