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
        return '<h1>Something is broken!</h1>'
@app.route('/ip')
def get_my_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return jsonify({'ip': request.environ['REMOTE_ADDR']})
    else:
        return {'ip': request.environ['HTTP_X_FORWARDED_FOR']}


if __name__ == '__main__':
    app.run(debug=True)