# Generated by Django 5.1.6 on 2025-02-23 01:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunch', '0017_alter_lunchitem_student_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lunchitem',
            name='student_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to='lunch.student'),
        ),
    ]
