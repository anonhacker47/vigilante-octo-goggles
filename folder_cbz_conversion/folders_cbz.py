import os
import shutil

cbr=".cbr"
cbz=".cbz"
rar=".rar"
zip=".zip"

path=r"<Path for the directory goes here>"
print(path)

os.chdir(path)

dirs = [f for f in os.listdir(path) if os.path.isdir(f)]
print(dirs)

def repackrar():
  for dir in dirs:
     shutil.make_archive(dir, 'zip', dir)
     shutil.rmtree(dir)

repackrar()
print("Repack Completed")
print("Renaming to cbz")

zip_files = [f for f in os.listdir(path) if f.endswith(zip)]
for zip_file in zip_files:
    if zip in zip_file:
     newfile = zip_file.replace(zip,cbz)
     os.rename(zip_file,newfile)
     print(newfile)
