from asyncio.proactor_events import constants
import os
import patoolib

def repackrar(path,repack_from,repack_to):

    rar_files = [f for f in os.listdir(path) if f.endswith(repack_from)]
    print(rar_files)

    for rar_file in rar_files:
        newfile=rar_file.replace(repack_from,repack_to)
        patoolib.repack_archive(rar_file,newfile)
        os.remove(rar_file)