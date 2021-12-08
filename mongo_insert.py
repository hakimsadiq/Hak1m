import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["hakim"]
mycol = mydb["mahasiswa"]
mydict = { "nama": "Muh. Hakim Sadiq", "nim": "1929141012" }
mycol.insert_one(mydict)