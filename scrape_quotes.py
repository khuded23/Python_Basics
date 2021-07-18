#Webscraping Excercise from
#https://github.com/khuded23/Complete-Python-3-Bootcamp/blob/master/13-Web-Scraping/01-Web-Scraping-Exercises.ipynb

#Goal:

# get names of all the authors
# get all the quotes on the page
# extract top 10 element tags

import requests
import lxml
import bs4

count =1

while True:
    url = "https://quotes.toscrape.com/page/{}/"
    base_url = url.format(count)
    result = requests.get(base_url)
    soup = bs4.BeautifulSoup(result.text,'lxml')
    obj = soup.select(".quote")


    if result.ok != True:
        print("End of webpages!!")
        break
    elif obj == []:
        print('no more quotes found')
        break
    else:
        print('page num',count)
        count +=1
        for item in obj:
            quote = item.select('.text')
            author = item.select('.author')
            print('Quote',quote[0].text)
            print('Author Name:',author[0].text+'\n')
     
