import csv
import os
import shutil

from tqdm import tqdm

# Define the CSV file path
root_dir = os.path.join('.','data','celebA')
data_dir = os.path.join(root_dir,'img_align_celeba')

split_dir = {0:'train',1:'val',2:'test'}
classes = {10:"blond", 9: "black",12: "brown", 18: "gray", 36:"wearing_hat"}
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
for k,v in count.items():
    print(k,v/i)

# extract gender, blond hair attributes from others
count = {}
with open(os.path.join(root_dir,'list_attr_celeba.csv'), "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    reader_header = next(csv_reader)  # Get the header row

    header = ["image_id", "Blond_Hair", "Black_Hair", "Brown_Hair", "Gray_Hair", "Wearing_Hat", "Split"]
    header_ids = [reader_header.index(attribute) for attribute in header[:-1]] #drop split


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
            id, blond, black, brown, gray, hat = attributes #removed male
            #check hair color
            hair_blond = -1
            hair_black = -1
            hair_brown = -1
            hair_gray = -1

            if int(hat) == 1:
                hair_color = 36
            elif int(blond) == 1:
                hair_color = 10
                hair_blond = 1
            elif int(black) == 1:
                hair_color = 9
                hair_black = 1
            elif int(brown) == 1:
                hair_color = 12
                hair_brown = 1
            elif int(gray) == 1:
                hair_color = 18
                hair_gray = 1
            else:
                hair_color = 0
                # "others"
            # print(int(hat))
            # blond = int(blond)
            if hair_color != 0:
                # only use images with specified features
                split = splits[id]
                filename = os.path.join(data_dir,id)
                cls = classes[hair_color]
                destination = os.path.join(root_dir,split_dir[split],cls)

                if not dry_run:
                    shutil.copy(filename, destination)

                writer.writerow([id, hair_blond, hair_black, hair_brown, hair_gray, hat, split])

                keyxd = f"blond_{hair_blond}_black_{hair_black}_brown_{hair_brown}_gray_{hair_gray},_hat_{hat}"
                if split not in count.keys():
                    count[split] = {}
                    count[split]['Blond_Hair']={-1:0,1:0}
                    count[split]['Black_Hair'] = {-1: 0, 1: 0}
                    count[split]['Brown_Hair'] = {-1: 0, 1: 0}
                    count[split]['Gray_Hair'] = {-1: 0, 1: 0}
                    count[split]['Wears_Hat'] = {-1: 0, 1: 0}
                if keyxd not in count[split].keys():
                    count[split][keyxd] = 0

                count[split][keyxd] += 1
                count[split]['Blond_Hair'][hair_blond] += 1
                count[split]['Black_Hair'][hair_black] += 1
                count[split]['Brown_Hair'][hair_brown] += 1
                count[split]['Gray_Hair'][hair_gray] += 1
                count[split]['Wears_Hat'][int(hat)] += 1
print(count)
for k,v in count.items():
    print(k,split_dir[k],'-'*50,'total',sum([vv for kk, vv in v.items() if 'blond_' in kk]))
    for kk,vv in v.items():
        print('_'*5,kk,vv)