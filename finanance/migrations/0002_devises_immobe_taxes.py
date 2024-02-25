# Generated by Django 4.0 on 2023-02-20 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finanance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Immobe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_immob', models.CharField(max_length=100)),
                ('date_acquz', models.DateField()),
                ('val_origin_meth', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Taxes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_taxe', models.CharField(max_length=100)),
                ('type_taxe', models.CharField(max_length=100)),
            ],
        ),
    ]
