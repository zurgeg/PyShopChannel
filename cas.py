from app import app
from flask import render_template
@app.route('/ListContentSets.xml')
def lcs():
  return render_template('ListContentSets.xml')
