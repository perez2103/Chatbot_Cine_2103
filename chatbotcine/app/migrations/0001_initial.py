# Generated by Django 3.0 on 2021-03-20 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CienciaFiccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('dic_peliculas_cf', models.CharField(max_length=100)),
                ('titulos', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PeliculasCiencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('puntuacion', models.CharField(max_length=100)),
                ('titulos', models.CharField(max_length=100)),
                ('fk_ciencia_ficcion', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.CienciaFiccion')),
            ],
        ),
    ]
