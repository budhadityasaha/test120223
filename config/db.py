from pymongo import MongoClient
import pymongo
#local server:
#conn = MongoClient()

#cloud server:
#conn = pymongo.MongoClient("mongodb+srv://babu:IcwB1955t1XodUoF@cluster0.7uwgio0.mongodb.net/?retryWrites=true&w=majority")
conn = pymongo.MongoClient("mongodb+srv://kumkum:OYknFce61MP47fdh@cluster0.o99j87w.mongodb.net/?retryWrites=true&w=majority")
#print(conn.list_database_names())
#db = conn.testdb
#print(db.list_collection_names())
