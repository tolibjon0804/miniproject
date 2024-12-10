from flask import Flask, render_template, request
import pg8000

app = Flask(__name__)

conn = pg8000.connect(
        user="tolibjon",
        password="0804",
        host="localhost",
        port=5432,
        database="tolibjon"
    )


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        level = request.form["level"]
        return render_template("timetable.html", level=level, data=[], message="Loading please wait...")

    return render_template("index.html")


@app.route("/timetable", methods=["GET"])
def timetable():
    level = request.args.get('level')
    if not level:
        return "Level not provided", 400

    cur = conn.cursor()
    cur.execute("SELECT * FROM timetable WHERE level = %s;", level)
    rows = cur.fetchall()

    if rows:
        return render_template("timetable.html", level=level, data=rows, message="")
    else:
        return render_template("timetable.html", level=level, data=[], message="No data found for this level.")


@app.route("/students", methods=["GET"])
def students():
    cur = conn.cursor()
    query = "SELECT * FROM students"

    cur.execute(query)
    rows = cur.fetchall()

    if rows:
        return render_template("students.html", data=rows)
    else:
        return render_template("students.html", data=[], message="No assignments found.")


if __name__ == "__main__":
    app.run(debug=True)
