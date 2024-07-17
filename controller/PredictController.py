from fastapi import APIRouter, HTTPException
from type.ProductType import ProductResponse
from service.PredictService import PredictService

from type.PredictType import PredictRequest

predict_router = APIRouter()
@predict_router.post("/", response_model=ProductResponse)
def predict_product(request: PredictRequest):
    product = PredictService().predict(request.imageBase64)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
