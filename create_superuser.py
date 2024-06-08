# Create a script to create a superuser
import pymongo
from pymongo import MongoClient
from werkzeug.security import generate_password_hash

MONGO_DB_URI = "mongodb+srv://adityaseth936:adityaseth0905@nebulasource.ueavgem.mongodb.net/NebulaSourceDB?retryWrites=true&w=majority&appName=NebulaSource"
client = MongoClient(MONGO_DB_URI)
db = client['NebulaSourceDB']

# Define superuser credentials
superuser = {
    "username": "admin",
    "email": "adityaseth936@gmail.com",
    "password": generate_password_hash("8882187203"),  # Hash the password
    "is_superuser": True,
    "is_staff": True
}

# Insert superuser into the users collection
db.users.insert_one(superuser)
print("Superuser created successfully!")
