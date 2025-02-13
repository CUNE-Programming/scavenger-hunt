from django.db import models

# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class LocationPage(Page):
    name = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    location_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    hint = RichTextField(blank=True)
    hint_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    # modify your content_panels:
    content_panels = Page.content_panels + [
        FieldPanel("name"),
        FieldPanel("description"),
        FieldPanel("location_image"),
        FieldPanel("hint"),
        FieldPanel("hint_image"),
    ]
