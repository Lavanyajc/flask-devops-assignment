from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hii from Lavanya JC's Flask app deployed via GitHub Actions, ECR, and EC2!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

