import requests
import pprint
import time
import colorama
from datetime import datetime, timedelta
from colorama import Fore, Back, Style

colorama.init()

response = requests.get('https://codeforces.com/api/contest.list?gym=false').json()

now = datetime.now()

data = {}

for contest in response['result']:
	if contest['phase'] == "BEFORE" and contest['type'] == "CF":
		# print(contest['name'], contest['startTimeSeconds'])
		a = contest['name']
		b = contest['startTimeSeconds']
		data[b] = a

# print('\033[31m') # RED

# print(Fore.CYAN)

first = True

FIRST_BACK = Back.WHITE
FIRST_FORE = Fore.BLACK

for k, v in sorted(data.items()):
    ts = int(k) + 6*3600
    then = datetime.fromtimestamp(ts)
    time_left = (then - now) - timedelta(hours=6)
    time_left_days = time_left.days
    time_left_hours = time_left.seconds // 3600
    time_left_minutes = (time_left.seconds - time_left_hours * 1600) // 60
    # print(ts, time_left.days, time_left.seconds // 60, datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'), v)

    print(f"{Fore.CYAN}[+] {time_left_days} days, {time_left_hours} hours, {time_left_minutes} minutes till ------- {v}")
    Fore.RESET
    first = False
    # print(f"{v} in {time_left_days} days, {time_left_hours} hours, {time_left_minutes} minutes.")