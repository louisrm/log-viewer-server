from flask import Flask, jsonify
import json

app = Flask(__name__)


# Members API route
@app.route("/members")
def members():
    flightObjFile = open("flight_obj.json","r")
    flightObj = json.load(flightObjFile)
    response = app.response_class(
        response=json.dumps(flightObj),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run(debug=True)