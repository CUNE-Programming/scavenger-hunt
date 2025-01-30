from django.db import models

# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class LocationPage(Page):
    name = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    hint = RichTextField(blank=True)

    # modify your content_panels:
    content_panels = Page.content_panels + [FieldPanel('name'), FieldPanel('description'), FieldPanel('hint')]