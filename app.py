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
            "name": "siman",
            "age": 22,
                "gender": "male"
        },
        {
            "name": "kumari",
            "age": 25,
              "gender": "female"
        },
        {
            "name": "haju",
            "age": 30,
             "gender": "male"
        }
    ]
    return data
   
app.run(debug=True)