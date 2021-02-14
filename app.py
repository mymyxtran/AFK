from flask import Flask
import csv
app = Flask(__name__)

@app.route('/')
def get_csv():
    jsonArray = []   
    with open('./data/store_data.csv', newline='') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', quotechar='"')
        headers = reader.next()
        for row in datareader[1:]:
            jsonArray.append(dict(zip(headers, row)))
    
    return {"0" : jsonArray} ## return JSON
        
if __name__ == "__main__":
    app.run()        
