from cf import *

def main():
    handle = getHandle()
    response = getUserRating(handle)
    x, y = getXandY(response)
    plot(x, y, handle)
    

if __name__ == '__main__':
    main()