# 💰 CLI Banking System

A simple yet robust command-line banking system built with **Python**. This project is designed to demonstrate clean code practices, rigorous input handling, and a modular software architecture.

---

## ✨ Features

- **👤 User Management:** Create and manage customer profiles.
- **🏦 Account Management:** Open bank accounts linked to existing users.
- **💸 Financial Operations:** Secure deposits and withdrawals with business rule validations.
- **📜 Transaction Statement:** Full history of all financial activities.
- **🛡️ Error Handling:** Robust input validation to prevent system crashes.
- **🏗️ Clean Code:** Clear separation between the user interface (CLI) and business logic.

---

## 🧱 Project Structure

The project is organized to support scalability and maintainability:

```text
cli-banking-system/
│
├── main.py            # Application entry point
├── README.md          # Project documentation
│
└── modules/           # Modular expansion (Future)
    ├── models.py      # Data structures (User, Account)
    ├── services.py    # Business logic (withdraw, deposit)
    └── utils.py       # Input handling and helpers
```

> Note: The project is currently implemented in a single file for simplicity, but it follows a modular structure that can be easily expanded.

---

## 🚀 Getting Started

### Clone the repository

```text
git clone https://github.com/your-username/cli-banking-system.git  
cd cli-banking-system  
```
### Run the application
```text
python main.py  
```
---

## 🖥️ Usage
```text
[d] Deposit  
[s] Withdraw  
[e] Statement  
[nu] New User  
[nc] New Account  
[lc] List Accounts  
[q] Quit  
```
---

## 🧠 Design Decisions

- Separation of concerns → Input handling is isolated from business logic  
- User-friendly input → The system validates and converts user input automatically  
- Scalability → Easy transition to APIs or GUI applications  
- Clean code → Readable, maintainable, and modular design  

---

## 🔮 Future Improvements

- Data persistence (SQLite or JSON)  
- REST API version (Flask or FastAPI)  
- Web interface  
- Authentication system  

---

## 📚 Learning Goals

- Python fundamentals  
- Object-Oriented Programming (OOP)  
- CLI application design  
- Software architecture basics  

---

## ⭐ Final Thoughts

This is a beginner-friendly project with a strong focus on writing code like a real-world developer.

If you found this useful or interesting, feel free to star the repository!
