from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import re
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Cargar la base de conocimientos desde el archivo JSON
with open('C:/Users/Acer Aspire3/Downloads/veterinaria-chatbot/scripts/chatbot_knowledge.json', 'r', encoding='utf-8') as f:
    knowledge_base = json.load(f)

class RuleBasedChatbot:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.context = {
            'last_topic': None,
            'conversation_count': 0
        }
        
    def normalize_text(self, text):
        """Normaliza el texto para mejor coincidencia"""
        text = text.lower()
        # Remover acentos
        replacements = {
            'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
            'ñ': 'n', '¿': '', '?': '', '¡': '', '!': ''
        }
        for old, new in replacements.items():
            text = text.replace(old, new)
        return text.strip()
    
    def match_intent(self, user_message):
        """Identifica la intención del usuario basándose en palabras clave"""
        normalized_message = self.normalize_text(user_message)
        
        best_match = None
        best_score = 0
        
        for intent_name, intent_data in self.knowledge_base['intents'].items():
            score = 0
            for pattern in intent_data['patterns']:
                normalized_pattern = self.normalize_text(pattern)
                # Coincidencia exacta
                if normalized_pattern in normalized_message:
                    score += 10
                # Coincidencia de palabras clave
                pattern_words = normalized_pattern.split()
                for word in pattern_words:
                    if len(word) > 3 and word in normalized_message:
                        score += 2
            
            if score > best_score:
                best_score = score
                best_match = intent_name
        
        return best_match if best_score > 0 else None
    
    def get_entity(self, user_message, entity_type):
        """Extrae entidades específicas del mensaje"""
        entities = self.knowledge_base.get('entities', {})
        
        if entity_type not in entities:
            return None
        
        normalized_message = self.normalize_text(user_message)
        
        for entity_value, entity_patterns in entities[entity_type].items():
            for pattern in entity_patterns:
                if self.normalize_text(pattern) in normalized_message:
                    return entity_value
        
        return None
    
    def apply_rules(self, intent, user_message):
        """Aplica reglas específicas basadas en la intención"""
        rules = self.knowledge_base.get('rules', {})
        
        if intent in rules:
            rule = rules[intent]
            
            # Verificar condiciones
            if 'conditions' in rule:
                for condition in rule['conditions']:
                    entity_type = condition.get('entity')
                    entity_value = self.get_entity(user_message, entity_type)
                    
                    if entity_value:
                        # Aplicar acción basada en la entidad
                        if entity_value in condition.get('values', {}):
                            return condition['values'][entity_value]
            
            # Retornar respuesta por defecto de la regla
            if 'default_response' in rule:
                return rule['default_response']
        
        return None
    
    def get_response(self, user_message):
        """Genera una respuesta basada en reglas"""
        self.context['conversation_count'] += 1
        
        # Identificar intención
        intent = self.match_intent(user_message)
        
        if not intent:
            return self.knowledge_base['fallback_responses'][
                self.context['conversation_count'] % len(self.knowledge_base['fallback_responses'])
            ]
        
        # Actualizar contexto
        self.context['last_topic'] = intent
        
        # Aplicar reglas específicas
        rule_response = self.apply_rules(intent, user_message)
        if rule_response:
            return rule_response
        
        # Obtener respuesta de la intención
        intent_data = self.knowledge_base['intents'][intent]
        responses = intent_data['responses']
        
        # Seleccionar respuesta (rotar para variedad)
        response_index = self.context['conversation_count'] % len(responses)
        return responses[response_index]

# Inicializar el chatbot
chatbot = RuleBasedChatbot(knowledge_base)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        response = chatbot.get_response(user_message)
        
        return jsonify({
            'response': response,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'chatbot': 'running'})

if __name__ == '__main__':
    print("🤖 Chatbot VetCare iniciado en http://localhost:5000")
    print("📚 Base de conocimientos cargada exitosamente")
    app.run(debug=True, port=5000)
