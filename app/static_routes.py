import os

from bottle import Bottle, static_file, get

app = Bottle()


@app.route("/static/css/<filepath:re:.*\.css>", name='css')
def css(filepath):
    return static_file(filepath, root="static/css")


@app.route("/static/fonts/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>", name='font')
def font(filepath):
    return static_file(filepath, root="static/fonts")


@app.route("/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>", name='img')
def img(filepath):
    return static_file(filepath, root="static/img")


@app.route("/static/js/<filepath:re:.*\.js>", name='js')
def js(filepath):
    return static_file(filepath, root="static/js")


@app.route("/static/video/<filepath:re:.*\.mp4>", name='video')
def video(filepath):
    return static_file(filepath, root="static/video")
