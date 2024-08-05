# Generated by Django 4.2.14 on 2024-08-04 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0006_alter_portfolio_project_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='project_URL',
            field=models.URLField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='project_category',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='project_client',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='project_date',
            field=models.TextField(max_length=5000, null=True),
        ),
    ]
