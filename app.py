from flask import Flask, make_response #constructor
from flask_migrate import Migrate
from models import db, User, Post, Profile

# Creation of Flask application object
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db' # # configure a database connection to the local file app.db.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Prevents a lot of unnecessary information.
# app.json.compact = False

# Creation of a migration object
migrate = Migrate(app, db) #Creates a connection between the app instance and the database.
db.init_app(app) # Initializes the app to use the db.

@app.route("/")
def index():
    return "<h1>Welcome to Flask!</h1>"

@app.route("/users/<string:username>")
def getUsername(username):
    return f"<h1>Welcome to Flask development, {username}!</h1>"

@app.route('/users')
def getUsers():
    users =[{"id": user.id, "username": user.username, "age": user.age, "email": user.email, "role": user.role} for user in User.query.all()]
    # print(users)
    return make_response(users, 200)

@app.route("/posts")
def posts():
    # GET => Retrieves all the records from the database
    posts = [post.to_dict() for post in User.query.all()]
    return make_response(posts, 200)

# @app.route("/numbers/<int:num>")
# def getNumber(num):
#     return f"<h1>The number is {num}!</h1>"

# @app.route("/floats/<float:num>")
# def getFloat(num):
#     return f"<h1>The number is {num}!</h1>"

if __name__ == "__main__":
    app.run(port=5000, debug=True)