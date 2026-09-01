from django.db import models
from django.utils.text import slugify

# Create your models here.

class Link(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url = models.URLField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} | {self.clicks}"

    def click(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            
            # Keep appending a counter until a unique slug is found
            while Link.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            
            self.slug = slug

        return super().save(*args, **kwargs)