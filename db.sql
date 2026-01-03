CREATE DATABASE globetrotter;
USE globetrotter;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100)
);
CREATE TABLE trips (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    name VARCHAR(100),
    start_date DATE,
    end_date DATE,
    description TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
CREATE TABLE cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(100),
    cost_per_day INT
);
CREATE TABLE activities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    cost INT
);
CREATE TABLE trip_cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    trip_id INT,
    city_id INT,
    days INT,
    FOREIGN KEY (trip_id) REFERENCES trips(id),
    FOREIGN KEY (city_id) REFERENCES cities(id)
);
CREATE TABLE trip_activities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    trip_city_id INT,
    activity_id INT,
    FOREIGN KEY (trip_city_id) REFERENCES trip_cities(id),
    FOREIGN KEY (activity_id) REFERENCES activities(id)
);
