# Generated by Django 4.0.6 on 2022-07-13 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0007_merge_20220713_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='detail_content',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='place',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project_app.post'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='sequence',
            field=models.IntegerField(blank=True),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project_app.post')),
            ],
        ),
    ]
