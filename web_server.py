# Importing python dependencies
from flask import Flask

# Initializing flask application
app = Flask(__name__)

# Function for the url address 
# "localhost:5000/"
@app.route("/")
def helloworld():
    return "Hello World!"

# Function for the url address 
# "localhost:5000/info"
@app.route("/info")
def myinfo():
    info = "Dev Name: Rishabh Khandelwal"
    return info

# Function for the url address 
# "localhost:5000/submission"
@app.route("/submission")
def submit():
    sub = "This is my final submission"
    return sub

# Main python function
if __name__ == "__main__":

    # Runs the app on local machine and port 5000
    app.run(host='0.0.0.0', port=5000)