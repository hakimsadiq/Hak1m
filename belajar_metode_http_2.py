from flask import Flask, request
import json
import pymongo
app = Flask(__name__)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["hakim"]
mycol = mydb["mahasiswa"]
@app.route("/")
@app.route("/index")
def hello_world():
 return {
     'deskripsi': 'Selamat Datang di Kelas Pemrograman Jaringan'
 }
@app.route("/mahasiswa", methods = ['GET'])
def get_mahasiswa():
    results = mycol.find()
    json_data = []
    for result in results:
        result['_id'] = str(result['_id'])
        json_data.append(result)
    return json.dumps(json_data)
@app.route("/mahasiswa", methods = ['POST'])
def post_mahasiswa():
    data_nama = request.form.get("nama")
    data_nim = request.form.get("nim")
    mydict = { "nama": data_nama, "nim": data_nim }
    mycol.insert_one(mydict)
    return {
        "description": "Berhasil menyimpan data"
    }
@app.route('/mahasiswa/<nim>', methods=['PUT'])
def update_mahasiswa(nim):
    myquery = { "nim": nim }
    data_nama = request.form.get("nama")
    newvalues = { "$set": { "nama": data_nama} }
    mycol.update_one(myquery, newvalues)
    return {
        "description": "Berhasil mengupdate data"
    }  
@app.route('/mahasiswa/<nim>', methods=['DELETE'])
def delete_mahasiswa(nim):
    myquery= {"nim":nim}
    mycol.delete_one(myquery)
    return {
        "description": "Berhasil menghapus data"
    }  
if __name__ == '__main__':
 app.run(debug=True)
