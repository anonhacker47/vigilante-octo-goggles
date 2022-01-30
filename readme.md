# vigilante-octo-goggles
A python script to convert cbr files to cbz.

This is a python script written in python to for auto converting .cbr files to .cbz

## How to Use

```
   pip install -r requirements.txt
   #edit main.py and add your comics head folder path instead of <Head Directory goes here>.
   run main.py
```

## Note: Just add the top most path to the main.py since the script will go inside each subdirectory and change all cbr files to cbz files.

## Troubleshooting

Sometimes due to file corruption/unsupported rar file the script may fail and all the cbr in a particular folder will be renamed to rar
and console will output some error instead of "Task Completed".

Then, go to the folder and select all the rar files's and use winrar and select "extract files to separate folders" and run folders_cbz.py 
(add the directory path before running), all folders will be made into cbzs.
