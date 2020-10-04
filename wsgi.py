from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Base url with port",request.host_url

if __name__ == "__main__":
    application.run()
