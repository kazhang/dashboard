from django.utils.translation import ugettext_lazy as _ 

from horizon import tables

#class RuleFilterAction(tables.FilterAction):
#    def filter(self, rules, filter_string):
#        q = filter_string.lower()
#
#        def comp(rule):
#            if q in rule.lower():
#                return True
#            return False
#
#        return filter(comp, tenants)

class CRUSHRuleTable(tables.DataTable):
    rule_id = tables.Column("rule_id",
                            verbose_name=_("Rule ID"))
    rule_name = tables.Column("rule_name",
                              verbose_name=_("Rule Name"))
    rule_type = tables.Column("type",
                              verbose_name=_("Rule Type"))

    def get_object_id(self, obj):
        return obj['rule_id']

    class Meta:
        name = "CRUSHRule"
        verbose_name = _("CRUSH Rules")
