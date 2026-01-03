# imports
from flask import Flask, request, jsonify
import mysql.connector

# app + db config
app = Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="****",
    database="globetrotter"
)
cursor = db.cursor()

# -------- AUTH --------
@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    cursor.execute(
    "INSERT INTO users (email, password) VALUES (%s, %s)",
    (data["email"], data["password"])
    )
    db.commit()
    return jsonify({"message": "Signup successful"})

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    cursor.execute(
        "SELECT id FROM users WHERE email=%s AND password=%s",
        (data["email"], data["password"])
    )
    user = cursor.fetchone()
    if user:
        return jsonify({"message": "Login success", "user_id": user[0]})
    return jsonify({"message": "Invalid credentials"}), 401

# -------- TRIPS --------
@app.route("/create-trip", methods=["POST"])
def create_trip():
    data = request.json
    cursor.execute(
    "INSERT INTO trips (user_id, name, start_date, end_date, description) VALUES (%s,%s,%s,%s,%s)",
    (data["user_id"], data["name"], data["start_date"], data["end_date"], data["description"])
    )
    db.commit()
    return jsonify({"message": "Trip created"})

@app.route("/my-trips/<int:user_id>")
def my_trips(user_id):
    cursor.execute("SELECT * FROM trips WHERE user_id=%s", (user_id,))
    trips = cursor.fetchall()
    return jsonify(trips)

# -------- ITINERARY --------
@app.route("/add-city", methods=["POST"])
def add_city():
    data = request.json
    cursor.execute(
        "INSERT INTO trip_cities (trip_id, city_id, days) VALUES (%s,%s,%s)",
        (data["trip_id"], data["city_id"], data["days"])
    )
    db.commit()
    return jsonify({"message": "City added"})

@app.route("/add-activity", methods=["POST"])
def add_activity():
    data = request.json
    cursor.execute(
        "INSERT INTO trip_activities (trip_city_id, activity_id) VALUES (%s,%s)",
        (data["trip_city_id"], data["activity_id"])
    )
    db.commit()
    return jsonify({"message": "Activity added"})

# -------- BUDGET --------
@app.route("/trip-budget/<int:trip_id>")
def trip_budget(trip_id):
    cursor.execute("""
        SELECT SUM(c.cost_per_day * tc.days)
        FROM trip_cities tc
        JOIN cities c ON tc.city_id = c.id
        WHERE tc.trip_id = %s
    """, (trip_id,))
    total = cursor.fetchone()[0]
    return jsonify({"total_budget": total or 0})
@app.route("/")
def home():
    return "GlobeTrotter Backend is running ✅"
if __name__ == "__main__":
    app.run(debug=True)
