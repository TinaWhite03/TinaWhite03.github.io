# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId
from pymongo.errors import PyMongoError

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username=None, password=None): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'SNHU1234' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this Update method to implement the C in CRUD. 
    def create(self, data):
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except PyMongoError:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Read method
    def read(self, query=None):
        """Read documents from collection."""
        try:
            # Use empty dict if no query provided
            query = query or {}
            cursor = self.collection.find(query)
            return list(cursor)
        except PyMongoError:
            return []

    # Update method
    def update(self, query, update_data):
        """Update documents matching query."""
        if not query or not update_data:
            return {"error": "Query and update data required"}
        
        try:
            result = self.collection.update_many(query, {"$set": update_data})
            return {
                "matched": result.matched_count,
                "modified": result.modified_count
            }
        except PyMongoError:
            return {"error": "Update failed"}

    # Delete method
    def delete(self, query):
        """Delete documents matching query."""
        if not query:
            return {"error": "Delete query required"}
        
        try:
            result = self.collection.delete_many(query)
            return {"deleted": result.deleted_count}
        except PyMongoError:
            return {"error": "Delete failed"}