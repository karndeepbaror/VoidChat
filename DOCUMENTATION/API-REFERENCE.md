
# 📡 API Reference — VoidChat

> *Socket.IO events — for developers and tinkerers.*

---

## 🔌 Connection

| Event | Direction | Payload |
|-------|-----------|---------|
| `connect` | Client → Server | None |
| `disconnect` | Client → Server | None |

---

## 👤 User Events

| Event | Direction | Payload | Description |
|-------|-----------|---------|-------------|
| `join` | Client → Server | `{name, emoji}` | Join public room |
| `user_list` | Server → Client | `[{name, emoji, sid}]` | List of active users |

---

## 💬 Message Events

| Event | Direction | Payload | Description |
|-------|-----------|---------|-------------|
| `message` | Client → Server | `{text}` | Send message |
| `message` | Server → Client | `{name, emoji, text, time}` | Broadcast message |

---

## ⌨️ Typing Events

| Event | Direction | Payload |
|-------|-----------|---------|
| `typing` | Client → Server | `{name}` |
| `stop_typing` | Client → Server | `{}` |

---

## 📡 System Events

| Event | Direction | Payload |
|-------|-----------|---------|
| `system` | Server → Client | `{text}` |

> 🔍 All events are **room‑based** (public room only).
