from application import db

from store.models import Store

class Species(db.Document):
    name = db.StringField(db_field="n")

    meta = {
        'indexes': [('name')]
    }

class Breed(db.Document):
    name = db.StringField(db_field="n")
    species = db.ReferenceField(Species, db_field="s")

    meta = {
        'indexes': [('name')]
    }

class Pet(db.Document):
    external_id = db.StringField(db_field="ei")
    name = db.StringField(db_field="n")
    species = db.ReferenceField(Species, db_field="s")
    breed = db.ReferenceField(Breed, db_field="b")
    age = db.IntField(db_field="a")
    store = db.ReferenceField(Store, db_field="st")
    price = db.DecimalField(db_field="p", precision=2, rounding='ROUND_HALF_UP')
    sold = db.BooleanField(db_field="sl", default=False)
    received_date = db.DateTimeField(db_field="rd")
    sold_date = db.DateTimeField(db_field="sd")

    meta = {
        'indexes': [('external_id', 'sold')]
    }
