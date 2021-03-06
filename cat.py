import sys
import json

# handle exception

if len(sys.argv) < 3:
    raise Exception('# of argv must be greater than 2.')


# accept argument

notebook_path_list = sys.argv[1:]  # path of notebook, using list slicing
# TODO why start from 1

cells_list = []

target_notebook = {}

# use for loop for all the notebooks
for path in notebook_path_list:
    with open(path) as notebook:
        # notebook = open(path)
        notebook_str = notebook.read()
        notebook_json = json.loads(notebook_str)
        cell_to_use = notebook_json['cells']
        cells_list += cell_to_use
#        notebook.close()  # close the file after use

target_notebook['cells'] = cells_list

cells_for_metadata = json.loads(open(notebook_path_list[1]).read())

del cells_for_metadata['cells']  # Remain the metadata (settings) of jupynb. aka delete the cells data.

target_notebook.update(cells_for_metadata)  # Add the settings in  notebook1_json to target_notebook

target_string = json.dumps(target_notebook)  # dumps() turn json into string

target = open('target_notebook.ipynb', 'w')

target.write(target_string)
