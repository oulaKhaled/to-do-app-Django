# Generated by Django 4.2.5 on 2023-10-02 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0017_alter_task_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='days',
        ),
    ]