from peewee import *
from money import Money
from datetime import date


db = SqliteDatabase('inventory.db')


class Item(Model):
    name = CharField()
    value = CharField()
    location = CharField()
    quantity = IntegerField()
    notes = TextField()
    date = DateField()

    class Meta:
        database = db


def init():
	db.connect()
	db.create_tables([Item])


