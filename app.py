from flask import Flask, render_template
# root path of the application
app = Flask(__name__)

@app.route("/") 
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)