import time
import requests
from notifd.web import app
from flask import request


@app.route("/admin/broadcast", methods=["POST"])
def broadcast():
    body = request.get_json() or {}
    message = body["message"]
    user_ids = body["user_ids"]
    sent = 0
    for uid in user_ids:
        r = requests.post(
            "https://push.example.com/send",
            json={"user_id": uid, "message": message},
            timeout=5,
        )
        if r.status_code == 200:
            sent += 1
        time.sleep(0.05)
    return {"sent": sent}
