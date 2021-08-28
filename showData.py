from main import *

# important data that I want to add
item1 = Item(name='Iphone12', price=500, barcode='331111234563', description='wdffdsfdfdsf')
item2 = Item(name='Iphone10', price=400, barcode='111111111111', description='noob')
item3 = Item(name='Iphone11', price=800, barcode='111111111111', description='this is the right')

# adding data to database
# db.session.add(item1)
# db.session.add(item2)
# db.session.add(item3)
# db.session.commit()

Item.query.filter_by(price=500)
for item in Item.query.filter_by(price= 500):
    print(item.name)
# showing all datas
# for item in Item.query.all():
#    print(item.name)
#    print(item.price)
#   print(item.description)
#    print(item.id)
#    print(item.barcode)
