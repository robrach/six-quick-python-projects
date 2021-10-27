import os


def rename_files():
    i = 0
    path = "/home/robert/Six_Quick_Python_Projects/2 - renaming bulk files/" \
           "files_for_test/"
    for filename in os.listdir(path):
        old_file_name = path + filename
        new_file_name = path + "exfile_" + str(i)

        print('\nold:', old_file_name)
        print('new:', new_file_name)

        os.rename(old_file_name, new_file_name)
        i += 1


if __name__ == '__main__':
    rename_files()