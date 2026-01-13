from flask import Flask, jsonify



app = Flask(__name__)

@app.route('/')
def home():
    return "this is an /"

@app.route('/api')
def Endpoint():

   JSONlist = get_data()
   return jsonify(JSONlist)

def get_data():
    data = [
        {
            "name": "siddu",
            "age": 22,
                "gender": "male"
        },
        {
            "name": "ravi",
            "age": 25,
              "gender": "male"
        },
        {
            "name": "haju",
            "age": 30,
             "gender": "male"
        }
    ]
    return data
   
app.run(debug=True)