# Generated by Django 5.2 on 2025-04-10 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_availablefom_room_availablefrom'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIToken',
            fields=[
                ('token', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
    ]
