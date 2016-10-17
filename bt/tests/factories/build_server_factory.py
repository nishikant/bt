import factory
from bt.models.build_server import BuildServer
from bt.tests.factories.build_site_factory import BuildSiteFactory

class BuildServerFactory(factory.Factory):
    class Meta:
        model = BuildServer

    site_id = factory.SubFactory(BuildSiteFactory)

    server_name = "qpweb1"
    instance_user = "questionpro"
    batch = 1
    start_app = 1
    property_file = 'questionpro'