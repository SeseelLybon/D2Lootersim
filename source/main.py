import pyglet
from pyglet.window import key
import random

from pyglet.window import mouse

#fps_display = pyglet.clock.ClockDisplay()
window = pyglet.window.Window(width=1000,height=600)

import logging

from label_generator import batch
from label_generator import items_dict
from label_generator import avg_power
from label_generator import items_key_list

tiers = {"worn":(-10,-5),
         "fine":(-5,0),
         "masterwork":(0,5),
         "legendary":(5,10),
         "exotic":(10,15)}

def throw_loot():
    itemtype = random.choice(items_key_list)
    Litem = items_dict.get(itemtype)
    cap = 100

    tierkey = random.choice(list(tiers.keys()))
    tierval = tiers.get(tierkey)
    rand=0
    if Litem.power <= cap:
        rand = avg_power.power+random.randint(tierval[0],tierval[1])
        if rand > cap:
            rand = cap
        if Litem.power < rand:
            Litem.power = rand
    print(itemtype, tierkey, rand)
    pass


@window.event
def on_draw():

    throw_loot()

    avg = 0
    for value in items_dict.values():
        value.label.text = value.text+str(value.power)
        avg+=value.power
    avg//=6+3
    avg_power.power = avg
    avg_power.label.text = avg_power.text+str(avg_power.power)

    # Draw calls -------------------------------------------------

    window.clear()
    batch.draw()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        pass





logging.critical("Pyglet.run()")

#import cProfile
#cProfile.run('pyglet.app.run()')

pyglet.app.run()

logging.critical("End of main")