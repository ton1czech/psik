import os

def organize():
    name = os.getlogin()
    os.chdir(f"/home/{name}/Downloads")

    files = os.listdir()

    for file in files:
        if file.endswith(".html"):
            print("Programming")
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
            print("Images")

if __name__ == "__main__":
    organize()