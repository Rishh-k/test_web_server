from flask import Flask
app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello World!"

@app.route("/myinfo")
def myinfo():
    info = "Dev Name: Rishabh Khandelwal"
    return info

@app.route("/submission")
def submit():
    info = "This is my final submission"
    return info

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)