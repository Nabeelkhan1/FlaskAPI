from flask import Flask, render_template

app = Flask(_name_)

@app.route("/")
def hello_world():
    return render_template("work.html")

@app.route("/contact")
def sci():
    return render_template("scical.html")

#@app.route("/about")
#def about():
    return render_template("about.html")

if _name_ == "_main_":
    app.run(debug=True)