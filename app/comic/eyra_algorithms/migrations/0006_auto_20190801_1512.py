# Generated by Django 2.2.4 on 2019-08-01 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eyra_algorithms', '0005_auto_20190801_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]