from ..base import ShopifyResource
from shopify import mixins


class Variant(ShopifyResource, mixins.Metafields):
    pass
