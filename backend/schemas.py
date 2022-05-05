"""Fix "Fatal error in launcher: Unable to create process using ..." error. Put me besides those EXE made by pip. (They are made by distutils, and used by pip)"""
import re
import sys
import os
from glob import glob


script_path = os.path.dirname(os.path.realpath(__file__))
real_int_path = sys.executable
_t = script_path.rpartition(os.sep)[0] + os.sep + 'python.exe'
if script_path.lower().endswith('scripts') and os.path.isfile(_t):
    real_int_path = _t

print('real interpreter path: ' + real_int_path)
print()

for i in glob('*.exe'):
    with open(i, 'rb+') as f:
        img = f.read()
        match = re.search(rb'#![a-zA-Z]:\\.+\.exe', img)
        if not match:
            print("can't fix file: " + i)
            continue
        int_path = match.group()[2:].decode()
        int_path_start = match.start() + 2
        int_path_end = match.end()

        if int_path.lower() == real_int_path.lower():
            continue
        print('fix interpreter path: %s in %s' % (int_path, i))
        f.seek(int_path_start)
        f.write(real_int_path.encode())
        f.write(img[int_path_end:])
