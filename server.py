"""
VoidChat — Anonymous Public Chat Server
Developer : Karndeep Baror
GitHub    : github.com/karndeepbaror
Tagline   : "The Digital Phantom That Strikes Without Warning."

Install:
    pip install flask flask-socketio eventlet

Run:
    python server.py

Open in browser:  http://localhost:5000
"""

from flask import Flask, send_file, request
from flask_socketio import SocketIO, emit, join_room, leave_room
from datetime import datetime
import os, logging

# ── CONFIG ──────────────────────────────────────────────────────────────
HOST     = "0.0.0.0"
PORT     = int(os.environ.get("PORT", 5000))
SECRET   = os.environ.get("SECRET_KEY", "voidchat-secret-2025")
LOG_MSGS = False   # Keep False for full anonymity. True = debug only.
ROOM     = "public"
# ────────────────────────────────────────────────────────────────────────

logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(levelname)s  %(message)s")
log = logging.getLogger("VoidChat")

app = Flask(__name__, static_folder=".", static_url_path="")
app.config["SECRET_KEY"] = SECRET
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet",
                    logger=False, engineio_logger=False)

# In-memory only — wiped on restart (by design, no persistence)
users: dict = {}   # sid -> {name, emoji, sid}


@app.route("/")
def index():
    return send_file("index.html")


@socketio.on("connect")
def on_connect():
    log.info(f"Socket connected  [{request.sid[:8]}…]")


@socketio.on("join")
def on_join(data):
    sid   = request.sid
    name  = str(data.get("name", "Ghost#0000"))[:40]
    emoji = str(data.get("emoji", "👻"))[:8]

    users[sid] = {"name": name, "emoji": emoji, "sid": sid}
    join_room(ROOM)

    emit("user_list", list(users.values()), room=ROOM)
    emit("system", {"text": f"{emoji} {name} joined the void"}, room=ROOM)
    log.info(f"JOIN  {name}  [{sid[:8]}…]  total={len(users)}")


@socketio.on("message")
def on_message(data):
    sid  = request.sid
    user = users.get(sid)
    if not user:
        return

    text = str(data.get("text", "")).strip()[:500]
    if not text:
        return

    payload = {
        "name":  user["name"],
        "emoji": user["emoji"],
        "text":  text,
        "time":  datetime.now().strftime("%I:%M %p"),
    }
    if LOG_MSGS:
        log.info(f"MSG   [{user['name']}]: {text[:60]}")

    emit("message", payload, room=ROOM)


@socketio.on("typing")
def on_typing(data):
    sid  = request.sid
    user = users.get(sid)
    if user:
        emit("typing", {"name": user["name"]}, room=ROOM, skip_sid=sid)


@socketio.on("stop_typing")
def on_stop_typing(data):
    emit("stop_typing", {}, room=ROOM, skip_sid=request.sid)


@socketio.on("disconnect")
def on_disconnect():
    sid  = request.sid
    user = users.pop(sid, None)
    if user:
        leave_room(ROOM)
        emit("user_list", list(users.values()), room=ROOM)
        emit("system", {"text": f"{user['emoji']} {user['name']} left the void"}, room=ROOM)
        log.info(f"LEFT  {user['name']}  [{sid[:8]}…]  remaining={len(users)}")


if __name__ == "__main__":
    banner = """
╔══════════════════════════════════════════════════════╗
║   ██╗   ██╗ ██████╗ ██╗██████╗  ██████╗██╗  ██╗    ║
║   ██║   ██║██╔═══██╗██║██╔══██╗██╔════╝██║  ██║    ║
║   ██║   ██║██║   ██║██║██║  ██║██║     ███████║    ║
║   ╚██╗ ██╔╝██║   ██║██║██║  ██║██║     ██╔══██║    ║
║    ╚████╔╝ ╚██████╔╝██║██████╔╝╚██████╗██║  ██║    ║
║     ╚═══╝   ╚═════╝ ╚═╝╚═════╝  ╚═════╝╚═╝  ╚═╝   ║
╠══════════════════════════════════════════════════════╣
║  Developer : Karndeep Baror                          ║
║  GitHub    : github.com/karndeepbaror                ║
║  Tagline   : The Digital Phantom That Strikes...     ║
╠══════════════════════════════════════════════════════╣"""
    print(banner)
    print(f"║  Server    : http://localhost:{PORT}                   ║")
    print(f"║  Room      : #{ROOM}                               ║")
    print(f"║  Logging   : {'ON (debug)' if LOG_MSGS else 'OFF — anonymous mode'}                  ║")
    print("╚══════════════════════════════════════════════════════╝\n")

    socketio.run(app, host=HOST, port=PORT, debug=False)
