# Generated by Django 5.1.6 on 2025-02-20 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunch', '0011_alter_lunchitem_other_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lunchitem',
            name='other_option',
            field=models.CharField(blank=True, default=' ', max_length=50, null=True),
        ),
    ]
