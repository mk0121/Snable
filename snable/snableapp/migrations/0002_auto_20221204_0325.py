# Generated by Django 3.0.7 on 2022-12-03 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snableapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='mobile_no',
            field=models.CharField(max_length=20),
        ),
    ]
