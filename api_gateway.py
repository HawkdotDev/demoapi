import requests
from flask import Flask, jsonify

app = Flask(__name__)

# Routes to access the other APIs
@app.route('/google', methods=['GET'])
def call_google_api():
    response = requests.get('https://your-google-app-engine-url.com/api/google')
    return jsonify(response.json())

@app.route('/azure', methods=['GET'])
def call_azure_api():
    response = requests.get('https://your-azure-url.com/api/azure')
    return jsonify(response.json())

@app.route('/aws', methods=['GET'])
def call_aws_api():
    response = requests.get('https://your-aws-lambda-url.com/api/aws')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)

