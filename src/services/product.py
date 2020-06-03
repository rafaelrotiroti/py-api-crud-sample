from ..models.product import Product as ProductModel, db
from ..serializer import ProductSchema

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

class Product:


    def __init__(self):
        self.product_schema = ProductSchema()


    def insert_product(self, data):
        product =  ProductModel(data['valor'], data['url'], data['nome'])
        db.session.add(product)
        db.session.commit()
        return product_schema.dump(product)

    def load_products(self):
        products_schema = ProductSchema(many=True)
        products_query = ProductModel.query.all()
        return products_schema.dump(products_query)

    def load_this_product(self, product_id):
        product_schema = ProductSchema()
        product_query = ProductModel.query.filter_by(id=product_id).one()
        return product_schema.dump(product_query)

    def delete_this_product(self, product_id):
        product = ProductModel.query.filter_by(id=product_id).one()
        db.session.delete(product)
        db.session.commit()
        return {'Produto': product_id, 'Deletado': True }

    def update_this_product(self, product_id, data):
        product_schema = ProductSchema()
        this_product = ProductModel.query.filter_by(id=product_id).one()
        
        this_product.valor = data['valor']
        this_product.url = data['url']
        this_product.nome = data['nome']
        
        db.session.commit()

        return product_schema.dump(this_product)
