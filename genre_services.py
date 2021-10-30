from models import Venue, Show, Artist, Genre, db

def getGenresFromStringList(strings):
    print(strings)
    return [Genre.query.filter_by(name=string).first() for string in strings]