import numpy as np
import json
import nltk
import pickle
import random
import re
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

# Función para descargar recursos
def download_nltk_resources():
    resources = ['punkt', 'stopwords']
    
    for resource in resources:
        try:
            if resource == 'stopwords':
                nltk.data.find('corpora/stopwords')
            else:
                nltk.data.find(f'tokenizers/{resource}')
        except LookupError:
            print(f"📥 Descargando {resource}...")
            nltk.download(resource, quiet=True)

class EnhancedVeterinaryChatbot:
    def __init__(self, model_file='chatbot_model.pkl'):
        self.stemmer = PorterStemmer()
        self.conversation_history = []
        self.user_context = {
            'mascota_tipo': None,
            'mascota_edad': None,
            'ultimo_intent': None
        }
        
        # Descargar recursos primero
        download_nltk_resources()
        
        # Cargar stopwords
        try:
            from nltk.corpus import stopwords
            self.spanish_stopwords = stopwords.words('spanish')
        except:
            self.spanish_stopwords = []
        
        self.load_model(model_file)
        
    def load_model(self, model_file):
        try:
            with open(model_file, 'rb') as f:
                model_data = pickle.load(f)
            
            self.model = model_data['model']
            self.vectorizer = model_data['vectorizer']
            self.intents = model_data['intents']
            self.accuracy = model_data.get('accuracy', 0)
            self.spanish_stopwords = model_data.get('spanish_stopwords', [])
            
            print(f"✅ Modelo cargado (Precisión: {self.accuracy:.2%})")
            print(f"📊 Intents disponibles: {len(self.intents['intents'])}")
            
        except FileNotFoundError:
            print("❌ Modelo no encontrado. Ejecuta primero: python train_model.py")
            exit()
        except Exception as e:
            print(f"❌ Error cargando modelo: {e}")
            exit()
    
    def preprocess_text(self, text):
        if not isinstance(text, str):
            return ""
            
        # Limpieza de texto
        text = text.lower().strip()
        text = re.sub(r'[^\w\sáéíóúñ]', '', text)
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
            return text
    
    def extract_entities(self, text):
        # Extraer información importante del texto
        entities = {
            'mascota_tipo': None,
            'mascota_edad': None,
            'urgencia': False
        }
        
        text_lower = text.lower()
        
        # Detectar tipo de mascota
        if any(word in text_lower for word in ['perro', 'canino', 'cachorro', 'perrito']):
            entities['mascota_tipo'] = 'perro'
        elif any(word in text_lower for word in ['gato', 'felino', 'gatito', 'minino']):
            entities['mascota_tipo'] = 'gato'
        
        # Detectar edad
        edad_patterns = [
            r'(\d+)\s*(meses|mes)',
            r'(\d+)\s*(años|año)',
            r'cachorro|gatito',
            r'adulto|anciano'
        ]
        
        for pattern in edad_patterns:
            match = re.search(pattern, text_lower)
            if match:
                if 'cachorro' in match.group() or 'gatito' in match.group():
                    entities['mascota_edad'] = 'cachorro'
                elif 'adulto' in match.group():
                    entities['mascota_edad'] = 'adulto'
                elif 'anciano' in match.group():
                    entities['mascota_edad'] = 'anciano'
                elif match.group(1):
                    entities['mascota_edad'] = match.group(1) + ' ' + match.group(2)
                break
        
        # Detectar urgencia
        urgent_words = ['emergencia', 'urgente', 'grave', 'accidente', 'envenenamiento', 'sangrado']
        entities['urgencia'] = any(word in text_lower for word in urgent_words)
        
        return entities
    
    def update_context(self, entities, intent):
        # Actualizar contexto de la conversación
        if entities['mascota_tipo']:
            self.user_context['mascota_tipo'] = entities['mascota_tipo']
        if entities['mascota_edad']:
            self.user_context['mascota_edad'] = entities['mascota_edad']
        
        self.user_context['ultimo_intent'] = intent
        
        # Guardar en historial
        self.conversation_history.append({
            'intent': intent,
            'entities': entities,
            'context': self.user_context.copy()
        })
    
    def predict_intent(self, message):
        try:
            # Preprocesar mensaje
            processed_text = self.preprocess_text(message)
            
            # Vectorizar
            X = self.vectorizer.transform([processed_text])
            
            # Predecir
            intent_tag = self.model.predict(X)[0]
            confidence = np.max(self.model.predict_proba(X))
            
            # Extraer entidades
            entities = self.extract_entities(message)
            
            # Actualizar contexto
            self.update_context(entities, intent_tag)
            
            return intent_tag, confidence, entities
            
        except Exception as e:
            print(f"⚠️ Error en predicción: {e}")
            return "fallback", 0.0, {}
    
    def get_enhanced_response(self, intent_tag, user_message, entities):
        # Buscar respuesta base
        base_response = "Lo siento, no tengo información sobre eso. ¿Puedes contactarnos al 555-INFORMES para más detalles?"
        
        for intent in self.intents['intents']:
            if intent['tag'] == intent_tag:
                if intent['responses']:
                    base_response = random.choice(intent['responses'])
                break
        
        # Personalizar respuesta según contexto
        enhanced_response = self.personalize_response(base_response, entities)
        
        return enhanced_response
    
    def personalize_response(self, response, entities):
        # Personalizar respuesta según el contexto
        if self.user_context['mascota_tipo']:
            if 'perro' in response.lower() and self.user_context['mascota_tipo'] == 'gato':
                response = response.replace('perro', 'gato').replace('canino', 'felino')
            elif 'gato' in response.lower() and self.user_context['mascota_tipo'] == 'perro':
                response = response.replace('gato', 'perro').replace('felino', 'canino')
        
        # Añadir información de urgencia si es necesario
        if entities['urgencia'] and 'emergencia' not in response.lower():
            response = "🚨 " + response + " \n\n⚠️ **ESTO ES URGENTE** - Contacta inmediatamente al 555-EMERGENCIA"
        
        return response

    def chat(self):
        print("🐕 ¡Hola! Soy VetAssistant - Tu asistente veterinario 🐱")
        print("=" * 50)
        
        while True:
            try:
                user_input = input("\n👤 Tú: ").strip()
                
                if user_input.lower() in ['salir', 'exit', 'quit', 'adiós', 'chao']:
                    print("\n🤖 VetAssistant: ¡Gracias por visitarnos! Cuida mucho a tu mascota 🐾")
                    break
                
                if not user_input:
                    continue
                
                # Predecir intención con entidades
                intent, confidence, entities = self.predict_intent(user_input)
                
                print(f"   [Intención: {intent} | Confianza: {confidence:.2f}]")
                
                # Obtener respuesta mejorada
                if confidence < 0.3:
                    response = "No estoy seguro de entender. ¿Podrías reformular? Puedo ayudarte con: horarios, citas, vacunas, emergencias, alimentación, etc."
                else:
                    response = self.get_enhanced_response(intent, user_input, entities)
                
                print(f"🤖 VetAssistant: {response}")
                
            except KeyboardInterrupt:
                print("\n\n🤖 VetAssistant: ¡Hasta luego! 🐕🐱")
                break
            except Exception as e:
                print(f"\n🤖 VetAssistant: Ocurrió un error. Por favor, intenta de nuevo.")
                print(f"   Error: {e}")

if __name__ == "__main__":
    chatbot = EnhancedVeterinaryChatbot()
    chatbot.chat()