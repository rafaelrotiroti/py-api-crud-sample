from flask_restful import Api
from .controllers.product import Product

def create_api(app):
    
    api = Api(app)

    api.add_resource(Product, '/products', '/products/<int:product_id>')

