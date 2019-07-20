from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/about')
def about():
  return '<h1>About:</h1>'

@app.route('/hello/<whom>')
def hello(whom):
  return render_template("hello.html", whom = whom)


@app.route('/100_plus/<int:n>')
def adder(n):
  return f'100 + {n} = {100 + n}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)