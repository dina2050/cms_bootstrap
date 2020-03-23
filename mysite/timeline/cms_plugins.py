from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .models import TimelinePluginModel
@plugin_pool.register_plugin
class TimelinePlugin(CMSPluginBase):
    model = TimelinePluginModel
    render_template = "timeline.html"
    name = "une super timeline de foufou"
    cache = False