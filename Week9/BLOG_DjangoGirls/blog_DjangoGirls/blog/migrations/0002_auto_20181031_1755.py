# Generated by Django 2.1.2 on 2018-10-31 11:55

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('author_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]