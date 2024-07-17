import os
import hashlib
from tkinter import Tk, filedialog

def select_folder(prompt):
    root = Tk()
    root.withdraw()  # Esconde a janela principal do Tkinter
    folder_selected = filedialog.askdirectory(title=prompt)
    return folder_selected

def get_file_hash(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()

def get_files_with_hashes(directory):
    files_hashes = {}
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_hash = get_file_hash(file_path)
            files_hashes[file_hash] = file_path
    return files_hashes

def delete_files_in_b_not_in_a(files_in_a, directory_b):
    files_in_b = get_files_with_hashes(directory_b)
    for file_hash, file_path in files_in_b.items():
        if file_hash in files_in_a:
            os.remove(file_path)
            print(f'Deleted: {file_path}')

if __name__ == "__main__":
    folder_a = select_folder("Select Folder A (source images)")
    folder_b = select_folder("Select Folder B (target images)")

    if folder_a and folder_b:
        files_in_a = get_files_with_hashes(folder_a)
        delete_files_in_b_not_in_a(files_in_a, folder_b)
        print("Completed deletion of matching images in Folder B.")
    else:
        print("Both folders need to be selected.")
