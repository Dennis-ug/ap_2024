from django.db import models
from wagtail.models import Page

from home.models import HomePage


# Create your models here.
class Footer(Page):
    template = "service/footer.html"
    x = models.URLField(max_length=100, blank=False, null=True)
    fb = models.URLField(max_length=100, blank=False, null=True)
    ig = models.URLField(max_length=100, blank=False, null=True)
    linkedIn = models.URLField(max_length=100, blank=False, null=True)

    def get_context(self, request, *args, **kwargs):
        from home.models import HomePage
        context = super().get_context(request, *args, **kwargs)
        context["home"] = HomePage.objects.live().public().first()

        return context
