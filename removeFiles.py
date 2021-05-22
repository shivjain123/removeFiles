import os
import shutil
import time

def checkStuff():

        deleted_folders = 0
        deleted_files = 0

        days = 30

        path = input("Please enter the path.")

        DaysToSeconds = days * 24 * 60 * 60

        seconds = time.time() - DaysToSeconds

        ctime = os.stat(path).st_ctime

        if (os.path.exists(path)):

            for folders, sub_folders, files in os.walk(path):

                if (seconds >= ctime):

                    shutil.rmtree(path)
                    deleted_folders += 1

                    break

                else:
                    for sub_folders in folders:

                        folder_path = os.path.join(folders, sub_folders)

                        if (seconds >= ctime):

                            shutil.rmtree(folder_path)
                            deleted_folders += 1

                            break

                    for file in files:

                        file_path = os.path.join(folders, file)

                        if (seconds >= ctime):

                            os.remove(file_path)
                            deleted_files += 1

                            break

        elif (seconds >= ctime):

            os.remove(path)
            deleted_files += 1

        else:

            print(f'"{path}" is not found')
            deleted_files += 1 

            print(f"Total folders deleted: {deleted_folders}")
            print(f"Total files deleted: {deleted_files}")

checkStuff()