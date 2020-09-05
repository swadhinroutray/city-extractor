import flask
from geotext import GeoText
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/hello', methods=['GET'])
def hello():
    return flask.jsonify({
        "Hello": "Hello, how are you?"
    })
@app.route('/getcity', methods=['POST'])
def home():
    print("Hello")
    reqData = flask.request.get_json(force=True)
    print(reqData)
    text = (reqData['text'])
    print(text)
    places = GeoText(text)
    print(places.cities)
    return flask.jsonify({
            "City":places.cities[0] 
        })
if __name__ =='__main__':
    app.run(port=8080)