# Generated by Django 5.0.7 on 2024-07-29 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0022_assignment_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='of_course',
            new_name='course',
        ),
        migrations.RemoveField(
            model_name='examination',
            name='of_course',
        ),
        migrations.AddField(
            model_name='examination',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examinations', to='lessons.lesson'),
            preserve_default=False,
        ),
    ]
