import sys
from cf import *

def main():
    n = len(sys.argv)

    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        print("usage: python3 <command>\n\nCommands:\n\n-C\t\t\t->  List all the upcoming contests by time remaining.")
        print("-h or --help\t\t->  Help menu")
        print("-p -rating <handle>\t-> Plot rating of handle over time")
    elif sys.argv[1] == "-C" or sys.argv[1] == "--contest":
        init()
        response = getContestInfo(isGym=False)
        data = getContestList(response)
        showContestList(data)
    elif sys.argv[1] == "-p" or sys.argv[1] == "--plot":
        if sys.argv[2] == "-rating" or sys.argv[2] == "-r":
            if n == 4:
                response = getUserRating(sys.argv[3])
                x, y = getXandY(response)
                plot(x, y, sys.argv[3])
            else:
                handle = getHandle()
                response = getUserRating(handle)
                x, y = getXandY(response)
                plot(x, y, handle)

if __name__ == '__main__':
    main()