import factory
from .. import models
from . import BuildSiteFactory

class BuildServerFactory(factory.Factory):
    class Meta:
        model = models.BuildServer

    site_id = factory.SubFactory(BuildSiteFactory)

    server_name = "qpweb1"
    instance_user = "questionpro"
    batch = 1
    start_app = 1
    property_file = 'questionpro'