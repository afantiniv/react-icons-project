from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
    __tablename__="user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(1000), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    is_admin = db.Column(db.Boolean(), unique=False, nullable=True)
    firstname = db.Column(db.String(40), unique=False, nullable=True)
    lastname = db.Column(db.String(120), unique=False, nullable=True)
    telnumber = db.Column(db.String(120), unique=False, nullable=True)
    address = db.Column(db.String(120), unique=False, nullable=True)
    country = db.Column(db.String(120), unique=False, nullable=True)
    age = db.Column(db.String(120), unique=False, nullable=True)
    profile_picture_id = db.Column(db.Integer, db.ForeignKey("imagen.id"))
    profile_picture = db.relationship("Imagen")


    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "photo":self.profile_picture_id,
            "firstname":self.firstname,
            "is_active":self.is_active,
            "lastname":self.lastname,
            "telnumber":self.telnumber,
            "address":self.address,
            "country":self.country,
            "age":self.age,
            # do not serialize the password, its a security breach
        }

class TokenBlockedList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token=db.Column(db.String(200), unique=True, nullable=False)
    email=db.Column(db.String(200), nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "token":self.token,
            "email":self.email,
            "created_at":self.created_at
        }


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    type_music = db.Column(db.String(80), unique=False, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    artist_picture_id = db.Column(db.Integer, db.ForeignKey("imagen.id"))
    artist_picture = db.relationship("Imagen")

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
            # do not serialize the password, its a security breach
        }

class Imagen(db.Model):
    __tablename__ = "imagen"
    id = db.Column(db.Integer, primary_key=True)
    resource_path = db.Column(db.String(250), unique=True, nullable=False)
    description = db.Column(db.String(200))


class Posts(db.Model):
    __tablename__="posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), unique=False, nullable=False)
    make = db.Column(db.String(120), unique=False, nullable=False)
    model = db.Column(db.String(120), unique=False, nullable=False)
    style = db.Column(db.String(120), unique=False, nullable=False)
    fuel = db.Column(db.String(120), unique=False, nullable=False)
    transmission = db.Column(db.String(120), unique=False, nullable=False)
    financing = db.Column(db.Boolean(), unique=False, nullable=False)
    doors = db.Column(db.Integer, unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    price = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String(240), unique=False, nullable=False)
    #photo = ??
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship(User)

    def __repr__(self):
        return f'<Post: {self.id}>'
    
    def serializeCompact(self):
       return {
        "title":self.title,
        #"photo":self.photo,
        "year":self.year,
        "make":self.make,
        "model":self.model,
        "price":self.price,
        "post_id":self.id
        }
    
    def serializeFull(self):
       return {
        "title":self.title,
        "make":self.make,
        "model":self.model,
        "style":self.style,
        "fuel":self.fuel,
        "transmission":self.transmission,
        "financing":self.financing,
        "doors":self.doors,
        "year":self.year,
        "price":self.price,
        "description":self.description,
        "user_id":self.user_id
        }

class Fav_posts(db.Model):
    __tablename__= "Fav_posts"
    id = db.Column(db.Integer, primary_key=True)
    post_id=db.Column(db.Integer, db.ForeignKey("posts.id"))
    post=db.relationship(Posts)
    user_id=db.Column(db.Integer, db.ForeignKey("user.id"))
    user=db.relationship(User)

    def __repr__(self):
        return '<Fav_posts %r>' %self.id

    def serialize(self):
        return {
            "Fav #:":self.id,
            "post":self.post.title,
            "user_id":self.user_id,
        }
