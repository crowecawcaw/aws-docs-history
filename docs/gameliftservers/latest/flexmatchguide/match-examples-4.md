# Example: Use explicit sorting to find best

matches

This example sets up a simple match with two teams of three players. It illustrates
how to use explicit sorting rules to help find the best possible matches as quickly as
possible. These rules sort all active matchmaking tickets to create the best matches
based on certain key requirements. This example is implemented with the following
instructions:

- Create two teams of players.
- Include exactly three players in each team.
- Include the following player attributes:
  - Experience level (if not provided, default to 50).
  - Preferred game modes (can list multiple values) (if not provided,
    default to “coop” and “deathmatch”).
  - Preferred game maps, including map name and preference weighting (if
    not provided, default to `"defaultMap"` with a weight of
    100).

- Set up presorting:
  - Sort players based on their preference for the same game map as the
    anchor player. Players can have multiple favorite game maps, so this
    example uses a preference value.
  - Sort players based on how closely their experience level matches the
    anchor player. With this sort, all players in all teams will have
    experience levels that are as close as possible.

- All players across all teams must have selected at least one game mode in
  common.
- All players across all teams must have selected at least one game map in
  common.
  Notes on using this rule set:

- The game map sort uses an absolute sort that compares the mapPreference
  attribute value. Because it is first in the rule set, this sort is performed
  first.
- The experience sort uses a distance sort to compare a prospective player's
  skill level with the anchor player's skill.
- Sorts are performed in the order they are listed in a rule set. In this
  scenario, players are sorted by game map preference, and then by experience
  level.

```
{
    "name": "multi_map_game",
    "ruleLanguageVersion": "1.0",
    "playerAttributes": [{
        "name": "experience",
        "type": "number",
        "default": 50
    }, {
        "name": "gameMode",
        "type": "string_list",
        "default": [ "deathmatch", "coop" ]
    }, {
        "name": "mapPreference",
        "type": "string_number_map",
        "default": { "defaultMap": 100 }
    }, {
        "name": "acceptableMaps",
        "type": "string_list",
        "default": [ "defaultMap" ]
    }],
    "teams": [{
        "name": "red",
        "maxPlayers": 3,
        "minPlayers": 3
    }, {
        "name": "blue",
        "maxPlayers": 3,
        "minPlayers": 3
    }],
    "rules": [{
        // We placed this rule first since we want to prioritize players preferring the same map
        "name": "MapPreference",
        "description": "Favor grouping players that have the highest map preference aligned with the anchor's favorite",
        // This rule is just for sorting potential matches.  We sort by the absolute value of a field.
        "type": "absoluteSort",
        // Highest values go first
        "sortDirection": "descending",
        // Sort is based on the mapPreference attribute.
        "sortAttribute": "mapPreference",
        // We find the key in the anchor's mapPreference attribute that has the highest value.
        // That's the key that we use for all players when sorting.
        "mapKey": "maxValue"
    }, {
        // This rule is second because any tie-breakers should be ordered by similar experience values
        "name": "ExperienceAffinity",
        "description": "Favor players with similar experience",
        // This rule is just for sorting potential matches.  We sort by the distance from the anchor.
        "type": "distanceSort",
        // Lowest distance goes first
        "sortDirection": "ascending",
        "sortAttribute": "experience"
    }, {
        "name": "SharedMode",
        "description": "The players must have at least one game mode in common",
        "type": "collection",
        "operation": "intersection",
        "measurements": [ "flatten(teams[*].players.attributes[gameMode])"],
        "minCount": 1
    }, {
        "name": "MapOverlap",
        "description": "The players must have at least one map in common",
        "type": "collection",
        "operation": "intersection",
        "measurements": [ "flatten(teams[*].players.attributes[acceptableMaps])"],
        "minCount": 1
    }]
}
```
