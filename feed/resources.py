from import_export import resources
from .models import Catagory, Product, Cart

class CatagoryResource(resources.ModelResource):
    class Meta:
        model = Catagory

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product

class CartResource(resources.ModelResource):
    class Meta:
        model = Cart
