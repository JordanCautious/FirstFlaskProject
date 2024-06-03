from flask import Blueprint, render_template

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html", name="Jordan", age=23, quote="Jack of all "
                                                                            "trades, master of none, but still better"
                                                                            " than a master of one. - Shakespeare")
