# Example: Create a large match

This example illustrates how to set up a rule set for matches that can exceed 40
players. When a rule set describes teams with a total maxPlayer count greater than 40,
it is processed as a large match. Learn more in [Design a FlexMatch large-match rule
set](match-design-rulesets-large.md "match-design-rulesets-large.md").

The example rule set creates a match using the following instructions:

- Create one team with up to 200 players, with a minimum requirement of 175
  players.
- Balancing criteria: Select players based on similar skill level. All players
  must report their skill level to be matched.
- Batching preference: Group players by similar balancing criteria when creating
  matches.
- Latency rules: Set the maximum acceptable player latency of 150
  milliseconds.
- If the match is not filled quickly, relax the requirements to complete a match
  in reasonable time.

      + After 10 seconds, accept a team with 150 players.
      + After 12 seconds, raise the maximum acceptable latency to 200
       milliseconds.
      + After 15 seconds, accept a team with 100 players.

  Notes on using this rule set:

- Because the algorithm uses the "largest population" batching preference,
  players are first sorted based on the balancing criteria. As a result, matches
  tend to be fuller and contain players that are more similar in skill. All
  players meet acceptable latency requirements, but they may not get the best
  possible latency for their location.
- The algorithm strategy used in this rule set, "largest population", is the
  default setting. To use the default, you can opt to omit the setting.
- If you've enabled match backfill, do not relax player count requirements too
  quickly, or you may end up with too many partially filled game sessions. Learn
  more in [Relax large match
  requirements](match-design-rulesets-large-relax.md "match-design-rulesets-large-relax.md").

```
{
    "name": "free-for-all",
    "ruleLanguageVersion": "1.0",
    "playerAttributes": [{
        "name": "skill",
        "type": "number"
    }],
    "algorithm": {
        "balancedAttribute": "skill",
        "strategy": "balanced",
        "batchingPreference": "largestPopulation"
    },
    "teams": [{
        "name": "Marauders",
        "maxPlayers": 200,
        "minPlayers": 175
    }],
    "rules": [{
        "name": "low-latency",
        "description": "Sets maximum acceptable latency",
        "type": "latency",
        "maxLatency": 150
    }],
    "expansions": [{
        "target": "rules[low-latency].maxLatency",
        "steps": [{
            "waitTimeSeconds": 12,
            "value": 200
        }],
    }, {
        "target": "teams[Marauders].minPlayers",
        "steps": [{
            "waitTimeSeconds": 10,
            "value": 150
        }, {
            "waitTimeSeconds": 15,
            "value": 100
        }]
    }]
}
```
