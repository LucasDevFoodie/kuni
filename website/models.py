from django.db import models
from django.utils.text import slugify


class Package(models.Model):
    name_en = models.CharField(max_length=200)
    name_es = models.CharField(max_length=200)

    description_en = models.TextField()
    description_es = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    image = models.ImageField(upload_to="packages/")

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True,
    )

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_en)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_en


class Blog(models.Model):
    title_en = models.CharField(max_length=200)
    title_es = models.CharField(max_length=200)

    subtitle_en = models.CharField(max_length=255)
    subtitle_es = models.CharField(max_length=255)

    description_en = models.TextField()
    description_es = models.TextField()

    image = models.ImageField(upload_to="blogs/")

    package = models.OneToOneField(
        Package,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="blog",
    )

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True,
    )

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_en)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_en


class AgencySettings(models.Model):
    name = models.CharField(max_length=200)

    logo = models.ImageField(
        upload_to="agency/",
        blank=True,
        null=True,
    )

    description_en = models.TextField(blank=True)
    description_es = models.TextField(blank=True)

    email = models.EmailField()

    telephone_1 = models.CharField(max_length=30)
    telephone_2 = models.CharField(
        max_length=30,
        blank=True,
    )

    address = models.CharField(
        max_length=255,
        blank=True,
    )

    instagram_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)

    def __str__(self):
        return self.name
