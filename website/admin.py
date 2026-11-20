from django.contrib import admin
from .models import Package, Blog

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = (
        "name_en",
        "name_es",
        "price",
        "is_available",
        "created_at",
    )

    list_filter = ("is_available",)
    search_fields = ("name_en", "name_es")
    readonly_fields = ("created_at", "updated_at")

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title_en",
        "title_es",
        "package",
        "is_available",
        "created_at",
    )

    list_filter = ("is_available",)
    search_fields = ("title_en", "title_es")

