from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .models import TeamPluginModel
@plugin_pool.register_plugin
class TeamPlugin(CMSPluginBase):
    model = TeamPluginModel
    render_template = "team.html"
    name = "our team"
    cache = False