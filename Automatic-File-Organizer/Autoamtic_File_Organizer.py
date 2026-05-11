import os
import shutil

# The folder you want to organize (you can change this)
folder_path = r"C:\Users\YourName\Downloads"   # <-- Enter your path

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Archives": [".zip", ".rar"],
    "Audio": [".mp3", ".wav"],
    "Others": []
}

# Ensure folders exist
for folder in file_types.keys():
    folder_dir = os.path.join(folder_path, folder)
    if not os.path.exists(folder_dir):
        os.makedirs(folder_dir)

# Organize files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    # skip folders
    if os.path.isdir(file_path):
        continue

    moved = False

    for folder_name, extensions in file_types.items():
        if any(file.lower().endswith(ext) for ext in extensions):
            shutil.move(file_path, os.path.join(folder_path, folder_name, file))
            print(f"Moved: {file} → {folder_name}")
            moved = True
            break

    # if no category matched
    if not moved:
        shutil.move(file_path, os.path.join(folder_path, "Others", file))
        print(f"Moved: {file} → Others")

print("✅ Folder Successfully Organized!")
