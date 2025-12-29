from django.db import models


class Category(models.Model):
    """Category model for different event services"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome icon class")
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Package(models.Model):
    """Readymade packages with pricing"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.TextField(help_text="Enter features separated by new lines")
    image = models.ImageField(upload_to='packages/', blank=True, null=True)
    is_popular = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_popular', 'price']

    def __str__(self):
        return self.name

    def get_features_list(self):
        """Return features as a list"""
        return [feature.strip() for feature in self.features.split('\n') if feature.strip()]
