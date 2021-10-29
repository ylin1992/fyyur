from app import db, Venue, Show, Artist, Genre

data=[{
    "city": "San Francisco",
    "state": "CA",
    "venues": [{
      "id": 1,
      "name": "The Musical Hop",
      "num_upcoming_shows": 0,
    }, {
      "id": 3,
      "name": "Park Square Live Music & Coffee",
      "num_upcoming_shows": 1,
    }]
  }, {
    "city": "New York",
    "state": "NY",
    "venues": [{
      "id": 2,
      "name": "The Dueling Pianos Bar",
      "num_upcoming_shows": 0,
    }]
  }]


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