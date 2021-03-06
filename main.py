from cf import *

def main():
    init()
    response = getContestInfo(isGym=False)
    data = getContestList(response)
    showContestList(data)

if __name__ == '__main__':
    main()