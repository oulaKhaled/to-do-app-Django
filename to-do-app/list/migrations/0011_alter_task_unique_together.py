# Generated by Django 4.2.5 on 2023-09-29 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0010_alter_task_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='task',
            unique_together=set(),
        ),
    ]
