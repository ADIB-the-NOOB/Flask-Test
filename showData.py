from main import *

db.create_all()
item1 = Item(name = 'Iphone12',price = 500,barcode = '331111234563', description = 'wdffdsfdfdsf' )



a = Item.query.all()
print(a)
