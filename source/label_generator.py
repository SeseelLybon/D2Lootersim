import pyglet

from item import Item

batch = pyglet.graphics.Batch()


weapon_primary_label = pyglet.text.Label("Primary weapon: ",
                        font_name='Times New Roman',
                        font_size=15,
                        x=50, y=200,
                        anchor_x='left', anchor_y='center',
                        batch=batch)
weapon_primary_item = Item(weapon_primary_label)


weapon_secondary_label = pyglet.text.Label("Secondary weapon: ",
                        font_name='Times New Roman',
                        font_size=15,
                        x=50, y=250,
                        anchor_x='left', anchor_y='center',
                        batch=batch)
weapon_secondary_item = Item(weapon_secondary_label)


weapon_power_label = pyglet.text.Label("Power weapon: ",
                        font_name='Times New Roman',
                        font_size=15,
                        x=50, y=300,
                        anchor_x='left', anchor_y='center',
                        batch=batch)
weapon_power_item = Item(weapon_power_label)


armour_helmet_label = pyglet.text.Label("Helmet:",
                        font_name='Times New Roman',
                        font_size=15,
                        x=300, y=100,
                        anchor_x='left', anchor_y='center',
                        batch=batch)
armour_helmet_item = Item(armour_helmet_label)


armour_gloves_label = pyglet.text.Label("Gloves: ",
                        font_name='Times New Roman',
                        font_size=15,
                        x=300, y=150,
                        anchor_x='left', anchor_y='center',
                        batch=batch)
armour_gloves_item = Item(armour_gloves_label)


armour_chest_label = pyglet.text.Label("Chest: ",
                        font_name='Times New Roman',
                        font_size=15,
                        x=300, y=200,
                        anchor_x='left', anchor_y='center',
                        batch=batch)
armour_chest_item = Item(armour_chest_label)


armour_greaves_label = pyglet.text.Label("Greaves: ",
                        font_name='Times New Roman',
                        font_size=15,
                        x=300, y=250,
                        anchor_x='left', anchor_y='center',
                        batch=batch)
armour_greaves_item = Item(armour_greaves_label)


armour_boots_label = pyglet.text.Label("Boots: ",
                        font_name='Times New Roman',
                        font_size=15,
                        x=300, y=300,
                        anchor_x='left', anchor_y='center',
                        batch=batch)
armour_boots_item = Item(armour_boots_label)


armour_token_label = pyglet.text.Label("Token: ",
                        font_name='Times New Roman',
                        font_size=15,
                        x=300, y=350,
                        anchor_x='left', anchor_y='center',
                        batch=batch)
armour_token_item = Item(armour_token_label)


avg_power_label = pyglet.text.Label("Light: ",
                        font_name='Times New Roman',
                        font_size=15,
                        x=50, y=100,
                        anchor_x='left', anchor_y='center',
                        batch=batch)
avg_power = Item(avg_power_label)


items_dict = dict()


items_dict["primary"]      = weapon_primary_item
items_dict["secondary"]    = weapon_secondary_item
items_dict["Power"]        = weapon_power_item

items_dict["helmet"]       = armour_helmet_item
items_dict["token"]        = armour_token_item
items_dict["gloves"]       = armour_gloves_item
items_dict["chest"]        = armour_chest_item
items_dict["greaves"]      = armour_greaves_item
items_dict["boots"]        = armour_boots_item

items_key_list = list(items_dict.keys())