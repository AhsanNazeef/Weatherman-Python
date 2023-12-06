import sys
import os
import calendar
# First argument -e -a -c
# Second argument  year/month
# Third argument pathToFile


def get_arguments():
    path = "." + sys.argv[3]
    if not os.path.exists(path):
        raise Exception("Path Does not exist")
    args = sys.argv[2].split("/")
    if len(args) >= 2:
        year = int(args[0])
        month = int(args[1])
        if(month > 12 or month < 1):
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
    print(year, month, folder_path)
except IndexError:
    print("Please provide all arguments")
except ValueError:
    print("Please pass correct values")
except Exception as e:
    print(e)
