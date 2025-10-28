# Example: Create two teams with evenly matched

players

This example illustrates how to set up two equally matched teams of players with the
following instructions.

- Create two teams of players.
  - Include between four and eight players in each team.
  - Final teams must have the same number of players.

- Include a player’s skill level (if not provided, default to 10).
- Choose players based on whether their skill level is similar to other players.
  Ensure that both teams have an average player skill within 10 points of each
  other.
- If the match is not filled quickly, relax the player skill requirement to
  complete a match in reasonable time.

      + After 5 seconds, expand the search to allow teams with average player
       skills within 50 points.
      + After 15 seconds, expand the search to allow teams with average player
       skills within 100 points.

  Notes on using this rule set:

- This example allows for teams to be any size between four and eight players
  (although they must be the same size). For teams with a range of valid sizes,
  the matchmaker makes a best-effort attempt to match the maximum number of
  allowed players.
- The `FairTeamSkill` rule ensures that teams are evenly matched
  based on player skill. To evaluate this rule for each new prospective player,
  FlexMatch tentatively adds the player to a team and calculates the averages. If
  rule fails, the prospective player is not added to the match.
- Since both teams have identical structures, you could opt to create just one
  team definition and set the team quantity to "2". In this scenario, if you named
  the team "aliens", then your teams would be assigned the names "aliens_1" and
  "aliens_2".

```
{
    "name": "aliens_vs_cowboys",
    "ruleLanguageVersion": "1.0",
    "playerAttributes": [{
        "name": "skill",
        "type": "number",
        "default": 10
    }],
    "teams": [{
        "name": "cowboys",
        "maxPlayers": 8,
        "minPlayers": 4
    }, {
        "name": "aliens",
        "maxPlayers": 8,
        "minPlayers": 4
    }],
    "rules": [{
        "name": "FairTeamSkill",
        "description": "The average skill of players in each team is within 10 points from the average skill of all players in the match",
        "type": "distance",
        // get skill values for players in each team and average separately to produce list of two numbers
        "measurements": [ "avg(teams[*].players.attributes[skill])" ],
        // get skill values for players in each team, flatten into a single list, and average to produce an overall average
        "referenceValue": "avg(flatten(teams[*].players.attributes[skill]))",
        "maxDistance": 10 // minDistance would achieve the opposite result
    }, {
        "name": "EqualTeamSizes",
        "description": "Only launch a game when the number of players in each team matches, e.g. 4v4, 5v5, 6v6, 7v7, 8v8",
        "type": "comparison",
        "measurements": [ "count(teams[cowboys].players)" ],
        "referenceValue": "count(teams[aliens].players)",
        "operation": "=" // other operations: !=, <, <=, >, >=
    }],
    "expansions": [{
        "target": "rules[FairTeamSkill].maxDistance",
        "steps": [{
            "waitTimeSeconds": 5,
            "value": 50
        }, {
            "waitTimeSeconds": 15,
            "value": 100
        }]
    }]
}
```
