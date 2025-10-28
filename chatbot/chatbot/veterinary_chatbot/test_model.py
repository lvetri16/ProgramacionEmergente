from chatbot import EnhancedVeterinaryChatbot

def test_chatbot():
    chatbot = EnhancedVeterinaryChatbot()
    
    test_cases = [
        "Hola, tengo un cachorro de 2 meses, ¿qué vacunas necesita?",
        "Mi gato no come desde ayer",
        "¿Cuánto cuesta una consulta?",
        "Necesito desparasitar a mi perro",
        "Es urgente, mi perro se comió chocolate",
        "¿Recomiendan esterilizar gatos?",
        "Horario de atención por favor"
    ]
    
    print("🧪 TESTEO DEL CHATBOT MEJORADO")
    print("=" * 50)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest {i}: {test_case}")
        print("-" * 40)
        
        intent, confidence, entities = chatbot.predict_intent(test_case)
        response = chatbot.get_enhanced_response(intent, test_case, entities)
        
        print(f"Intención: {intent}")
        print(f"Confianza: {confidence:.2f}")
        print(f"Entidades: {entities}")
        print(f"Respuesta: {response}")
        print("-" * 40)

if __name__ == "__main__":
    test_chatbot()