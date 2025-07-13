CREATE TABLE IF NOT EXISTS Daily_Calories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    food TEXT,
    protein INTEGER,
    calories INTEGER,
    date TEXT
);

CREATE TABLE IF NOT EXISTS Workouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    exersise_name TEXT NOT NULL,
    Reps_Per_Set INTEGER,
    Total_Sets INTEGER,
    Weight_Used TEXT,
    date TEXT
);

