from model.ProductModel import ProductModel

class PredictService:
    def __init__(self):
        self.test = "haha"

    def predict(self, image: str) -> ProductModel:
        return ProductModel(id=1, name="product test", price=11)