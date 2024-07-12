from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from service.ProductService import ProductService
from type.ProductType import Product,ProductCreation
from model.ProductModel import ProductModel

product_router = APIRouter()
product_service = ProductService()

class ProductCreate(BaseModel):
    label_id: int
    image: str
    product_name: str
    price: int
class ProductUpdate(BaseModel):
    label_id: int
    image: str
    product_name: str
    price: int

@product_router.get("/", response_model=List[Product])
async def get_products():
    products = await product_service.getProducts()
    return products

@product_router.post("/", response_model=ProductCreation)
async def create_product(product_create: ProductCreate):
    product = ProductModel(
        label_id=product_create.label_id,
        image=product_create.image,
        product_name=product_create.product_name,
        price=product_create.price
    )
    created_product = await product_service.createProduct(product)
    return created_product

@product_router.put("/{id}", response_model=Product)
async def update_product(id: int, product_update: ProductUpdate):
    product = ProductModel(
        label_id=product_update.label_id,
        image=product_update.image,
        product_name=product_update.product_name,
        price=product_update.price
    )
    updated_product = await product_service.updateProductById(id, product)
    return updated_product

@product_router.delete("/{id}", response_model=bool)
async def delete_product(id: int):
    success = await product_service.delProductById(id)
    print("success", success)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return success
