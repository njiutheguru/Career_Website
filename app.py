from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world():
  return 'hello world, this is steve a flask developer. If i may ask, what is this bigger hype about django whereas flask is the real thing?'

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)



