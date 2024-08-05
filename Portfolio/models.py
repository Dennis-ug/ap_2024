from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page
from wagtail import blocks

from streams import block


# Create your models here.

class Portfolio(Page):
    template = "Portfolio/portfolio-details.html"
    project_name = models.CharField(max_length=1000, null=True, blank=False)
    project_summary = models.TextField(max_length=5000, null=True, blank=False)
    project_category = models.CharField(max_length=5000, null=True, blank=False)
    project_client = models.CharField(max_length=5000, null=True, blank=False)
    project_date = models.DateField(max_length=5000, null=True, blank=False)
    project_URL = models.URLField(max_length=5000, null=True, blank=False)
    project_thumbnail = models.ForeignKey("wagtailimages.Image", blank=True, null=True, on_delete=models.SET_NULL)
    project_details = StreamField([

        ("details", block.RichtextBlock()),

    ],
        null=True,
        blank=False, )

    project_galley = StreamField([
        ('photo', block.CustomImageBlock())

    ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("project_name"),
        FieldPanel("project_summary"),
        FieldPanel("project_thumbnail"),
        FieldPanel("project_galley"),
        FieldPanel("project_details"),
        FieldPanel("project_category"),
        FieldPanel("project_client"),
        FieldPanel("project_date"),
        FieldPanel("project_URL"),
        # FieldPanel("project_URL"),

    ]
