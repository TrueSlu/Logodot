from flask import Flask, send_file
app = Flask(__name__)

@app.route("/")
def serve_react_app():
    return "hello"
    #return send_file("app/build/index.html")

@app.route("/static/<filename>")
def serve_static(filename):
    return send_file("./styles/" + filename)
    #return send_file("./app/build/static" + filename)

if __name__ == '__main__':
    app.run(debug=True)