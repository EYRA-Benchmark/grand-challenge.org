# Generated by Django 2.0.9 on 2018-10-23 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("challenges", "0013_auto_20181019_1642")]

    operations = [
        migrations.RemoveField(
            model_name="challenge", name="is_open_for_submissions"
        ),
        migrations.RemoveField(
            model_name="challenge", name="last_submission_date"
        ),
        migrations.RemoveField(
            model_name="challenge", name="number_of_downloads"
        ),
        migrations.RemoveField(
            model_name="challenge", name="number_of_submissions"
        ),
        migrations.RemoveField(
            model_name="challenge", name="offers_data_download"
        ),
        migrations.RemoveField(
            model_name="challenge", name="submission_page_name"
        ),
        migrations.RemoveField(
            model_name="externalchallenge", name="download_page"
        ),
        migrations.RemoveField(
            model_name="externalchallenge", name="is_open_for_submissions"
        ),
        migrations.RemoveField(
            model_name="externalchallenge", name="last_submission_date"
        ),
        migrations.RemoveField(
            model_name="externalchallenge", name="number_of_downloads"
        ),
        migrations.RemoveField(
            model_name="externalchallenge", name="number_of_submissions"
        ),
        migrations.RemoveField(
            model_name="externalchallenge", name="offers_data_download"
        ),
        migrations.RemoveField(
            model_name="externalchallenge", name="submission_page"
        ),
        migrations.AddField(
            model_name="challenge",
            name="cached_latest_result",
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="challenge",
            name="cached_num_participants",
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name="challenge",
            name="cached_num_results",
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]