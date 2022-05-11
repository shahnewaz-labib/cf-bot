import sys
import requests
import pprint

def getUserInfo(username):
    URL = 'https://codeforces.com/api/user.status?handle=chroot_&from=1&count=3000'

    response = requests.get(URL).json()

    if response["status"] != "OK":
        print(response["status"])
        sys.exit()

    problems = response["result"]

    for item in problems:
        if "verdict" in item and item["verdict"] == "OK":
            print(item["problem"]["name"])

if __name__ == "__main__":
    getUserInfo("_labib")
