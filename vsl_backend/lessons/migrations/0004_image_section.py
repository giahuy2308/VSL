# Generated by Django 5.0.7 on 2024-07-16 08:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_image_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='section',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='lessons.section'),
            preserve_default=False,
        ),
    ]
