from django.db import models
import datetime
# Create your models here.

class Client(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "Clients"
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title

class ProductionArea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "Production areas"
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title

class FeatureRequest(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    priority = models.PositiveIntegerField(blank=False, default=1)
    production_area = models.ForeignKey('ProductionArea', on_delete=models.CASCADE)
    target_date = models.DateField(default=datetime.date.today)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "Feature Requests"
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        super(FeatureRequest, self).save(*args, **kwargs)
