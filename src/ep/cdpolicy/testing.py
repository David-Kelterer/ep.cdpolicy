from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class EpCdpolicy(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import ep.cdpolicy
        xmlconfig.file('configure.zcml',
                       ep.cdpolicy,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ep.cdpolicy:default')

EP_CDPOLICY_FIXTURE = EpCdpolicy()
EP_CDPOLICY_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(EP_CDPOLICY_FIXTURE, ),
                       name="EpCdpolicy:Integration")