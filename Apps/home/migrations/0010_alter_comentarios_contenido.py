# Generated by Django 3.2.6 on 2021-09-16 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_comentarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='contenido',
            field=models.TextField(max_length=200),
        ),
    ]
