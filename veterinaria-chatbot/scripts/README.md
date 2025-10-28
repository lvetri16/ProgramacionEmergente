# Chatbot VetCare - Sistema Basado en Reglas

## 🤖 Descripción

Este es un chatbot completamente basado en reglas (rule-based) para la clínica veterinaria VetCare. No utiliza inteligencia artificial ni machine learning, sino un sistema de coincidencia de patrones y reglas predefinidas.

## 📋 Características del Chatbot

### Sistema Basado en Reglas
- **Coincidencia de patrones**: Identifica intenciones mediante palabras clave
- **Extracción de entidades**: Detecta tipos de animales, urgencias, etc.
- **Reglas condicionales**: Aplica lógica específica según el contexto
- **Respuestas predefinidas**: Base de conocimientos en JSON
- **Manejo de contexto**: Recuerda el tema de conversación
- **Normalización de texto**: Maneja acentos y variaciones

### Intenciones Soportadas
1. **Saludo y despedida**
2. **Horarios de atención**
3. **Servicios veterinarios**
4. **Consultas generales**
5. **Vacunación**
6. **Cirugías**
7. **Emergencias**
8. **Precios**
9. **Agendamiento de citas**
10. **Ubicación**
11. **Contacto**
12. **Equipo médico**
13. **Especies atendidas**
14. **Formas de pago**

### Entidades Reconocidas
- **Tipos de animales**: perro, gato, conejo, ave, roedor
- **Nivel de urgencia**: alta, media, baja

## 🚀 Instalación y Uso

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. **Instalar dependencias**:
\`\`\`bash
cd scripts
pip install -r requirements.txt
\`\`\`

2. **Iniciar el servidor del chatbot**:
\`\`\`bash
python chatbot_server.py
\`\`\`

El servidor se iniciará en `http://localhost:5000`

3. **Usar el sitio web**:
- Ejecutar el sitio web: `npm run dev` (en la carpeta del proyecto)
- Abre el sitio web de VetCare en tu navegador `http://localhost:3000`
- Haz clic en el botón del chatbot (esquina inferior derecha)
- ¡Comienza a chatear!

## 🔧 Arquitectura del Sistema

### Componentes

1. **chatbot_server.py** (Backend Flask)
   - Servidor HTTP que procesa mensajes
   - Clase `RuleBasedChatbot` con toda la lógica
   - Endpoints REST para comunicación

2. **chatbot_knowledge.json** (Base de Conocimientos)
   - Intenciones con patrones y respuestas
   - Entidades y sus variaciones
   - Reglas condicionales
   - Respuestas de fallback

3. **chatbot-widget.tsx** (Frontend React)
   - Interfaz de usuario del chat
   - Comunicación con el backend
   - Manejo de estado de mensajes

### Flujo de Procesamiento

\`\`\`
Usuario escribe mensaje
    ↓
Frontend envía a /chat
    ↓
Normalización de texto
    ↓
Identificación de intención (match_intent)
    ↓
Extracción de entidades (get_entity)
    ↓
Aplicación de reglas (apply_rules)
    ↓
Selección de respuesta
    ↓
Respuesta al usuario
\`\`\`

## 📝 Personalización

### Agregar Nuevas Intenciones

Edita `chatbot_knowledge.json`:

\`\`\`json
{
  "intents": {
    "nueva_intencion": {
      "patterns": [
        "palabra clave 1",
        "palabra clave 2"
      ],
      "responses": [
        "Respuesta 1",
        "Respuesta 2"
      ]
    }
  }
}
\`\`\`

### Agregar Nuevas Entidades

\`\`\`json
{
  "entities": {
    "nueva_entidad": {
      "valor1": ["sinonimo1", "sinonimo2"],
      "valor2": ["sinonimo3", "sinonimo4"]
    }
  }
}
\`\`\`

### Agregar Nuevas Reglas

\`\`\`json
{
  "rules": {
    "nombre_regla": {
      "conditions": [
        {
          "entity": "tipo_entidad",
          "values": {
            "valor_entidad": "Respuesta específica"
          }
        }
      ],
      "default_response": "Respuesta por defecto"
    }
  }
}
\`\`\`

## 🧪 Pruebas

### Ejemplos de Conversación

**Saludo**:
- Usuario: "Hola"
- Bot: "¡Hola! Bienvenido a VetCare..."

**Consulta de horarios**:
- Usuario: "¿A qué hora abren?"
- Bot: "Nuestro horario de atención es..."

**Emergencia**:
- Usuario: "Mi perro está muy mal, es urgente"
- Bot: "🚨 EMERGENCIA DETECTADA..."

**Información de servicios**:
- Usuario: "¿Qué servicios tienen?"
- Bot: "En VetCare ofrecemos..."

## 🔍 Debugging

El servidor incluye logs en consola. Para ver qué está pasando:

\`\`\`python
print(f"[DEBUG] Intent detected: {intent}")
print(f"[DEBUG] Entity found: {entity}")
\`\`\`

## 📊 Ventajas del Sistema Basado en Reglas

✅ **Predecible**: Respuestas consistentes y controladas
✅ **Transparente**: Fácil de entender y debuggear
✅ **Sin entrenamiento**: No requiere datos de entrenamiento
✅ **Rápido**: Respuestas instantáneas
✅ **Mantenible**: Fácil de actualizar y expandir
✅ **Sin dependencias de IA**: No requiere APIs externas

## 🚧 Limitaciones

⚠️ No entiende contexto complejo
⚠️ Requiere patrones exactos o similares
⚠️ No aprende de conversaciones
⚠️ Limitado a reglas predefinidas

## 🔐 Seguridad

- CORS habilitado para desarrollo
- Validación de entrada
- Manejo de errores robusto
- Sin almacenamiento de datos personales

## 📞 Soporte

Para problemas o preguntas:
- Email: contacto@vetcare.com
- Teléfono: +52 (55) 1234-5678
