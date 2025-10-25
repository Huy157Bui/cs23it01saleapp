from cs23it01saleapp.saleappv2.eapp.models import Category, Product

def get_categories():
    return Category.query.all()
def get_products(kw=None, category_id=None):
    products = Product.query

    if category_id:
        products = products.filter(Product.category_id==category_id)

    if kw:
        products = products.filter(Product.name.contains(kw))

    return products.all()