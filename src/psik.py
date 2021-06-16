import os

name = os.getlogin()
os.chdir(f"/home/{name}/Downloads")
dir = os.getcwd()

print(dir)