from os.path import exists as exist
import os
import getpass
from random import randint

user = getpass.getuser()
main = f"C:\\Users\\{user}\\AppData\\Local\\Temp\\temp_machen"

if not exist(main):
    os.mkdir(main)

os.chdir(main)

def make_newmains(main: str) -> str:
    if main is None:
        return "none"

    if not exist(main):
        return "not exist"
    
    return os.path.join(main, f"{randint(0, 999999999)}")

while True:
    os.mkdir(make_newmains(main))
    print("new main made")
