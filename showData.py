from main import *

# db.session.add(item1)
# db.session.commit()

db.session.add(item2)
db.session.commit()

a = Item.query.all()
print(a)
