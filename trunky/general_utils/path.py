import os


def create_dir_if_doesnt_exist(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
