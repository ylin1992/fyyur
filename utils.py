from app import Venue, Show, Artist, Genre, db



def initGenreDataBase():
    print("==> Initializing Genre database...")
    if len(Genre.query.all()) > 0:
        return

    genres = [Genre(name=d)
            for d in sample_genres()]
    try:
        for genre in genres:
            db.session.add(genre)
        db.session.commit()
        print("==> Done...")
    except Exception as e:
        print(e)
        db.session.rollback()
    finally:
        db.session.close()


def sample_genres():
    data = [('Blues', 'Blues'),
    ('Classical', 'Classical'),
    ('Country', 'Country'),
    ('Electronic', 'Electronic'),
    ('Folk', 'Folk'),
    ('Funk', 'Funk'),
    ('Hip-Hop', 'Hip-Hop'),
    ('Heavy Metal', 'Heavy Metal'),
    ('Instrumental', 'Instrumental'),
    ('Jazz', 'Jazz'),
    ('Musical Theatre', 'Musical Theatre'),
    ('Pop', 'Pop'),
    ('Punk', 'Punk'),
    ('R&B', 'R&B'),
    ('Reggae', 'Reggae'),
    ('Rock n Roll', 'Rock n Roll'),
    ('Soul', 'Soul'),
    ('Swing', 'Swing'),
    ('Other', 'Other')]
    return [d[0] for d in data]