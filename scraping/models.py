from django.db import models

from django.db import models

class SiteInfo(models.Model):
    url = models.URLField(unique=True)
    classification = models.CharField(max_length=255)
    category = models.CharField(max_length=255, blank=True, null=True)
    ranking_change = models.IntegerField(blank=True, null=True)
    avg_duration = models.DurationField(blank=True, null=True)
    pages_per_visit = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    bounce_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    top_countries = models.TextField(blank=True, null=True)
    gender_distribution = models.TextField(blank=True, null=True)
    age_distribution = models.TextField(blank=True, null=True)
  

    def __str__(self):
        return self.url

