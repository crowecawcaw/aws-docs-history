# Example: Create a multi-team large match

This example illustrates how to set up a rule set for matches with multiple teams that
can exceed 40 players. This example illustrates how to create multiple identical teams
with one definition and how asymmetrically sized teams are filled during match
creation.

The example rule set creates a match using the following instructions:

- Create ten identical "hunter" teams with up to 15 players, and one "monster"
  team with exactly 5 players.
- Balancing criteria: Select players based on number of monster kills. If
  players don't report their kill count, use a default value of 5.
- Batching preference: Group players based on the regions where they report the
  fastest player latency.
- Latency rule: Sets a maximum acceptable player latency of 200 milliseconds.
- If the match is not filled quickly, relax the requirements to complete a match
  in reasonable time.

      + After 15 seconds, accept teams with 10 players.
      + After 20 seconds, accept teams with 8 players.

  Notes on using this rule set:

- This rule set defines teams that can potentially hold up to 155 players, which
  makes it a large match. (10 x 15 hunters + 5 monsters = 155)
- Because the algorithm uses the "fastest region" batching preference, players
  tend to be placed in regions where they report faster latency and not in regions
  where they report high (but acceptable) latency. At the same time, matches are
  likely to have fewer players, and the balancing criteria (number of monster
  skills) may vary more widely.
- When an expansion is defined for a multi-team definition (quantity > 1), the
  expansion applies to all teams created with that definition. So by relaxing the
  hunter team minimum players setting, all ten hunter teams are affected
  equally.
- Since this rule set is optimized to minimize player latency, the latency rule
  acts as a catch-all to exclude players who have no acceptable connection
  options. We don't need to relax this requirement.
- Here's how FlexMatch fills matches for this rule set before any expansions take
  effect:
  - No teams have reached minPlayers count yet. Hunter teams have 15 open
    slots, while Monster team has 5 open slots.
    - The first 100 players are assigned (10 each) to the ten hunter
      teams.
    - The next 22 players are assigned sequentially (2 each) to
      hunter teams and monster team.

  - Hunter teams have reached minPlayers count of 12 players each. Monster
    team has 2 players and has not reached minPlayers count.
    - The next three players are assigned to the monster
      team.

  - All teams have reached minPlayers count. Hunter teams each have three
    open slots. Monster team is full.
    - The final 30 players are assigned sequentially to the hunter
      teams, ensuring that all hunter teams have nearly the same size
      (plus or minus one player).

- If you've enabled backfill for matches created with this rule set, do not
  relax player count requirements too quickly, or you may end up with too many
  partially filled game sessions. Learn more in [Relax large match
  requirements](match-design-rulesets-large-relax.md "match-design-rulesets-large-relax.md").

```
{
    "name": "monster-hunters",
    "ruleLanguageVersion": "1.0",
    "playerAttributes": [{
        "name": "monster-kills",
        "type": "number",
        "default": 5
    }],
    "algorithm": {
        "balancedAttribute": "monster-kills",
        "strategy": "balanced",
        "batchingPreference": "fastestRegion"
    },
    "teams": [{
        "name": "Monsters",
        "maxPlayers": 5,
        "minPlayers": 5
    }, {
        "name": "Hunters",
        "maxPlayers": 15,
        "minPlayers": 12,
        "quantity": 10
    }],
    "rules": [{
        "name": "latency-catchall",
        "description": "Sets maximum acceptable latency",
        "type": "latency",
        "maxLatency": 150
    }],
    "expansions": [{
        "target": "teams[Hunters].minPlayers",
        "steps": [{
            "waitTimeSeconds": 15,
            "value": 10
        }, {
            "waitTimeSeconds": 20,
            "value": 8
        }]
    }]
}
```
