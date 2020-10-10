stuff = {"food": 16, "veg": 57, "yar": 45}

print(stuff.get("yar"))

print(stuff.items())

print(stuff.keys())

new_items = {"rocks": 45, "salt": 54}
stuff.update(new_items)
print(stuff)