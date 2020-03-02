from django.db import models


# Create your models here.
class SiteNode(models.Model):
    siteName = models.CharField(max_length=30)
    dateTime = models.DateTimeField()
    pH = models.CharField(max_length=10)
    DO = models.CharField(max_length=10)
    NH4 = models.CharField(max_length=10)
    CODMn = models.CharField(max_length=10)
    TOC = models.CharField(max_length=10)
    level = models.CharField(max_length=10)
    attribute = models.CharField(max_length=30, blank=True)
    status = models.CharField(max_length=20)
    class Meta():
        unique_together = (('siteName', 'dateTime'),)
        db_table = 'site_node'
        verbose_name = '站点'
        ordering = ['-id']
