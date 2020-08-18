from bs4 import BeautifulSoup
with open('my.txt', 'r', encoding='utf-8') as f:
    a=f.read()
soup=BeautifulSoup(a)
ll=soup.findAll('div',class_='r')
link=[]
text=[]
for i in ll:
    link.append(i.a.get('href'))
    text.append(i.a.text)
ll=soup.findAll('span',class_='st')
des=[]
for j in ll:
    des.append(j.text)
for i,j,k in zip(link,text,des):
    print('link= '+i+' text= '+j+' des= '+k)
