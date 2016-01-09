from flask import Flask, render_template, request
from jinja2.exceptions import FilterArgumentError

app = Flask(__name__)


@app.route("/")
def index():
    name = request.args.get('name', 'guy')
    return render_template("index.html", name=name)


@app.template_filter('first_char')
def cuonglm(s):
    if isinstance(s, (str, unicode)):
        return s[0] if s else ''
    else:
        raise FilterArgumentError('Argument must be string')


if __name__ == "__main__":
    app.run(debug=True)
