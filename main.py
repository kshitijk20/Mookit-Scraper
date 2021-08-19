from bs4 import BeautifulSoup
from lxml import html
import codecs
import pandas as pd

## Using BeautifulSoup
with codecs.open('source2.html', 'r', encoding='utf-8', errors='ignore') as fdata:
    soup=BeautifulSoup(fdata,'lxml')

## Number of lectures that we want to scrap out
n=int(input("Enter the number of lectures you want to scrap\n"))

week_list=[]
lecture_list=[]
links_list=[]
all_weeks=[]
body=soup.find('body')

## For storing all the week numbers corresponding to lecture numbers within a particular week
f=0
for each_week in body.find_all('div',class_='weekDetailsBox'):
    k=0
    for i in each_week.find_all('div',class_='lectureInfoBoxText'):
      k+=1
       
    for x in range(k):
        all_weeks.append('Week '+str(f))
    f+=1

## For storing the week numbers corresponding to n
for i in range(n):
    week_list.append(all_weeks[i])

# print(week_list)

## For storing the lectures names corresponding to n
i=0
for lecture in body.find_all_next('div',class_='lectureInfoBoxText'):
    if(i<n):
        lecture_list.append(lecture.text.replace('\r\n','').strip())
        i+=1

# print(lecture_list)

## For storing the links corresponding to the Lectures(depends on the value of n)
k=0
for link in body.find_all('div',class_="lectureItem completeRowLectureColorWatched"):
    if(k<n):
        #Storing the links by adding the left out part of url with the 'href' attribute in anchor tag
        y="https://hello.iitk.ac.in/mth102aa2021/"+link.a['href']
        links_list.append(y)
        k+=1

# print(links_list)

data= {'Week No.': week_list, 'Lecture Name': lecture_list, 'Lecture Video Links': links_list}
df=pd.DataFrame(data)

#Saving to dataframe
df.to_csv('mookit.csv')