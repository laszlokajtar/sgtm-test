from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'sGTM test website'

app.run()