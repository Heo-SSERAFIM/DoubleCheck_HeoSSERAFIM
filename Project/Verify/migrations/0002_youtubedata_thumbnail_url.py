# Generated by Django 3.2.20 on 2023-08-11 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Verify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtubedata',
            name='thumbnail_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
