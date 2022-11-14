
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, redirect, url_for, render_template
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
  return render_template('main.html')

@app.route('/result/<result>')
def success(result):
  app.logger.info('testing info log')
  return f'The result is: {result}'
 
 
@app.route('/predict', methods=['POST'])
def login():
  if request.method == 'POST':
    radius = int(request.form['radius'])
    prediction = 0
    if (radius > 2):
      prediction = 1
    return redirect(url_for('success', result=prediction))
    
 
# main driver function
if __name__ == '__main__':
 
  # run() method of Flask class runs the application
  # on the local development server.
  app.run(debug=True)