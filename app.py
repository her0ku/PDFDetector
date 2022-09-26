from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
async def hello_world():  # put application's code here
    return 'Hello World!'


@app.get('/home')
async def call_main_page():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()
