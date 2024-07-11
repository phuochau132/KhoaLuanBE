class ProductModel:
    def __init__(self, id, label_id, class_name, image, product_name, price):
        self.id = id
        self.label_id = label_id
        self.class_name = class_name
        self.image = image
        self.product_name = product_name
        self.price = price

    def to_dict(self):
        return {
            'id': self.id,
            'label_id': self.label_id,
            'class_name': self.class_name,
            'image': self.image,
            'product_name': self.product_name,
            'price': self.price
        }
