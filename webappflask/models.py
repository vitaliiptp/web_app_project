from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from webappflask import db, login_manager
from flask_login import UserMixin
import uuid



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    # __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    # def __init__(self, username, email, image_file, password, posts, budget, items):
    #     self.username = username
    #     self.email = email
    #     self.image_file = image_file
    #     self.password = password
    #     self.posts = posts
    #     self.budget = budget
    #     self.items = items
    #     self.uuid = str(uuid.uuid4())

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
        else:
            return f"{self.budget}$"

    def can_purchase(self, item_obj):
        return self.budget >= item_obj.price

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    # __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # def __init__(self, title, date_posted, content, user_id):
    #     self.title = title
    #     self.date_posted = date_posted
    #     self.content = content
    #     self.user_id = user_id
    #     self.uuid = str(uuid.uuid4())

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class Item(db.Model):
    # __tablename__ = 'items'

    id = db.Column(db.Integer(), primary_key=True)
    uuid = db.Column(db.String(36), unique=True)
    image_file = db.Column(db.String(20), nullable=False, default='default_item.jpg')
    name = db.Column(db.String(36), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    author = db.Column(db.String(36), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # def __init__(self, name, price, image_file, user_id, author):
    #     self.name = name
    #     self.price = price
    #     self.image_file = image_file
    #     self.author = author
    #     self.user_id = user_id
    #     self.uuid = str(uuid.uuid4())

    def __repr__(self):
        return f'Item {self.name}'

    def buy(self, user):
        self.owner = user.id
        user.budget -= self.price
        db.session.commit()


class Recipe(db.Model):
    # __tablename__ = 'recipes'

    id = db.Column(db.Integer(), primary_key=True)
    uuid = db.Column(db.String(36), unique=True)
    title = db.Column(db.String(length=100), nullable=False, unique=True)
    serves = db.Column(db.String(length=36), nullable=False)
    preptime = db.Column(db.String(length=12), nullable=False)
    description = db.Column(db.String(length=1500), nullable=False)

    # def __init__(self, title, serves, preptime, description):
    #     self.title = title
    #     self.serves = serves
    #     self.preptime = preptime
    #     self.description = description
    #     self.uuid = str(uuid.uuid4())

    def __repr__(self):
        return f'Recipe {self.name}'
