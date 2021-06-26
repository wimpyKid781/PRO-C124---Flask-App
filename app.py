from flask import Flask,jsonify, request

app = Flask(__name__)

List = [
    {
        'id': 1,

        'Name': u'John',

        'Contact': u'7829301928',

        'done': False
    },
    {
        'id': 2,

        'Name': u'Mark',

        'Contact': u'1920389183', 

        'done': False
    },
    {
        'id': 3,

        'Name': u'Jeff',

        'Contact': u'5620192736', 

        'done': False
    }
]

@app.route("/add-data", methods=["POST"])

def add_task():

    if not request.json:

        return jsonify({

            "status":"error",

            "message": "Please provide the data!"

        },400)

    contact = {

        'id': List[-1]['id'] + 1,

        'Name': request.json['Name'],
        
        'Contact': request.json.get('Contact', ""),
        
        'done': False
    }
    
    List.append(contact)
    
    return jsonify({
    
        "status":"success",
    
        "message": "Contact added succesfully!"
    })
    

@app.route("/get-data")

def get_task():

    return jsonify({

        "data" : List

    }) 

if (__name__ == "__main__"):

    app.run(debug=True)