# Generated by Django 4.2.14 on 2024-08-03 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0026_delete_uploadedimage'),
        ('home', '0014_homepage_about_company_achievements'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='image_company_achievements',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.image'),
        ),
    ]
