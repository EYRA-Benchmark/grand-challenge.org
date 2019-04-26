# Generated by Django 2.1.8 on 2019-04-26 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eyra_algorithms', '0002_implementation_command'),
    ]

    operations = [
        migrations.RenameField(
            model_name='implementation',
            old_name='container',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='interface',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='Moment of creation'),
        ),
    ]
