import json
import requests

from django import http
from django.utils.translation import ugettext_lazy as _
from horizon import tabs
from horizon import exceptions
from .tabs import CephTabs


class IndexView(tabs.TabView):
    # A very simple class-based view...
    tab_group_class = CephTabs
    template_name = 'admin/ceph/index.html'

    def get_osd_tree(self):
        resp = requests.Session().request('GET', 
                                          'http://10.0.120.141:5000/api/v0.1/osd/tree', 
                                           headers = {'Accept': 'application/json', 
                                                      'Content-Type': 'application/json'})
        resp = json.loads(resp.text)
        osd_nodes = resp['output']['nodes']
        id_node = {}
        for node in osd_nodes:
            id_node[node['id']] = node
        for node in osd_nodes:
            if node.has_key('children'):
                children = []
                for child in node['children']:
                    children.append(id_node[child])
                node['children'] = children

        for node in osd_nodes:
            if node['type'] == 'root':
                return node
        return {}

    def get_obj_location(self, pool, object):
        url = 'http://10.0.120.141:5000/api/v0.1/osd/map?pool=%s&object=%s' % (pool, object)
        resp = requests.Session().request('GET',
                                           url,
                                           headers = {'Accept': 'application/json', 
                                                      'Content-Type': 'application/json'})
        resp = json.loads(resp.text)
        return {'location': resp['output']}

    def get(self, request, *args, **kwargs):
        if self.request.GET.get("json", False):
            try:
                osd_tree = self.get_osd_tree()
            except:
                osd_tree = {}
                exceptions.handle(request,
                                  _('Unable to retrieve osd tree.'))
            data = json.dumps(osd_tree)
            return http.HttpResponse(data)
        elif self.request.GET.get("pool", False) != False:
            try:
                osd_loc = self.get_obj_location(self.request.GET.get("pool", False),
                                                self.request.GET.get("object", False))
            except:
                osd_loc = {}
                exceptions.handle(request,
                                  _('Unable to retrieve object location.'))
            data = json.dumps(osd_loc)
            return http.HttpResponse(data)
        else:
            return super(IndexView, self).get(request, *args, **kwargs)

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        return context
