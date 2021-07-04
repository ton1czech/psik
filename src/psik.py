import os
from time import monotonic
import shutil
from curtsies.fmtfuncs import magenta, cyan, green, bold

def organize():
    start = monotonic()
    count = 0
    accept = input(magenta("Are you sure you want to organize your Downloads directory? [y/N]: "))
    if accept == "y" or accept == "Y" or accept == "yes":
        print(cyan("Scanning the Downloads directory..."))
        dir = f"/home/{os.getlogin()}"
        os.chdir(f"{dir}/Downloads")
        files = os.listdir()
        print(bold(cyan(f"Found {len(files)} files.")))
        print(magenta("Moving files..."))

        for file in files:
            ## Documents ##
            # websites #
            if file.endswith(".html") or file.endswith(".js") or file.endswith(".ts") or file.endswith(".css") or file.endswith(".scss") or file.endswith(".php") or file.endswith(".jsx"):
                temp_dir = f"{dir}/Documents/programming/websites"
                if not os.path.exists(temp_dir):
                    os.makedirs(temp_dir)
                shutil.move(file, f"{temp_dir}/{file}")
                count += 1

            # python #
            elif file.endswith(".py") or file.endswith(".pyw") or file.endswith(".pyx"):
                temp_dir = f"{dir}/Documents/programming/python"
                if not os.path.exists(temp_dir):
                    os.makedirs(temp_dir)
                shutil.move(file, f"{temp_dir}/{file}")
                count += 1

            # go #
            elif file.endswith(".go"):
                temp_dir = f"{dir}/Documents/programming/go"
                if not os.path.exists(temp_dir):
                    os.makedirs(temp_dir)
                shutil.move(file, f"{temp_dir}/{file}")
                count += 1

            # rust #
            elif file.endswith(".rs"):
                temp_dir = f"{dir}/Documents/programming/rust"
                if not os.path.exists(temp_dir):
                    os.makedirs(temp_dir)
                shutil.move(file, f"{temp_dir}/{file}")
                count += 1

            # c #
            elif file.endswith(".c"):
                temp_dir = f"{dir}/Documents/programming/c"
                if not os.path.exists(temp_dir):
                    os.makedirs(temp_dir)
                shutil.move(file, f"{temp_dir}/{file}")
                count += 1

            # c# #
            elif file.endswith(".cs"):
                temp_dir = f"{dir}/Documents/programming/c#"
                if not os.path.exists(temp_dir):
                    os.makedirs(temp_dir)
                shutil.move(file, f"{temp_dir}/{file}")
                count += 1

            # c++ #
            elif file.endswith(".cpp"):
                temp_dir = f"{dir}/Documents/programming/c++"
                if not os.path.exists(temp_dir):
                    os.makedirs(temp_dir)
                shutil.move(file, f"{temp_dir}/{file}")
                count += 1

            ## Pictures ##
            # raster #
            elif file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".tiff") or file.endswith(".gif") or file.endswith(".heif") or file.endswith(".raw"):
                temp_dir = f"{dir}/Pictures/raster"
                if not os.path.exists(temp_dir):
                    os.makedirs(temp_dir)
                shutil.move(file, f"{temp_dir}/{file}")
                count += 1

            # vector #
            elif file.endswith(".svg") or file.endswith(".ai"):
                temp_dir = f"{dir}/Pictures/vector"
                if not os.path.exists(temp_dir):
                    os.makedirs(temp_dir)
                shutil.move(file, f"{temp_dir}/{file}")
                count += 1
            
            ## Videos ##
            elif file.endswith(".mp4") or file.endswith(".mov") or file.endswith(".mkv") or file.endswith(".webm") or file.endswith(".flv") or file.endswith("avi") or file.endswith(".m4v") or file.endswith(".mpg") or file.endswith(".mpeg"):
                temp_dir = f"{dir}/Videos"
                if not os.path.exists(temp_dir):
                    os.makedirs(temp_dir)
                shutil.move(file, f"{temp_dir}/{file}")
                count += 1
            
            ## Music ##
            elif file.endswith(".mp3") or file.endswith(".aac") or file.endswith("flac") or file.endswith("m4a") or file.endswith(".opus") or file.endswith("wav") or file.endswith(".webm"):
                temp_dir = f"{dir}/Music"
                if not os.path.exists(temp_dir):
                    os.makedirs(temp_dir)
                shutil.move(file, f"{temp_dir}/{file}")
                count += 1
        print(bold(green(f"\nMoved {count} files in {format(monotonic() - start, '.3f')} seconds.\n\nDownloads directory organized by psik.")))
    else:
        print(cyan("All right\nshutting down..."))
        accept = False
            
if __name__ == "__main__":
    organize()