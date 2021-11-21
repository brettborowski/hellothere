import sys
import subprocess
import sqlalchemy.orm
from flask import Flask, render_template, request, redirect, escape, Markup
from .db import LocalSession


app = Flask(__name__)

db_session = LocalSession()
db_session: sqlalchemy.orm.Session

@app.route("/info/")
def info():
    pip_result = subprocess.run(["pip", "list"], capture_output=True)
    pip_list = pip_result.stdout.decode("utf-8")
    e = db_session.bind.engine
    db_info = f"{e}\n" \
              f"driver: {e.driver}\n"
    return render_template(
        "info.html",
        executable=sys.executable,
        version=sys.version,
        path=sys.path,
        pip_list=pip_list,
        db_info=db_info,
    )


@app.route("/", methods=["GET", "POST"])
def index():
    if name := request.form.get("name"):
        return redirect(f"/{name}")
    else:
        return hello("World")


@app.route("/<name>")
def hello(name):
    return render_template("index.html", name=name)
