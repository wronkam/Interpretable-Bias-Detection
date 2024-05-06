import csv
import os
import shutil

# Define the CSV file path
root_dir = os.path.join('.','data','waterbirds')
file_name = os.path.join(root_dir,'metadata.csv')
split_dir = {0:'train',1:'val',2:'test'}

# Read the CSV file with its header
with open(file_name, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # Get the header row

    # Print the header
    print("Header:")
    print(", ".join(header))
    cls = {}
    splits = {}
    # Print the values
    print("Values:")
    i = 0
    for k,v in split_dir.items():
        os.makedirs(os.path.join(root_dir,v),exist_ok=True)
    for row in csv_reader:
        id, file, y, split, place,place_f = row
        place_f = place_f.split('/')[1]
        classez = {'0':'landbird','1':'waterbird'}[y]
        dir,image = file.split('/')
        split = int(split)
        print(split_dir[split],split,file)
        dest = os.path.join(root_dir,split_dir[split],classez)
        os.makedirs(dest,exist_ok=True)
        shutil.copy(os.path.join(root_dir,file),os.path.join(dest,image))

