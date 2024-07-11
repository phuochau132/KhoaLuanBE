from pydantic import BaseModel

class Product(BaseModel):
    id: int
    label_id: int
    class_name: str
    image: str
    product_name: str
    price: int
