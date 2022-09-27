#!/usr/bin/env python
# coding: utf-8

# # Flipkart OnePlus Series web scraping

# In[57]:


from  bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


oneplus_list = list()
oneplus_url = 'https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_1_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_1_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles%7CMobiles&requestId=955e697b-01b6-49cd-95ab-82440adb5d24&as-backfill=on&p%5B%5D=facets.brand%255B%255D%3DOnePlus&sort=price_desc'
response = requests.get(oneplus_url)
soup = BeautifulSoup(response.text,'html.parser')

containers = soup.findAll('div',{'class':'_2kHMtA'})

for container in containers:
    
    product=container.find('div',{'class':'_4rR01T'})
    productName=(product.text.split('-')[0].strip())

    stars = container.find('div',{'class':'_3LWZlK'})
    try: Stars = stars.text
    except: Stars = ''
    
    try:
        Rating = container.find('span',{'class':'_2_R_DZ'})
        Ratings = Rating.text.split('&')[0]
        Reviews = Rating.text.split('&')[1]
    except: Ratings = Reviews = '' 

    price = container.find('div',{'class':'_30jeq3 _1_WHN1'}).text.replace(',',' ')
    info = container.findAll('li',{'class':'rgWa7D'})
    Ram = info[0].text
    Display = info[1].text
    Camera = info[2].text
    Battary = info[3].text
    
    Image = container.img
    ImagesURL = Image.get('src')
    
    oneplus_list.append([productName,Stars,Ratings,Reviews,price,Ram,Display,Camera,Battary,ImagesURL])
    
    
df = pd.DataFrame(oneplus_list, columns=['ProductName', 'Stars', 'Ratings', 'Reviews', 'Price', 'Ram', 'Display', 'Camera', 
                                         'Battary', 'ImagesURL'])
df


# In[58]:


df.drop_duplicates(inplace=True)


# In[59]:


df.shape


# In[61]:


df.loc[df.ProductName.str.contains('OnePlus 10 Pro')]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




