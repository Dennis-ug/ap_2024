# Generated by Django 5.0.7 on 2024-07-31 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_homepage_contact_homepage_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
