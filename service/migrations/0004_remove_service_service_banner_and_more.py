# Generated by Django 4.2.14 on 2024-08-02 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_service_service_banner_service_service_details_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='service_banner',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service_details',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service_name',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service_surmmary',
        ),
    ]
