# Generated by Django 2.1.8 on 2019-06-14 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eyra_benchmarks', '0004_auto_20190614_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='visualization_url',
            field=models.URLField(blank=True, help_text='Visualization URL', null=True),
        ),
    ]