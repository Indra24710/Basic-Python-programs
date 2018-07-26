from bs4 import BeautifulSoup
from prettytable import PrettyTable
t= PrettyTable(['Code','Name','Start'])
url='http://books.toscrape.com/'
page= requests.get(url)
soup =BeautifulSoup(page.content,'html.parser')
#print(soup.prettify())
div=soup.findAll('div',class_="col-sm-8 col-md-9")
#print(len(div))
ol=div[0].section.findAll('ol',class_="row")
#print(len(ol))
li=ol[0].findAll("li")
#print(li[0])
p_div=li[0].findAll('div',class_='product_price')
#print(p_div[0].p.text)
t=PrettyTable(['Sr.No','Name','Price'])
for i in range(len(li)):
  p_div=li[i].findAll('div',class_='product_price')
  t.add_row([i+1,li[i].article.h3.a["title"],p_div[0].p.text])
t.align='l'
print(t)
