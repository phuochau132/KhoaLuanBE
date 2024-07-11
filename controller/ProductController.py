from fastapi import APIRouter, HTTPException
from typing import List
from service.ProductService import ProductService
from type.ProductType import Product

product_router = APIRouter()
product_service = ProductService()

@product_router.get("/", response_model=List[Product])
async def get_products():
    products = await product_service.getProducts()
    return products
