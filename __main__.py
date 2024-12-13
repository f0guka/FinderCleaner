import os
#from modules import *
from modules.display_tree import display_tree
from modules.list_external_mounts import list_external_volumes
from modules.list_target_files import list_target_files

def del_targets(directory):
    '''
    删除目标文件和文件夹
    '''
    target_paths = list_target_files(directory)
    
    if not target_paths:
        print("\nNo target files or folders found in the specified directory.")
        print("\nGOOD NEWS! It's clean! No Finder rubbish found!")
        return
    
    # 显示目录树和目标文件
    display_tree(directory, target_paths)
    
    # 询问用户是否删除
    confirm = input("\nDo you want to delete all the marked files and folders? (y/n): ").strip().lower()
    if confirm == "y":
        for path in target_paths:
            try:
                if os.path.isfile(path):
                    os.remove(path)
                    print(f"Deleted file: {path}")
                elif os.path.isdir(path):
                    os.rmdir(path)  # 删除空文件夹
                    print(f"Deleted folder: {path}")
            except Exception as e:
                print(f"Failed to delete {path}: {e}")
        print("\nAll target files and folders have been deleted.")
    else:
        print("\nOperation cancelled. No files were deleted.")


def main():
    """
    主程序，接受用户输入路径，列出目标文件并提供删除选项
    """
    while True:
        print("\n\nChoose a mode from the following list:")
        print("[1] Delete from a external volume")
        print("[2] Delete from a specific path")
        print("[3] Exit")
        mode_choice = input("Enter your choice: ").strip()

        if mode_choice == "1":
            external_volumes = list_external_volumes()
            if external_volumes:
                print("\nConnected external storage devices:")
                n = 0
                for volume in external_volumes:
                    n += 1
                    print(f"[{n}] {volume}")
            else:
                print("\n\033[91mError: No external storage devices found.\033[0m")
                continue

            try:
                volume_choice = int(input("Enter the number corresponding to the external volume: ").strip())
                if 1 <= volume_choice <= len(external_volumes):
                    directory = external_volumes[volume_choice - 1]
                else:
                    print("\n\033[91mError: Invalid choice. Please try again.\033[0m")
                    continue
            except ValueError:
                print("\n\033[91mError: Invalid input. Please enter a number.\033[0m")
                continue
            
        elif mode_choice == "2":
            directory = input("Please enter the directory path: ").strip().strip("'\"")
            if not directory:
                print("\n\033[91mError: No directory path provided. Please provide a valid directory path.\033[0m")
                continue
            directory = os.path.normpath(directory) # 标准化路径
            if not os.path.exists(directory):
                print("\n\033[91mError: The provided path does not exist. Please check the path and try again.\033[0m")
                continue
            
        elif mode_choice == "3":
            break

        else:
            print("\n\033[91mError: Invalid choice. Please try again.\033[0m")
            continue

        del_targets(directory)


if __name__ == "__main__":
    banner = """


    ===========================================
           Welcome to Finder Cleaner!
                  Version 0.0.2
    ===========================================
    """
    print(banner)
    main()
