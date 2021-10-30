from app import Venue, Show, Artist, Genre, db, app

with app.app_context():
    try:
        Venue.query.delete()
        Artist.query.delete()
        Show.query.delete()
        Genre.query.delete()
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()