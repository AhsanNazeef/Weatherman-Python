import sys
import os
import calendar
from datetime import datetime

# First argument -e -a -c
# Second argument  year/month
# Third argument pathToFile
positive_color = "\033[1;32m"
negative_color = "\033[1;31m"
positive_number = "+"
negative_number = "-"


def draw_temperature_chart(path):
    with open(path, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            data = line.strip().split(',')
            if len(data) > 1:
                date = datetime.strptime(data[0], '%Y-%m-%d')
                day = date.day
                highest_temp = int(data[1])
                lowest_temp = int(data[3])
                print(f"\033[0mDay {day}:")
                print("Highest Temperature:", end=" ")
                if highest_temp > 0:
                    print(positive_color + positive_number *
                          highest_temp, flush=True)
                else:
                    print(negative_color + negative_number *
                          abs(highest_temp), flush=True)
                print(f"({data[1]}°C)")

                print("\033[0mLowest Temperature: ", end=" ")
                if lowest_temp > 0:
                    print(positive_color + positive_number *
                          lowest_temp, flush=True)
                else:
                    print(negative_color + negative_number *
                          abs(lowest_temp), flush=True)
                print(f"({data[3]}°C)")
                print()


def calculate_monthly_averages(path):
    with open(path, 'r') as file:
        next(file)  # Skip the header line
        max_temperatures = []
        min_temperatures = []
        humidities = []
        for line in file:
            data = line.strip().split(',')
            if len(data) > 1:
                date = datetime.strptime(data[0], '%Y-%m-%d')
                max_temperatures.append(float(data[1]))
                min_temperatures.append(float(data[3]))
                humidities.append(float(data[7]))

        # Calculate average highest temperature, average lowest temperature, and average humidity
        avg_highest_temp = sum(max_temperatures) / len(max_temperatures)
        avg_lowest_temp = sum(min_temperatures) / len(min_temperatures)
        avg_humidity = sum(humidities) / len(humidities)

        print(f"Average highest temperature: {avg_highest_temp:.2f}°C")
        print(f"Average lowest temperature: {avg_lowest_temp:.2f}°C")
        print(f"Average humidity: {avg_humidity:.2f}%")


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
    elif (sys.argv[1] == "-a"):
        calculate_monthly_averages(filtered_files[0])
    elif (sys.argv[1] == "-c"):
        draw_temperature_chart(filtered_files[0])

except IndexError:
    print("Please provide all arguments")
except ValueError:
    print("Please pass correct values")
except Exception as e:
    print(e)
