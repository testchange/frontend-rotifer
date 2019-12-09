from flask import Flask, jsonify, request

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({'data': 'pong!'})

@app.route('/upload', methods=['POST'])
def uploadFile():
    if request.method == 'POST':
        file = request.files['file']
        file.save("./test.jpg")
        print(file)
    return "Success"




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)