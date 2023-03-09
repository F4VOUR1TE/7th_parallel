from firebase import firebase
from firebase_admin import credentials, auth, db, storage
import firebase_admin

cred = credentials.Certificate("files/butilka-firebase-adminsdk-tqp9f-dd117b3e5a.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://butilka-default-rtdb.firebaseio.com/'})

users_database = {
        "1274981264": {
            "username": "user_1",
            "last_activity": 1619212557
            },
        "4254785764": {
            "username": "user_2",
            "last_activity": 1603212638
            }
}

db.reference("/users_database/").set(users_database)

user_3_id = "2148172489"
user_3 = {
    "username": "user_3",
    "last_activity": 1603212638
}

db.reference("/users_database/" + user_3_id).set(user_3)

print(db.reference("/users_database/").get())