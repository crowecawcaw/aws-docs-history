# Example: Set team-level requirements and latency

limits

This example illustrates how to set up player teams and apply a set of rules to each
team instead of each individual player. It uses a single definition to create three
equally matched teams. It also establishes a maximum latency for all players. Latency
maximums can be relaxed over time to complete the match. This example sets out the
following instructions:

- Create three teams of players.
  - Include between three and five players in each team.
  - Final teams must contain the same or nearly the same number of players
    (within one).

- Include the following player attributes:
  - A player’s skill level (if not provided, default to 10).
  - A player’s character role (if not provided, default to
    “peasant”).

- Choose players based on whether their skill level is similar to other players
  in the match.
  - Ensure that each team has an average player skill within 10 points of
    each other.

- Limit teams to the following number of “medic” characters:
  - An entire match can have a maximum of five medics.

- Only match players who report latency of 50 milliseconds or less.
- If a match is not filled quickly, relax the player latency requirement as
  follows:

      + After 10 seconds, allow player latency values up to 100 ms.
      + After 20 seconds, allow player latency values up to 150 ms.

  Notes on using this rule set:

- The rule set ensures that teams are evenly matched based on player skill. To
  evaluate the `FairTeamSkill` rule, FlexMatch tentatively adds the
  prospective player to a team and calculates the average skill of players in the
  team. It then compares it against the average skill of players in both teams. If
  rule fails, the prospective player is not added to the match.
- The team- and match-level requirements (total number of medics) are achieved
  through a collection rule. This rule type takes a list of character attributes
  for all players and checks against the maximum counts. Use `flatten`
  to create a list for all players in all teams.
- When evaluating based on latency, note the following:
  - Latency data is provided in the matchmaking request as part of the
    Player object. It is not a player attribute, so it does not need to be
    listed as one.
    To obtain accurate latency measurements, use
    Amazon GameLift Servers's UDP ping beacons. These endpoints enable you to measure actual UDP
    network latency between player devices and each of the potential
    hosting locations, resulting in more accurate placement decisions
    than using ICMP pings. For more information on using UDP ping beacons to
    measure latency, refer to [UDP ping beacons](../developerguide/reference-udp-ping-beacons.md "../developerguide/reference-udp-ping-beacons.md").
  - The matchmaker evaluates latency by region. Any region with a latency
    higher than the maximum is ignored. To be accepted for a match, a player
    must have at least one region with a latency below the maximum.
  - If a matchmaking request omits latency data one or more players, the
    request is rejected for all matches.

```
{
    "name": "three_team_game",
    "ruleLanguageVersion": "1.0",
    "playerAttributes": [{
        "name": "skill",
        "type": "number",
        "default": 10
    },{
        "name": "character",
        "type": "string_list",
        "default": [ "peasant" ]
    }],
    "teams": [{
        "name": "trio",
        "minPlayers": 3,
        "maxPlayers": 5,
        "quantity": 3
    }],
    "rules": [{
        "name": "FairTeamSkill",
        "description": "The average skill of players in each team is within 10 points from the average skill of players in the match",
        "type": "distance",
        // get players for each team, and average separately to produce list of 3
        "measurements": [ "avg(teams[*].players.attributes[skill])" ],
        // get players for each team, flatten into a single list, and average to produce overall average
        "referenceValue": "avg(flatten(teams[*].players.attributes[skill]))",
        "maxDistance": 10 // minDistance would achieve the opposite result
    }, {
        "name": "CloseTeamSizes",
        "description": "Only launch a game when the team sizes are within 1 of each other.  e.g. 3 v 3 v 4 is okay, but not 3 v 5 v 5",
        "type": "distance",
        "measurements": [ "max(count(teams[*].players))"],
        "referenceValue": "min(count(teams[*].players))",
        "maxDistance": 1
    }, {
        "name": "OverallMedicLimit",
        "description": "Don't allow more than 5 medics in the game",
        "type": "collection",
        // This is similar to above, but the flatten flattens everything into a single
        // list of characters in the game.
        "measurements": [ "flatten(teams[*].players.attributes[character])"],
        "operation": "contains",
        "referenceValue": "medic",
        "maxCount": 5
    }, {
        "name": "FastConnection",
        "description": "Prefer matches with fast player connections first",
        "type": "latency",
        "maxLatency": 50
    }],
    "expansions": [{
        "target": "rules[FastConnection].maxLatency",
        "steps": [{
            "waitTimeSeconds": 10,
            "value": 100
        }, {
            "waitTimeSeconds": 20,
            "value": 150
        }]
    }]
}
```
