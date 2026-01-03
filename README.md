# Odoo-Hackathon- GlobeTrotter – Travel Planning Web App

GlobeTrotter is a **full-stack travel planning web application** built as part of a hackathon.
It helps users plan trips, manage itineraries, and estimate travel budgets.

The project demonstrates **frontend–backend integration using REST APIs**.

---

## 🚀 Features

* User Authentication (Signup & Login)
* Create and manage trips
* Add cities and activities to trips
* Calculate trip budget
* Frontend–Backend integration using Flask APIs

---

## 🛠️ Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python (Flask)
* MySQL

### Tools

* Git & GitHub
* REST APIs

---

## Project Structure

```
GlobeTrotter/
│
├── CSS/
│   └── styles.css
│
├── js/
│   ├── config.js
│   └── theme.js
│
├── pages/
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── create-trip.html
│   ├── itinerary.html
│   └── budget.html
│
├── app.py        # Flask backend
├── db.sql        # Database schema
└── README.md
```

---

## How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone <your-github-repo-link>
cd GlobeTrotter
```

### 2️⃣ Setup Database

* Import `db.sql` into MySQL
* Update database credentials in `app.py`

### 3️⃣ Run Backend

```bash
python app.py
```

Backend runs on:

```
http://127.0.0.1:5000
```

### 4️⃣ Run Frontend

* Open any HTML file (e.g., `login.html`) in browser
* Or use VS Code Live Server

---


## Future Enhancements

* JWT-based authentication
* Password hashing
* Deployment on cloud
* Improved UI/UX
* Role-based access



