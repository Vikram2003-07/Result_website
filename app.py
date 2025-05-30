from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to your Excel file
# This assumes semres.xlsx is in the same folder as app.py
excel_file_path = os.path.join(BASE_DIR, 'semres.xlsx')

df = pd.read_excel(excel_file_path)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        usn = request.form.get("usn").strip().upper()
        row = df[df['USN'] == usn]
        if not row.empty:
            row = row.iloc[0].to_dict()
            return render_template("result.html", usn=usn, details=row)
        else:
            error = f"USN '{usn}' not found."
            return render_template("index.html", error=error)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)