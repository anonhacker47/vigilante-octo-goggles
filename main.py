import os
from functions.rename import rename
from functions.repack import repackrar
from constants import rar,cbr,cbz,zip

directory=r"<Head Directory goes here>"

subfolders = [x[0] for x in os.walk(directory)]

for path in subfolders:
     print(path)
     os.chdir(path)
     rename(filetype="cbr_file",file_path=path,rename_from=cbr,rename_to=rar)
    #  files = [f for f in os.listdir(path)]
    #  for file in files:
    #      if cbr in file:
    #          newfile = file.replace(cbr,rar)
    #          os.rename(file,newfile)
    #          print(newfile) vi
     repackrar(path=path,repack_from=rar,repack_to=zip)
 
     print("Repack Completed")
     print("Renaming to cbz")
     
     rename(filetype="zip_files",file_path=path,rename_from=zip,rename_to=cbz)

    #  zip_files = [f for f in os.listdir(path) if f.endswith(zip)]
    #  for zip_file in zip_files:
    #      if zip in zip_file:
    #       newfile = zip_file.replace(zip,cbz)
    #       os.rename(zip_file,newfile)
    #       print(newfile)
 
print("Task Completed")