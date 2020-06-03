from .base import BaseController
from ..services.product import Product as Service

class Product(BaseController):

    def __init__(self):
        self.service = Service()

    def post(self):
        data = self.get_json_from_request()
        return self.service.insert_product(data)

    def get(self, product_id=None):
        if product_id:
            return self.service.load_this_product(product_id)
        products = self.service.load_products()
        return { 'Total de produtos': len(products), 'produtos': products}

    def put(self, product_id):
        data = self.get_json_from_request()
        return self.service.update_this_product(product_id, data)

    def delete(self, product_id):
        return self.service.delete_this_product(product_id)
    