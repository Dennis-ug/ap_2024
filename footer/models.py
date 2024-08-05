from django.db import models
from wagtail.models import Page

from home.models import HomePage


# Create your models here.
class Footer(Page):
    template = "service/service-details.html"
    x = models.URLField(max_length=100, blank=False, null=True)
    fb = models.URLField(max_length=100, blank=False, null=True)
    ig = models.URLField(max_length=100, blank=False, null=True)
    linkedIn = models.URLField(max_length=100, blank=False, null=True)

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["contact"] = HomePage.objects.first().live().public()

        return context
