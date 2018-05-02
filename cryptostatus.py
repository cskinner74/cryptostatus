import requests
import json
import sys
import argparse

#Parser section
parser = argparse.ArgumentParser(description="Check current altcoin prices.\nAPI provided by https://chasing-coins.com/api")
parser.add_argument("coin", help="Abbreviation of coin to look up")
parser.add_argument("-hl", "--highlow", help="Display 24 Hour High/Low", action="store_true")
parser.add_argument("-n", "--notices", help="Show recent notices", action="store_true")
args = parser.parse_args()

#Current price lookup
url = 'https://chasing-coins.com/api/v1/std/coin/'+args.coin.upper()
r = requests.get(url)
data = r.json()
cprice=data['price']
print('Current price: $' + cprice)
hour = data['change']['hour']
day = data['change']['day']
print("Change:")
print("Past hour: $" + hour)
print("Past day: $" + day)

#24 hour high low 
if(args.highlow):
	url = 'https://chasing-coins.com/api/v1/std/highlow_24h/'+args.coin.upper()
	r = requests.get(url)
	data = r.json()
	high = data['high']
	high_time = data['high_time']
	low = data['low']
	low_time = data['low_time']
	print('\n24 Hour High/Low data')
	print("High of $"+str(high)+" at "+high_time)
	print("Low of $"+str(low)+" at "+low_time)

#Notices
if(args.notices):
	print('\nRecent Notices for '+args.coin.upper())
	url = 'https://chasing-coins.com/api/v1/std/notices/'+args.coin.upper()
	r = requests.get(url)
	data = r.json()
	for l in data:
		time = l['created_at']
		notice = l['notice']
		print(time+": "+notice)
	
