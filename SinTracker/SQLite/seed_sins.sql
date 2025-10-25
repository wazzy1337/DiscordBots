/*
This is seed data.
It contains the original sins, and their penalty cost upon inception of our BG3 playthrough.
*/
INSERT INTO sin (sin_name, sin_description, sin_points)
VALUES
    ('Tactical Failure/Betrayal/Cowardice', 'Letting players down in combat', 1),
    ('Thievery', 'Stealing from a homie', 1),
    ('Troublemaking', 'Getting the group into trouble with NPCs', 2),
    ('Cuckery', 'Getting in the way of a homie gettin'' some.', 5),
    ('Hoarding', 'Keeping items for themselves, refusing to share with the party.', 1),
    ('Researching', 'Gaining advance knowledge, spoiling the adventure and making encounters easier than intended.', 5),
    ('Lateness', 'Arriving late to the sesh, causing delays and forcing the boyz to wait for your arse', 1),
    ('Immoral Acts', 'Engaging in scandalous or inappropriate behaviour, disrupting the party’s aura & decorum', 5),
    ('Unnecessary Killing', 'Killing creatures or NPCs without reason or by accident, needlessly endangering the party or spoiling potential story outcomes.', 2),
    ('Annoyance', 'Behaviour/actions that upset or annoy NPCs, causing them to abandon the camp. Also, applies to players.', 5),
    ('Running Ahead', 'Rushing ahead of the party, triggering fights and/or missing group coordination', 2),
    ('Hogging Dialogue', 'Controlling conversation, preventing other players from helping decide dialogue options. Also, includes not telling players they''re in dialogue', 2),
    ('Missed Opportunity', 'Missing obvious attacks or spells', 1),
    ('Get Opportunitied', 'Getting struck by an attack of opportunity.', 1),
    ('Spell Misfire', 'Using wrong spells/items for the situation.', 1),
    ('Neglecting the Homies', 'Failing to protect, heal etc party members.', 1),
    ('Trap Twat', 'Setting off traps.', 1),
    ('Friendly Fire', 'Hitting the homies.', 1),
    ('Socially Retarded', 'Failing persuasion or deception checks.', 1),
    ('Blocking', 'Blocking the homies in combat / movement.', 1),
    ('Headstrong', 'Ignoring the homies plan.', 1),
    ('Unnecessary Death', 'Dying when it could have easily been avoided.', 1),
    ('Nature Blind', 'Standing in avoidable shit.', 1),
    ('Shameful Reload', 'Reloading a previous save to undo failures or avoiding certain consequences/outcomes.', 1),
    ('Critical Miss', 'Failing a roll spectacularly, rolling a 1.', 1)