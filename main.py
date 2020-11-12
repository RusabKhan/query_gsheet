from flask import Flask, render_template, request
import sqlConverter

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        query = request.form["query"]
        return render_template("index.html", content= sqlConverter.queryMaker(query),
                               header="Keyword,Min Search Value,Max search volume,Competition,Competition (indexed value)")
    else:
        return render_template("index.html", content="empty", header="empty")


if __name__ == "__main__":
    app.run(debug=True)
