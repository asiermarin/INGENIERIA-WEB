# Generated by Django 3.0.5 on 2020-04-21 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPruebaDos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='un_numero',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]
