# Generated by Django 4.1.7 on 2023-03-03 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0005_alter_city_name_alter_country_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='nombre',
            new_name='name',
        ),
    ]
