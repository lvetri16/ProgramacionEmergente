import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os
from PIL import Image
import customtkinter as ctk
from tkinter import filedialog
import threading
import time

# ----------------------------
# CONFIGURACIÓN DE LA APP
# ----------------------------
ctk.set_appearance_mode("light")  # "light", "dark" o "system"
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("🍎 Clasificador de Frutas con IA")
app.geometry("460x650")
app.resizable(False, False)

# ----------------------------
# CARGAR EL MODELO
# ----------------------------
model = tf.keras.models.load_model("modelo_frutas.keras")

# Ruta del dataset (para obtener nombres de clases)
data_dir = r"C:\Users\CHUWI-Notebook\.cache\kagglehub\datasets\moltean\fruits\versions\61\fruits-360_3-body-problem\fruits-360-3-body-problem\Training"
clases = sorted(os.listdir(data_dir))

# ----------------------------
# FUNCIONES
# ----------------------------
def analizar_imagen(file_path):
    """Analiza la imagen en un hilo separado para no congelar la interfaz"""
    time.sleep(1)  # Pequeña pausa visual
    progreso.set(0.3)
    app.update_idletasks()

    img = Image.open(file_path)
    img_array = image.img_to_array(img.resize((128, 128))) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    progreso.set(0.6)
    app.update_idletasks()

    # Predicción
    pred = model.predict(img_array)
    indice = np.argmax(pred)
    fruta_predicha = clases[indice]
    confianza = np.max(pred) * 100

    progreso.set(1.0)
    app.update_idletasks()

    # Cambiar color según confianza
    color = "#2b9348" if confianza > 80 else "#ee9b00" if confianza > 60 else "#d00000"

    resultado_label.configure(
        text=f"🍇 Fruta: {fruta_predicha}\nConfianza: {confianza:.2f}%",
        text_color=color
    )
    boton_subir.configure(state="normal")
    boton_reiniciar.configure(state="normal")


def cargar_imagen():
    file_path = filedialog.askopenfilename(
        filetypes=[("Archivos de imagen", "*.jpg *.png *.jpeg")]
    )
    if not file_path:
        return

    # Mostrar imagen seleccionada
    img = Image.open(file_path)
    img = img.resize((250, 250))
    img_tk = ctk.CTkImage(light_image=img, size=(250, 250))
    panel_img.configure(image=img_tk)
    panel_img.image = img_tk

    resultado_label.configure(text="🔍 Analizando imagen...", text_color="#333")
    progreso.set(0)
    boton_subir.configure(state="disabled")
    boton_reiniciar.configure(state="disabled")

    # Analizar en segundo plano
    threading.Thread(target=analizar_imagen, args=(file_path,), daemon=True).start()


def reiniciar():
    """Limpia la pantalla para analizar una nueva imagen"""
    panel_img.configure(image=None)
    panel_img.image = None
    resultado_label.configure(text="Sube una imagen para clasificar 🍌", text_color="#000")
    progreso.set(0)

# ----------------------------
# INTERFAZ GRÁFICA
# ----------------------------
titulo = ctk.CTkLabel(app, text="Clasificador de Frutas con IA", font=("Arial Rounded MT Bold", 22))
titulo.pack(pady=20)

frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(pady=10, padx=20, fill="both", expand=False)

panel_img = ctk.CTkLabel(frame, text="", width=250, height=250)
panel_img.pack(pady=20)

boton_subir = ctk.CTkButton(
    app,
    text="📂 Seleccionar imagen",
    command=cargar_imagen,
    font=("Arial", 14),
    width=220,
    height=40,
    corner_radius=10
)
boton_subir.pack(pady=10)

progreso = ctk.CTkProgressBar(app, width=300)
progreso.pack(pady=10)
progreso.set(0)

resultado_label = ctk.CTkLabel(app, text="Sube una imagen para clasificar 🍎", font=("Arial", 14))
resultado_label.pack(pady=15)

boton_reiniciar = ctk.CTkButton(
    app,
    text="🔄 Reiniciar",
    command=reiniciar,
    font=("Arial", 13),
    width=150,
    height=35,
    corner_radius=8,
    fg_color="#999",
    hover_color="#777"
)
boton_reiniciar.pack(pady=10)
boton_reiniciar.configure(state="disabled")

creditos = ctk.CTkLabel(app, text="Desarrollado por Diego Gonzalez 💻", font=("Arial", 10), text_color="#555")
creditos.pack(side="bottom", pady=5)

# ----------------------------
# INICIAR APP
# ----------------------------
app.mainloop()
