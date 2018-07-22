import json

notebook1 = open('7.ipynb')
notebook1_str = notebook1.read()

# Turn string to dictionary (json)
notebook1_json = json.loads(notebook1_str)
#print(notebook1_json)

cells1 = notebook1_json['cells']

notebook2 = open('to_add.ipynb')
notebook2_str = notebook2.read()
notebook2_json = json.loads(notebook2_str)

#print(notebook2_str)
cells2 = notebook1_json['cells']

target_cells = cells1 + cells2 # json

target_string = json.dumps(target_cells)

target = open('target_notebook.ipynb', 'w')

target.write(target_string)
#print(target_cells)