from flask import Flask
application = Flask(__name__)


hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)


print(local_ip)

@application.route("/")
def hello():
    return "Hello World!"
    return local_ip

if __name__ == "__main__":
    application.run()
