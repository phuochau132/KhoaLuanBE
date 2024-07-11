from typing import List
from model.ProductModel import ProductModel
from dao.ProductDao import getAllProduct

class ProductService:
    def __init__(self):
        self.test = "haha"

    async def getProducts(self) -> List[ProductModel]:
        products = await getAllProduct()
        return [ProductModel(**product) for product in products]
