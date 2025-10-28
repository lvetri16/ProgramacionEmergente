import tkinter as tk
from tkinter import scrolledtext, ttk
import threading
import time
from chatbot import EnhancedVeterinaryChatbot
import json
from datetime import datetime

class ModernVeterinaryChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("VetAssistant")
        self.root.geometry("400x700")
        self.root.configure(bg='#000000')
        self.root.resizable(True, True)
        
        # Configurar estilo moderno
        self.setup_styles()
        
        # Cargar el chatbot
        self.chatbot = EnhancedVeterinaryChatbot()
        
        # Configurar la interfaz
        self.setup_ui()
        
    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Colores modernos (tema oscuro)
        self.colors = {
            'bg': '#0a0a0a',
            'bg_light': '#1a1a1a',
            'accent': '#00d4aa',
            'accent_hover': '#00b894',
            'text_primary': '#ffffff',
            'text_secondary': '#888888',
            'user_bubble': '#00d4aa',
            'bot_bubble': '#2a2a2a',
            'input_bg': '#1a1a1a',
            'border': '#333333'
        }
        
    def setup_ui(self):
        # Frame principal con bordes redondeados
        self.main_frame = tk.Frame(self.root, bg=self.colors['bg'], padx=0, pady=0)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header minimalista
        self.setup_header()
        
        # Área de chat
        self.setup_chat_area()
        
        # Input area
        self.setup_input_area()
        
        # Quick actions
        self.setup_quick_actions()
        
    def setup_header(self):
        header_frame = tk.Frame(self.main_frame, bg=self.colors['bg'], height=80)
        header_frame.pack(fill=tk.X, padx=20, pady=(20, 10))
        header_frame.pack_propagate(False)
        
        # Logo y título
        title_label = tk.Label(
            header_frame,
            text="🐕 VetAssistant",
            font=('Segoe UI', 20, 'bold'),
            fg=self.colors['text_primary'],
            bg=self.colors['bg']
        )
        title_label.pack(anchor='w')
        
        subtitle_label = tk.Label(
            header_frame,
            text="Asistente virtual veterinario",
            font=('Segoe UI', 10),
            fg=self.colors['text_secondary'],
            bg=self.colors['bg']
        )
        subtitle_label.pack(anchor='w', pady=(2, 0))
        
        # Separador
        separator = tk.Frame(header_frame, height=1, bg=self.colors['border'])
        separator.pack(fill=tk.X, side=tk.BOTTOM, pady=(10, 0))
    
    def setup_chat_area(self):
        # Frame para el área de chat
        chat_container = tk.Frame(self.main_frame, bg=self.colors['bg'])
        chat_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Canvas para fondo personalizado
        self.chat_canvas = tk.Canvas(
            chat_container,
            bg=self.colors['bg'],
            highlightthickness=0,
            relief='flat'
        )
        
        # Scrollbar personalizada
        self.scrollbar = ttk.Scrollbar(
            chat_container,
            orient=tk.VERTICAL,
            command=self.chat_canvas.yview
        )
        
        self.scrollable_frame = tk.Frame(self.chat_canvas, bg=self.colors['bg'])
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.chat_canvas.configure(scrollregion=self.chat_canvas.bbox("all"))
        )
        
        self.canvas_window = self.chat_canvas.create_window(
            (0, 0),
            window=self.scrollable_frame,
            anchor="nw",
            width=400
        )
        
        self.chat_canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.chat_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Bind para ajustar el ancho del frame
        self.chat_canvas.bind('<Configure>', self.on_canvas_configure)
        
        # Mensaje de bienvenida
        self.add_bot_message("¡Hola! Soy VetAssistant, tu ayudante virtual de veterinaria. 😊\n\nEstoy aquí para orientarte sobre el cuidado de tu mascota. ¿En qué puedo ayudarte?")
    
    def on_canvas_configure(self, event):
        # Ajustar el ancho del frame interno al canvas
        self.chat_canvas.itemconfig(self.canvas_window, width=event.width)
    
    def setup_input_area(self):
        input_frame = tk.Frame(self.main_frame, bg=self.colors['bg'], padx=20, pady=15)
        input_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        # Frame interno para input con bordes redondeados
        input_container = tk.Frame(input_frame, bg=self.colors['input_bg'], relief='flat')
        input_container.pack(fill=tk.X, padx=(0, 10))
        
        self.user_input = tk.Entry(
            input_container,
            font=('Segoe UI', 12),
            bg=self.colors['input_bg'],
            fg=self.colors['text_primary'],
            relief='flat',
            bd=0,
            insertbackground=self.colors['text_primary']
        )
        self.user_input.pack(fill=tk.X, padx=15, pady=12)
        self.user_input.bind('<Return>', self.send_message)
        self.user_input.bind('<KeyPress>', self.on_input_keypress)
        
        # Placeholder
        self.user_input.insert(0, "Escribe tu mensaje...")
        self.user_input.config(fg=self.colors['text_secondary'])
        self.user_input.bind('<FocusIn>', self.on_input_focus_in)
        self.user_input.bind('<FocusOut>', self.on_input_focus_out)
        
        # Botón de enviar moderno
        self.send_button = tk.Button(
            input_frame,
            text="↑",
            font=('Segoe UI', 14, 'bold'),
            bg=self.colors['accent'],
            fg=self.colors['bg'],
            relief='flat',
            bd=0,
            cursor='hand2',
            width=3,
            command=self.send_message
        )
        self.send_button.pack(side=tk.RIGHT)
        
        self.update_send_button()
    
    def on_input_focus_in(self, event):
        if self.user_input.get() == "Escribe tu mensaje...":
            self.user_input.delete(0, tk.END)
            self.user_input.config(fg=self.colors['text_primary'])
    
    def on_input_focus_out(self, event):
        if not self.user_input.get():
            self.user_input.insert(0, "Escribe tu mensaje...")
            self.user_input.config(fg=self.colors['text_secondary'])
    
    def on_input_keypress(self, event):
        self.update_send_button()
    
    def update_send_button(self):
        text = self.user_input.get()
        if text and text != "Escribe tu mensaje...":
            self.send_button.config(bg=self.colors['accent'], state=tk.NORMAL)
        else:
            self.send_button.config(bg=self.colors['border'], state=tk.DISABLED)
    
    def setup_quick_actions(self):
        quick_frame = tk.Frame(self.main_frame, bg=self.colors['bg'], padx=20, pady=10)
        quick_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        quick_actions = [
            {"icon": "⏰", "text": "Horario", "question": "¿Cuál es su horario de atención?"},
            {"icon": "💉", "text": "Vacunas", "question": "¿Qué vacunas necesita mi mascota?"},
            {"icon": "📅", "text": "Cita", "question": "Quiero agendar una cita"},
            {"icon": "🚑", "text": "Urgencia", "question": "Es una emergencia"}
        ]
        
        for action in quick_actions:
            btn = tk.Button(
                quick_frame,
                text=f"{action['icon']} {action['text']}",
                font=('Segoe UI', 10),
                bg=self.colors['bg_light'],
                fg=self.colors['text_primary'],
                relief='flat',
                bd=1,
                cursor='hand2',
                padx=15,
                pady=8,
                command=lambda q=action['question']: self.quick_action(q)
            )
            btn.pack(side=tk.LEFT, padx=(0, 10))
            
            # Efecto hover
            self.bind_hover_effect(btn, self.colors['bg_light'], self.colors['accent'])
    
    def bind_hover_effect(self, widget, normal_color, hover_color):
        def on_enter(e):
            widget.config(bg=hover_color, fg=self.colors['bg'])
        
        def on_leave(e):
            widget.config(bg=normal_color, fg=self.colors['text_primary'])
        
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)
    
    def add_message(self, message, sender='user'):
        message_frame = tk.Frame(self.scrollable_frame, bg=self.colors['bg'])
        message_frame.pack(fill=tk.X, padx=5, pady=2)
        
        # Frame para la burbuja
        bubble_frame = tk.Frame(message_frame, bg=self.colors['bg'])
        
        if sender == 'user':
            bubble_frame.pack(anchor='e', padx=(50, 0))
            bubble_bg = self.colors['user_bubble']
            text_color = self.colors['bg']
        else:
            bubble_frame.pack(anchor='w', padx=(0, 50))
            bubble_bg = self.colors['bot_bubble']
            text_color = self.colors['text_primary']
        
        # Burbuja de chat con bordes redondeados
        bubble = tk.Label(
            bubble_frame,
            text=message,
            font=('Segoe UI', 11),
            bg=bubble_bg,
            fg=text_color,
            wraplength=300,
            justify=tk.LEFT,
            padx=15,
            pady=10,
            relief='flat',
            bd=0
        )
        bubble.pack()
        
        # Timestamp
        timestamp = datetime.now().strftime("%H:%M")
        time_label = tk.Label(
            bubble_frame,
            text=timestamp,
            font=('Segoe UI', 8),
            bg=self.colors['bg'],
            fg=self.colors['text_secondary']
        )
        time_label.pack(pady=(2, 0))
        
        # Scroll automático al final
        self.scroll_to_bottom()
    
    def scroll_to_bottom(self):
        self.chat_canvas.update_idletasks()
        self.chat_canvas.yview_moveto(1.0)
    
    def add_bot_message(self, message):
        self.add_message(message, 'bot')
    
    def add_user_message(self, message):
        self.add_message(message, 'user')
    
    def send_message(self, event=None):
        user_text = self.user_input.get().strip()
        if not user_text or user_text == "Escribe tu mensaje...":
            return
        
        # Limpiar input
        self.user_input.delete(0, tk.END)
        self.update_send_button()
        
        # Mostrar mensaje del usuario
        self.add_user_message(user_text)
        
        # Procesar en un hilo separado
        threading.Thread(
            target=self.process_bot_response, 
            args=(user_text,), 
            daemon=True
        ).start()
    
    def quick_action(self, question):
        self.user_input.delete(0, tk.END)
        self.user_input.insert(0, question)
        self.user_input.config(fg=self.colors['text_primary'])
        self.update_send_button()
        self.send_message()
    
    def process_bot_response(self, user_text):
        # Mostrar indicador de typing
        self.show_typing_indicator()
        
        # Pequeña pausa para efecto visual
        time.sleep(0.5)
        
        try:
            # Procesar con el chatbot
            intent, confidence, entities = self.chatbot.predict_intent(user_text)
            response = self.chatbot.get_enhanced_response(intent, user_text, entities)
            
            # Ocultar indicador y mostrar respuesta
            self.root.after(0, lambda: self.hide_typing_indicator(response))
            
        except Exception as e:
            error_msg = "Lo siento, ocurrió un error. Por favor, intenta de nuevo."
            self.root.after(0, lambda: self.hide_typing_indicator(error_msg))
    
    def show_typing_indicator(self):
        self.typing_frame = tk.Frame(self.scrollable_frame, bg=self.colors['bg'])
        self.typing_frame.pack(fill=tk.X, padx=5, pady=2)
        
        typing_bubble = tk.Frame(self.typing_frame, bg=self.colors['bot_bubble'])
        typing_bubble.pack(anchor='w', padx=(0, 50))
        
        self.typing_label = tk.Label(
            typing_bubble,
            text="● ● ●",
            font=('Segoe UI', 16),
            bg=self.colors['bot_bubble'],
            fg=self.colors['accent'],
            padx=15,
            pady=10
        )
        self.typing_label.pack()
        
        self.scroll_to_bottom()
        self.animate_typing()
    
    def animate_typing(self):
        def animate(dots):
            if hasattr(self, 'typing_label'):
                self.typing_label.config(text="● " * dots + "○ " * (3 - dots))
                dots = (dots + 1) % 4
                self.root.after(500, lambda: animate(dots))
        
        animate(1)
    
    def hide_typing_indicator(self, response):
        if hasattr(self, 'typing_frame'):
            self.typing_frame.destroy()
        
        # Mostrar respuesta
        self.add_bot_message(response)

def main():
    # Configurar la ventana principal
    root = tk.Tk()
    
    # Centrar la ventana en la pantalla
    window_width = 400
    window_height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 4
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    # Crear la aplicación
    app = ModernVeterinaryChatbotGUI(root)
    
    # Ejecutar
    root.mainloop()

if __name__ == "__main__":
    main()