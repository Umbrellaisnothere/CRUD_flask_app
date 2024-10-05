from flask import Flask, make_response,request #constructor
from flask_migrate import Migrate
from models import db, User, Post, Profile
from flask_cors import CORS

# Creation of Flask application object
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db' # # configure a database connection to the local file app.db.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Prevents a lot of unnecessary information.
# app.json.compact = False

# Creation of a migration object
migrate = Migrate(app, db) #Creates a connection between the app instance and the database.
db.init_app(app) # Initializes the app to use the db.
CORS(app)
# Building APIs
# http => GET, POST, PATCH OR DELETE
# GET => Retrieve all the records from the database
#     => retrieve a single record from the database
    
# POST => Creating a new record and inserting it into the database

# PATCH => Update some record fields

# DELETE => Removes records from the database

@app.route("/")
def index():
    return "<h1>Welcome to Flask!</h1>"

@app.route("/users/<string:username>")
def getUsername(username):
    return f"<h1>Welcome to Flask development, {username}!</h1>"

@app.route('/users')
def getUsers():
    users =[post.to_dict() for user in User.query.all()]
    # print(users)
    return make_response(users, 200)

@app.route("/posts", methods=["GET", "POST"])
def posts():
    if request.method == 'GET':
        # GET => Retrieve all the records from the database  
        posts =  [post.to_dict() for post in Post.query.all()]
        # print(posts)
        return make_response(posts, 200)

    if request.method == "POST":
        # POST => Creating a new record and inserting it into the database
        data = request.get_json()
        if not data or 'content' not in data or 'user_id' not in data:
            return make_response({"error": "Content and user_id are required"}, 400)

        # Create post instance then save it to the database
        new_post = Post(content=data['content'], user_id=data['user_id'])
        db.session.add(new_post)
        db.session.commit()

        return make_response({"message": "Post created successfully"}, 201)

@app.route('/posts/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def post(id):
    post = Post.query.get(id)
    if not post:
        return make_response({"message": "No post found"}, 404)
    
    if request.method == 'GET':
        return make_response(post.to_dict(), 200)
    
    if request.method == 'DELETE':
        db.session.delete(post)
        db.session.commit()
        
        return make_response({"message": "post deleted"}, 200)
    
    if request.method == 'PATCH':
        data = request.get_json()
        if 'content' in data:
            post.content = data['content']  # Update the content if provided
            db.session.commit()
            return make_response({"message": "Post updated successfully"}, 200)
# => retrieve a single record from the database

# PATCH => Update some record fields
# DELETE => Removes records from the database

# Ignore the rest of the code

# @app.route("/numbers/<int:num>")
# def getNumber(num):
#     return f"<h1>The number is {num}!</h1>"

# @app.route("/floats/<float:num>")
# def getFloat(num):
#     return f"<h1>The number is {num}!</h1>"

if __name__ == "__main__":
    app.run(port=5000, debug=True)