from flask import Flask
app = Flask(__name__)
config = None
import ecs
debug = True
if debug:
  app.run(host='0.0.0.0',port=80)
