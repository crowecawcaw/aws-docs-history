# Example: Create a large match with players with

similar attributes

This example illustrates how to set up a rule set for matches with two teams using
`batchDistance`. In the example:

- The `SimilarLeague` rule ensures all players in a match have a
  `league` within 2 of other players.
- The `SimilarSkill` rule ensures all players in a match have a
  `skill` within 10 of other players. If a player has been waiting
  10 seconds, the distance is expanded to 20. If a player has been waiting 20
  seconds, the distance is expanded to 40.
- The `SameMap` rule ensures all players in a match have requested
  the same `map`.
- The `SameMode` rule ensures all players in a match have requested
  the same `mode`.

```
{
    "ruleLanguageVersion": "1.0",
    "teams": [{
        "name": "red",
        "minPlayers": 100,
        "maxPlayers": 100
    }, {
        "name": "blue",
        "minPlayers": 100,
        "maxPlayers": 100
    }],
    "algorithm": {
        "strategy":"balanced",
        "balancedAttribute": "skill",
        "batchingPreference":"fastestRegion"
    },
    "playerAttributes": [{
        "name": "league",
        "type": "number"
    },{
        "name": "skill",
        "type": "number"
    },{
        "name": "map",
        "type": "string"
    },{
        "name": "mode",
        "type": "string"
    }],
    "rules": [{
        "name": "SimilarLeague",
        "type": "batchDistance",
        "batchAttribute": "league",
        "maxDistance": 2
    }, {
        "name": "SimilarSkill",
        "type": "batchDistance",
        "batchAttribute": "skill",
        "maxDistance": 10
    }, {
        "name": "SameMap",
        "type": "batchDistance",
        "batchAttribute": "map"
    }, {
        "name": "SameMode",
        "type": "batchDistance",
        "batchAttribute": "mode"
    }],
    "expansions": [{
        "target": "rules[SimilarSkill].maxDistance",
        "steps": [{
            "waitTimeSeconds": 10,
            "value": 20
        }, {
            "waitTimeSeconds": 20,
            "value": 40
        }]
    }]
}
```
