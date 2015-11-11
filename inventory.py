from peewee import *
from money import Money
from datetime import date
import click

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

@click.group()
def main():
    """inventory

    This is a personal inventory tool designed to keep track of all my shit.
    Spurred by moving 4 times in the past year.
    """

@main.command()
def init():
    db.connect()
    db.create_tables([Item])

@main.command()
def value():
    for item in Item.select():
	print item.value

@main.command() 
def list():
    print "name | quantity | value"
    for item in Item.select():
	print str(item.name) + "|" + str(item.quantity)  + "|" + str(item.value)


@main.command()
def add():
    item = Item()
    item.name = raw_input("name: ")
    item.value = Money(amount=raw_input("amount: "), currency='USD')
    item.location = raw_input("location: ")
    item.quantity = int(raw_input("quantity: "))
    item.notes = raw_input("notes: ")
    item.date = date.today()
    item.save()


if __name__ == '__main__':
    main()
