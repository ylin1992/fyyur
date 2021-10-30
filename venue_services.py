import re
from exceptions import DataNotFoundException
from models import Venue, Show, Artist, Genre, db
import genre_services
import artist_services
import show_services
import datetime

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


def getVenueFromID(venue_id):
    venue = Venue.query.get(venue_id)
    if (venue is None):
        raise DataNotFoundException
    pastShows = venue.getPastShows()
    upcomingShows  = venue.getUpcomingShows()
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
        "past_shows": [{ 
            "artist_id": show.artist_id,
            "artist_name": artist_services.getArtistNameFromID(show.artist_id),
            "artist_image_link": artist_services.getArtistImageLinkFromID(show.artist_id),
            "start_time": str(show.start_time)
        } for show in upcomingShows],
        "upcoming_shows": [{ 
            "artist_id": show.artist_id,
            "artist_name": artist_services.getArtistNameFromID(show.artist_id),
            "artist_image_link": artist_services.getArtistImageLinkFromID(show.artist_id),
            "start_time": str(show.start_time)
        } for show in upcomingShows],
        "past_shows_count": len(pastShows),
        "upcoming_shows_count": len(upcomingShows),
    }



def searchVenueFromTerm(searchTerm):
    result = Venue.query.filter(Venue.name.ilike("%" + searchTerm + "%")).all()
    response = {
        "count": len(result),
        "data": [{
            "id": v.id,
            "name": v.name,
            "num_upcoming_shows": 0
        } for v in result],
    }
    return response

def createVenueFromForm(formData):
    print(formData.name.data)
    venue = Venue(
        name=formData.name.data,
        city=formData.city.data,
        state=formData.state.data,
        address=formData.address.data,
        phone=formData.phone.data,
        image_link=formData.image_link.data,
        genres=genre_services.getGenresFromStringList(formData.genres.data),
        facebook_link=formData.facebook_link.data,
        website=formData.website_link.data,
        seeking_talent=formData.seeking_talent.data,
        seeking_description=formData.seeking_description.data
    )
    try:
        db.session.add(venue)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    finally:
        db.session.close()




def updateVenueByForm(venue_id, formData):
    venue = Venue.query.get(venue_id)
    
    try:
        venue.name=formData.name.data
        venue.city=formData.city.data
        venue.state=formData.state.data
        venue.address=formData.address.data
        venue.phone=formData.phone.data
        venue.image_link=formData.image_link.data
        venue.genres=genre_services.getGenresFromStringList(formData.genres.data)
        venue.facebook_link=formData.facebook_link.data
        venue.website=formData.website_link.data
        venue.seeking_talent=formData.seeking_talent.data
        venue.seeking_description=formData.seeking_description.data
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    finally:
        db.session.close()

def preFilling(venue_id, form):
    venue = Venue.query.get(venue_id)
    form.name.data = venue.name
    form.genres.data = [g.name for g in venue.genres]
    form.address.data = venue.address
    form.city.data = venue.city
    form.state.data = venue.state
    form.phone.data = venue.phone
    form.website_link.data = venue.website
    form.facebook_link.data = venue.facebook_link
    form.seeking_talent.data = venue.seeking_talent
    form.seeking_description.data = venue.seeking_description
    form.image_link.data = venue.image_link

def deleteVenueById(venue_id):
    try:
        Venue.query.filter_by(id=venue_id).delete()
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()

def getVenueNameByID(venue_id):
    return Venue.query.get(venue_id).name

def getImageLinkByID(venue_id):
    return Venue.query.get(venue_id).image_link