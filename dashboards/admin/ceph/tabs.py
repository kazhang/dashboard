from django.core.urlresolvers import reverse  # noqa
from django.utils.translation import ugettext_lazy as _  # noqa

from horizon import exceptions
from horizon import tabs

from openstack_dashboard import api


class OverviewTab(tabs.Tab):
    name = _("Overview")
    slug = "overview"
    template_name = "admin/ceph/_overview.html"

    def get_context_data(self, request):
        return None

class TopologyTab(tabs.Tab):
    name = _("Topology")
    slug = "topology"
    template_name = "admin/ceph/_topology.html"
    preload = False

    def get_context_data(self, request):
        return None

class CephTabs(tabs.TabGroup):
    slug = "ceph_tabs"
    tabs = (OverviewTab, TopologyTab, )
