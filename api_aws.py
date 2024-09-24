from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def aws_api():
    return jsonify(message="Hello from aws !!!")

if __name__ == '__main__':
    app.run(debug=True)

