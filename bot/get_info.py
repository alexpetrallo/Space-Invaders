import requests
from bs4 import BeautifulSoup as bs
import os

#dis is the website, guy
url = 'https://www.pexels.com/search/models'

page =  request.get(url)
soup = bs(page.text, 'html.paser')

#locate the elements with an img tag
image_tags = soup.findAll('img')

#create dir of the images
if not os.path.exists('models'):
    os.markedirs('models')

#move that dir to a new dir
os.chdir('models')

#i think i gotta make this to order the file shits to call
for image in image_tags:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('model-' + str(x) + '.jpg','wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x +=1
    except:
        pass
