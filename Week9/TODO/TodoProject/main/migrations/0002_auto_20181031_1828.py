# Generated by Django 2.1.2 on 2018-10-31 12:28

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='task',
            managers=[
                ('created', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='created',
        ),
    ]