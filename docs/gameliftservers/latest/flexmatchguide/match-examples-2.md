# Example: Create uneven teams (Hunters vs Monster)

This example describes a game mode in which a group of players hunt a single monster.
People choose either a hunter or a monster role. Hunters specify the minimum skill level
for the monster that they want to face. The minimum size of the hunter team can be
relaxed over time to complete the match. This scenario sets out the following
instructions:

- Create one team of exactly five hunters.
- Create a separate team of exactly one monster.
- Include the following player attributes:
  - A player’s skill level (if not provided, default to 10).
  - A player’s preferred monster skill level (if not provided, default to
    10).
  - Whether the player wants to be the monster (if not provided, default
    to 0 or false).

- Choose a player to be the monster based on the following criteria:
  - Player must request the monster role.
  - Player must meet or exceed the highest skill level preferred by the
    players who are already added to the hunter team.

- Choose players for the hunter team based on the following criteria:
  - Players who request a monster role cannot join the hunter team.
  - If the monster role is already filled, player must want a monster
    skill level that is lower than the skill of the proposed monster.

- If a match is not filled quickly, relax the hunter team's minimum size as
  follows:

      + After 30 seconds, allow a game to start with only four players in the
       hunter team.
      + After 60 seconds, allow a game to start with only three people in the
       hunter team.

  Notes on using this rule set:

- By using two separate teams for hunters and monster, you can evaluate
  membership based on different sets of criteria.

```
{
    "name": "players_vs_monster_5_vs_1",
    "ruleLanguageVersion": "1.0",
    "playerAttributes": [{
        "name": "skill",
        "type": "number",
        "default": 10
    },{
        "name": "desiredSkillOfMonster",
        "type": "number",
        "default": 10
    },{
        "name": "wantsToBeMonster",
        "type": "number",
        "default": 0
    }],
    "teams": [{
        "name": "players",
        "maxPlayers": 5,
        "minPlayers": 5
    }, {
        "name": "monster",
        "maxPlayers": 1,
        "minPlayers": 1
    }],
    "rules": [{
        "name": "MonsterSelection",
        "description": "Only users that request playing as monster are assigned to the monster team",
        "type": "comparison",
        "measurements": ["teams[monster].players.attributes[wantsToBeMonster]"],
        "referenceValue": 1,
        "operation": "="
    },{
        "name": "PlayerSelection",
        "description": "Do not place people who want to be monsters in the players team",
        "type": "comparison",
        "measurements": ["teams[players].players.attributes[wantsToBeMonster]"],
        "referenceValue": 0,
        "operation": "="
    },{
        "name": "MonsterSkill",
        "description": "Monsters must meet the skill requested by all players",
        "type": "comparison",
        "measurements": ["avg(teams[monster].players.attributes[skill])"],
        "referenceValue": "max(teams[players].players.attributes[desiredSkillOfMonster])",
        "operation": ">="
    }],
    "expansions": [{
        "target": "teams[players].minPlayers",
        "steps": [{
            "waitTimeSeconds": 30,
            "value": 4
        },{
            "waitTimeSeconds": 60,
            "value": 3
        }]
    }]
}
```
