# Generated by Django 4.2.4 on 2023-08-25 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_userclass_secondname_remove_userclass_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userclass',
            name='username',
        ),
    ]
