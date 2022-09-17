from flask import Flask, render_template
from flask_talisman import Talisman

app = Flask(__name__)

@app.route("/") #www.edgargtz.com
def index():
    return render_template("index.html")

# Wrap Flask app with Talisman
Talisman(app, content_security_policy=None)

if __name__ == "__main__":
    app.run(debug=True)