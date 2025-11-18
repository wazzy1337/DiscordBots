/* Logs an audit record for a sin being added to a player (Sinner).
*  Parameters:
*   :sin_id -> The ID of the sin committed.
*   :player_id -> The ID of the sinner
*   :auditor_id -> The ID of the player who raised and logged the sin.
*/

INSERT INTO sin_audit_trail (sin_id, player_id, auditor_id, timestamp)
VALUES (?, ?, ?, CURRENT_TIMESTAMP);
