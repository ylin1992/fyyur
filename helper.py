from app import Venue, Show, Artist, Genre, db



def getAreas():
    venues = Venue.query.order_by('state', 'city').all()
    if (len(venues) == 0):
        return []
    areas = []
    currentState = venues[0].state
    currentCity = venues[0].city
    area = {}
    for v in venues:
        city = v.city
        state = v.state
        if (city != currentCity or state != currentState or len(area) == 0):
            area = {
                'city': city,
                'state': state,
                'venues': [{
                    'id': v.id,
                    'name': v.name,
                    'num_upcoming_shows': 0 # TODO: add a function to caculate upcoming shows
                }]
            }
            areas.append(area)
        else:
            area['venues'].append({
                'id': v.id,
                'name': v.name,
                'num_upcoming_shows': 0
            })
    return areas

data1={
"id": 1,
"name": "The Musical Hop",
"genres": ["Jazz", "Reggae", "Swing", "Classical", "Folk"],
"address": "1015 Folsom Street",
"city": "San Francisco",
"state": "CA",
"phone": "123-123-1234",
"website": "https://www.themusicalhop.com",
"facebook_link": "https://www.facebook.com/TheMusicalHop",
"seeking_talent": True,
"seeking_description": "We are on the lookout for a local artist to play every two weeks. Please call us.",
"image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
"past_shows": [{
    "artist_id": 4,
    "artist_name": "Guns N Petals",
    "artist_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
    "start_time": "2019-05-21T21:30:00.000Z"
}],
"upcoming_shows": [],
"past_shows_count": 1,
"upcoming_shows_count": 0,
}


def getVenueFromID(venue_id):
    venue = Venue.query.get(venue_id)
    return {
        'id': venue.id,
        'name': venue.name,
        'genres': [g.name for g in venue.genres],
        'address': venue.address,
        'city': venue.city,
        'state': venue.state,
        'phone': venue.phone,
        "website": venue.website,
        "facebook_link": venue.facebook_link,
        "seeking_talent": venue.seeking_talent,
        "seeking_description": venue.seeking_description,
        "image_link": venue.image_link,
        "past_shows": [{ # TODO: adjust show and artist to one-to-many
            "artist_id": 4,
            "artist_name": "Guns N Petals",
            "artist_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
            "start_time": "2019-05-21T21:30:00.000Z"
        }],
        "upcoming_shows": [],
        "past_shows_count": 1,
        "upcoming_shows_count": 0,
    }
