# Generated by Django 5.0.7 on 2024-07-18 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='administrator',
        ),
        migrations.RemoveField(
            model_name='community',
            name='participant',
        ),
        migrations.RemoveField(
            model_name='page',
            name='community',
        ),
        migrations.RemoveField(
            model_name='page',
            name='author',
        ),
        migrations.RemoveField(
            model_name='reaction',
            name='author',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Community',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.DeleteModel(
            name='Reaction',
        ),
    ]