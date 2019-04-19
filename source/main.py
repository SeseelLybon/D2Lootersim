import pyglet

#fps_display = pyglet.clock.ClockDisplay()
window = pyglet.window.Window(width=1000,height=600)

from label_generator import batch
from label_generator import weapon_dict
from label_generator import armour_dict





@window.event
def on_draw():
    for key, value in weapon_dict:
        value[0].text = value[1]
    for key, value in armour_dict:
        value[0].
    batch.draw()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        print("Hello world")