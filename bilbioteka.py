# CLASSES
# 1. Movies
class Movie:
   def __init__(self, title, year, category):
       self.title = title
       self.year = year
       self.category = category
       # Variables
       self._plays = 0
   def play(self, step=1):
       self._plays += step
   def __str__(self):
       return f'{self.title}  ({self.year}) {self._plays}'
   def __repr__(self):
       return 'Film(tytuł: %s, rok: %s, gatunek: %s, wyświetlenia: %f)' % (self.title, self.year, self.category, self._plays)
   def isSeries(self):
        return False

# 2. TV SERIES
class Tvseries(Movie):
    def __init__(self,  enumber, snumber, *args, **kwargs): 
       super().__init__(*args, **kwargs) 
       self.enumber = enumber
       self.snumber = snumber
       # Variables
       self._plays = 0
    def play(self, step=1):
       self._plays += step
    def __str__(self):
       return f'{self.title} {self.snumber}{self.enumber}'
    def __repr__(self):
       return 'Serial(tytuł: %s, rok: %s, gatunek: %s, wyświetlenia: %f)' % (self.title, self.year, self.category, self._plays)
    def isSeries(self):
        return True

# FUNCTIONS
def get_movies(lista):
    movie_list = []
    for item in lista:
        if item.isSeries() == False:
            movie_list.append(item)
    print(movie_list)


def get_series(lista):
    series_list = []
    for item in lista:
        if item.isSeries() == True:
            series_list.append(item)
    print(series_list)


def search(lista):
    search_title = input("Wpisz tytuł, którego szukasz: ")
    for item in enumerate(lista):
        if item.title == search_title:
           print(item)
        else:
            None


def generate_views(lista):
    for k in range(10):
        for l in lista:
            l.play()
    return lista

    
def top_titles(lista):
    print("NAJPOPULARNIEJSZE FILMY I SERIALE")
    for item in lista:
        by_plays = (sorted(lista, key=lambda item: item._plays, reverse=True))
    print(by_plays[:2])


movie1 = Movie(title = "The Shawshank Redemption", year = "1994", category= "drama")
movie2 = Movie(title = "Intouchables", year = "2011", category = "drama")
movie3 = Movie(title = "Shrek", year = "2001", category = "cartoon")

tvseries1 = Tvseries(title = "Our Planet", year = "2019", category = "documentary", enumber = "E01", snumber = "S01")
tvseries2 = Tvseries(title = "Chernobyl", year = "2019", category = "historical", enumber = "E01", snumber = "S01")

biblioteka = [movie1, movie2, movie3, tvseries1, tvseries2]

generate_views(biblioteka) #OK. Działa.

print("")
top_titles(biblioteka)

print("")
search(biblioteka) #nie wyświelta poprawnie indeksu z listy

 

