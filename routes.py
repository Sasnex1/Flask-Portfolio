import os

from flask import Blueprint, render_template, request, url_for
import socket

from werkzeug.utils import redirect

app_routes = Blueprint('app_routes', __name__)

def check_server(host,port):
    try:
        with socket.create_connection((host,port), timeout=2):
            return True
    except:
        return False

@app_routes.route("/", methods=["GET", "POST"])
def index():
    host = "ftp.BreezyMC.de"
    port = 25565
    status = check_server(host,port)

    return render_template('index.html', server_online=status,)

@app_routes.route("/guestbook", methods=["GET", "POST"])
def guestbook():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        if name and message:
            with open("guestbook.txt", "a", encoding="utf-8") as f:
                f.write(f"{name}: {message}\n")
        return redirect(url_for("app_routes.guestbook"))

    # Einträge lesen
    if os.path.exists("guestbook.txt"):
        with open("guestbook.txt", "r", encoding="utf-8") as f:
            entries = f.readlines()
    else:
        entries = []

    return render_template("guestbook.html", entries=reversed(entries))

@app_routes.route('/projects')
def projects():
    return render_template('projects.html')