#!/usr/bin/env python
# coding: utf-8

# Write a python program to display all the hearder tags from wikipedia.org

# In[11]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[12]:



page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
soup = BeautifulSoup(page.content)

header_tags = []
for header in soup.find_all(['h1','h2','h3','h4','h5','h6']):
    header_tags.append(header.name+" "+header.text.strip())

header_tags


# Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)

# In[13]:


page = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
soup = BeautifulSoup(page.content)

movie = []
rating = []
yearofrelease = []

for i in soup.find_all('td',class_="titleColumn"):
    
    movie.append(i.text.replace('\n'," "))
    if len(movie) == 100:
        break
    




for i in soup.find_all('td', class_="ratingColumn imdbRating"):
    
    rating.append(i.text.strip())
    if len(rating) == 100:
        break
    




for i in soup.find_all('span', class_="secondaryInfo"):
    yearofrelease.append(i.text.strip())
    if len(yearofrelease) == 100:
        break

movie
rating
yearofrelease


df = pd.DataFrame({'MoviesName':movie,'Ratings':rating,'Yearofrelease':yearofrelease})
df


# Write a python program to display IMDB’s Top rated 100 Indian movies data.

# In[14]:


page=requests.get('https://www.imdb.com/india/top-rated-indian-movies/')
soup=BeautifulSoup(page.content)   


movie=[]
rating = []
yearofrelease = []

for i in soup.find_all('td',class_="titleColumn"):
    movie.append(i.text.strip().replace('\n'," "))
    if len(movie)==100:
        break
movie



for i in soup.find_all('td',class_="ratingColumn imdbRating"):
    rating.append(i.text.strip())
    if len(rating) == 100:
        break
rating


for i in soup.find_all('span', class_="secondaryInfo"):
    yearofrelease.append(i.text)
    if len(yearofrelease) == 100:
        break

yearofrelease  


df = pd.DataFrame({'MoviesName': movie,'Ratings':rating,'Yearofrelease':yearofrelease})
df


# Write a python program to scrape product name, price and discounts from https://meesho.com/bagsladies/pl/p7vbp

# In[50]:


page=requests.get('https://meesho.com/bags%02ladies/pl/p7vbp')
soup=BeautifulSoup(page.content)


name=[]
price=[]
discount=[]

for i in soup.find_all('p',class_='Text__StyledText-sc-oo0kvp-0 cPgaBh NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 hofZGw NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 hofZGw'):
    name.append(i.text.strip())
for i in soup.find_all('h5',class_='Text__StyledText-sc-oo0kvp-0 dLSsNI'):
    price.append(i.text.strip())
for i in soup.find_all('p',class_='Text__StyledText-sc-oo0kvp-0 iDRzyZ NewProductCard__DiscountTextParagraph-sc-j0e7tu-16 dppwvY NewProductCard__DiscountTextParagraph-sc-j0e7tu-16 dppwvY'):
    discount.append(i.text.strip())


df = pd.DataFrame({'Productname': name,'Price':price,'Discounts':discount})
df


# # Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

# In[15]:


page=requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
soup = BeautifulSoup(page.content)
#scrape team names
team = soup.find_all("span",class_='u-hide-phablet')
team_name = []
for i in team:
    team_name.append(i.text)
matches = [] 
points = [] 
ratings = [] 
new_list = [] 

for i in soup.find_all("td",class_='rankings-block__banner--matches'): 
    matches.append(i.text)
for i in soup.find_all("td",class_='rankings-block__banner--points'):
    points.append(i.text)
for i in soup.find_all("td",class_='rankings-block__banner--rating u-text-right'):
    ratings.append(i.text.replace("\n",""))
for i in soup.find_all("td",class_='table-body__cell u-center-text'):
    new_list.append(i.text)
for i in range(0,len(new_list)-1,2):
    matches.append(new_list[i]) 
    points.append(new_list[i+1]) 
for i in soup.find_all("td",class_='table-body__cell u-text-right rating'):
    ratings.append(i.text)
    

icc=pd.DataFrame({})
icc['Team_name']=team_name[:10]
icc['Matches']=matches[:10]
icc['Points']=points[:10]
icc['Ratings']=ratings[:10]
icc    


# b) Top 10 ODI Batsmen in men along with the records of their team and rating.

# In[16]:


page = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting")
soup = BeautifulSoup(page.content)
players = [] 
team_name = [] 
rating = [] 

for i in soup.find_all("div",class_='rankings-block__banner--name-large'): 
    players.append(i.text)
for i in soup.find_all("div",class_='rankings-block__banner--nationality'): 
    team_name.append(i.text.replace("\n",""))
for i in soup.find_all("div",class_='rankings-block__banner--rating'): 
    rating.append(i.text)
for i in soup.find_all("td",class_='table-body__cell rankings-table__name name'):
    for j in i.find_all('a'):
        players.append(j.text)
for i in soup.find_all("span",class_='table-body__logo-text'): 
    team_name.append(i.text)
for i in soup.find_all("td",class_='table-body__cell rating'): 
    rating.append(i.text)

Batsmen=pd.DataFrame({})
Batsmen['Player']=players[:10]
Batsmen['Team']=team_name[:10]
Batsmen['Rating']=rating[:10]
Batsmen


# c) Top 10 ODI bowlers along with the records of their team and rating
# 

# In[17]:


page = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling")
soup = BeautifulSoup(page.content)

players = [] 
team_name = []  
rating = []

for i in soup.find_all("div",class_='rankings-block__banner--name-large'): 
    players.append(i.text)
for i in soup.find_all("div",class_='rankings-block__banner--nationality'): 
    team_name.append(i.text.replace("\n",""))
for i in soup.find_all("div",class_='rankings-block__banner--rating'): 
    rating.append(i.text)
for i in soup.find_all("td",class_='table-body__cell rankings-table__name name'):
    for j in i.find_all('a'):
        players.append(j.text)
for i in soup.find_all("span",class_='table-body__logo-text'): 
    team_name.append(i.text)
for i in soup.find_all("td",class_='table-body__cell rating'): 
    rating.append(i.text)

bowlers=pd.DataFrame({})
bowlers['Player']=players[:10]
bowlers['Team']=team_name[:10]
bowlers['Rating']=rating[:10]
bowlers


# # Write a python program to scrape cricket rankings from ‘www.icc-cricket.com’.
# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# 

# In[18]:


page = requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")
soup = BeautifulSoup(page.content)

womens_team = soup.find_all("span",class_='u-hide-phablet')
womens_team_name = []
for i in womens_team:
    womens_team_name.append(i.text)
womens_matches = [] 
womens_points = [] 
womens_ratings = [] 
womens_new_list = [] 
for i in soup.find_all("td",class_='rankings-block__banner--matches'): 
    womens_matches.append(i.text)
for i in soup.find_all("td",class_='rankings-block__banner--points'):
    womens_points.append(i.text)
for i in soup.find_all("td",class_='rankings-block__banner--rating u-text-right'):
    womens_ratings.append(i.text.replace("\n",""))
for i in soup.find_all("td",class_='table-body__cell u-center-text'):
    womens_new_list.append(i.text)
for i in range(0,len(womens_new_list)-1,2):
    womens_matches.append(womens_new_list[i]) 
    womens_points.append(womens_new_list[i+1]) 
for i in soup.find_all("td",class_='table-body__cell u-text-right rating'):
    womens_ratings.append(i.text)

womens_icc=pd.DataFrame({})
womens_icc['Team_name']=womens_team_name[:10]
womens_icc['Matches']=womens_matches[:10]
womens_icc['Points']=womens_points[:10]
womens_icc['Ratings']=womens_ratings[:10]
womens_icc    


# b) Top 10 women’s ODI players along with the records of their team and rating.

# In[19]:


page = requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting")
soup = BeautifulSoup(page.content)
players = [] 
team_name = [] 
rating = [] 

for i in soup.find_all("div",class_='rankings-block__banner--name-large'): 
    players.append(i.text)
for i in soup.find_all("div",class_='rankings-block__banner--nationality'): 
    team_name.append(i.text.replace("\n",""))
for i in soup.find_all("div",class_='rankings-block__banner--rating'): 
    rating.append(i.text)
for i in soup.find_all("td",class_='table-body__cell rankings-table__name name'):
    for j in i.find_all('a'):
        players.append(j.text)
for i in soup.find_all("span",class_='table-body__logo-text'):
    team_name.append(i.text)
for i in soup.find_all("td",class_='table-body__cell rating'): 
    rating.append(i.text)

top_players=pd.DataFrame({})
top_players['Player']=players[:10]
top_players['Team']=team_name[:10]
top_players['Rating']=rating[:10]
top_players


# c)Top 10 women’s ODI all-rounder along with the records of their team and rating.

# In[20]:


page = requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder")


soup = BeautifulSoup(page.content)

players = [] 
team_name = []  
rating = []  

for i in soup.find_all("div",class_='rankings-block__banner--name-large'): 
    players.append(i.text)
for i in soup.find_all("div",class_='rankings-block__banner--nationality'): 
    team_name.append(i.text.replace("\n",""))
for i in soup.find_all("div",class_='rankings-block__banner--rating'): 
    rating.append(i.text)
for i in soup.find_all("td",class_='table-body__cell rankings-table__name name'):
    for j in i.find_all('a'):
        players.append(j.text)
for i in soup.find_all("span",class_='table-body__logo-text'): 
    team_name.append(i.text)
for i in soup.find_all("td",class_='table-body__cell rating'): 
    rating.append(i.text)

all_rounder=pd.DataFrame({})
all_rounder['Player']=players[:10]
all_rounder['Team']=team_name[:10]
all_rounder['Rating']=rating[:10]
all_rounder


# Write a python program to scrape details of all the posts from coreyms.com.
# Scrape the heading, date, content

# In[21]:


page = requests.get('https://coreyms.com/')
soup = BeautifulSoup(page.content)

heading=[]
date = []
content = []
youtubevideo =[]

for i in soup.find_all('a',class_="entry-title-link"):
    heading.append(i.text)
    if len(heading)==9:
        break

for i in soup.find_all('time',class_='entry-time'):
    date.append(i.text)
    if len(date)==9:
        break

for i in soup.find_all("div", class_="entry-content"):
    content.append(i.text)
    if len(content)==9:
        break
        
for i in soup.find_all("span", class_="embed-youtube"):
    youtubevideo.append(i.text)
    
    
heading
date
content
youtubevideo

df = pd.DataFrame({'Heading':heading, 'Date':date, 'Content':content, 'Youtube':youtubevideo})
df


# Write a python program to scrape house details from mentioned URL.
# It should include house title, location, area, EMI and price from https://www.nobroker.in/ .Enter three localities which are Indira Nagar, Jayanagar, Rajaji Nagar.

# In[16]:


page = requests.get('https://www.nobroker.in/property/rent/hyderabad/multiple?searchParam=W3sibGF0IjoxNy40NDc0NDc1LCJsb24iOjc4LjM1NjkyNzUsInBsYWNlSWQiOiJDaElKZzVwcF9KU1R5enNSaHBYNzU2M2VkX2ciLCJwbGFjZU5hbWUiOiJJbmRpcmEgTmFnYXIifSx7ImxhdCI6MTcuNTAwMDcyOCwibG9uIjo3OC40MDUxOTU5OTk5OTk5OSwicGxhY2VJZCI6IkNoSUpzWEZxb3VtUnl6c1JiWlZ5ZGVqMkdKSSIsInBsYWNlTmFtZSI6IkpheWFuYWdhciBDb2xvbnkifV0=&radius=2.0&sharedAccomodation=0&city=hyderabad&locality=Indira%20Nagar,&locality=Jayanagar%20Colony')
soup = BeautifulSoup(page.content, 'html.parser')

housetitle = []
location = []
area = []
price = []
emi = []
for i in soup.find_all('span',class_="capitalize text-defaultcolor mb-0.5p font-semibold no-underline hover:text-primary-color po:overflow-hidden po:overflow-ellipsis po:max-w-95 po:m-0 po:font-normal group-hover:text-primary-color group-hover:nounderline"):
    housetitle.append(i.text)
for i in soup.find_all('div',class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0 po:max-w-95"):
    location.append(i.text)
for i in soup.find_all('div',class_="flex flex-col w-33pe items-center border-r border-r-solid border-card-overview-border-color tp:w-half po:w-full last:border-r-1", itemprop="additionalProperty"):
    area.append(i.text)
for i in soup.find_all('div',class_="font-semi-bold heading-6", id="roomType"):
    price.append(i.text)

data = {'House': housetitle, 'Location': location, 'Area': area, 'Price': price}
print(len(housetitle),len(location), len(price),len(area))
df = pd.DataFrame.from_dict(data, orient='columns')
df = df.transpose()
print(df)


# Write a python program to scrape mentioned details from dineout.co.in :
# a) Restaurant b)cuisine c)Location d) Ratings e) Image URL

# In[17]:


page = requests.get('https://www.dineout.co.in/delhi-restaurants/welcome-back?city_name=delhi&limit=21&start=0&cityId=0&listing=1&showAvailableTicket=0&tag%5B%5D=Welcome%20Back&tag%5B%5D=Welcome%20Back')
soup = BeautifulSoup(page.content)
restaurantname = []
cuisine=[]
location = []
rating = []
image = []

for i in soup.find_all('a',class_="restnt-name ellipsis"):
    restaurantname.append(i.text)
for i in soup.find_all('a',class_="restnt-name ellipsis"):
    cuisine.append(i.text)
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
for i in soup.find_all('div',class_="restnt-rating rating-4"):
    rating.append(i.text)
for i in soup.find_all('img',class_="no-img"):
    image.append(i['data-src'])
    
df = pd.DataFrame({'Restaurant': restaurantname,'Cuisine':cuisine,'Location':location, 'Rating': rating,'image_url':image})
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




