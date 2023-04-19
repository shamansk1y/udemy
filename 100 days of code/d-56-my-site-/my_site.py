from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home(name=None):
    return render_template('my_site.html', name=name)


if __name__ == '__main__':
    app.run(debug=True) 