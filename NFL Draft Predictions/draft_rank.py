from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import requests

BASE_URL = "http://www.nfl.com/draft/history/fulldraft?season="

Draft_rank = []
Draft_round = []
Name = []
POS = []
College = []
Year = []

for year in range(2004,2020):
    
    URL = BASE_URL+str(year)

    html = urlopen(URL).read()
    soup = BeautifulSoup(html, "lxml")
    table = soup.find('table',class_= 'sortable')

    for section in soup.findAll('table'):
        draft_round_header = section.findAll('thead')
        draft_round = draft_round_header[0].find('a')['name']
        for item in section.findAll('tbody'):
            for row in item.findAll('tr'):
                info = row.findAll('td')
                Draft_rank.append(info[0].text)
                Draft_round.append(draft_round)
                Name.append(info[2].text.replace('\n',''))
                POS.append(info[3].text)
                College.append(info[4].text)
                Year.append(year)
    print("year",year)

df = pd.DataFrame(Year,columns=['Year'])
df['Draft_rank'] = Draft_rank
df['Draft_round'] = Draft_round
df['Name'] = Name
df['Position'] = POS
df['College'] = College

df.to_csv("draft_rank.csv", index=False)

                        
