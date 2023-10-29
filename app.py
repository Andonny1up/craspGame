import pyglet
from pyglet.window import key
from utils.dice import Dice
from utils.game_window import GameWindow

def main():
    #window = GameWindow(800, 600, 'Juego de Craps')
    window = pyglet.window.Window(width=800, height=600, caption="Craps Game")
    point_probabilidad = {4: '33.34%',
                          5: '40.00%',
                          6: '45.45%',
                          8: '45.45%',
                          9: '40.00%',
                          10: '33.34%',}
    
    now_roll_pro = {2: '2.78%',
                    3: '5.56%',
                    4: '8.33%',
                    5: '11.11%',
                    6: '13.89%',
                    7: '16.66%',
                    8: '13.89%',
                    9: '11.11%',
                    10: '8.33%',
                    11: '5.56%',
                    12: '2.78%',}
    
    dice1 = Dice()
    dice2 = Dice()
    rolling = False
    roll_count = 0
    max_roll_count = 6
    end = False
    #primer tiro
    firs_roll = True
    #punto = 0
    point = 0
    cont = 0
    
    sound_dice = pyglet.media.load("resources/dice.mp3",streaming=False)
    title_label = pyglet.text.Label('Craps Game',
                        font_name='Times New Roman',
                        font_size=36,
                        x=window.width // 2,
                        y=window.height - 50,
                        anchor_x='center',
                        anchor_y='center')
    
    
    result_label = pyglet.text.Label('Resultado: 0',
                         font_name='Times New Roman',
                         font_size=18,
                         x=10,
                         y=window.height - 80,
                         anchor_x='left',
                         anchor_y='top')
    
    
    count_label = pyglet.text.Label('Cantidad de Tiros: 0',
                         font_name='Times New Roman',
                         font_size=18,
                         x=590,
                         y=window.height - 80,
                         anchor_x='left',
                         anchor_y='top')
    
    pro_roll = pyglet.text.Label('Probabilidad Tiro Actual: 0',
                         font_name='Times New Roman',
                         font_size=18,
                         x=10,
                         y=window.height - 110,
                         anchor_x='left',
                         anchor_y='top')
    
    
    point_pro_label = pyglet.text.Label('Probabilidad de salir 7 u 11: 22.22%',
                         font_name='Times New Roman',
                         font_size=18,
                         x=10,
                         y=window.height - 140,
                         anchor_x='left',
                         anchor_y='top')
    
    
    point_label = pyglet.text.Label('El punto es: 0',
                         font_name='Times New Roman',
                         font_size=18,
                         x=590,
                         y=window.height - 110,
                         anchor_x='left',
                         anchor_y='top')
    point_label.visible = False


    win_label = pyglet.text.Label('¡Ganaste!',
                      font_name='Arial',
                      font_size=36,
                      x=window.width // 2,
                      y=window.height // 2,
                      anchor_x='center',
                      anchor_y='center')
    win_label.visible = False
    
    @window.event
    def on_draw():
        window.clear()
        pyglet.gl.glClearColor(0.0, 0.4, 0.0, 1.0)
        title_label.draw()
        result_label.draw()
        point_label.draw()
        point_pro_label.draw()
        count_label.draw()
        pro_roll.draw()
        
        dice1_image = dice1.faces[dice1.value]
        dice2_image = dice2.faces[dice2.value]
        dice1_image.blit(x=400, y=0+50*roll_count, width=50, height=50)
        dice2_image.blit(x=350, y=0+40*roll_count, width=50, height=50)
        if end:
            win_label.draw()
        


    # @window.event
    # def on_key_press(symbol, modifiers):
    #     if symbol == key.SPACE:
    #         for i in range(5):
    #             dice1.roll()
    #             dice2.roll()

    @window.event
    def on_key_press(symbol, modifiers):
        nonlocal rolling, roll_count
        if symbol == key.SPACE:
            if not rolling and not end:
                rolling = True
                roll_count = 0
                pyglet.clock.schedule_interval(update_dice, 0.2)
                pyglet.clock.schedule_once(play_sound, 0.2)
        
        if symbol == key.ENTER and end:
            reset_game()
                


    def play_sound(dt):
        sound_dice.play()
            
            
    def update_dice(dt):
        nonlocal rolling, roll_count,end, firs_roll, cont
        dice1.roll()
        dice2.roll()
        roll_count += 1
        if roll_count >= max_roll_count:
            rolling = False
            pyglet.clock.unschedule(update_dice)
            result_label.text = 'Resultado: {}'.format(dice1.value + dice2.value)
            cont += 1
            count_label.text = 'Cantidad de Tiros: {}'.format(cont)
            rsult = dice1.value + dice2.value
            pro_roll.text = 'Probabilidad Tiro Actual: {}'.format(now_roll_pro[rsult])
            craps_condition(rsult)
            

    
    def craps_condition(rsult):
        nonlocal end, firs_roll, point
        
        if firs_roll:
            firs_roll = False
            if rsult == 7 or rsult == 11 :
                end = True
                win_label.visible = True
            elif rsult == 2 or rsult == 3 or rsult == 12:
                end = True
                win_label.text = "¡Perdiste!"
                win_label.visible = True
            else:
                point = rsult
                point_label.text = 'El punto es: {}'.format(point)
                point_pro_label.text = 'Probabilidad punto: {}'.format(point_probabilidad[point])
                point_label.visible = True
                    
            window.dispatch_event('on_draw')
        else:
            if rsult == point:
                end = True
                win_label.visible = True
            elif rsult == 7:
                end = True
                win_label.text = "¡Perdiste!"
                win_label.visible = True
            
    
    
    def reset_game():
        nonlocal rolling, roll_count, end, firs_roll, cont
        rolling = False
        roll_count = 0
        end = False
        win_label.visible = False
        result_label.text = 'Resultado: 0'
        count_label.text = 'Cantidad de Tiros: 0'
        cont = 0
        win_label.text = "¡Ganaste!"
        point_label.visible = False
        firs_roll = True
        point_pro_label.text = 'Probabilidad de salir 7 u 11: 22.22%'
        pro_roll.text = 'Probabilidad Tiro Actual: 0'
            
    pyglet.app.run()



if __name__ == '__main__':
    main()