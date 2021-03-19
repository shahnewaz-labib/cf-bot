from cf import *
import requests
import pprint

def main():
    response = requests.get('https://codeforces.com/api/user.info?handles=DmitriyH;Fefer_Ivan').json()
    pprint.pprint(response)
    

if __name__ == '__main__':
    main()