# Generated by Django 4.2.14 on 2024-08-09 08:39

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_homepage_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('Staff', wagtail.blocks.StructBlock([('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(max_length=40, required=True)), ('name', wagtail.blocks.TextBlock(max_length=200, required=True)), ('whatsApp', wagtail.blocks.URLBlock(help_text='Enter the link to whatsApp.', required=False)), ('instagram', wagtail.blocks.URLBlock(help_text='Enter link to instagram', required=False)), ('linkedin', wagtail.blocks.URLBlock(help_text='Enter link to linkedin', required=False)), ('x', wagtail.blocks.URLBlock(help_text='Enter link to x', required=False))])))]))], blank=True, null=True),
        ),
    ]
