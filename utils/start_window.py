import pyglet
import time
from pyglet.window import key
#from .dice import Dice
from .game_window import GameWindow

class StartWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(800, 600, caption="Craps Game - Inicio")
        self.background_image = pyglet.image.load("../resources/Craps_fondo.jpg")
        self.background_sprite = pyglet.sprite.Sprite(self.background_image)
        self.music = pyglet.media.load("../resources/Sakamoto_theme.mp3", streaming=False)
        self.music_player = pyglet.media.Player()
        self.music_player.queue(self.music)
        self.music_player.loop = True
        self.label = pyglet.text.Label("Presione Enter para jugar",
                                       font_name="Arial",
                                       font_size=24,
                                       x=self.width // 2,
                                       y=self.height // 2,
                                       anchor_x="center",
                                       anchor_y="center")

    def on_draw(self):
        self.clear()
        self.background_sprite.draw()
        self.label.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ENTER:
            self.music_player.pause()
            self.close()
            game_window = GameWindow(800, 600, "Craps Game")

def main():
    start_window = StartWindow()
    start_window.music_player.play()
    pyglet.app.run()

if __name__ == "__main__":
    main()
