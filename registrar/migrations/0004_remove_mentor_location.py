# Generated by Django 4.2.4 on 2023-08-08 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrar', '0003_mentor_email_mentor_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='location',
        ),
    ]
