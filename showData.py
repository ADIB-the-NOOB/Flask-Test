from main import *

db.create_all()
item1 = Item(name='Iphone12', price=500, barcode='331111234563', description='wdffdsfdfdsf')
item2 = Item(name= 'Iphone10', price=400, barcode='111111111111', description='noob')

a = Item.query.all()
print(a)
