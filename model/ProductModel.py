class ProductModel:
    def __init__(self, image, product_name, price, label_id, id=None, class_name=None):
        self.id = id  # Optional field
        self.label_id = label_id
        self.image = image
        self.product_name = product_name
        self.price = price
        self.class_name = class_name  # Optional field

    def to_dict(self):
        return {
            'id': self.id,
            'label_id': self.label_id,
            'image': self.image,
            'product_name': self.product_name,
            'price': self.price,
            'class_name': self.class_name
        }
