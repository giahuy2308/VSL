# Generated by Django 5.0.7 on 2024-07-16 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='no',
            field=models.PositiveIntegerField(default=1),
        ),
    ]