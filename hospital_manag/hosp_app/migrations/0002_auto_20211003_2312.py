# Generated by Django 3.1.7 on 2021-10-04 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosp_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='postal_code',
            field=models.CharField(max_length=20),
        ),
    ]