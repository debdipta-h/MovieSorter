import mechanize
from BeautifulSoup import BeautifulSoup
import re

def browse(movieName):
    print(movieName);
    base_url='https://www.imdb.com/find?q=';
    movie='+'.join(movieName.split());
    final_url=base_url+movie+'&s=all';
    br=mechanize.Browser();
    br.open(final_url);
    link=br.find_link(url_regex=re.compile(r'/title/tt.*'));
    linx=br.follow_link(link);
    #print("bori");
    #print(linx.read());
    return linx;


def parse(movie_link):
    genre=[];
    soup=BeautifulSoup(movie_link.read());
    links=soup.findAll(itemprop='genre');
    #print(links);
    for link in links:
        content=link.contents[0];
        if re.match('\s',content)==None:
            genre.append(content.encode('ascii'));
    return genre;

def searchGenre(movie_name):
    movie_link=browse(movie_name);
    genre=parse(movie_link);
    return genre;
def  main():
    movie_link=browse('The Lion King (1994)');
    genre=parse(movie_link);
    print(genre);


if __name__=="__main__":main()

