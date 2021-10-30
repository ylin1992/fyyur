from models import Venue, Show, Artist, Genre, db
import datetime
import exceptions
def getShows():
    shows = Show.query.order_by('venue_id').all()
    data = []
    for show in shows:
        artist = Artist.query.get(show.artist_id)
        venue = Venue.query.get(show.venue_id)
        data.append({
            "venue_id": venue.id,
            "venue_name": venue.name,
            "artist_id": artist.id,
            "artist_name": artist.name,
            "artist_image_link": artist.image_link,
            "start_time": str(show.start_time)
        })
    return data

def createShowFromForm(formData):
    venue = Venue.query.get(formData.venue_id.data)
    artist = Artist.query.get(formData.artist_id.data)
    if venue is None:
        raise exceptions.DataNotFoundException(f'Venue ID: {formData.venue_id.data} not found')
    if artist is None:
        raise exceptions.DataNotFoundException(f'Artist ID: {formData.artist_id.data} not found')
    try:
        show = Show(
            start_time=formData.start_time.data,
            venue_id=formData.venue_id.data,
            artist_id=formData.artist_id.data
        )
        venue.shows.append(show)
        artist.shows.append(show)
    except Exception as e:
        raise e

    try:
        db.session.add(show)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    finally:
        db.session.close()

def getPastShowsByArtist(artist_id):
    showsQuery = Show.query.filter_by(artist_id=artist_id)
    shows = showsQuery.filter(Show.start_time < datetime.datetime.now()).all()
    return shows

def getUpcomingByArtist(artist_id):
    showsQuery = Show.query.filter_by(artist_id=artist_id)
    shows = showsQuery.filter(Show.start_time > datetime.datetime.now()).all()
    return shows

def getPastShowsByVenue(venue_id):
    showsQuery = Show.query.filter_by(venue_id=venue_id)
    shows = showsQuery.filter(Show.start_time < datetime.datetime.now()).all()
    return shows

def getUpcomingByVenue(venue_id):
    showsQuery = Show.query.filter_by(venue_id=venue_id)
    shows = showsQuery.filter(Show.start_time > datetime.datetime.now()).all()
    return shows