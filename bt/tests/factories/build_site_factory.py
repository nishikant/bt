import factory

from bt.models.build_site import BuildSite
class BuildSiteFactory(factory.Factory):
    class Meta:
        model = BuildSite

    site_name = "QP"