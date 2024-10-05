from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

# Association table
user_groups = db.Table("user_groups",
                       db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
                       db.Column("group_id", db.Integer, db.ForeignKey("groups.id"), primary_key=True)
                       )

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    
     # serialize_only = ("id", "username", "age")
    serialize_rules = ("-profile.user", "-posts.user", "-groups.users")

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    age = db.Column(db.Integer)
    
    profile = db.relationship("Profile", backref="user", uselist=False, cascade="all, delete-orphan")
    
    posts = db.relationship("Post", back_populates="user")

    groups = db.relationship("Group", secondary=user_groups, back_populates="users")


class Profile(db.Model, SerializerMixin):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # username = db.Column(db.String(80), unique=True, nullable=False)
    # age = db.Column(db.Integer)
    # profile = db.relationship('Profile', backref='user', cascade = 'all, delete-orphans')


class Post(db.Model, SerializerMixin):
    __tablename__ = "posts"
    
    serialize_rules = ("-user.posts", "-user.groups")

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    user = db.relationship("User", back_populates="posts")


class Group(db.Model, SerializerMixin):
    __tablename__ = "groups"
    id  =  db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(20))
    
    users = db.relationship("User", secondary=user_groups, back_populates="groups")