# Generated by Django 4.2.5 on 2023-09-29 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_task_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='days',
            field=models.CharField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], max_length=10, null=True),
        ),
    ]
