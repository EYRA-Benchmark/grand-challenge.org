# Generated by Django 2.1.7 on 2019-02-26 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import grandchallenge.eyra_data.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataFile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, default='', help_text='Description of this dataset in markdown.', null=True)),
                ('frozen', models.BooleanField(default=False)),
                ('file', models.FileField(blank=True, null=True, upload_to=grandchallenge.eyra_data.models.get_data_file_name)),
                ('sha', models.CharField(blank=True, max_length=40, null=True)),
                ('original_file_name', models.CharField(blank=True, max_length=150, null=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='_datasets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DataType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, default='', help_text='Description of this data type in markdown.', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='datafile',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eyra_data.DataType'),
        ),
    ]
