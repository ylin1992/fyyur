from models import Venue, Show, Artist, Genre, db
import services

def getArtistList():
    artists = Artist.query.all()
    return [{
        "id": a.id,
        "name": a.name,
    } for a in artists]

def getArtistByID(artist_id):
    artist = Artist.query.get(artist_id)
    if artist is None:
        return None
    
    return {
        "id": artist.id,
        "name": artist.name,
        "genres": [g.name for g in artist.genres],
        "city": artist.city,
        "state": artist.state,
        "phone": artist.phone,
        "website": artist.website,
        "facebook_link": artist.facebook_link,
        "seeking_venue": artist.seeking_venue,
        "seeking_description": artist.seeking_description,
        "image_link": artist.image_link,
        "past_shows": [{
        "venue_id": 1,
        "venue_name": "The Musical Hop",
        "venue_image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
        "start_time": "2019-05-21T21:30:00.000Z"
        }],
        "upcoming_shows": [],
        "past_shows_count": 1,
        "upcoming_shows_count": 0,
    }

def searchArtistFromTerm(searchTerm):
    result = Artist.query.filter(Artist.name.ilike("%" + searchTerm + "%")).all()
    response = {
        "count": len(result),
        "data": [{
            "id": v.id,
            "name": v.name,
            "num_upcoming_shows": 0
        } for v in result],
    }
    return response

def createArtistFromForm(formData):
    print(formData.name.data)
    artist = Artist(
        name=formData.name.data,
        city=formData.city.data,
        state=formData.state.data,
        phone=formData.phone.data,
        image_link=formData.image_link.data,
        genres=services.getGenresFromStringList(formData.genres.data),
        facebook_link=formData.facebook_link.data,
        website=formData.website_link.data,
        seeking_venue=formData.seeking_venue.data,
        seeking_description=formData.seeking_description.data
    )
    try:
        db.session.add(artist)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    finally:
        db.session.close()

def updateArtistByForm(artist_id, formData):
    artist = Artist.query.get(artist_id)
    
    try:
        artist.name=formData.name.data
        artist.city=formData.city.data
        artist.state=formData.state.data
        artist.phone=formData.phone.data
        artist.image_link=formData.image_link.data
        artist.genres=services.getGenresFromStringList(formData.genres.data)
        artist.facebook_link=formData.facebook_link.data
        artist.website=formData.website_link.data
        artist.seeking_venue=formData.seeking_venue.data
        artist.seeking_description=formData.seeking_description.data
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    finally:
        db.session.close()


def preFilling(artist_id, form):
    artist = Artist.query.get(artist_id)
    form.name.data = artist.name
    form.genres.data = [g.name for g in artist.genres]
    form.city.data = artist.city
    form.state.data = artist.state
    form.phone.data = artist.phone
    form.website_link.data = artist.website
    form.facebook_link.data = artist.facebook_link
    form.seeking_venue.data = artist.seeking_venue
    form.seeking_description.data = artist.seeking_description
    form.image_link.data = artist.image_link