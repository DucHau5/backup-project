import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://dantri.com.vn/cong-nghe.htm' 

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('article')

data = []

for article in articles:
    title = article.find('h3') 
    description = article.find('p')  
    image = article.find('img')  
    
    article_url = article.find('a')['href']
    article_response = requests.get(article_url)
    article_soup = BeautifulSoup(article_response.text, 'html.parser')
    content = article_soup.find('div', {'class': 'fck_detail'})
    
    data.append({
        'Title': title.get_text() if title else None,
        'Description': description.get_text() if description else None,
        'Image URL': image['src'] if image else None,
        'Content': content.get_text() if content else None,
    })

df = pd.DataFrame(data)

df.to_csv('dantri_articles.csv', index=False) 

