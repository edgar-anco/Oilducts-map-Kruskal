from flask import Flask, render_template

app = Flask(__name__)

# Routes to Render Something
@app.route('/')
def home():
    return render_template("home_map.html")

@app.route('/riskmap', strict_slashes=False)
def risk_map():
    return render_template("risk_map.html")

@app.route('/about', strict_slashes=False)
def about():
    return render_template("about.html")

# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)
