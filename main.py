import os
from PIL import Image
def get_files(path,type,to):
    if not os.path.exists(path):
        return print(f"Path {path} does not exist.")
    if not os.path.isdir(path):
        return print(f"Path {path} is not a directory.")
    if not os.access(path, os.R_OK):
        return print(f"Path {path} is not readable.")
    if not os.access(path, os.W_OK):
        return print(f"Path {path} is not writable.")
    if not os.access(path, os.X_OK):
        return print(f"Path {path} is not executable.")
    if not os.access(path, os.F_OK):
        return print(f"Path {path} does not exist.")
    if os.listdir(path) == []:
        return print(f"Path {path} is empty.")
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            file_name, file_extension = os.path.splitext(file)
            if file_extension.lower() == f'.{type}':
                try:
                    im = Image.open(os.path.join(path, file))
                    im.save(os.path.join(path, file_name + f'.{to}'))
                    os.remove(os.path.join(path, file))
                    print(f"Converted {file} to {file_name}.{to}. \n Danger: \n{type == 'png' and to !='webp' and " -By default, we can not convert png to other formats without loss of quality. \n - Permission denied error may result in corrupted files"} ")
                except Exception as e:
                    print(f"Error processing file {file}: {e}")

def main():
    files = ["png", "jpg", "webp", "gif", "bmp", "tiff", "eps", "pdf", "svg", "ico", "raw", "avif", "heic", "indd", "ai", "fla"]
    print("Welcome to the minimalist bulk file converter.")
    path = input("Enter the path of the directory: ")
    if not os.path.exists(path):
        print("Path does not exist.")
        path = input("Enter the path of the directory: ")
    print("Select the type of files you want to convert:")
    num_columns = (len(files) + 4)
    for i in range(5):
        for j in range(num_columns):
            idx = i + j*5
            if idx < len(files):
                print(f"{idx+1}. {files[idx]:<5}", end='')
        print()
    print("\n0. Exit")

    choice = int(input("Enter the number of the file type you want to convert: "))
    if choice == 0:
        print("Exiting...")
        return
    if choice == 1:
        print("Warning: Converting png may result in loss of quality and may result in corrupted files!")
        wishToContinue = input("Do you wish to continue? (y/n): ")
        if wishToContinue.lower() != 'y':
            print("Exiting...")
            return 
    if choice == 3:
        print("Warning: Converting webp may result in loss of quality and may result in corrupted files!")
        print("WEBP is reccomended to be converted to PNG!")
    while choice < 0 or choice > len(files):
        print("Invalid choice. Enter a number between 0 and 16!")
        choice = int(input("Enter the number of the file type you want to convert: "))
    choice = files[choice-1]

    choice2 = int(input("Enter the number of the file type you want to convert to: "))
    if choice == 0:
        print("Exiting...")
        return
    while choice2 < 0 or choice2 > len(files):
        print(f"Invalid choice. Enter a number between 0 and {len(files)}!")
        choice2 = int(input("Enter the number of the file type you want to convert: "))
    choice2 = files[choice2-1]
    if choice == choice2:
        print("You can't convert to the same file type!")
        return
    try:
        get_files(path=path, type=choice, to=choice2)
        print("Done!")
    except Exception as e:
        print(f"Error: {e}")
main()