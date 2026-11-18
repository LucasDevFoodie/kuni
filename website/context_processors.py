from .models import AgencySettings

def agency_settings(request):
    # Only one setting, available across every template
    return { "agency": AgencySettings.objects.first()} 