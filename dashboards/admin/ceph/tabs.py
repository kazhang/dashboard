from django.core.urlresolvers import reverse  # noqa
from django.utils.translation import ugettext_lazy as _  # noqa

from horizon import exceptions
from horizon import tabs

from openstack_dashboard import api

from .tables import CRUSHRuleTable

import requests
import json

class OverviewTab(tabs.Tab):
    name = _("Overview")
    slug = "overview"
    template_name = "admin/ceph/_overview.html"

    def get_context_data(self, request):
        resp = requests.Session().request('GET', 
                                          'http://10.0.120.141:5000/api/v0.1/status', 
                                           headers = {'Accept': 'application/json', 'Content-Type': 'application/json'})
        return {'resp': resp}

class TopologyTab(tabs.Tab):
    name = _("Topology")
    slug = "topology"
    template_name = "admin/ceph/_topology.html"
    preload = False

    def get_context_data(self, request):
        return None

class CRUSHRuleTab(tabs.TableTab):
    name = _("CRUSH Rule")
    slug = "CRUSHRule"
    table_classes = (CRUSHRuleTable,)
    template_name = "horizon/common/_detail_table.html"
    preload = False

    def get_CRUSHRule_data(self):
        resp = requests.Session().request('GET', 
                                          'http://10.0.120.141:5000/api/v0.1/osd/crush/rule/dump', 
                                           headers = {'Accept': 'application/json', 'Content-Type': 'application/json'})
        data = json.loads(resp.text)
        data = data['output']
        return data

class QueryTab(tabs.Tab):
    name = _("Query")
    slug = "query"
    template_name = "admin/ceph/_query.html"
    preload = False

    def get_context_data(self, request):
        return None

class CephTabs(tabs.TabGroup):
    slug = "ceph_tabs"
    tabs = (OverviewTab, TopologyTab, CRUSHRuleTab, QueryTab)
