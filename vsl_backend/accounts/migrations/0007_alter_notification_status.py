# Generated by Django 5.0.7 on 2024-07-18 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_notification_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='status',
            field=models.CharField(choices=[('Read', 'read'), ('Unread', 'unread')], default='Unread', max_length=100),
        ),
    ]
