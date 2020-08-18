from flask import Flask, render_template, url_for, request, session, redirect, g, jsonify
from google.google import Google

app = Flask(__name__)
app.secret_key='Hellothere'

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/google',methods=['GET','POST'])
def google():
    try:
        ret=Google(request.args["country"],request.args["query"])
        return jsonify({'response' : ret})
    except:
        return 'TADA'

if __name__ == '__main__':
    app.run(debug=True)