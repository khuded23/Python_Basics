'''
This program scrapes images from a wiki page and stores them locally

'''



import requests
import lxml
import bs4



url = 'https://en.wikipedia.org/wiki/Cristiano_Ronaldo'

result = requests.get(url)
soup = bs4.BeautifulSoup(result.text,'lxml')


def getimg(url):
    count = 0
    for link in url:
        nlink = 'https:'+link
        print(nlink)
        imagename = "cr7"+'-'+str(count)+'.jpg'
        with open(imagename,'wb') as f:
            print(imagename)
            result = requests.get(nlink)
            f.write(result.content)
            count +=1
            print(count)


image = soup.select('.thumbimage')
count = 0
# #print(image)
imagelist = []
for img in image:
    newimg = image[count]['src']
    count +=1
    imagelist.append(newimg)

getimg(imagelist)
