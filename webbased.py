import requests
import webbrowser
from bs4 import BeautifulSoup
import jsonupdater
username = jsonupdater.getusername()
def where(data):
    data = data.split(" ")
    location = data[data.index("is") + 1:]
    search_terms = '+'.join(location)
    url = "https://www.google.com/maps/search/?api=1&query={}".format(search_terms)
    chrome_browser = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
    chrome_browser.open_new_tab(url)
    return("Hold on " + username +", I will show you where " + ' '.join(location) + " is.")

def search(data):
    data = data.split(" ")
    if "Search" in data:
        data = data[data.index("Search")+1:]
    else:
        data = data[data.index("search") + 1:]
    search_terms = '+'.join(data)
    url = "https://www.google.com.tr/search?q={}".format(search_terms)
    chrome_browser = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
    chrome_browser.open_new_tab(url)
    return ('searching ' + " ".join(data) + 'on Google')

def browse(data):
    data = data.split(" ")
    if "browse" in data:
        data = data[data.index("browse")+1:]
    else:
        data = data[data.index("open")+1:]
    keyword = '+'.join(data)
    browse = "https://www.google.co.uk/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q=" + keyword
    r = requests.get(browse)
    soup = BeautifulSoup(r.text, 'html.parser')
    container = soup.find('div', {'id': 'search'})
    url = container.find('cite').text
    chrome_browser = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
    chrome_browser.open_new_tab(url)
    return ('opening ' + " ".join(data))