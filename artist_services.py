from app import Venue, Show, Artist, Genre, db

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
    result = Artist.query.filter(Artist.name.like("%" + searchTerm + "%")).all()
    response = {
        "count": len(result),
        "data": [{
            "id": v.id,
            "name": v.name,
            "num_upcoming_shows": 0
        } for v in result],
    }
    return response
