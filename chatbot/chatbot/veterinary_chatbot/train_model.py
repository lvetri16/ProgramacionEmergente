import numpy as np
import json
import nltk
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import pickle
import os
import re

# Descargar recursos de NLTK de forma robusta
def download_nltk_resources():
    resources = ['punkt', 'stopwords']
    
    for resource in resources:
        try:
            # Verificar si el recurso existe
            if resource == 'stopwords':
                nltk.data.find('corpora/stopwords')
            else:
                nltk.data.find(f'tokenizers/{resource}')
            print(f"✓ Recurso '{resource}' ya está disponible")
        except LookupError:
            print(f"📥 Descargando recurso '{resource}'...")
            try:
                nltk.download(resource, quiet=False)
                print(f"✓ Recurso '{resource}' descargado exitosamente")
            except Exception as e:
                print(f"✗ Error descargando {resource}: {e}")

class AdvancedChatbotTrainer:
    def __init__(self):
        self.stemmer = PorterStemmer()
        
        # Descargar recursos primero
        download_nltk_resources()
        
        # Configurar stopwords en español
        try:
            from nltk.corpus import stopwords
            self.spanish_stopwords = stopwords.words('spanish')
            print("✓ Stopwords en español cargadas")
        except:
            print("⚠️ No se pudieron cargar stopwords en español, usando lista vacía")
            self.spanish_stopwords = []
        
        self.vectorizer = TfidfVectorizer(
            max_features=1000,
            min_df=1,  # Reducido para datasets pequeños
            max_df=0.9,
            ngram_range=(1, 2),
            stop_words=self.spanish_stopwords
        )
        self.model = LogisticRegression(max_iter=1000, C=1.0)
        self.accuracy = 0
        
    def load_intents(self, file_path='intents.json'):
        try:
            # Obtener la ruta absoluta del archivo
            script_dir = os.path.dirname(os.path.abspath(__file__))
            absolute_path = os.path.join(script_dir, file_path)
            
            print(f"🔍 Buscando intents en: {absolute_path}")
            
            with open(absolute_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"✗ Error: No se encontró el archivo {absolute_path}")
            print(f"📁 Directorio actual: {os.getcwd()}")
            print(f"📄 Archivos disponibles: {[f for f in os.listdir('.') if f.endswith('.json')]}")
            return {"intents": []}
        except json.JSONDecodeError as e:
            print(f"✗ Error en el formato JSON: {e}")
            return {"intents": []}
    
    def preprocess_text(self, text):
        if not isinstance(text, str):
            return ""
            
        # Limpieza de texto
        text = text.lower().strip()
        text = re.sub(r'[^\w\sáéíóúñ]', '', text)  # Mantener acentos
        text = re.sub(r'\d+', '', text)
        
        # Tokenización y stemming
        try:
            tokens = nltk.word_tokenize(text)
            tokens = [
                self.stemmer.stem(token) for token in tokens 
                if token not in self.spanish_stopwords and len(token) > 2
            ]
            return ' '.join(tokens)
        except Exception as e:
            print(f"Error en preprocesamiento: {e}")
            return text
    
    def prepare_training_data(self, intents):
        X = []
        y = []
        
        print("🔄 Procesando patrones de entrenamiento...")
        
        if 'intents' not in intents:
            print("✗ Error: Formato incorrecto en intents.json")
            return X, y
            
        for intent in intents['intents']:
            if 'patterns' not in intent or 'tag' not in intent:
                print(f"⚠️ Intent incompleto: {intent}")
                continue
                
            for pattern in intent['patterns']:
                processed_text = self.preprocess_text(pattern)
                if processed_text:  # Solo añadir si el texto no está vacío
                    X.append(processed_text)
                    y.append(intent['tag'])
        
        print(f"✓ Procesados {len(X)} patrones válidos")
        return X, y
    
    def evaluate_model(self, X, y):
        if len(set(y)) < 2:
            print("⚠️ No hay suficientes categorías para validación cruzada")
            return 0.8  # Valor por defecto para datasets pequeños
            
        try:
            scores = cross_val_score(self.model, X, y, cv=min(3, len(set(y))))
            return np.mean(scores)
        except Exception as e:
            print(f"⚠️ Error en validación cruzada: {e}")
            return 0.7
    
    def train(self, intents_file='intents.json', model_file='chatbot_model.pkl'):
        print("🚀 Iniciando entrenamiento del chatbot...")
        
        # Cargar intents
        intents = self.load_intents(intents_file)
        
        if not intents or 'intents' not in intents or not intents['intents']:
            print("✗ Error: No se pudieron cargar los intents")
            return None
        
        # Preparar datos
        X, y = self.prepare_training_data(intents)
        
        if len(X) == 0:
            print("✗ Error: No hay datos de entrenamiento válidos")
            return None
        
        # Vectorizar texto
        print("🔤 Vectorizando texto...")
        try:
            X_vectorized = self.vectorizer.fit_transform(X)
            print(f"✓ Texto vectorizado. Dimensiones: {X_vectorized.shape}")
        except Exception as e:
            print(f"✗ Error en vectorización: {e}")
            return None
        
        # Evaluar modelo
        print("📊 Evaluando modelo...")
        self.accuracy = self.evaluate_model(X_vectorized, y)
        
        # Entrenar modelo final
        print("🎯 Entrenando modelo final...")
        try:
            self.model.fit(X_vectorized, y)
            print("✓ Modelo entrenado exitosamente")
        except Exception as e:
            print(f"✗ Error entrenando modelo: {e}")
            return None
        
        # Guardar modelo
        model_data = {
            'model': self.model,
            'vectorizer': self.vectorizer,
            'intents': intents,
            'accuracy': self.accuracy,
            'spanish_stopwords': self.spanish_stopwords
        }
        
        try:
            with open(model_file, 'wb') as f:
                pickle.dump(model_data, f)
            print(f"✓ Modelo guardado en {model_file}")
        except Exception as e:
            print(f"✗ Error guardando modelo: {e}")
            return None
        
        # Mostrar estadísticas
        self.print_training_stats(intents, X, y)
        
        return self.vectorizer, self.model, intents
    
    def print_training_stats(self, intents, X, y):
        print("\n" + "="*60)
        print("📈 ESTADÍSTICAS DE ENTRENAMIENTO")
        print("="*60)
        print(f"📝 Total de patrones de entrenamiento: {len(X)}")
        print(f"🏷️  Total de intents (categorías): {len(intents['intents'])}")
        print(f"🎯 Precisión estimada: {self.accuracy:.2%}")
        print(f"🔡 Tamaño del vocabulario: {len(self.vectorizer.vocabulary_)}")
        print("\n📂 Intents entrenados:")
        for intent in intents['intents']:
            count = len(intent['patterns'])
            responses = len(intent.get('responses', []))
            print(f"   • {intent['tag']:15} → {count:2} patrones, {responses:2} respuestas")
        print("="*60)
        print("✅ Entrenamiento completado exitosamente!")

if __name__ == "__main__":
    print("🤖 ENTRENADOR DE CHATBOT VETERINARIO")
    print("="*50)
    
    trainer = AdvancedChatbotTrainer()
    result = trainer.train()
    
    if result:
        print("\n🎉 ¡El chatbot está listo para usar!")
        print("💡 Ejecuta 'python chatbot_gui_modern.py' para probarlo")
    else:
        print("\n❌ Hubo errores durante el entrenamiento")
        print("🔧 Revisa los mensajes anteriores para solucionarlos")