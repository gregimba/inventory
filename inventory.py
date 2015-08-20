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



def str_to_usd(string):
     amount = int(string)
     return Money(amount=amount,currency='USD')

def init():
    db.connect()
    db.create_tables([Item])

def value():
    for item in Item.select():
	print item.value

def list():
    print "name | quantity | value"
    for item in Item.select():
	print str(item.name) + "|" + str(item.quantity)  + "|" + str(item.value)

def add():
    item = Item()
    item.name = raw_input("name: ")
    item.value = Money(amount=raw_input("amount: "), currency='USD')
    item.location = raw_input("location: ")
    item.quantity = int(raw_input("quantity: "))
    item.notes = raw_input("notes: ")
    item.date = date.today()
    item.save()
