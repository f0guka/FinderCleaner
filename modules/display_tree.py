import os

def display_tree(directory, target_paths):
    """
    显示目录树，同时标记目标文件。如果某个目录及其子目录没有目标文件，则不显示该目录。
    """
    print(f"Scanning directory: {directory}\n")

    # 获取所有包含目标文件的父目录集合
    target_dirs = {os.path.dirname(path) for path in target_paths}

    for root, dirs, files in os.walk(directory):
        # 过滤掉不包含目标文件的目录
        dirs[:] = [d for d in dirs if os.path.join(root, d) in target_dirs]
        files = [f for f in files if os.path.join(root, f) in target_paths]

        # 如果当前目录和子目录都没有目标文件，跳过
        if not files and not dirs:
            continue

        # 计算当前层级
        level = root.replace(directory, "").count(os.sep)
        indent = "│   " * level + "├── " if level > 0 else ""
        # 打印当前目录
        print(f"{indent}{os.path.basename(root)}/")

        # 打印文件
        for i, file in enumerate(files):
            file_path = os.path.join(root, file)
            is_last_file = (i == len(files) - 1)
            subindent = "│   " * (level + 1) + ("└── " if is_last_file else "├── ")
            if file_path in target_paths:
                print(f"{subindent}\033[94m{file}\033[0m")

    print(f"\nFinished! A total of \033[94m{len(target_paths)}\033[0m target files found.")

if __name__ == "__main__":
    # For module test only
    from modules.list_target_files import list_target_files

    directory = input("Please enter the directory path: ").strip().strip("'\"")
    directory = os.path.normpath(directory)

    target_paths = list_target_files(directory)

    display_tree(directory, target_paths)


