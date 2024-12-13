import os
from .tartgets import TARGET_FILES

def list_target_files(directory):
    """
    遍历目录，找到所有目标文件和文件夹路径，并返回路径列表
    """
    target_paths = []
    for root, dirs, files in os.walk(directory):
        # 检查文件
        for file in files:
            for target in TARGET_FILES:
                if file.startswith(target):
                    target_paths.append(os.path.join(root, file))
        # 检查文件夹
        for dir_ in dirs:
            if dir_ in TARGET_FILES:
                target_paths.append(os.path.join(root, dir_))
    return target_paths

if __name__ == "__main__":
    # For module test only
    directory = input("Please enter the directory path: ").strip().strip("'\"")
    directory = os.path.normpath(directory)

    target_paths = list_target_files(directory)
    print(target_paths)