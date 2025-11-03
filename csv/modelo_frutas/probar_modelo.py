import tensorflow as tf
import numpy as np
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras.preprocessing import image
import os



# Cargar modelo
model = tf.keras.models.load_model("modelo_frutas.keras")

# Cargar las clases (etiquetas de frutas)
data_dir = r"C:\Users\CHUWI-Notebook\.cache\kagglehub\datasets\moltean\fruits\versions\61\fruits-360_3-body-problem\fruits-360-3-body-problem\Training"



clases = sorted(os.listdir(data_dir))

# Cargar imagen a probar
img_path = 'manzana.jpg'


 # 🔹 cambia por una imagen real
img = image.load_img(img_path, target_size=(100, 100))
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

# Predicción
predicciones = model.predict(img_array)
indice = np.argmax(predicciones)
print("🍎 Fruta predicha:", clases[indice])
