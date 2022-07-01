import requests
from bs4 import BeautifulSoup
import lxml
import json

support_team = "manchester united"


def fetch_event():
    while True:
        source = requests.get(f"https://www.sportinglife.com/football/live/vidiprinter").text
        page = BeautifulSoup(source, "lxml")
        page = page.find("div", class_="Layout__VidiPrinter-sc-194n5h1-0 fQKndu")
        event = page.find("div", class_="Vidiprinter__VidiLine-sc-2htt9j-3 eDlWUR")
        live_event = event.text.strip()
        if support_team in live_event.lower():
            return live_event



