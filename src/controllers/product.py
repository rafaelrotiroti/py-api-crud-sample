from .base import BaseController
from ..services.product import Product as Service

class Product(BaseController):

    def __init__(self):
        self.service = Service()

    def post(self):        
        try:
            data = self.get_json_from_request()
            return self.service.insert_product(data)
        except Exception as e:
            # Melhorar Exceptions com exceções personalizadas.
            return self.return_unexpected_error(e)

    def get(self, product_id=None):
        try:
            if product_id:
                return self.service.load_this_product(product_id)
            products = self.service.load_products()
            return { 'Total de produtos': len(products), 'produtos': products}
        except Exception as e:
            # Melhorar Exceptions com exceções personalizadas.
            return self.return_unexpected_error(e)

    def put(self, product_id):
        try:
            data = self.get_json_from_request()
            return self.service.update_this_product(product_id, data)
        except Exception as e:
            # Melhorar Exceptions com exceções personalizadas.
            return self.return_unexpected_error(e)

    def delete(self, product_id):
        try:
            return self.service.delete_this_product(product_id)
        except Exception as e:
            # Melhorar Exceptions com exceções personalizadas.
            return self.return_unexpected_error(e)
    