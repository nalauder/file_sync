import shutil
import os

source = input('Enter Directory: ')
dest1 = '/home/nick/Dropbox/Study'


files = os.listdir(source)

for f in files:
        shutil.copy(source+f, dest1)