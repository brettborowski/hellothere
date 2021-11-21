import sys
import subprocess
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/info/")
def info():
    pip_result = subprocess.run(["pip", "list"], capture_output=True)
    pip_list = pip_result.stdout.decode("utf-8")
    return render_template(
        "info.html",
        executable=sys.executable,
        version=sys.version,
        path=sys.path,
        pip_list=pip_list,
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
