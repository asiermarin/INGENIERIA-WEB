# Generated by Django 3.0.4 on 2020-03-31 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Duracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('duracionMin', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('fecha_creacion', models.DateField()),
                ('numero_articulo', models.IntegerField()),
                ('duracion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPruebaDos.Duracion')),
                ('genero', models.ManyToManyField(to='appPruebaDos.Genero')),
            ],
        ),
    ]