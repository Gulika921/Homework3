# Generated by Django 3.1.5 on 2021-06-24 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0012_auto_20210624_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carreleasedate',
            name='date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
