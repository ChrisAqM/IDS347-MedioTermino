from pymongo import MongoClient
import configuration as C

myclient = MongoClient(C.CON_STRING)
mydb = myclient[C.CON_CLIENT]

myview = mydb["Consulta 5"]
cursor = myview.find()

for result in cursor:
  print(result)
