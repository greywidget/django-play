# Generated by Django 3.1.2 on 2020-10-30 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='completed',
        ),
    ]
