# Generated by Django 5.2 on 2025-04-10 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_apitoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='apitoken',
            name='username',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
