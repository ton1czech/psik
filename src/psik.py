import os
import shutil

def organize():
    accept = input("Are you sure you want to organize your Downloads directory? [y/N]: ")
    if accept == "y" or accept == "Y" or accept == "yes":
        print("Scanning the Downloads directory...")
        dir = f"/home/{os.getlogin()}"
        os.chdir(f"{dir}/Downloads")

        for file in os.listdir():
            # Documents
            if file.endswith(".html") or file.endswith(".js") or file.endswith(".ts"):
                temp_dir = f"{dir}/Documents/programming/websites"
                if not os.path.exists(temp_dir):
                    os.makedirs(temp_dir)
                shutil.move(file, f"{temp_dir}/{file}")
                print("Website file moved")

            # Pictures
            elif file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                print("Picture file moved")
            
            # Videos
            elif file.endswith(".mp4") or file.endswith(".mov") or file.endswith(".mkv"):
                print("Video file moved")
            
            # Musik
            elif file.endswith(".mp3"):
                print("Musik file moved")

            # Other
            else:
                temp_dir = f"{dir}/Documents/other"
                if not os.path.exists(temp_dir):
                    os.makedirs(temp_dir)
                shutil.move(file, f"{temp_dir}/{file}")
                print("Other file moved")
    else:
        print("All right\nshutting down...")
        accept = False
            
if __name__ == "__main__":
    organize()