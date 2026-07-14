import os
import shutil

# 🔹 Ask user for folder path
path = input("Enter folder path to organize: ")

# 🔹 File type categories
file_types = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

# 🔹 Counters
moved_files = 0

# 🔹 Loop through files
for file in os.listdir(path):
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):
        moved = False

        for folder, extensions in file_types.items():
            for ext in extensions:
                if file.lower().endswith(ext):
                    folder_path = os.path.join(path, folder)

                    # Create folder if not exists
                    if not os.path.exists(folder_path):
                        os.mkdir(folder_path)

                    # Handle duplicate file names
                    new_path = os.path.join(folder_path, file)
                    count = 1

                    while os.path.exists(new_path):
                        name, extension = os.path.splitext(file)
                        new_name = f"{name}_{count}{extension}"
                        new_path = os.path.join(folder_path, new_name)
                        count += 1

                    shutil.move(file_path, new_path)
                    moved_files += 1
                    moved = True
                    break

            if moved:
                break

        # Move unknown files
        if not moved:
            other_folder = os.path.join(path, "Others")
            if not os.path.exists(other_folder):
                os.mkdir(other_folder)

            shutil.move(file_path, os.path.join(other_folder, file))
            moved_files += 1

# 🔹 Summary
print(f"\n✅ Total files organized: {moved_files}")
print("🎉 Folder cleaned successfully!")



