import sys
import os

# First argument -e -a -c
# Second argument  year/month
# Third argument pathToFile


def getArguments():
    path = sys.argv[3]
    if not os.path.exists("." + path):
        raise Exception("Path Does not exist")
    args = sys.argv[2].split("/")
    if len(args) >= 2:
        year = args[0]
        month = args[1]
    else:
        year = args[0]
        month = None
    return (year, month, path)


try:
    if (sys.argv[1] not in ["-e", "-a", "-c"]):
        raise Exception("Invalid argument")
    year, month, path = getArguments()
    getArguments()
except IndexError:
    print("Please provide all arguments")
except Exception as e:
    print(e)
