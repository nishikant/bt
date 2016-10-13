import factory
from .. import models
from . import

class BuildServerFactory(factory.Factory):
    class Meta:
        model = models.BuildServer

    site_id =