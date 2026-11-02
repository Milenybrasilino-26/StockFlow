from flask import Blueprint, render_template

from app.services.dashboard_service import obter_indicadores_estoque

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/dashboard")
def dashboard():
    indicadores = obter_indicadores_estoque()

    return render_template(
        "dashboard.html",
        indicadores=indicadores
    )