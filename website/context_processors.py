from django.conf import settings

def agency_settings(request):
    # Only one setting, available across every template. values will rarely change
    return {
        "agency": settings.AGENCY,
    }