# Generated by Django 2.1.7 on 2019-02-28 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eyra_algorithms', '0001_initial'),
        ('eyra_benchmarks', '0003_auto_20190228_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='benchmark',
            name='interface',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='benchmarks', to='eyra_algorithms.Interface'),
        ),
    ]
