# Generated by Django 5.1.6 on 2025-02-20 19:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('option_id', models.AutoField(primary_key=True, serialize=False)),
                ('option', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(blank=True, max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='LunchItem',
            fields=[
                ('lunch_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('lunch_date', models.DateField(auto_now_add=True)),
                ('other_option', models.CharField(max_length=50)),
                ('lunch_option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lunch.option')),
                ('student_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lunch.student')),
            ],
            options={
                'ordering': ['lunch_option', 'student_name'],
            },
        ),
    ]
