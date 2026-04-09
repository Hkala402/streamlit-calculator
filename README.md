# 🧮 Web Calculator

A clean, keyboard-friendly web calculator built with **Python (Flask)** and vanilla **HTML/CSS/JavaScript**.

The frontend sends math expressions to a Flask REST API, which evaluates them server-side and returns the result as JSON — demonstrating full-stack communication between a browser and a Python backend.

---

## 🚀 Features

- Basic arithmetic — addition, subtraction, multiplication, division
- Keyboard support (type numbers and operators directly)
- Toggle sign (`+/−`) and percentage (`%`)
- Error handling — division by zero, invalid expressions
- Chain calculations from previous results
- Clean, dark UI with monospace display font

---

## 🛠️ Tech Stack

| Layer     | Technology              |
|-----------|-------------------------|
| Backend   | Python 3, Flask         |
| Frontend  | HTML, CSS, JavaScript   |
| API       | REST (JSON over HTTP)   |

---

## 📁 Project Structure

```
webcalculator/
│
├── app.py                  ← Flask server & API routes
├── requirements.txt        ← Python dependencies
├── README.md
└── templates/
    └── index.html          ← UI (HTML + CSS + JS)
```

---

## ⚙️ How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/Hkala402/web-calculator.git
cd web-calculator

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the server
python app.py

# 4. Open in browser
http://127.0.0.1:5000
```

---

## 🔄 How It Works

```
User clicks "="
     ↓
JavaScript collects expression (e.g. "8*9+2")
     ↓
fetch() → POST /calculate  {"expression": "8*9+2"}
     ↓
Flask evaluates → returns {"result": "74", "error": null}
     ↓
JavaScript displays result on screen
```

---

## 👤 Author

**Himanshu Kala** — AI QA Engineer  
🌐 [himanshukala.co.in](https://himanshukala.co.in) · 🐙 [github.com/Hkala402](https://github.com/Hkala402)
