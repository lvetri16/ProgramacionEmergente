import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
import os

# ===============================
# 📂 Cargar dataset
# ===============================
data_dir = r"C:\Users\CHUWI-Notebook\.cache\kagglehub\datasets\moltean\fruits\versions\61\fruits-360_3-body-problem\fruits-360-3-body-problem"

train_dir = os.path.join(data_dir, "Training")
test_dir = os.path.join(data_dir, "Test")

# Aumento de datos para mejorar generalización
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(rescale=1./255)

train_data = train_datagen.flow_from_directory(
    train_dir,
    target_size=(128, 128),
    batch_size=32,
    class_mode="categorical"
)

test_data = test_datagen.flow_from_directory(
    test_dir,
    target_size=(128, 128),
    batch_size=32,
    class_mode="categorical"
)

# ===============================
# 🧠 Crear modelo CNN mejorado
# ===============================
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(128, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Dropout(0.3),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(len(train_data.class_indices), activation='softmax')
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0005),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# ===============================
# 🏋️ Entrenamiento
# ===============================
history = model.fit(
    train_data,
    epochs=10,  # puedes subir a 20 si tienes tiempo
    validation_data=test_data
)

# ===============================
# 💾 Guardar modelo
# ===============================
model.save("modelo_frutas.keras")

print("✅ Modelo entrenado y guardado con éxito")
