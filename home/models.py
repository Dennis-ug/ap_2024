from django.db import models

from wagtail.admin.panels.field_panel import FieldPanel  # , StreamFieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page
# from wagtail.blocks import blocks as streamfield_blocks

from streams import block


class HomePage(Page):
    templates = "home/home_page.html"

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_sub_title = models.CharField(max_length=100, blank=False, null=True)
    about_information = models.TextField(max_length=5000, blank=False, null=True)
    contact = models.CharField(max_length=100, blank=False, null=True)
    email = models.CharField(max_length=100, blank=False, null=True)
    address = models.CharField(max_length=100, blank=False, null=True)

    content = StreamField(
        [

            ("Staff", block.CardBlock()),

        ],
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_sub_title"),
        FieldPanel("about_information"),
        FieldPanel("content"),
        FieldPanel("contact"),
        FieldPanel("email"),
        FieldPanel("address")

    ]

