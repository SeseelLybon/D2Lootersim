import pyglet

from item import Item

batch = pyglet.graphics.Batch()

weapon_primary_label = pyglet.text.Label("Primary: ",
                        font_name='Times New Roman',
                        font_size=12,
                        x=50, y=200,
                        anchor_x='left', anchor_y='center',
                        batch=batch)
weapon_primary_item = Item(weapon_primary_label)

weapon_secondary_label = pyglet.text.Label("Secondary: ",
                        font_name='Times New Roman',
                        font_size=12,
                        x=50, y=250,
                        anchor_x='left', anchor_y='center',
                        batch=batch)
weapon_primary_item = Item(weapon_primary_label)

weapon_power_label = pyglet.text.Label("Power: ",
                        font_name='Times New Roman',
                        font_size=12,
                        x=300, y=350,
                        anchor_x='left', anchor_y='center',
                        batch=batch)
weapon_primary_item = Item(weapon_primary_label)

armour_helmet_label = pyglet.text.Label("Helmet:",
                        font_name='Times New Roman',
                        font_size=12,
                        x=300, y=100,
                        anchor_x='left', anchor_y='center',
                        batch=batch)
weapon_primary_item = Item(weapon_primary_label)

armour_gloves_label = pyglet.text.Label("Gloves: ",
                        font_name='Times New Roman',
                        font_size=12,
                        x=300, y=150,
                        anchor_x='left', anchor_y='center',
                        batch=batch)

armour_chest_label = pyglet.text.Label("Chest: ",
                        font_name='Times New Roman',
                        font_size=12,
                        x=300, y=200,
                        anchor_x='left', anchor_y='center',
                        batch=batch)
weapon_primary_item = Item(weapon_primary_label)

armour_greaves_label = pyglet.text.Label("Greaves: ",
                        font_name='Times New Roman',
                        font_size=12,
                        x=300, y=250,
                        anchor_x='left', anchor_y='center',
                        batch=batch)
weapon_primary_item = Item(weapon_primary_label)

armour_boots_label = pyglet.text.Label("Boots: ",
                        font_name='Times New Roman',
                        font_size=12,
                        x=300, y=300,
                        anchor_x='left', anchor_y='center',
                        batch=batch)
weapon_primary_item = Item(weapon_primary_label)

armour_token_label = pyglet.text.Label("Token: ",
                        font_name='Times New Roman',
                        font_size=12,
                        x=300, y=350,
                        anchor_x='left', anchor_y='center',
                        batch=batch)
weapon_primary_item = Item(weapon_primary_label)

avg_power_label = pyglet.text.Label("Light: ",
                        font_name='Times New Roman',
                        font_size=12,
                        x=50, y=100,
                        anchor_x='left', anchor_y='center',
                        batch=batch)
weapon_primary_item = Item(weapon_primary_label)

items_dict = dict()

avg_power = [avg_power_label,0]

items_dict["primary"]      = [weapon_primary_label,10]
items_dict["secondary"]    = [weapon_secondary_label,10]
items_dict["Power"]        = [weapon_power_label,10]

items_dict["helmet"]       = [armour_helmet_label,10]
items_dict["token"]        = [armour_token_label,10]
items_dict["gloves"]       = [armour_gloves_label,10]
items_dict["chest"]        = [armour_chest_label,10]
items_dict["greaves"]      = [armour_greaves_label,10]
items_dict["boots"]        = [armour_boots_label,10]