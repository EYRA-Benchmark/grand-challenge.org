# Generated by Django 2.1.7 on 2019-04-15 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eyra_data', '0002_auto_20190415_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='image',
            field=models.CharField(default='https://www.staging.eyrabenchmark.net/static/media/logo.3fc4ddae.png', help_text='DataSet image', max_length=255),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='data_files',
            field=models.ManyToManyField(blank=True, related_name='data_sets', to='eyra_data.DataFile'),
        ),
    ]