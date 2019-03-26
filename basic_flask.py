from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    """
    Returns the string "Hello, world" to the caller
    """
    return "Hello111, world"
    pass


@app.route("/data/<name>", methods=["GET"])
def hello_name(name):

    return "Hello111, {}".format(name)


@app.route("/name", methods=["GET"])
def getData():
    """
    Returns the data dictionary below to the caller as JSON
    """
    data = {
      "name": "Willy",
      "team": "braincrush"
      }
    return jsonify(data) # respond to the API caller with a JSON representation of data. jsonify is important, as it sets response headers that indicate the respose is in JSON as well


@app.route("/hello/<name>", methods=["GET"])
def h_name(name):
    print("hello")
    d = {
        "message": "Hello there, {}".format(name)
    }
    return jsonify(d)


@app.route("/sum", methods=["POST"])
def sum():
    r = request.get_json()  # parses the POST request body as JSON
    s = r["a"] + r["b"]  # adds JSON dict parameter "a" and "b" together
    return s, 200


if __name__ == "__main__":
  # d = {"message": "Hello there {}".format(name)}
  # h = h_name("test")
  # print(h)
  app.run(host="0.0.0.0")
