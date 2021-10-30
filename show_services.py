from models import Venue, Show, Artist, Genre, db
import services
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
            "start_time": show.start_time
        })
    return data

def createShowFromForm(formData):
    if Venue.query.get(formData.venue_id.data) is None:
        raise exceptions.DataNotFoundException(f'Venue ID: {formData.venue_id.data} not found')
    if Artist.query.get(formData.artist_id.data) is None:
        raise exceptions.DataNotFoundException(f'Artist ID: {formData.artist_id.data} not found')
    try:
        show = Show(
            start_time=formData.start_time.data,
            venue_id=formData.venue_id.data,
            artist_id=formData.artist_id.data
        )
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