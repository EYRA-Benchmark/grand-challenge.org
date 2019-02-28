# Generated by Django 2.1.7 on 2019-02-28 10:32

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eyra_benchmarks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='benchmark',
            name='metrics_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
