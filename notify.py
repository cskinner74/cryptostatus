#!/usr/bin/python3

import requests
import argparse
import json
import notify2
import time

#Parser to get coin
parser = argparse.ArgumentParser(description="Get notifications for price changes.")
parser.add_argument("coin", help="Abbreviation of coin to look up")
parser.add_argument("low", help="Low price threshold", type=float)
parser.add_argument("high", help="High price threshold", type=float)
parser.add_argument("interval", help="Check interval in seconds", type=int)
args = parser.parse_args()

#Get price
coin = args.coin.upper()
url = 'https://chasing-coins.com/api/v1/std/coin/'+coin
r = requests.get(url)
data = r.json()
cprice = data['price']

#Setup notification window 
result = ""
result = result + str(coin) + " $" + str(cprice) + "\n"
notify2.init("Cryptocurrency rates notifier")
n = notify2.Notification("Crypto Notifer")
n.set_timeout(1000)
n.update("PRICE ALERT", result)

#Daemon
print("Process running, 'CTRL+Z' then 'bg' to move to background")
print("Process will stop after an alert is triggered to prevent alert spam")
cont = True

#Initial check, if alert is triggered, don't go to while loop
if float(cprice) < args.low or float(cprice) > args.high:
    n.show()
    cont = False
#If initial check doesn't alert, run script until it does
while cont:
    if float(cprice) < args.low or float(cprice) > args.high:
        n.show()
        cont = False
    time.sleep(args.interval)
