import kagglehub

# Descargar el dataset de frutas
path = kagglehub.dataset_download("moltean/fruits")

print("✅ Dataset descargado correctamente.")
print("📂 Ruta de los archivos:", path)
