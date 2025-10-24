-- players (Sinners) table: tracks each player (sinner) and their total sins.
CREATE TABLE IF NOT EXISTS players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_name TEXT,
    player_nickname TEXT,
    total_sins INTEGER DEFAULT 0 
);