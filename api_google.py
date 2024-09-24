from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/google', methods=['GET'])
def google_api():
    return jsonify({"message": "Hello from Google App Engine!"})

if __name__ == '__main__':
    app.run(debug=True)
