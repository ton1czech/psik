import os

def organize():
    name = os.getlogin()
    os.chdir(f"/home/{name}/Downloads")

if __name__ == "__main__":
    organize()