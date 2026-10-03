# 🎮 Rock Paper Scissors — OOP Edition

> A feature-rich, interactive command-line Rock Paper Scissors game built in Python using Object-Oriented Programming principles.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Architecture-OOP-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

---

## ✨ Features

- 🎯 **Player vs. Computer Gameplay:** Test your luck against an automated AI opponent.
- 🎲 **Randomized AI Moves:** Computer choices generated dynamically using Python's `random` module.
- 🛡️️ **Robust Input Validation:** Prevents crashes and handles invalid user inputs gracefully.
- 🏆 **Live Scoreboard:** Keeps real-time track of scores across multiple rounds.
- 🔄 **Replayability:** Seamless play-again loop to play as long as you want.
- 🧩 **Clean OOP Architecture:** Built with modular classes for scalability and readability.

---

## 🧠 Core Concepts Applied

| 🏗️ Object-Oriented Concepts | 🐍 Python Fundamentals |
| :--- | :--- |
| • **Classes & Objects** | • **Lists & Collections** |
| • **Constructors (`__init__`)** | • **User Input Processing** |
| • **Attributes & Methods** | • **`random` Module** |
| • **Inheritance (`super()`)** | • **`if / elif / else` Logic** |
| • **Encapsulation** | • **`while` Control Loops** |
| | • **String Formatting (`f-strings`)** |

---

## 🏗️ Project Architecture

- 👤 **`Player` Class:** Manages human player state (`name`, `choice`, `score`, `input`).
- 🤖 **`Computer` Class:** Inherits from `Player` to auto-generate choices (Rock, Paper, or Scissors).
- 🎮 **`Game` Class:** Main engine controlling game loops, winner calculation, score tracking, and result displays.

---

## 📜 Game Rules

| Choice | Beats | Outcome |
| :---: | :---: | :---: |
| 🪨 **Rock** | ✂️ Scissors | 🪨 > ✂️ |
| 📄 **Paper** | 🪨 Rock | 📄 > 🪨 |
| ✂️ **Scissors** | 📄 Paper | ✂️ > 📄 |

> 🤝 **Note:** Matching choices result in a tie round!

---

## ▶️ How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/maniakhan15/rock-paper-scissors-oop.git](https://github.com/maniakhan15/rock-paper-scissors-oop.git)
   cd rock-paper-scissors-oop
   Execute the game script:
Bash
python "rock-paper-scissor game.py"


## 📌 Project Goal
This project was built to practice core Object-Oriented Programming (OOP) principles in Python by turning basic game logic into clean, reusable, and modular code.

🛠️ Built With
Language: Python 🐍

Paradigm: Object-Oriented Programming (OOP)

IDE: VS Code
