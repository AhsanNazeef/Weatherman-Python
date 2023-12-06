import sys
import os
import calendar

# First argument -e -a -c
# Second argument  year/month
# Third argument pathToFile


def filter_files(path, year, month):
    files_in_folder = os.listdir(folder_path)
    file_names = []
    for file_name in files_in_folder:
        if month and year:
            if str(year) in file_name and str(month) in file_name:
                full_file_path = os.path.join(folder_path, file_name)
                file_names.append(full_file_path)
        else:
            if str(year) in file_name:
                full_file_path = os.path.join(folder_path, file_name)
                file_names.append(full_file_path)
    return file_names


def get_arguments():
    path = "." + sys.argv[3]
    if not os.path.exists(path):
        raise Exception("Path Does not exist")
    args = sys.argv[2].split("/")
    if len(args) >= 2:
        year = int(args[0])
        month = int(args[1])
        if (month > 12 or month < 1):
            raise Exception("Invalid Month")
        month = calendar.month_abbr[month]
    else:
        year = args[0]
        month = None
    return (year, month, path)


try:
    if (sys.argv[1] not in ["-e", "-a", "-c"]):
        raise Exception("Invalid argument")
    year, month, folder_path = get_arguments()
    filtered_files = filter_files(folder_path, year, month)
except IndexError:
    print("Please provide all arguments")
except ValueError:
    print("Please pass correct values")
except Exception as e:
    print(e)
