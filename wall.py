"""Anime Walls"""
import requests
import json
import sys
from bs4 import BeautifulSoup
name = sys.argv
global api_fetch
api_fetch = "https://animechan.vercel.app/api/random"
try:
    r = requests.get(api_fetch)
    if r.status_code == 200:
        chan_quote = json.loads(r.text)
        for key in chan_quote:
            print(f"{key} : {chan_quote[key]}")
except IndexError:
    print("[+] Usage: python3 %s <anime name> " % sys.argv[0])
    print("[+] Example: python3 %s naruto" % sys.argv[0])