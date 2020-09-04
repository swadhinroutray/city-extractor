import flask
from geotext import GeoText
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/getcity', methods=['POST'])
def home():
    print("Hello")
    reqData = flask.request.get_json(force=True)
    print(reqData)
    text = (reqData['text'])
    print(text)
    places = GeoText(text)
    print(places.cities)
    dict ={
        "city": places.cities[0]
    }
    return dict
app.run()