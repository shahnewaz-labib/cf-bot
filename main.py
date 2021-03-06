import sys
from cf import *

def main():
    if "-C" in sys.argv:
        init()
        response = getContestInfo(isGym=False)
        data = getContestList(response)
        showContestList(data)
    elif "--help" or "-h" in sys.argv:
        print("usage: python3 <command>\n\nCommands:\n\n-C\t\t\t->  List all the upcoming contests by time remaining.")
        print("-h or --help\t\t->  Help menu")

if __name__ == '__main__':
    main()