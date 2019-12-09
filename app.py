from flask import Flask, jsonify, request
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/upload', methods=['POST'])
def uploadFile():
    if request.method == 'POST':
        file = request.files['file']
        file.save("./test.jpg")
        print(file)
    return "Success"




if __name__ == '__main__':
    app.run()
