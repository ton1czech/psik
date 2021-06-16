import os

def organize():
    accept = input("Are you sure you want to organize your Downloads directory? [y/N]: ")
    if accept == "y" or accept == "Y" or accept == "yes":
        accept = True
    else:
        print("All right\nshutting down...")
        accept = False

    if accept == True:
        print("Scanning the Downloads directory...")
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