# Generated by Django 3.2 on 2024-10-16 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_auto_20241013_1132'),
        ('assignment', '0002_auto_20241014_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(default='c', on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='exam.course'),
        ),
    ]
