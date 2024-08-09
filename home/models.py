from django.db import models

from wagtail.admin.panels.field_panel import FieldPanel  # , StreamFieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from Portfolio.models import Portfolio
from service.models import Service
# from wagtail.blocks import blocks as streamfield_blocks

from streams import block


class HomePage(Page):
    templates = "home/home_page.html"

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_sub_title = models.CharField(max_length=100, blank=False, null=True)
    back_ground_photo = models.ForeignKey("wagtailimages.Image", blank=True, null=True,
                                          on_delete=models.SET_NULL,
                                          related_name="+"
                                          )
    about_photo = models.ForeignKey("wagtailimages.Image", blank=True, null=True,
                                    on_delete=models.SET_NULL,
                                    related_name="+"
                                    )
    about_information = StreamField([

        ("details", block.RichtextBlock()),

    ],
        null=True,
        blank=False, )
    about_company_achievements = models.TextField(max_length=5000, blank=False, null=True)
    image_company_achievements = models.ForeignKey("wagtailimages.Image", blank=True, null=True,
                                                   on_delete=models.SET_NULL
                                                   )
    contact = models.CharField(max_length=100, blank=False, null=True)
    email = models.CharField(max_length=100, blank=False, null=True)
    address = models.CharField(max_length=100, blank=False, null=True)
    happy_clients_number = models.IntegerField(blank=False, null=True)
    projects_number = models.IntegerField(blank=False, null=True)
    support_hours = models.IntegerField(blank=False, null=True)
    hard_workers = models.IntegerField(blank=False, null=True)
    profile = models.FileField(upload_to="uploads", null=True, blank=True)
    testimonial = StreamField([
        ("testimonials", block.TestimonialBlock())
        , ],

        null=True,
        blank=True,
    )

    content = StreamField(
        [

            ("Staff", block.CustomBlock()),

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
        FieldPanel("address"),
        FieldPanel("about_company_achievements"),
        FieldPanel("profile"),
        FieldPanel("image_company_achievements"),
        FieldPanel("back_ground_photo"),
        FieldPanel("about_photo"),
        FieldPanel("testimonial"),
        FieldPanel("happy_clients_number"),
        FieldPanel("projects_number"),
        FieldPanel("support_hours"),
        FieldPanel("hard_workers")

    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["services"] = Service.objects.live().public()
        context["portfolios"] = Portfolio.objects.live().public()

        return context
