from imdb import IMDb ,IMDbError

# create an instance of the IMDb class
ia = IMDb()

# Search a movie
# movies = ia.search_movie('matrix')
# the_matrix.infoset2keys me devuelve todos los atributos que tiene
# get a movie and print its director(s)
the_matrix = ia.get_movie('0133093')
print('Tipo: ' + the_matrix['kind'])
print('Titulo: ' + the_matrix['title'])
print('Año: ' + str(the_matrix['year']))
print('Duracion: ' + str(the_matrix['runtime'][0]))
print('Puntaje: ' + str(the_matrix['rating']))
print('Generos: ' + ", ".join(the_matrix['genres']))
print('Img: ' + the_matrix['cover url']) #'full-size cover url'
print(the_matrix['director']) # tipo lista
print(the_matrix['cast'][0:4]) # tipo lista

serie = ia.get_movie('0386676')
print('Tipo: ' + serie['kind'])

# Search person
#people = ia.search_person('angelina')

import pdb; pdb.set_trace()

def print_movie():
    try:
        movie_name = input()
        movies = ia.get_movie(movie_name)
        for x in movies:
            print(x)
    except IMDbError as e:
        print(e)

#print_movie()
