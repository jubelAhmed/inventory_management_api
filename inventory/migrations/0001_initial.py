# Generated by Django 3.2.7 on 2021-12-07 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('note', models.TextField(blank=True, max_length=500, null=True)),
                ('stock', models.IntegerField(default=0)),
                ('stock_availability', models.BooleanField(default=True)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.supplier')),
            ],
        ),
    ]
