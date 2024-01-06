import time
from glob import glob
import os,shutil
import argparse
start = time.time()
parser = argparse.ArgumentParser(
                    prog='FoldersSort',
                    description='Sorts all files in current directories and subdirectories in folders with its extensions.')
parser.add_argument('-r','--rename',action='store_true',help='Rename files with same names. Default is False.')
parser.add_argument('-o','--overwrite',action='store_true',help='Overwrite files with same names. Default is False.')
parser.add_argument('-e','--exceptions',help='Path to a file containing list of files which will not be organized, each on new line. Default is None, but list contains script itself.')
filename=os.path.split(__file__)[-1]
args = parser.parse_args()
ow=args.overwrite
ren=args.rename
exs=args.exceptions
e=[filename]
if exs is not None:
    e.append(exs)
    with open(exs) as f:
        for i in f:
            e.append(i.rstrip())

def renmd(p,x):
    pn=p.replace('.',f'_{x}.',-1)
    if os.path.exists(pn):
        return renmd(p,x+1)
    return pn
a=glob('**/*',recursive=True)
for i in e:
    if i in a:
        a.remove(i)
for i in a:
    if os.path.isdir(i)==0:
        ext=os.path.join(os.path.split(i)[-1].split('.')[-1])
        cr=os.path.split(ext)[-1]
        pr=os.path.split(os.path.split(ext)[-2])[-1]
        if os.path.exists(ext)==0 and cr!=pr:
            os.mkdir(ext)
        if cr!=pr:
            if os.path.split(i)[-1].split('.')[-1]==os.path.split(ext)[-1]:
                if os.path.exists(ext):
                    try:
                        shutil.move(os.path.abspath(i),ext)
                    except shutil.Error:
                        if os.path.exists(os.path.join(os.path.abspath(ext),i)):
                            if ren:
                                shutil.move(os.path.abspath(i),os.path.join(os.path.abspath(ext),renmd(i,0)))
                            if ow:
                                shutil.move(os.path.abspath(i),os.path.join(os.path.abspath(ext),i))
ex_end=time.time()
print(f'Done! Organized in {ex_end-start}s.')