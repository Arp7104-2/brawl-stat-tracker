from backend import app
import flask
import requests
import os

BASE_URL="https://api.brawlstars.com/v1"
REQUEST_HEADER = {"Authorization": "Bearer" + os.environ['BRAWL_API_KEY']}

example_json = {"hello": "world"}

@app.route("/")
def index():
    return flask.render_template("place_holder.html")

@app.route("/player/<int:player_id>")
def get_player():
    player_id = flask.request.get("player_id")
    player_url = f"{BASE_URL}/{player_id}"
    response = requests.get(player_url, headers=REQUEST_HEADER)
    player_json = response.json()
    return flask.jsonify(player_json)

@app.route()
def get_club():
    return flask.jsonify(example_json)