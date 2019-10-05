import requests
from bs4 import BeautifulSoup
import pandas as pd

res = requests.get("https://internshala.com/internships/computer%20science-internship")

soup = BeautifulSoup(res.content, 'html.parser')

allData = soup.find_all("div",{"class":"internship_list_container"})

print(type(allData))

cards = allData[1].find_all("div",{"class":"internship_meta"})
cardsBelow = allData[1].find_all("div",{"class":"button_container"})

internshipCompanny = []
internshipType = []
Location = []
startDate = []
duration = []
stipend = []
applyBy = []
detailLink = []
list1 = []
list2 = []

for card in cards:
    headerDetail = card.find_all("div",{"class":"table-cell"})
    header = headerDetail[0].find_all("h4")
    
    internshipType.append(header[0].text.strip())
    internshipCompanny.append(header[1].text.strip())
    Location.append( card.find_all("a",{"class":"location_link"})[0].text.strip())
    
    timeDetail = card.find_all("td")

    startDate.append(timeDetail[0].text.strip())
    duration.append(timeDetail[1].text.strip())
    stipend.append(timeDetail[2].text.strip())
    applyBy.append(timeDetail[4].text.strip())
i=0
for card in cardsBelow:

    infoLink = card.find("a").get("href")
    internshalaLink ="https://internshala.com"
    actualLink = internshalaLink+infoLink
    
    detailLink.append(actualLink)
    list1 = [internshipCompanny[i], internshipType[i], Location[i], startDate[i], duration[i], stipend[i], applyBy[i]]
    list2.append(list1)
    i = i+1


for i in range(5):
    print(applyBy[i])
# for listPrint in list2:
#     print(listPrint)
#     print(" ------------ ")


df=pd.DataFrame(list2)
df.columns=['Company Name','Internship Type','Location','Start Date','Duration','Stipend', 'End Date']
print(df)
df.to_csv('Internshala_Data.csv')
