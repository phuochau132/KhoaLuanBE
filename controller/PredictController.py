from fastapi import APIRouter, HTTPException
from type.ProductType import Product
from service.PredictService import PredictService

from type.PredictType import PredictRequest

predict_router = APIRouter()
@predict_router.post("/", response_model=Product)
def predict_product(request: PredictRequest):
    product = PredictService().predict(request.imageBase64)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
