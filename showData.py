from main import *


# important data that I want to add
item1 = Item(name='Iphone12', price=500, barcode='331111234563', description='wdffdsfdfdsf')
item2 = Item(name='Iphone10', price=400, barcode='111111111111', description='noob')
item3 = Item(name='Iphone11', price=800, barcode='111111111111', description='this is the right')

# adding data to database
db.session.add(item1)
db.session.add(item2)
db.session.add(item3)
db.session.commit()
 
#showing all datas
a = Item.query.all()
print(a)
