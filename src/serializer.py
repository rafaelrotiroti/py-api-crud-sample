from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field, ModelSchema

from .models.product import Product as ProductModel

ma = Marshmallow()

def configuration(app):
    ma.init_app(app)


class ProductSchema(ModelSchema):
    class Meta:
        model = ProductModel
        include_fk = True
        load_instance = True
