# Generated by Django 4.0.6 on 2022-07-13 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0012_alter_schedule_detail_content_alter_schedule_place_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='sequence',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
