from flask import Flask
from flask.json import jsonify
from data import Country

URL = 'https://www.mygov.in/corona-data/covid19-statewise-status'
ICMR_URL = 'https://covid.icmr.org.in/index.php/testing-labs-deatails'
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
  data=Country(URL)
  country_data_JSON = data.covidCountryData()
  return jsonify(country_data_JSON)

@app.route("/api/v1.0/state_data",methods=['GET'])
def state():
  data=Country(URL)
  state_data_JSON = data.state_data()
  return jsonify(state_data_JSON)

@app.route('/api/v1.0/icmr_lab_details',methods=['GET'])
def icmr_labs():
  labs = Country(ICMR_URL)
  icmr_labs_data_JSON = labs.icmrLabDetails()
  return jsonify(icmr_labs_data_JSON)

if __name__ == "__main__":
  app.run()