# Generated by Django 5.1.6 on 2025-02-24 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lunch', '0019_alter_lunchitem_options_alter_option_option'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lunchitem',
            options={'ordering': ['-student_name']},
        ),
    ]
