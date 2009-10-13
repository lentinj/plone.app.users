from zope.component import adapts
from zope.formlib import form
from zope.interface import implements

from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone import PloneMessageFactory as _
from Products.CMFPlone.interfaces import IPloneSiteRoot

from plone.app.controlpanel.form import ControlPanelForm
from registrationschema import IRegistrationSchema, UserDataWidget


# Property as it is named in portal_properties
JOIN_FORM_FIELDS='join_form_fields'


class RegistrationControlPanelAdapter(SchemaAdapterBase):

    adapts(IPloneSiteRoot)
    implements(IRegistrationSchema)

    def __init__(self, context):
        super(RegistrationControlPanelAdapter, self).__init__(context)
        pprop = getToolByName(context, 'portal_properties')
        self.context = pprop.site_properties

    def set_joinformfields(self, value):

        self.context._updateProperty(JOIN_FORM_FIELDS, value)


    def get_joinformfields(self):

        return self.context.getProperty(JOIN_FORM_FIELDS,[])

    join_form_fields = property(get_joinformfields, set_joinformfields)



class RegistrationControlPanel(ControlPanelForm):

    form_fields = form.FormFields(IRegistrationSchema)

    form_fields['join_form_fields'].custom_widget = UserDataWidget
    
    label = _("Registration settings")
    description = _("Registration settings for this site.")
    form_name = _("Registration settings")