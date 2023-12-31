# Generated by Django 4.1.10 on 2023-08-29 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0005_remove_userclass_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('niveau', models.CharField(max_length=100)),
                ('student', models.ManyToManyField(blank=True, limit_choices_to={'role': 'STUDENT'}, related_name='chapitres_suivis', to='user.userclass')),
                ('teacher', models.ForeignKey(blank=True, limit_choices_to={'role': 'TEACHER'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.userclass')),
            ],
        ),
    ]
