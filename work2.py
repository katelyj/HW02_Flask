from flask import Flask

shamaul = Flask(__name__)

@shamaul.route("/")
def what():
    return "idk what's happening help"

@shamaul.route("/1")
def whatWhat():
    return "help i still don't know what's happening"

@shamaul.route("/2")
def whatWhatWhat():
    return "i'm so lost"

if __name__ == '__main__':
    shamaul.run()
