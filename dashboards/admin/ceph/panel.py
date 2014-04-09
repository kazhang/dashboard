from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.admin import dashboard


class Ceph(horizon.Panel):
    name = _("Ceph")
    slug = "ceph"


dashboard.Admin.register(Ceph)
