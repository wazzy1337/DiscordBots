-- players (Sinners) table: tracks each player (sinner) and their total sins.
CREATE TABLE IF NOT EXISTS players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    discord_id INTEGER DEFAULT 0,
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

-- audit table: logs each instance of a player (sinner) being assigned a sin.
CREATE TABLE IF NOT EXISTS sin_audit_trail (
    audit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sin_id INTEGER NOT NULL,
    player_id TEXT NOT NULL,
    auditor_id TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    CHECK (timestamp GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9][0-9]:[0-9][0-9]:[0-9][0-9]'), -- ISO 8601 date format (YYYY-MM-DDTHH:MM:SS)
    FOREIGN KEY (sin_id) REFERENCES sin(sin_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id),
    FOREIGN KEY (auditor_id) REFERENCES players(player_id)
);