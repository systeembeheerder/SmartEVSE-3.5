#this script will be run by platformio.ini from its native directory
import os
os.system('cc -o src/pack src/pack.c')
os.system('src/pack data/* >src/packed_fs.c')

