import pymongo
from datetime import datetime
from flask import Flask,request

app = Flask(__name__)



@app.route('/varici',methods=['POST'])
def tugas():
    dt = datetime.now()

    client = pymongo.MongoClient("mongodb+srv://varici_05:cikamargareta@cluster0.zglzkr8.mongodb.net/?retryWrites=true&w=majority")
    db = client['varici']
    my_collections = db['tugas_8']

    kecepatan = request.args.get('kecepatan')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')

    projek = {'kecepatan': kecepatan,
            'latitude' : latitude,
            'longitude' : longitude,
            'timestamp' : dt 
             }
    result = my_collections.insert_many([projek])
    return ('data sudah disimpan diMongoDB')


    
if __name__ == '__main__':
        app.run(debug=True)