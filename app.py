import flask
from geotext import GeoText
app = flask.Flask(__name__)
app.config["DEBUG"] = False


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

app.run()