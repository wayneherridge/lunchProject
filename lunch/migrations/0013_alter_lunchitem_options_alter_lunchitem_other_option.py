# Generated by Django 5.1.6 on 2025-02-21 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunch', '0012_alter_lunchitem_other_option'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lunchitem',
            options={'ordering': ['-lunch_option', '-student_name']},
        ),
        migrations.AlterField(
            model_name='lunchitem',
            name='other_option',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
