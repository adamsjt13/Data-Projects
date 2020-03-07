from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

# Generate lists
Year = []
Name = []
College = []
POS = []
Height = []
Weight = []
Wonderlic = []
Forty = []
Bench = []
Vert = []
Broad = []
Shuttle = []
ThreeCone = []


BASE_URL = "http://nflcombineresults.com/nflcombinedata.php"

for year in range(2004,2020):
        URL = BASE_URL+"?year="+str(year)+"&pos=&college="

        html = urlopen(URL).read()
        soup = BeautifulSoup(html, "lxml")
        table = soup.find('table',class_= 'sortable')

        for item in table.find('tbody').findAll('tr'):
                info = item.findAll('td')
                Year.append(info[0].find(text=True))
                Name.append(info[1].find(text=True))
                College.append(info[2].find(text=True))
                POS.append(info[3].find(text=True))
                Height.append(info[4].find(text=True))
                Weight.append(info[5].find(text=True))
                Wonderlic.append(info[6].find(text=True))
                Forty.append(info[7].find(text=True))
                Bench.append(info[8].find(text=True))
                Vert.append(info[9].find(text=True))
                Broad.append(info[10].find(text=True))
                Shuttle.append(info[11].find(text=True))
                ThreeCone.append(info[12].find(text=True))

df=pd.DataFrame(Year,columns=['Year'])
df['Name'] = Name
df['College'] = College
df['Position'] = POS
df['Height'] = Height
df['Weight'] = Weight
df['Wonderlic'] = Wonderlic
df['40_yard_dash'] = Forty 
df['Bench_Press'] = Bench
df['Vertical_Jump'] = Vert 
df['Broad_Jump'] = Broad
df['Shuttle'] = Shuttle
df['3Cone'] = ThreeCone

df.to_csv("combine_stats.csv", index=False)

