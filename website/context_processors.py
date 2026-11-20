from .models import AgencySettings

from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver

AGENCY_SETTINGS = "agency_settings"

@receiver(post_save)
def clear_agency_settings_cache(sender, **kwargs):
    cache.delete(AGENCY_SETTINGS)

def agency_settings(request):
    # Only one setting, available across every template. values are cached as they will rarely change
    settings = cache.get(AGENCY_SETTINGS)

    if settings is None:
        settings = AgencySettings.objects.first()
        cache.set(AGENCY_SETTINGS, settings, 60 * 60)

    
    return { AGENCY_SETTINGS: settings,} 