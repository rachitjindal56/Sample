# from flask import Flask,jsonify
# from flask_restful import Api, Resource
# from flask_httpauth import HTTPBasicAuth

# app = Flask(__name__)
# api = Api(app)
# auth = HTTPBasicAuth()
# USER_DATA = {
#    "Username": "password",
#    "sample": "sampling.io",
#    "GPT-3": "OpenAI"
# }

# @auth.verify_password
# def verify(username, password):
#    if not (username and password):
#        return False
#    return USER_DATA.get(username) == password

# class endpoint(Resource):
#    @auth.login_required
#    def get(self):
#        return jsonify({"status":True})

# api.add_resource(endpoint,"/endpoint")


# if __name__=="__main__":
#    app.run(port=5000,debug=True)

# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request

# creating a Flask app
app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
def home():
   if (request.method == 'GET'):
      return jsonify({
        "responses": [
            {
                "type": "text",
                "delay": 1000,
                "message": "Have a great day!"
            }
        ],
      #   "attributes": {
      #       "foo": "bar",
      #       "baz": ""
      #   }
    })

@app.route('/<int:num>', methods = ['GET'])
def disp(num):

	return jsonify({'data': num**2})

if __name__ == '__main__':

	app.run(debug = True)
