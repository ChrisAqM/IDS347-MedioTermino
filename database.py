from pymongo import MongoClient
import configuration as C

def get_database():
    client = MongoClient(C.CON_STRING)
    return client[C.CON_CLIENT]

if __name__ == "__main__":
    dbname= get_database()