import re;
import searchMovie;
def refine(files):
    result=[];
    for file in files:
        result.append(re.split('[.\s]',file)[0]);
    return result;

def associate(movies):
    movie_names=extractName(movies);
    movie_list={};
    for name in movie_names:
        genre=searchMovie.searchGenre(name);
        movie_list[name]=genre;
    return movie_list;
    
def extractName(movies):
    movie_names=[];
    for movie in movies:
        tokens=re.split('[.]',movie);
        movie_names.append(tokens[0]);
    return movie_names;
