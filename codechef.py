import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
t= PrettyTable(['Code','Name','Start'])
url='https://www.codechef.com/contests'
page= requests.get(url)
soup =BeautifulSoup(page.content,'html.parser')
#print"soup.prettify()"
table=soup.findAll('table',class_="dataTable")
req_table=table[1]
tr=req_table.tbody.findAll('tr')
#print(len(tr))
td=tr[0].findAll('td')
#print(len(td))
#print(td[0].text)
for i in range(len(tr)):
  td=tr[i].findAll('td')
  t.add_row([td[0].text,td[1].text,td[2].text])
t.align="l"

print(t)
