# Generated by Django 3.1.5 on 2021-06-24 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0009_auto_20210624_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carreleasedate',
            name='date',
            field=models.DateField(),
        ),
    ]
