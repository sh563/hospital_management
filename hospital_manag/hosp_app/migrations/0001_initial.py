# Generated by Django 3.1.7 on 2021-10-04 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=45)),
                ('tell_no', models.IntegerField()),
                ('email_id', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('postal_code', models.TextField(max_length=20)),
                ('date', models.CharField(max_length=50)),
            ],
        ),
    ]
