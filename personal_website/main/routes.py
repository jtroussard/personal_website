import json, os
from pathlib import Path
from flask import render_template, request, Blueprint, redirect, url_for, flash, Markup

main = Blueprint("main", __name__)

data_filename = Path("./personal_website/data.json")
with open(data_filename) as file:
    data = json.load(file)

@main.route("/")
@main.route("/home")
def home():

    # We have to process some of the data strings
    intro_text = data['intro_text']
    data['intro_text'] = Markup(intro_text)
    return render_template("home.html", data=data)
