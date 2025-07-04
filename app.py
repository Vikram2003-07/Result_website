from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

df = pd.read_csv('semres.csv')
df.set_index('USN', inplace=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        usn = request.form.get("usn").strip().upper()
        if usn in df.index:
            row = df.loc[usn].to_dict()
            return render_template("result.html", usn=usn, details=row)
        else:
            error = f"USN '{usn}' not found."
            return render_template("index.html", error=error)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()