from flask import Flask,render_template
from flask.json import jsonify
from data import Country
import json

app = Flask(__name__)
app.config["DEBUG"]=False


@app.route("/")
def index():
  return render_template('maintainence.html')

# Error 404 Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# @app.route("/")
# def index():
#   return render_template('index.html')

# Older Support

# @app.route("/v2.0/country_data",methods=['GET','POST'])
# def countryData2():
#   data=Country()
#   country_data_JSON = data.covidCountryData()
#   return jsonify(["Now, you don't have to mention version number. Visit Homepage for more API endpoints",country_data_JSON])

# @app.route("/v2.0/state_data",methods=['GET'])
# def state2():
#   data=Country()
#   state_data_JSON = data.state_data()
#   return jsonify(["Now, you don't have to mention version number. Visit Homepage for more API endpoints",state_data_JSON])

# @app.route("/v2.0/icmr_lab_details",methods=['GET','POST'])
# def icmr_lab_details2():
#   return jsonify({
#     'note':'Lab Details are not published anymore',
#     'message':'Please visit Homepage for more API endpoints'
#   })

# @app.route("/v2.0/helpline_numbers",methods=['GET','POST'])
# def helpline_numbers2():
#   numbers = Country()
#   helpline_numbers_JSON = numbers.helplineNumbers()
#   return jsonify(["Now, you don't have to mention version number. Visit Homepage for more API endpoints",helpline_numbers_JSON])


# @app.route("/country_data",methods=['GET','POST'])
# def countryData():
#   data=Country()
#   country_data_JSON = data.covidCountryData()
#   return jsonify(country_data_JSON,data.covidTestCount())



# @app.route("/state_data",methods=['GET','POST'])
# def state():
#   data=Country()
#   state_data_JSON = data.state_data()
#   return jsonify(state_data_JSON)
 

# @app.route('/helpline_numbers',methods=['GET','POST'])
# def helpline_numbers():
#   numbers = Country()
#   helpline_numbers_JSON = numbers.helplineNumbers()
#   return jsonify(helpline_numbers_JSON)

# @app.route('/headlines',methods=['GET','POST'])
# def headlines():
#   headlines = Country()
#   headlines_JSON = headlines.headlines()
#   return json.dumps(headlines_JSON,sort_keys=False)


if __name__ == "__main__":
  app.run()