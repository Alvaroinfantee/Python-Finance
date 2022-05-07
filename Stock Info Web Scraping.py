from cgitb import html
import bs4 as bs
import requests

html = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = bs.BeautifulSoup(html.text)

tickers = []

table = soup.find('table',{'class':'wikitable sortable'})
rows = table.find_all('tr')[1:]
for row in rows:
    ticker = row.find_all('td')[0].text
    tickers.append(ticker[:-1])

print(tickers)