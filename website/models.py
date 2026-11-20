from django.db import models
from django.utils.text import slugify
from .mixin.translation import TranslatableModelMixin

class Package(TranslatableModelMixin, models.Model):
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

    @property
    def name(self):
        return self.get_translated_field("name")
    
    @property
    def description(self):
        return self.get_translated_field("description")
    
    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_en)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_en


class Blog(TranslatableModelMixin, models.Model):
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

    @property
    def title(self):
        return self.get_translated_field("title")

    @property
    def subtitle(self):
        return self.get_translated_field("subtitle")

    @property
    def description(self):
        return self.get_translated_field("description")

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_en)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_en
