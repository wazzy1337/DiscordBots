/* Adds the cost of a sin to a player's total sins
*  Parameters:
*   :player_id -> The ID of the sinner
*   :sin_cost  -> The sin's penalty value
*/

UPDATE players
SET total_sins = total_sins + ?
WHERE player_id = ?