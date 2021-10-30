from flask_sqlalchemy import SQLAlchemy

# TODO: connect to a local postgresql database

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

db = SQLAlchemy()


# Association tables
venues_shows = db.Table('venues_shows',
                        db.Column('venues_id', db.Integer, db.ForeignKey('Venue.id', ondelete='cascade'), primary_key=True),
                        db.Column('shows_id', db.Integer, db.ForeignKey('Show.id', ondelete='cascade'), primary_key=True),
                        )

artists_shows = db.Table('artists_shows',
                        db.Column('artist_id', db.Integer, db.ForeignKey('Artist.id', ondelete='cascade'), primary_key=True),
                        db.Column('show_id', db.Integer, db.ForeignKey('Show.id', ondelete='cascade'), primary_key=True)
                        )

artists_genres = db.Table('artists_genres',
                        db.Column('artist_id', db.Integer, db.ForeignKey('Artist.id', ondelete='cascade'), primary_key=True),
                        db.Column('genre_id', db.Integer, db.ForeignKey('Genre.id', ondelete='cascade'), primary_key=True)
                        )

venues_genres = db.Table('venues_genres',
                        db.Column('venue_id', db.Integer, db.ForeignKey('Venue.id', ondelete='cascade'), primary_key=True),
                        db.Column('genre_id', db.Integer, db.ForeignKey('Genre.id', ondelete='cascade'), primary_key=True)
                        )

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    
    website = db.Column(db.String(500))
    seeking_talent = db.Column(db.Boolean, nullable=False)
    seeking_description = db.Column(db.String(120))

    shows = db.relationship('Show',
                            secondary=venues_shows,
                            backref=db.backref('venues', lazy=True))
    genres = db.relationship('Genre',
                            secondary=venues_genres,
                            backref=db.backref('venues', lazy=True))


    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    # relationships:
    # upcoming_shows
    # past_shows
    # generes -> artists


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(120), nullable=True)

    shows = db.relationship('Show',
                            secondary=artists_shows,
                            backref=db.backref('artists', lazy=True))

    genres = db.relationship('Genre',
                            secondary=artists_genres,
                            backref=db.backref('artists', lazy=True))
    # relationships
    # past_shows -> shows
    # upcoming_shows -> shows

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
    __tablename__ = 'Show'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.String(), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id', ondelete='cascade'))
    # assume that one show is only hosted by one artist, hence one-to-one relationship
    # but the model is still opened to many-to-many relationship to handle
    # scenarios that one show can be hosted by multiple artists
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id', ondelete='cascade'))
    # relationship
    # artist_id
    
class Genre(db.Model):
    __tablename__ = 'Genre'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)


