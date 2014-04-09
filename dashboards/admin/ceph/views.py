from horizon import tabs
from .tabs import CephTabs


class IndexView(tabs.TabView):
    # A very simple class-based view...
    tab_group_class = CephTabs
    template_name = 'admin/ceph/index.html'

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        return context
