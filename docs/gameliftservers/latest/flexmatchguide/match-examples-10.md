# Example: Use a compound rule to create a match

with players with similar attributes or similar selections

This example illustrates how to set up a rule set for matches with two teams using
`compound`. In the example:

- The `SimilarLeagueDistance` rule ensures all players in a match
  have a `league` within 2 of other players.
- The `SimilarSkillDistance` rule ensures all players in a match have
  a `skill` within 10 of other players. If a player has been waiting 10
  seconds, the distance is expanded to 20. If a player has been waiting 20
  seconds, the distance is expanded to 40.
- The `SameMapComparison` rule ensures all players in a match have
  requested the same `map`.
- The `SameModeComparison` rule ensures all players in a match have
  requested the same `mode`.
- The `CompoundRuleMatchmaker` rule ensures a match if at least one
  of the following conditions is true:
  - Players in a match have requested the same `map` and the
    same `mode`.
  - Players in a match have comparable `skill` and
    `league` attributes.

```
{
    "ruleLanguageVersion": "1.0",
    "teams": [{
        "name": "red",
        "minPlayers": 10,
        "maxPlayers": 20
    }, {
        "name": "blue",
        "minPlayers": 10,
        "maxPlayers": 20
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
        "name": "SimilarLeagueDistance",
        "type": "distance",
        "measurements": ["max(flatten(teams[*].players.attributes[league]))"],
        "referenceValue": "min(flatten(teams[*].players.attributes[league]))",
        "maxDistance": 2
    }, {
        "name": "SimilarSkillDistance",
        "type": "distance",
        "measurements": ["max(flatten(teams[*].players.attributes[skill]))"],
        "referenceValue": "min(flatten(teams[*].players.attributes[skill]))",
        "maxDistance": 10
    }, {
        "name": "SameMapComparison",
        "type": "comparison",
        "operation": "=",
        "measurements": ["flatten(teams[*].players.attributes[map])"]
    }, {
        "name": "SameModeComparison",
        "type": "comparison",
        "operation": "=",
        "measurements": ["flatten(teams[*].players.attributes[mode])"]
    }, {
        "name": "CompoundRuleMatchmaker",
        "type": "compound",
        "statement": "or(and(SameMapComparison, SameModeComparison), and(SimilarSkillDistance, SimilarLeagueDistance))"
    }],
    "expansions": [{
        "target": "rules[SimilarSkillDistance].maxDistance",
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
