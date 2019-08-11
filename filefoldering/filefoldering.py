
import glob, os, shutil
from itertools import islice


def split_seq(fnames, dirfcnt):
    print('in function')
    fi_i = iter(fnames)
    item = list(islice(fi_i, dirfcnt))

    while item:
        yield item
        item = list(islice(fi_i, dirfcnt))

###### main program ####

#note: either resolve the full path of source and destination, or use the relative path to where the .py file is executed from

sourcepath = '20190617_single/' #source path. be sure to account for / or \ depending on the operating system
destpath = '20190617_single_events/' #destination path.
fnames = os.listdir(sourcepath)     #List of file names in source directory
dirfcnt = 8000     #Total files per directory
dirname = '' #leave blank, used for creating the directory


print('starting')

#checks if the destination parent exists
if not os.path.isdir(destpath):
    os.mkdir(destpath)

#creates a iterable list from the file listing
#uses a for loop to enumerate through the listing
#checks if the destination directory exists, then creates
# copies files into the directory up to the specified dirfcnt
for i, val in enumerate(list(split_seq(fnames, dirfcnt))):
    dirname = '{0:0>4}'.format(i)
    print('Creating directory: {}'.format(dirname))
    destfpath = destpath + dirname
    if not os.path.isdir(destfpath):
        os.mkdir(destfpath)
        print('directory created')

    for a in val:
        print('Copying file: {}'.format(a))
        shutil.copy2(sourcepath+a, destfpath+'/'+a) #remember to change the / for the type of os


print('end')
