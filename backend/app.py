from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "Alejandro",
        "lastname": "Curiel",
        "socialMedia":
        {
            "facebookUser": "AlejandroCuriel",
            "instagramUser": "AlejandroCuriel",
            "xUser": "AlejandroCuriel",
            "linkedin": "amin-AlejandroCuriel",
            "githubUser": "AlejandroCuriel"
        },
        "blog": "https://AlejandroCuriel.com",
        "author": "Alejandro Curiel"
    }

    return jsonify(value)

if __name__ == '__main__':
    app.run(port=5000)
