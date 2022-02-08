from flask import Flask, jsonify, request
import json

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'.tlog'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Example Data API route
@app.route("/exampleData")
def example_data():
    flightObjFile = open("flight_obj.json","r")
    flightObj = json.load(flightObjFile)
    response = app.response_class(
        response=json.dumps(flightObj),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/customData", methods=['POST'])
def custom_data():
    print(request.get_data())


    # check if the post request has the file part
    if 'file' not in request.files:
        print('no file')
        return 'nope', 400
    file = request.files['file']
  
    if file and allowed_file(file.filename):
        flightObjFile = open("flight_obj.json","r")
        flightObj = json.load(flightObjFile)
        response = app.response_class(
            response=json.dumps(flightObj),
            status=200,
            mimetype='application/json'
        )
        return response

    return 'extra nope', 400


if __name__ == "__main__":
    app.run(debug=True)