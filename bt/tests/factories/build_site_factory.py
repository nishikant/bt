import factory
from .. import models

class BuildSiteFactory(factory.Factory):
    class Meta:
        model = models.BuildSite

    site_name = "QP"