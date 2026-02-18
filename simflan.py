import os

def create_nested_folders(base_path, command):
    current_path = base_path
    tokens = command.split()

    i = 0
    last_folder = None

    while i < len(tokens):
        token = tokens[i]

        # make file
        if token == "-f":
            folder_name = tokens[i + 1]
            file_name = tokens[i + 2]

            target_path = os.path.join(base_path, folder_name)
            os.makedirs(target_path, exist_ok=True)

            file_path = os.path.join(target_path, file_name)
            with open(file_path, "w") as f:
                f.write("")

            print(f"[FILE CREATED] {file_path}")
            i += 3
            continue

        #handle (-in)
        elif token == "-in":
            folder_target = tokens[i + 1]
            subfolder = tokens[i + 2].replace(".", "")

            target_path = os.path.join(base_path, folder_target, subfolder)
            os.makedirs(target_path, exist_ok=True)

            print(f"[FOLDER CREATED] {target_path}")
            i += 3
            continue

        # Handle dot (.)
        elif token.endswith("."):
            folder_name = token.replace(".", "")
            folder_path = os.path.join(base_path, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            print(f"[FOLDER CREATED] {folder_path}")
            last_folder = folder_name
            i += 1
            continue

        # Handle (,)
        elif token.endswith(","):
            folder_name = token.replace(",", "")
            if last_folder:
                current_path = os.path.join(current_path, last_folder)
            folder_path = os.path.join(current_path, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            print(f"[FOLDER CREATED] {folder_path}")
            last_folder = folder_name
            i += 1
            continue

        else:
            # Folder (without . or ,)
            folder_path = os.path.join(base_path, token)
            os.makedirs(folder_path, exist_ok=True)

            print(f"[FOLDER CREATED] {folder_path}")
            last_folder = token
            i += 1


if __name__ == "__main__":
    base_path = input("Enter base path: ")
    command = input("Enter command: ")

    create_nested_folders(base_path, command)

