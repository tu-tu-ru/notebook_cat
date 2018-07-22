import json

notebook1 = open('7.ipynb')
notebook1_str = notebook1.read()

# Turn string to dictionary (json)
notebook1_json = json.loads(notebook1_str)
print(notebook1_json)

cells1 = notebook1['cells']

notebook2 = open('to_add.ipynb')
notebook2_str = notebook2.read()
print(notebook2_str)
cells2 = notebook2['cells']

target_cells = cells1 + cells2

print(target_cells)