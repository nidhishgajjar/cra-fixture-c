from notifd.web import app, json_route
from notifd.auth import user_required
from notifd.queue import enqueue
from flask import request


@app.route("/notify", methods=["POST"])
@user_required
@json_route
def notify():
    body = request.get_json() or {}
    channel = body.get("channel", "push")
    enqueue(channel, body)
    return {"queued": True}
