# Generated by Django 3.1.5 on 2021-06-24 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0011_auto_20210624_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carreleasedate',
            name='date',
            field=models.DateField(),
        ),
    ]