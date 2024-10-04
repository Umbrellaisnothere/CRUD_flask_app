from app import app
from models import User, db, Profile, Post, Group

with app.app_context():
    # User.query.delete
    # db.session.query(User).delete()
    # db.session.query(Profile).delete()
    # db.session.commit()

    User.query.delete()
    Profile.query.delete()
    Post.query.delete()
    Group.query.delete()
    
    # print("Deleting complete!")
    
    print("Seeding User data...")
    
    # adding users
    user1 = User(username="Felix", age=22)
    user2 = User(username="Brenda", age=19)
    user3 = User(username="Brighton", age=18)
    user4 = User(username="Ivy", age=20)
    user5 = User(username="Chelsea", age=30)
    
    db.session.add_all([user1, user2, user3, user4, user5])
    db.session.commit()
    
    # Adding profiles
    profile1 = Profile(bio=" Lovely", user_id=1)
    profile2 = Profile(bio="Caring", user_id=2)
    profile3 = Profile(bio="Love dancing", user_id=3)
    
    db.session.add_all([profile1, profile2, profile3])
    db.session.commit()
    
    # adding posts
    p1 = Post(content="Recreation activities", user=user1)
    p2 = Post(content="Traveling abroad conditions", user=user2)
    p3 = Post(content="Education requirements", user=user1)
    p4 = Post(content="Tourism", user=user2)
    p5 = Post(content="Fishing", user=user1)
    p6 = Post(content="Transportation", user=user3)
    p7 = Post(content="Human Resources", user=user4)
    p8 = Post(content="Agriculture", user=user5)
    p9 = Post(content="Hiking", user=user3)
    p10 = Post(content="Music and Arts", user=user1)
    
    db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])
    db.session.commit()
    
    
    # Add groups
    g1 = Group(group_name="Thanos")
    g2 = Group(group_name="Standard")
    g3 = Group(group_name="Mpeketoni")
    g4 = Group(group_name="Riverroad")
    g5 = Group(group_name="Recce")
    
    db.session.add_all([g1, g2, g3, g4, g5])
    db.session.commit()
    
    # Add users to a group
    g1.users.append(user1)
    g1.users.append(user2)
    g1.users.append(user3)
    
    # Add groups to user
    user1.groups.append(g1)
    user1.groups.append(g2)
    user1.groups.append(g3)

    # giving user profile
    # profile1.user_id = user1
    # profile2.user_id = user2
    # profile3.user_id = user3
    
    db.session.commit()

    
    print("Done seeding")
    
    # db.session.add_all(list)
    # db.session.commit()
    