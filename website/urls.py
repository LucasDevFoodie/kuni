from django.urls import path
from .views import (HomeView, PackageDetailView, BlogDetailView, ContactView)

urlpatterns = [
    path("", HomeView.as_view, name="home"),
    path("packages/<slug:slug>/", PackageDetailView.as_view, name="package-detail"),
    path("blog/<slug:slug>/", BlogDetailView.as_view, name="blog-detail"),
    path("contact/", ContactView.as_view, name="contact"),
]