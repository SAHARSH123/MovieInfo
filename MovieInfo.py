import requests
from bs4 import BeautifulSoup

#Taking input movie / tv series string
print('Search for movie')
inp = input()
print('Searching......')

#requesting google page for movie
page = requests.get("http://www.google.com/search?q=" + inp + "imdb rating")
soup = BeautifulSoup(page.content,'html.parser')

#fetching imdb page of movie
find_links = soup.find(id="search")
imdb_link=find_links.find(class_="hJND5c").find('cite').getText()
# print(imdb_link)

#requesting imdb page
imdb_page=requests.get(imdb_link)
imdb_soup=BeautifulSoup(imdb_page.content,'html.parser')


#movie_name
print('Movie Name')
movie_name=imdb_soup.find_all('h1')[0].getText()
print(movie_name)
print()

#rating
print('Movie Rating')
rating_div=imdb_soup.find(id="title-overview-widget")
rating=rating_div.find(class_="ratingValue").find(attrs={"itemprop":"ratingValue"}).getText()
print(rating)
print()

title_wrapper=imdb_soup.find(class_="title_wrapper")
#genre of movie
print('Movie Genres')
genres=title_wrapper.select("a[href*=genre]")
for index,genre in enumerate(genres):
	print(str(index+1)+": "+genre.getText())
print()

#movie release date
print('Release date')
movie_date=title_wrapper.select("a[href*=releaseinfo]")[0].getText()
print(movie_date)
print()

#movie summary
print('Story Line:')
summary=imdb_soup.find(id="titleStoryLine").find('p').find('span').getText()
print(summary)
print()

#movie cast director and writer
credits_link=requests.get(imdb_link+"fullcredits?ref_=tt_cl_sm#cast")
credit_soup=BeautifulSoup(credits_link.content,'html.parser')

# credit_div=credit_soup.find(id="fullcredits_content").find(class_="simpleTable simpleCreditsTable")
# print(credit_div)
#director
print("Director:")
if(credit_soup.find(id="fullcredits_content").find(class_="simpleTable simpleCreditsTable")==None):
	print("Director data not avialable\n")
else:	
	director = credit_soup.find(id="fullcredits_content").find(class_="simpleTable simpleCreditsTable").find_all('a')
	for index,dir_name in enumerate(director):
		print(str(index+1)+" "+dir_name.getText())

#writer
print("Writer")
if(credit_soup.find(id="fullcredits_content").find_all(class_="simpleTable simpleCreditsTable")==1):
	print("Writer data not avialable\n")
else:	
	writer = credit_soup.find(id="fullcredits_content").find_all(class_="simpleTable simpleCreditsTable")[1].find_all('a')
	for index,writer_name in enumerate(writer):
		print(str(index+1)+" "+writer_name.getText())


#cast
print("Cast")
if(credit_soup.find(id="fullcredits_content").find(class_="cast_list").find_all('a')==None):
	print("Cast Not available\n")
else:
	count=0
	cast=credit_soup.find(id="fullcredits_content").find(class_="cast_list").find_all(class_="primary_photo",limit=4)
	for i in cast:
		count=count+1
		print(str(count)+" "+i.find('img').get('title'))








