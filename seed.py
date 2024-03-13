from models import User, Post, db, default_image_url
from app import app 

with app.app_context():
    db.drop_all()
    db.create_all()
    
    User.query.delete()
    Post.query.delete()
    
    john = User(first_name='john',last_name='Williams',image_url=default_image_url)
    susan = User(first_name='susan',last_name='Hills',image_url=default_image_url)
    yun = User(first_name='yun',last_name='Fang',image_url=default_image_url)
    
    db.session.add(john)
    db.session.add(susan)
    db.session.add(yun)
    
    db.session.commit()

