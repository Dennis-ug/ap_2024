# Generated by Django 4.2.14 on 2024-08-09 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_alter_homepage_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='happy_clients',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hard_workers',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='project',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='support_hours',
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]
