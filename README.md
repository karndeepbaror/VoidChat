<div align="center">

# 💬 VOIDCHAT

### *The Digital Phantom That Strikes Without Warning.*

**Anonymous · No Logs · Ephemeral · Real‑Time**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com)
[![Socket.IO](https://img.shields.io/badge/Socket.IO-4.0+-black.svg)](https://socket.io)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

</div>

---

## 🕸️ **What is VoidChat?**

**VoidChat** is an **anonymous, ephemeral, real‑time public chat room** where **no identity is stored**, **no messages are logged**, and **every conversation vanishes when users leave**.

> 🔥 No signup. No tracking. No history. Just pure anonymous communication.

Built with **Flask‑SocketIO** and a **sleek WhatsApp‑like interface**, VoidChat is designed for privacy‑first conversations — whether you're a **security researcher**, a **privacy advocate**, or just someone who values **digital anonymity**.

---

## ✨ **Core Features**

| Feature | Description |
|---------|-------------|
| 🎭 **Full Anonymity** | Randomly generated usernames & avatars — no login, no email, no phone. |
| 🧹 **Ephemeral by Design** | No server‑side message storage. Messages exist only in memory and vanish on restart. |
| ⚡ **Real‑Time Messaging** | Instant message delivery with **WebSocket** via Socket.IO. |
| 👥 **Live User Presence** | See who's online in real time — join/leave notifications. |
| 🌓 **Dark / Light Theme** | One‑click toggle for comfortable viewing. |
| 📱 **Responsive UI** | Works flawlessly on desktop, tablet, and mobile. |
| 🔍 **Live User Search** | Filter active participants instantly. |
| 💬 **Typing Indicators** | Know when someone is composing a message (non‑intrusive). |
| 📊 **Live Stats Dashboard** | Online users, message count, session uptime. |
| 🧪 **No External Dependencies** | Runs locally — no third‑party tracking, no analytics. |

---

## 🛠️ **Tech Stack**

<div align="center">

| Layer | Technology |
|-------|------------|
| **Backend** | Python 3.8+ · Flask · Flask‑SocketIO |
| **Frontend** | HTML5 · CSS3 · JavaScript · Socket.IO Client |
| **Real‑Time** | WebSockets (Eventlet) |
| **Styling** | Custom CSS with Dark/Light variables |

</div>

## 📂 Project Structure (Clickable)

<table>
  <tr>
    <td><code>📁 VoidChat/</code></td>
    <td></td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;├── 📄 <a href="server.py"><code>server.py</code></a></td>
    <td>– Flask‑SocketIO backend (WebSocket + HTTP)</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;├── 📄 <a href="index.html"><code>index.html</code></a></td>
    <td>– Frontend UI · Socket.IO client · Animations</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;├── 📄 <a href="README.md"><code>README.md</code></a></td>
    <td>– Readme Page</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;└── 🧹</td>
    <td>– No database · No logs · No external storage</td>
  </tr>
</table>

> 🔍 **Click any filename** to view it directly on GitHub.

---

## 🚀 **Quick Start (Run Locally)**

#### 1. Clone the repository
```
git clone https://github.com/karndeepbaror/VoidChat
cd VoidChat 
cd VoidChat #main folder
```

#### 2. Install dependencies
```
pip install flask flask-socketio eventlet
```

#### 3. Run the server
```
python server.py
```

# 4. Open in browser
```
http://localhost:5000
```

## 🕸️ The VoidChat Philosophy

> *"The Digital Phantom That Strikes Without Warning."*

In a world where every click is tracked, every message archived, and every identity monetized — **VoidChat is the exception.**

- 🎭 **No name? No problem.** You are a ghost from the moment you join.
- 🧹 **No memory? By design.** The server remembers nothing. Neither should anyone else.
- ⚡ **No trace? Guaranteed.** Once you leave, you never existed.

**VoidChat isn't just a chat room. It's a statement.**

## 🔥 Why VoidChat?

| Problem | VoidChat Solution |
|---------|-------------------|
| Traditional chats log everything | ✅ **Zero logs** — nothing stored on disk |
| Identity tracking across sessions | ✅ **Random ephemeral identity** — no cookies, no fingerprint |
| Message persistence | ✅ **Messages vanish** on server restart or user disconnect |
| Complex setup | ✅ **One file backend + one HTML** — run anywhere |
| Privacy concerns | ✅ **No external APIs** — fully self‑contained |

## ⚡ VoidChat in Action — What Makes It Different?

| Aspect | Typical Chat Apps | VoidChat |
|--------|-------------------|----------|
| **Identity** | Email, phone, or social login | 🎭 **Random one‑time name + emoji** |
| **Data Storage** | Permanent databases, cloud logs | 🧹 **Zero disk writes — pure RAM** |
| **Message History** | Forever searchable | 💨 **Vanishes on disconnect / restart** |
| **Tracking** | IP logging, analytics, cookies | 🔥 **No external calls, no fingerprints** |
| **Deployment** | Heavy frameworks, databases | ⚡ **Single Python file + one HTML** |
| **Audience** | General public | 🕸️ **Privacy researchers, journalists, activists** |

> 🔒 **VoidChat doesn't just claim privacy — it's built on it from the ground up.**

## 🧪 Live Demo (Optional)

If you want to test without installing:

```
# Run on your local machine (5 seconds)
python server.py
# Share your IP with friends (same network)
```

## 📜 License & Ethical Use

Distributed under the **MIT License**. See `LICENSE` for more information.

> ⚠️ **Ethical Use Notice**  
> VoidChat is built for **privacy education, research, and legitimate anonymous communication**.  
> **Do not use** for illegal activities, harassment, or any malicious purpose.  
> The developer assumes no liability for misuse.

---

## ⭐ Support

If you find **VoidChat** useful for your privacy‑focused work or research:

- **Star** this repository ⭐
- **Share** it with others who value digital anonymity
- **Report issues** or suggest features via GitHub Issues

---

## 👨‍💻 Developer

<div align="center">

**Karndeep Baror**  
*Cyber Crime Investigator · Security Tool Builder · Open Source Contributor*

[![GitHub](https://img.shields.io/badge/GitHub-@karndeepbaror-black?logo=github)](https://github.com/karndeepbaror)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/karndeepbaror)

**Tagline:** *"The Digital Phantom That Strikes Without Warning."*

</div>

---

<div align="center">
  <sub>Built with 🔥 by Karndeep Baror — For the ones who speak without a trace.</sub>
</div>
