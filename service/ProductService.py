from typing import List
from model.ProductModel import ProductModel
from model.ProductCreationModel import ProductCreationModel
from dao.ProductDao import getAllProduct, createProduct, updateProductById, delProductById

class ProductService:
    async def getProducts(self) -> List[ProductModel]:
        products = await getAllProduct()
        return [ProductModel(**product) for product in products]

    async def createProduct(self, product) -> ProductCreationModel:
        await createProduct(product)
        created_product = ProductModel(
            label_id=product.label_id,
            image=product.image,
            product_name=product.product_name,
            price=product.price
        )
        return product

    async def updateProductById(self, id: int, product: ProductModel) -> ProductModel:
        await updateProductById(id, product.to_dict())
        return product

    async def delProductById(self, id: int) -> bool:
        return await delProductById(id)
