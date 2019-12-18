from splinter import Browser
from bs4 import BeautifulSoup
listings = {}
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path":"Resources/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)
def scrape():
    browser = init_browser()
   # listings = {}
    url = "http://www.canadianminingjournal.com/features/who-are-the-top-40/"
    browser.visit(url)
    html = browser.html
    title = []
    soup = BeautifulSoup(html, "html.parser")
    titles = soup.find_all("strong")
    for item in titles:
        title.append(item.text.replace("\xa0",""))
    listings["miningco"] = title
    browser.quit()
    return listings
scrape()
#for item in listings:
#   print (item.p.text)
import pandas as pd
titles_2 = []
for item in listings["miningco"]:
    item = item[5:-9]
    item = item.split(" (")
    titles_2.append(item)
df = pd.DataFrame(titles_2)
df.columns = ["Company","Revenue (Million)"]
df.to_csv("Resources/Top 40 Mining Companies by Revenue.csv")