from flask import Flask
from flask.json import jsonify
from data import covidCountryData

app = Flask(__name__)
app.config["DEBUG"]=False

@app.route("/")
def homepage():
  default_api = {
    'HTTP-Status':'404 (OK)',
    'name':'Incorrect URL',
    'message':'Add /api/v1.0/country_data at the end of the url'
  }
  return jsonify(default_api)

@app.route("/api/v1.0/status",methods=['GET','POST'])
def status():
  status_json = {
    'HTTP-Status':'200 (OK)',
    'success':'true'
  }
  return jsonify(status_json)

@app.route("/api/v1.0/country_data",methods=['GET','POST'])
def countryData():
  country_data_JSON = covidCountryData()
  return jsonify(country_data_JSON)

if __name__ == "__main__":
  app.run()
