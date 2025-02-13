from django.template.response import TemplateResponse
from wagtail.models import Page
from .models import LocationPage


def location(request):
    location_page = LocationPage.objects.get(slug="location")
    print(location_page.location_image)

    return TemplateResponse(
        request, "location/location_page.html", {"page": location_page}
    )
