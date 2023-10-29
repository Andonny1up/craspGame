import pyglet

class GameWindow(pyglet.window.Window):
    def __init__(self, width, height, caption):
        super().__init__(width, height, caption=caption)
        self.set_location(100, 100)
        self.load_resources()
        self.setup_event_handlers()
        
    def load_resources(self):
        # Carga las imágenes, sonidos y otros recursos necesarios
        pass
        
    def setup_event_handlers(self):
        # Configura los manejadores de eventos para la ventana
        pass
        
    def on_draw(self):
        self.clear()
        pyglet.gl.glClearColor(0.0, 0.4, 0.0, 1.0)  # Fondo verde (RGB: 0, 102, 0)
    
        
    def on_key_press(self, symbol, modifiers):
        # Lógica de manejo de eventos de teclado
        pass
        
    def on_mouse_press(self, x, y, button, modifiers):
        # Lógica de manejo de eventos de mouse
        pass