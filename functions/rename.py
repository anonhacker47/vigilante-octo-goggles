import os

def rename(filetype,file_path,rename_from,rename_to):
     filetype = [f for f in os.listdir(file_path) if f.endswith(rename_from) ]
     for file in filetype:
        if rename_from in file:
            newfile = file.replace(rename_from,rename_to)
            os.rename(file,newfile)
            # print(newfile)

