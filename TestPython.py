from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
   app.run(debug = True)

'''
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World !"

if __name__ == "__main__":
    app.run()
'''