from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'aircool-dev-key-change-in-production'


@app.route('/')
def index():
    return render_template('pages/index.html')


@app.route('/privacy-policy')
def privacy_policy():
    return render_template('pages/privacy_policy.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

