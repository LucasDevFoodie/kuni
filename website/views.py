from django.views.generic import (TemplateView, DetailView)
from .models import Package,Blog
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from .forms import ContactForm
from django.conf import settings

class HomeView(TemplateView):
    template_name = "website/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["packages"] = (Package.objects.filter(is_available=True).order_by("-created_at"))
        context["blogs"] = (Blog.objects.filter(is_available=True).select_related("package").order_by("-created_at"))

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

class ContactView(FormView):
    template_name = "website/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact")

    def form_valid(self, form):
        agency_email = settings.AGENCY["email"]

        if not agency_email:
            form.add_error(
                None,
                "Agency contact information is not configured."
            )
            return self.form_invalid(form)

        email = EmailMessage(
            subject=(
                f"Website enquiry from "
                f"{form.cleaned_data['name']}"
            ),
            body=(
                f"Name: {form.cleaned_data['name']}\n"
                f"Email: {form.cleaned_data['email']}\n"
                f"Telephone: {form.cleaned_data['telephone']}\n\n"
                f"Message:\n{form.cleaned_data['message']}"
            ),
            to=[agency_email],
            reply_to=[form.cleaned_data["email"]],
        )

        email.send(fail_silently=False)

        return super().form_valid(form)
