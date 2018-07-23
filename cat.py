import sys
import json

# accept argument

notebook_path1 = sys.argv[1]  # path of notebook
notebook_path2 = sys.argv[2]  #


# read notebook
notebook1 = open(notebook_path1)
notebook1_str = notebook1.read()

# Turn string to dictionary (json)
notebook1_json = json.loads(notebook1_str)

cells1 = notebook1_json['cells']

notebook2 = open(notebook_path2)
notebook2_str = notebook2.read()
notebook2_json = json.loads(notebook2_str)

cells2 = notebook1_json['cells']

del notebook1_json['cells']  # Remain the metadata (settings) of jupynb. aka delete the cells data.

target_cells = cells1 + cells2  # cat the two json

target_notebook = {}

target_notebook['cells'] = target_cells  # Add elements to the dictionary

target_notebook.update(notebook1_json)  # Add the settings in  notebook1_json to target_notebook

target_string = json.dumps(target_notebook)  # dumps() turn json into string

target = open('target_notebook.ipynb', 'w')

target.write(target_string)
