import requests
from bs4 import BeautifulSoup
movieName = input('Enter movie Name: ')
movieName = movieName.lower()
url ='https://www.imdb.com/chart/top/'
r = requests.get(url)

html = r.text
soup = BeautifulSoup(html,'html.parser')

tbody = soup.find('tbody',{'class':'lister-list'})
trow = tbody.findAll('tr')

for tr in trow:
        td = tr.find('td',{'class':'titleColumn'})
        imdbMovieName = td.a.string.lower().strip()
        if imdbMovieName == movieName:
            movieID = td.a['href']
            movieURL = f'https://www.imdb.com/{movieID}'
            r = requests.get(movieURL)
            html = r.text
            soup = BeautifulSoup(html,'html.parser')
            dir = soup.find('a',{'class':'ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link'})
            dirName = dir.string.strip()
            dirTD = dir['href']
            dirURL = f'https://www.imdb.com/{dirTD}'
            print('Director Name is: ',dirName,'and the URL is:',dirURL)
            r = requests.get(dirURL)
            html = r.text
            soup = BeautifulSoup(html,'html.parser')
            l=[]

            knownFor = soup.find('div',{'id':'knownfor'})
            movieDiv = knownFor.findAll('div',{'class':'knownfor-title'})
            for div in movieDiv:
                moviediv = div.find('div',{'class':'knownfor-title-role'})
                dirMovies = moviediv.a.string
                l.append(dirMovies)
                #print(dirMovies)
            break
print('Other movies of this director are: ',end='\n')
for nme in l:
    print(nme)
        