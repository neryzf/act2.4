# Generated by Django 3.2.6 on 2021-09-11 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_venta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
    ]
