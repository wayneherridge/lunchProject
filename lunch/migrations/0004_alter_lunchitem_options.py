# Generated by Django 5.1.6 on 2025-02-20 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lunch', '0003_alter_lunchitem_other_option'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lunchitem',
            options={'ordering': ['lunch_option', '-student_name']},
        ),
    ]
