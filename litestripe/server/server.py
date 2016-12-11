
import sys
sys.path.append('..')
from flask import Flask, render_template
from core.lite import Litestripe


app = Flask(__name__)
l = None

@app.route('/')
def home():
    return render_template('./static/index.html')

@app.route('/set')
def set_color():
    l.set_rgb(10, 10, 10)


def start(r, g, b ):
    l = Litestripe(r, g, b)
    app.run(host='0.0.0.0', port='8989')

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Not enough args")
        print("Usage: [Red pin] [Green pin] [Blue pin]")
    else:
        start(sys.argv[1], sys.argv[2], sys.argv[3])