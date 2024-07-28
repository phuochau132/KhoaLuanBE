import tensorflow as tf
import numpy as np
from pathlib import Path
from model.ProductModel import ProductModel
import os
import matplotlib.pyplot as plt

class ModelInference:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModelInference, cls).__new__(cls)
            cls._instance.labels = [
                "grocery-products", 
                "Bisconni Chocolate Chip Cookies 46.8gm", 
                "Coca Cola Can 250ml", 
                "Colgate Maximum Cavity Protection 75gm", 
                "Fanta 500ml", 
                "Fresher Guava Nectar 500ml", 
                "Fruita Vitals Red Grapes 200ml", 
                "Islamabad Tea 238gm", 
                "Kolson Slanty Jalapeno 18gm", 
                "Kurkure Chutney Chaska 62gm", 
                "LU Candi Biscuit 60gm", 
                "LU Oreo Biscuit 19gm", 
                "LU Prince Biscuit 55.2gm", 
                "Lays Masala 34gm", 
                "Lays Wavy Mexican Chili 34gm", 
                "Lifebuoy Total Protect Soap 96gm", 
                "Lipton Yellow Label Tea 95gm", 
                "Meezan Ultra Rich Tea 190gm", 
                "Peek Freans Sooper Biscuit 13.2gm", 
                "Safeguard Bar Soap Pure White 175gm", 
                "Shezan Apple 250ml", 
                "Sunsilk Shampoo Soft - Smooth 160ml", 
                "Super Crisp BBQ 30gm", 
                "Supreme Tea 95gm", 
                "Tapal Danedar 95gm", 
                "Vaseline Healthy White Lotion 100ml"
            ]

            current_file = Path(__file__).resolve()
            base_dir = current_file.parent.parent  # Đây là thư mục gốc của dự án
            # Đường dẫn tới file model_checkpoint.h5
            model_path = base_dir / "static" / "vit_v2"
            try:
                cls._instance.model = tf.keras.models.load_model(model_path)
                print("Model loaded successfully.")
            except Exception as e:
                print(f"Error loading model: {e}")
                cls._instance.model = None
        return cls._instance

    def predict(self, image_array) -> int:
        if self.model is None:
            return -1
        try:
            print(image_array.shape)
            plt.imshow(image_array)
            plt.axis('off') 
            plt.savefig('temp_image2.png')  
            plt.close() 
            output = self.model(np.expand_dims(image_array, axis=0))
            print(f"Model output: {output}")
            label = self.labels[np.argmax(output)]
            print(f"Predicted label: {label}")
            return np.argmax(output)

        except Exception as e:
            print(f"Error during prediction: {e}")
            return -1