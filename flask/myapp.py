from crypt import methods
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/update", methods=['POST'])
def update():
    if request.method == 'POST':
        mid = request.form['mid']
        status = request.form['status']
        time = request.form['time']
        f = open("static/jsonfile.txt", "w")
        f.write(mid)
        f.write('\n')
        f.write(status)
        f.write('\n')
        f.write(time)
        f.close()
        return "update"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)