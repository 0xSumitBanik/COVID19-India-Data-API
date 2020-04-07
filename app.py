from flask import Flask,render_template
from flask.json import jsonify
from data import Country

URL = 'https://www.mygov.in/corona-data/covid19-statewise-status'
ICMR_URL = 'https://covid.icmr.org.in/index.php/testing-labs-deatails'
app = Flask(__name__)
app.config["DEBUG"]=True

@app.route("/")
def index():
  return render_template('index.html')
  # return "Hello"
@app.route("/v2.0/status",methods=['GET','POST'])
def status():
  status_json = {
    'HTTP-Status':'200 (OK)',
    'success':'true'
  }
  return jsonify(status_json)

@app.route("/v2.0/country_data",methods=['GET','POST'])
def countryData():
  data=Country()
  country_data_JSON = data.covidCountryData(URL)
  return jsonify(country_data_JSON)

@app.route("/v2.0/state_data",methods=['GET'])
def state():
  data=Country()
  state_data_JSON = data.state_data(URL)
  return jsonify(state_data_JSON)

@app.route('/v2.0/icmr_lab_details',methods=['GET','POST'])
def icmr_labs():
  labs = Country()
  icmr_labs_data_JSON = labs.icmrLabDetails()
  return jsonify(icmr_labs_data_JSON)

@app.route('/v2.0/helpline_numbers',methods=['GET','POST'])
def helpline_numbers():
  numbers = Country()
  helpline_numbers_JSON = numbers.helplineNumbers()
  return jsonify(helpline_numbers_JSON)

if __name__ == "__main__":
  app.run()
