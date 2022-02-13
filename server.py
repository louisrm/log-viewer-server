import os
import simplejson as json
from flask import Flask, request
from werkzeug.utils import secure_filename
from parse_tlog import parse_tlog

# create uploads folder if not present
UPLOAD_FOLDER = os.getcwd() + '/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Verify file extension
ALLOWED_EXTENSIONS = {'tlog'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Return example flight data object
@app.route("/exampleData", methods=['GET'])
def example_data():
    flightObjFile = open("demoFlightData.json","r")
    flightObj = json.load(flightObjFile)
    response = app.response_class(
        response=json.dumps(flightObj),
        status=200,
        mimetype='application/json'
    )
    return response

# Parse and return custom flight data object
@app.route("/customData", methods=['POST'])
def custom_data():

    if 'file' not in request.files:
        return 'no file', 400

    file = request.files['file']
  
    if file and allowed_file(file.filename):
        print("here")

        filename = secure_filename(file.filename)
        filePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filePath)

        output = parse_tlog(filePath)

        os.remove(filePath)

        response = app.response_class(
            response=json.dumps(output, ignore_nan = True),
            status=200,
            mimetype='application/json'
        )
        return response

    return 'parse failed', 400


if __name__ == "__main__":
    app.run(debug=True)