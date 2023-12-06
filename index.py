import sys
import os
import calendar
from datetime import datetime

# First argument -e -a -c
# Second argument  year/month
# Third argument pathToFile


def max_min_humid_temp_of_year(files):
    max_temp = float('-inf')
    min_temp = float('inf')
    max_humidity = float('-inf')

    date_max_temp = ''
    date_min_temp = ''
    date_max_humidity = ''

    for file in files:
        max_temp, date_max_temp, min_temp, date_min_temp, max_humidity, date_max_humidity = get_max_min_humid_temp(
            file, max_temp, min_temp, max_humidity, date_max_temp, date_min_temp, date_max_humidity)

    # Format and print the overall results
    print(
        f"Highest overall: {max_temp}C on {get_month(date_max_temp.month)} {date_max_temp.day}")
    print(
        f"Lowest overall: {min_temp}C on {get_month(date_min_temp.month)} {date_min_temp.day}")
    print(
        f"Humidity overall: {max_humidity}% on {get_month(date_max_humidity.month)} {date_max_humidity.day}")


def get_month(month):
    return datetime.strptime(str(month), '%m').strftime('%B')


def get_max_min_humid_temp(path, max_temp, min_temp, max_humidity, date_max_temp, date_min_temp, date_max_humidity):
    with open(path, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            data = line.strip().split(',')
            if len(data) > 1:
                date = datetime.strptime(data[0], '%Y-%m-%d')
                max_temp_val = float(data[1])
                min_temp_val = float(data[3])
                humidity_val = float(data[7])

                if max_temp_val > max_temp:
                    max_temp = max_temp_val
                    date_max_temp = date

                if min_temp_val < min_temp:
                    min_temp = min_temp_val
                    date_min_temp = date

                if humidity_val > max_humidity:
                    max_humidity = humidity_val
                    date_max_humidity = date
    return (
        max_temp, date_max_temp,
        min_temp, date_min_temp,
        max_humidity, date_max_humidity
    )


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
    if (sys.argv[1] == "-e"):
        max_min_humid_temp_of_year(filtered_files)

except IndexError:
    print("Please provide all arguments")
except ValueError:
    print("Please pass correct values")
except Exception as e:
    print(e)
