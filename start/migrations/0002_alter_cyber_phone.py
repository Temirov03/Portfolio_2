# Generated by Django 4.2 on 2023-04-14 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("start", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cyber",
            name="phone",
            field=models.IntegerField(verbose_name="Telefon raqam"),
        ),
    ]
