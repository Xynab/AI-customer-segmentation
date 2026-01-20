from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("upload.html")

@app.route("/dashboard", methods=["POST"])
def dashboard():
    file = request.files["file"]
    df = pd.read_csv(file)

    cluster_counts = df["Customer_Type"].value_counts().to_dict()

    return render_template("dashboard.html", tables=df.head(20).to_html(), counts=cluster_counts)

if __name__ == "__main__":
    app.run(debug=True)
