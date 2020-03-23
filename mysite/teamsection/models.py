from django.db import models

# Create your models here.

class TeamMember(models.Model):
    first_name = models.CharField(max_length=180)
    last_name = models.CharField(max_length=180)
    role = models.CharField(max_length=180)
    picture = models.ImageField()
    linkedin = models.CharField(max_length=180)
    twitter = models.CharField(max_length=180)
    facebook = models.CharField(max_length=180)
from cms.models.pluginmodel import CMSPlugin   
class TeamPluginModel(CMSPlugin):
    members = models.ManyToManyField(TeamMember)

    def copy_relations(self, oldinstance):
        self.members.set(oldinstance.members.all())