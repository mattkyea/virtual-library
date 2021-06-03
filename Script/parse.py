# thanks https://stackoverflow.com/questions/18262293/how-to-open-every-file-in-a-folder

import os

yourpath = '.' #run in directory with all metadata files

#this will grab all files in ./folder/file structure
for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:
        print(os.path.join(root, name)) #name of file with folder/file
        with open(os.path.join(root,name), 'r') as f: #open
            text = f.read() #grab text (metadata)
            print (len(text)) #print length as test
            #here, we'll start parsing
            #grab all categories
            #write to a text file
            #we'll need ID and categories, might add book name and author too
            #I should also consider how to read this into UE4
