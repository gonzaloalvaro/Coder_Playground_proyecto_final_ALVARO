# Generated by Django 4.2.7 on 2023-12-17 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='Cuit',
            new_name='nro_cuit',
        ),
    ]
