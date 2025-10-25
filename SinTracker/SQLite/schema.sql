-- players (Sinners) table: tracks each player (sinner) and their total sins.
CREATE TABLE IF NOT EXISTS players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_name TEXT,
    player_nickname TEXT,
    total_sins INTEGER DEFAULT 0 
);

-- sin table: defines each type of action a player (sinner) can be penalized for.
CREATE TABLE IF NOT EXISTS sin (
    sin_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sin_name TEXT,
    sin_description TEXT,
    sin_points INTEGER DEFAULT 0 
);