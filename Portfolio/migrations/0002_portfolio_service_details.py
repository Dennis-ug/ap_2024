# Generated by Django 4.2.14 on 2024-08-04 18:26

from django.db import migrations
import streams.block
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='service_details',
            field=wagtail.fields.StreamField([('details', streams.block.RichtextBlock())], blank=True, null=True),
        ),
    ]
