import pyglet, random

class Dice:
    
    def __init__(self):
        self.value = 1
        self.faces = {}
        self.load_resources()
        
        
    def load_resources(self):
        for num in range(1,7):
            image_path = f'resources/dice_{num}.png'
            image = pyglet.image.load(image_path)
            self.faces[num] = image

    
    def roll(self):
        self.value = random.randint(1,6)