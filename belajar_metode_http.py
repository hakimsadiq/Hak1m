from flask import Flask, request
import json
import mysql.connector
app = Flask(__name__)
db = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd="",
 database="webservice",
)
@app.route("/")
@app.route("/index")
def hello_world():
 return {
 'deskripsi': 'Selamat Datang di Kelas Pemrograman Jaringan'
 }
@app.route("/mahasiswa", methods = ['GET'])
def get_mahasiswa():
 cursor = db.cursor()
 sql = "SELECT * FROM mahasiswa"
 cursor.execute(sql)
 row_headers=[x[0] for x in cursor.description]
 results = cursor.fetchall()
 json_data = []
 for result in results:
    json_data.append(dict(zip(row_headers,result)))
 
 return json.dumps(json_data, default=str)
@app.route("/mahasiswa", methods = ['POST'])
def post_mahasiswa():
 cursor = db.cursor()
 sql = "INSERT INTO mahasiswa (nama, nim) VALUES (%s, %s)"
 data = (request.form.get("nama"), request.form.get("nim"))
 cursor.execute(sql, data)
 db.commit()
 return {
 "description": "Berhasil menyimpan data"
 }
@app.route('/mahasiswa/<id>', methods=['PUT'])
def update_mahasiswa(id):
 cursor = db.cursor()
 sql = "UPDATE mahasiswa SET nama=%s, nim=%s WHERE id="+id
 data = (request.form.get("nama"), request.form.get("nim"))
 cursor.execute(sql, data)
 db.commit()
 return {
 "description": "Berhasil mengupdate data"
 }

@app.route('/mahasiswa/<id>', methods=['DELETE'])
def delete_mahasiswa(id):
    cursor = db.cursor()
    sql = "DELETE FROM mahasiswa WHERE id="+id
    cursor.execute(sql)
    db.commit()
    return {
        "description": "Berhasil menghapus data"
    }
if __name__ == '__main__':
 app.run(debug=True)