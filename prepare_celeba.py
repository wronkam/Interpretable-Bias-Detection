import csv
import os
import shutil

from tqdm import tqdm

# Define the CSV file path
root_dir = os.path.join('.','data','celebA')
data_dir = os.path.join(root_dir,'img_align_celeba')
split_dir = {0:'train',1:'val',2:'test'}
classes = {1:"blond",-1:"not_blond"}
dry_run = True
#
splits = {}
count = {}
with open(os.path.join(root_dir,'list_eval_partition.csv'), "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # Get the header row

    # Print the header
    print("Header:")
    print(", ".join(header))
    # Print the values
    i = 0
    for row in csv_reader:
        id, split = row
        split = int(split)
        splits[id] = split
        if split not in count:
            count[split] = 0
        count[split] += 1
        i+=1
print(count)
for k,v in count.items():
    print(k,v/i)

# extract gender, blond hair attributes from others
count = {}
with open(os.path.join(root_dir,'list_attr_celeba.csv'), "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    reader_header = next(csv_reader)  # Get the header row

    header = ["image_id", "Blond_Hair", "Male","Split"]
    header_ids = [reader_header.index(attribute) for attribute in header[:-1]]
    print(header_ids)

    for dir in split_dir.values():
        os.makedirs(os.path.join(root_dir,dir),exist_ok=True)
        for class_name in classes.values():
            os.makedirs(os.path.join(root_dir, dir,class_name), exist_ok=True)
    # Write the header to the CSV file

    with open(os.path.join(root_dir,'list_attr_celeba_extracted.csv'), 'w', newline='') as out_csv:
        writer = csv.writer(out_csv)
        writer.writerow(header)
        # Print the header
        i=0
        for row in tqdm(csv_reader,total=203555):
            attributes = [row[id] for id in header_ids]
            id, blond, male = attributes
            blond = int(blond)
            male = int(male)
            split = splits[id]
            filename = os.path.join(data_dir,id)
            cls = classes[blond]
            destination = os.path.join(root_dir,split_dir[split],cls)

            if not dry_run:
                shutil.copy(filename, destination)
            writer.writerow([id, blond, male, split])

            keyxd = f"blond_{blond}_male_{male}"
            if split not in count.keys():
                count[split] = {}
                count[split]['blond']={-1:0,1:0}
                count[split]['male'] = {-1: 0, 1: 0}
            if keyxd not in count[split].keys():
                count[split][keyxd] = 0
            count[split][keyxd] += 1
            count[split]['blond'][blond] += 1
            count[split]['male'][male] += 1
print(count)
for k,v in count.items():
    print(k,split_dir[k],'-'*50,'total',sum([vv for kk, vv in v.items() if 'blond_' in kk]))
    for kk,vv in v.items():
        print('_'*5,kk,vv)