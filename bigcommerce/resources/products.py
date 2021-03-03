from .base import *


class Products(ListableApiResource, CreateableApiResource,
               UpdateableApiResource, DeleteableApiResource,
               CollectionDeleteableApiResource, CountableApiResource):
    resource_name = 'products'

    def configurable_fields(self, id=None):
        if id:
            return ProductConfigurableFields.get(self.id, id, connection=self._connection)
        else:
            return ProductConfigurableFields.iterall(self.id, connection=self._connection)

    def custom_fields(self, id=None):
        if id:
            return ProductCustomFields.get(self.id, id, connection=self._connection)
        else:
            return ProductCustomFields.iterall(self.id, connection=self._connection)

    def discount_rules(self, id=None):
        if id:
            return ProductDiscountRules.get(self.id, id, connection=self._connection)
        else:
            return ProductDiscountRules.iterall(self.id, connection=self._connection)

    def images(self, id=None):
        if id:
            return ProductImages.get(self.id, id, connection=self._connection)
        else:
            return ProductImages.iterall(self.id, connection=self._connection)

    def options(self, id=None):
        if id:
            return ProductOptions.get(self.id, id, connection=self._connection)
        else:
            return ProductOptions.iterall(self.id, connection=self._connection)

    def reviews(self, id=None):
        if id:
            return ProductReviews.get(self.id, id, connection=self._connection)
        else:
            return ProductReviews.iterall(self.id, connection=self._connection)

    def rules(self, id=None):
        if id:
            return ProductRules.get(self.id, id, connection=self._connection)
        else:
            return ProductRules.iterall(self.id, connection=self._connection)

    def skus(self, id=None):
        if id:
            return ProductSkus.get(self.id, id, connection=self._connection)
        else:
            return ProductSkus.iterall(self.id, connection=self._connection)

    def videos(self, id=None):
        if id:
            return ProductVideos.get(self.id, id, connection=self._connection)
        else:
            return ProductVideos.iterall(self.id, connection=self._connection)

    def google_mappings(self):
        return GoogleProductSearchMappings.iterall(self.id, connection=self._connection)


class ProductConfigurableFields(ListableApiSubResource, DeleteableApiSubResource,
                                CollectionDeleteableApiSubResource, CountableApiSubResource):
    resource_name = 'configurable_fields'
    parent_resource = 'products'
    parent_key = 'product_id'
    count_resource = 'products/configurable_fields'


class ProductCustomFields(ListableApiSubResource, CreateableApiSubResource,
                          UpdateableApiSubResource, DeleteableApiSubResource,
                          CollectionDeleteableApiSubResource, CountableApiSubResource):
    resource_name = 'custom_fields'
    parent_resource = 'products'
    parent_key = 'product_id'
    count_resource = 'products/custom_fields'


class ProductDiscountRules(ListableApiSubResource, CreateableApiSubResource,
                           UpdateableApiSubResource, DeleteableApiSubResource,
                           CollectionDeleteableApiSubResource, CountableApiSubResource):
    resource_name = 'discount_rules'
    parent_resource = 'products'
    parent_key = 'product_id'
    count_resource = 'products/discount_rules'


class ProductImages(ListableApiSubResource, CreateableApiSubResource,
                    UpdateableApiSubResource, DeleteableApiSubResource,
                    CollectionDeleteableApiSubResource, CountableApiSubResource):
    resource_name = 'images'
    parent_resource = 'products'
    parent_key = 'product_id'
    count_resource = 'products/images'


class ProductOptions(ListableApiSubResource):
    resource_name = 'options'
    parent_resource = 'products'
    parent_key = 'product_id'


class ProductReviews(ListableApiSubResource, CreateableApiSubResource,
                   UpdateableApiSubResource, DeleteableApiSubResource,
                   CollectionDeleteableApiSubResource, CountableApiSubResource):
    resource_name = 'reviews'
    parent_resource = 'products'
    parent_key = 'product_id'
    count_resource = 'products/reviews'


class ProductRules(ListableApiSubResource, CreateableApiSubResource,
                   UpdateableApiSubResource, DeleteableApiSubResource,
                   CollectionDeleteableApiSubResource, CountableApiSubResource):
    resource_name = 'rules'
    parent_resource = 'products'
    parent_key = 'product_id'
    count_resource = 'products/rules'


class ProductSkus(ListableApiSubResource, CreateableApiSubResource,
                  UpdateableApiSubResource, DeleteableApiSubResource,
                  CollectionDeleteableApiSubResource, CountableApiSubResource):
    resource_name = 'skus'
    parent_resource = 'products'
    parent_key = 'product_id'
    count_resource = 'products/skus'


class ProductVideos(ListableApiSubResource, CountableApiSubResource, 
                    CreateableApiSubResource, DeleteableApiSubResource, 
                    CollectionDeleteableApiSubResource):
    resource_name = 'videos'
    parent_resource = 'products'
    parent_key = 'product_id'
    count_resource = 'products/videos'


class GoogleProductSearchMappings(ListableApiSubResource):
    resource_name = 'googleproductsearch'
    parent_resource = 'products'
    parent_key = 'product_id'
