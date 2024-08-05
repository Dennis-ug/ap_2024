from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from streams import block


class Service(Page):
    template = "service/service-details.html"
    service_name = models.CharField(max_length=100, blank=False, null=True)
    service_summary = models.TextField(max_length=1000, blank=False, null=True)
    service_details = StreamField([

        ("details", block.RichtextBlock()),

    ],
        null=True,
        blank=True,)
        # models.TextField(max_length=5000, blank=False, null=True)
    service_image = models.ForeignKey("wagtailimages.Image", blank=True, null=True, on_delete=models.SET_NULL
                                      )
    #
    content_panels = Page.content_panels + [
        FieldPanel("service_name"),
        FieldPanel("service_summary"),
        FieldPanel("service_details"),
        FieldPanel("service_image"),

    ]
# Create your models here.
