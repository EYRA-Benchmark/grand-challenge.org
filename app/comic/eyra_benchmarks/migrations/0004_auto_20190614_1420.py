# Generated by Django 2.1.8 on 2019-06-14 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eyra_benchmarks', '0003_auto_20190604_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='benchmark',
            name='image',
        ),
        migrations.AddField(
            model_name='benchmark',
            name='banner_image_url',
            field=models.CharField(default='https://www.staging.eyrabenchmark.net/static/media/logo.3fc4ddae.png', help_text='Benchmark banner image', max_length=255),
        ),
        migrations.AddField(
            model_name='benchmark',
            name='card_image_url',
            field=models.CharField(default='https://www.staging.eyrabenchmark.net/static/media/logo.3fc4ddae.png', help_text='Benchmark card image', max_length=255),
        ),
    ]