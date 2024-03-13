from models import User, Post, db 
from app import app 

# with app.app_context():
db.drop_all()
db.create_all()

User.query.delete()
Post.query.delete()

john = User(first_name=john,last_name=Williams)
susan = User(first_name=susan,last_name=Hills)
yun = User(first_name=yun,last_name=Fang)

db.session.add(john)
db.session.add(susan)
db.session.add(yun)

db.session.commit()

