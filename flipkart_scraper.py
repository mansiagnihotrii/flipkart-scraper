from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Firefox()

product = []
price = []
rating = []
for i in range(1,17):
	driver.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i))

	content = driver.page_source
	soup = BeautifulSoup(content,"html.parser")
	for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
		name = a.find('div',attrs={'class':'_3wU53n'})
		prices = a.find('div',attrs={'class':'_1vC4OE _2rQ-NK'})
		ratings = a.find('div',attrs={'class':'hGSR34'})
		product.append(name.text)
		price.append(prices.text)
		if ratings:
			rating.append(ratings.text[:3])
		else:
			rating.append('No rating')
	


df = pd.DataFrame({'Product Name':product,'Price':price,'Rating':rating}) 
df.to_csv('products.csv', index=False, encoding='utf-8')

