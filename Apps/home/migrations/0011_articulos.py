# Generated by Django 3.2.6 on 2021-09-16 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_comentarios_contenido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('creacion', models.DateField(auto_now_add=True)),
                ('admin', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.admins')),
                ('contenido', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.comentarios')),
                ('nombre', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.estudiante')),
            ],
        ),
    ]
