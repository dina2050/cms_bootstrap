from django.db import models

# Create your models here.

class Event(models.Model):
    date = models.DateField()
    titre = models.CharField(max_length=100)
    evenement=models.CharField(max_length=500)
    photo=models.ImageField()

from cms.models.pluginmodel import CMSPlugin 
class TimelinePluginModel(CMSPlugin):
    text = models.CharField(max_length=180)
    events = models.ManyToManyField(Event)

    def copy_relations(self, oldinstance):
        self.events.set(oldinstance.events.all())


