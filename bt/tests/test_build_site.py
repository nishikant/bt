from .factories.build_site_factory import BuildSiteFactory

class TestBuildSite():

    def test_qp_build_site(self):
        site = BuildSiteFactory()
        assert site.site_name == 'QP'

    def test_sa_build_site(self):
        site = BuildSiteFactory(site_name="SA")
        assert site.site_name == 'SA'

