from app impport app
from flask import render_template
@app.route('/GetECConfig.xml')
def getecconfig():
  return render_template('GetECConfig.xml')
