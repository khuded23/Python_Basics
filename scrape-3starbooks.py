import requests
import lxml
import bs4
import time

'''
Scraping all the books in toscrape.com with 3 star rating:
1.next scrape the price of the book
2. print only if the book is in stock

codeby: Kiran Huded

'''
#scrape all the book with rating three in books.toscrape.com

count = 1

while True:

    url = "https://books.toscrape.com/catalogue/page-{}.html"
    base_url=url.format(count)
    result = requests.get(base_url)

    if result.ok != True:
        print("End of webpages!!")
        break
    else:

        print('page num',count)
        count +=1
        soup = bs4.BeautifulSoup(result.text,'lxml')
        product = soup.select('.product_pod')
        #count +=1

        with open('3starbooks.txt','a+')as f:
            f.write("All the books with 3-start ratings:\n\n")

            for item in product:
                if item.select(".star-rating.Three") != []:
                    f.write(item.select('a')[1]['title']+'\n')
                    #print(item.select('a')[1]['title'])
