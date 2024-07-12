class ProductCreationModel:
    def __init__(self, image, product_name, price, label_id):
        self.label_id = label_id
        self.image = image
        self.product_name = product_name
        self.price = price
    def to_dict(self):
        return {
            'label_id': self.label_id,
            'image': self.image,
            'product_name': self.product_name,
            'price': self.price,
        }
