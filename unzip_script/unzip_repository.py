from split_file_reader.split_file_reader import SplitFileReader
import tkinter as tk
from tkinter import filedialog
import zipfile
import os.path


def unzip_all():
    """
    in the directory selection window point the program to the folder where all the .zipXXX files are downloaded.
    The program will then unzip everything to a folder next to the current with the same name and and suffix '_unzipped'
    this script works for both '.csv' and '.json' formatted files
    :return: None
    """
    root = tk.Tk()
    root.withdraw()
    dir_path = filedialog.askdirectory()
    # for file in os.listdir(dir_path):
    #     with SplitFileReader(file) as sfr:
    #         with zipfile.ZipFile(file=sfr, mode='w') as zipf:
    #             # for root, dirs, files in os.walk("./"):
    #             #     for file in files:
    #             #         if file.startswith("random_payload"):
    #             zipf.read(file)
    # filepaths = os.listdir(dir_path)
    filepaths = [dir_path + "/" + i for i in os.listdir(dir_path)]
    # unique_names = set()
    unique_names_dict = {}
    # [unique_names.add('.'.join(i.split('.')[0:-1])) for i in os.listdir(dir_path)]
    for file_name in os.listdir(dir_path):
        unique_names_dict['.'.join(file_name.split('.')[0:-1])] = unique_names_dict.get('.'.join(file_name.split('.')[0:-1]), [])
        unique_names_dict['.'.join(file_name.split('.')[0:-1])].append(dir_path + "/" + file_name)
    # print(len(unique_names_dict))
    if not os.path.isdir(dir_path + "_unzipped/"):
        os.makedirs(dir_path + "_unzipped/")
    for file_name in unique_names_dict:
        with SplitFileReader(unique_names_dict[file_name]) as sfr:
            with zipfile.ZipFile(sfr, mode="r") as tf:
                for filename in tf.namelist():
                    with tf.open(filename) as zipreader:
                        with open(dir_path + "_unzipped/" + filename.split('/')[-1], 'w') as unzipped_writer:
                            print(zipreader.read(), file=unzipped_writer)
                        # print(zipreader.read())
                # print(tf.filename)
                # for tff in tf.filelist:
                    # print("File in archive: ", tff)

unzip_all()