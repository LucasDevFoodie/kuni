from django.shortcuts import render

from django.views.generic import (TemplateView, DetailView)
from .models import Package,Blog, AgencySettings

class HomeView(TemplateView):
    template_name = "website/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["packages"] = (Package.objects.filter(is_available=True).order_by("-created_at"))
        context["blogs"] = (Blog.objects.filter(is_available=True).select_related("package").order_by("-created_at"))

        context["agency"] = AgencySettings.objects.first()

        return context

class PackageDetailView(DetailView):
    model = Package
    template_name = "website/package_detail.html"
    context_object_name = "package"

    def get_queryset(self):
        queryset = Package.objects.all()

        if not self.request.user.is_staff:
            queryset.filter(is_available=True)

        return queryset

class BlogDetailView(DetailView):
    model = Blog
    template_name = "website/blog_detail.html"
    context_object_name = "blog"

    def get_queryset(self):
        queryset = Blog.objects.all()

        if not self.request.user.is_staff:
            queryset = queryset.filter(is_available=True)

        return queryset

class ContactView(TemplateView):
    template_name = "website/contact.html"
