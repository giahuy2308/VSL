# Generated by Django 5.0.7 on 2024-07-18 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0004_remove_reaction_comment_remove_reaction_page_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
