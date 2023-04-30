def fruits(tuple_of_fruits):
   for item in tuple_of_fruits :
      if item.get("shape") == "sphere":
        if item.get("mass") >= 300 and item.get("mass") <= 600:
            if item.get("volume") >= 100 and item.get("volume") <= 500 :
               print(item.get("name") + " it is good fruit ... ")


fruits (
   (
        {'name':'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
        {'name':'mango', 'shape': 'square', 'mass': 150, 'volume': 120}, 
        {'name':'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
        {'name':'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250},
    ),
)