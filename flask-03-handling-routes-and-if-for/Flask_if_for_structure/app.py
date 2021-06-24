from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def home():
#     return 'This is home page for no path, <h1> Welcome Home</h1>' 

@app.route("/")
def head():
    first = "This is my first conditions experience"
    return render_template("index.html", message=False) 

@app.route("/fatma")
def header():
    name = ["ali", "fatma", "mostafa", "busra"]
    return render_template("body.html", object=name)






if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=80)
    # app.run(host='0.0.0.0', port=80)