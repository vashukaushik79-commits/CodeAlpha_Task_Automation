import os
import shutil

def organize_jpg_files():
    source_dir = "source_folder"
    target_dir = "copied_jpg_folder"

    if not os.path.exists(source_dir):
        os.makedirs(source_dir)
        print(f"'{source_dir}' created. Please add some .jpg files in it and rerun.")
        return

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    files = os.listdir(source_dir)
    jpg_count = 0

    for file_name in files:
        if file_name.lower().endswith('.jpg'):
            source_path = os.path.join(source_dir, file_name)
            target_path = os.path.join(target_dir, file_name)
            shutil.copy(source_path, target_path)
            print(f"Copied: {file_name} -> {target_dir}")
            jpg_count += 1

    print(f"\nTask Complete! Total {jpg_count} .jpg files automated and moved.")

if __name__ == "__main__":
    organize_jpg_files()
