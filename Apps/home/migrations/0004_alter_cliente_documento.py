# Generated by Django 3.2.6 on 2021-09-04 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_cliente_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='documento',
            field=models.CharField(choices=[('D', 'DPI'), ('C', 'CEDULA')], default='D', max_length=20),
        ),
    ]
