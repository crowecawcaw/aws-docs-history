# Example: Find intersections across multiple player

attributes

This example illustrates how to use a collection rule to find intersections in two or
more player attributes. When working with collections, you can use the
`intersection` operation for a single attribute, and the
`reference_intersection_count` operation for multiple attributes.

To illustrate this approach, this example evaluates players in a match based on their
character preferences. The example game is a "free-for-all" style in which all players
in a match are opponents. Each player is asked to (1) choose a character for themselves,
and (2) choose characters they want to play against. We need a rule that ensures that
every player in a match is using a character that is on all other players' preferred
opponents list.

The example rule set describes a match with the following characteristics:

- Team structure: One team of five players
- Player attributes:
  - _myCharacter_: The player's chosen
    character.
  - _preferredOpponents_: List of
    characters that the player wants to play against.

- Match rules: A potential match is acceptable if each character in use is on
  every player's preferred opponents list.
  To implement the match rule, this example uses a collection rule with the following
  property values:

- Operation – Uses `reference_intersection_count` operation to
  evaluate how each string list in the measurement value intersects with the
  string list in the reference value.
- Measurement – Uses the `flatten` property expression to
  create a list of string lists, with each string list containing one player's
  _myCharacter_ attribute value.
- Reference value – Uses the `set_intersection` property
  expression to create a string list of all _preferredOpponents_ attribute values that are common to every
  player in the match.
- Restrictions – `minCount` is set to 1 to ensure that each
  player's chosen character (a string list in the measurement) matches at least
  one of the preferred opponents common to all players. (a string in the reference
  value).
- Expansion – If a match is not filled within 15 seconds, relax the
  minimum intersection requirement.
  The process flow for this rule is as follows:

1. A player is added to the prospective match. The reference value (a string
   list) is recalculated to include intersections with the new player's preferred
   opponents list. The measurement value (a list of string lists) is recalculated
   to add the new player's chosen character as a new string list.
2. Amazon GameLift Servers verifies that each string list in the measurement value (the
   players' chosen characters) intersects with at least one string in the reference
   value (the players' preferred opponents). Since in this example each string list
   in the measurement contains only one value, the intersection is either 0 or
3.
4. If any string list in the measurement does not intersect with the reference
   value string list, the rule fails and the new player is removed from the
   prospective match.
5. If a match is not filled within 15 seconds, drop the opponent match
   requirement to fill the remaining player slots in the match.

```
{
    "name": "preferred_characters",
    "ruleLanguageVersion": "1.0",

    "playerAttributes": [{
        "name": "myCharacter",
        "type": "string_list"
    }, {
        "name": "preferredOpponents",
        "type": "string_list"
    }],

    "teams": [{
        "name": "red",
        "minPlayers": 5,
        "maxPlayers": 5
    }],

    "rules": [{
        "description": "Make sure that all players in the match are using a character that is on all other players' preferred opponents list.",
        "name": "OpponentMatch",
        "type": "collection",
        "operation": "reference_intersection_count",
        "measurements": ["flatten(teams[*].players.attributes[myCharacter])"],
        "referenceValue": "set_intersection(flatten(teams[*].players.attributes[preferredOpponents]))",
        "minCount":1
    }],
    "expansions": [{
        "target": "rules[OpponentMatch].minCount",
        "steps": [{
            "waitTimeSeconds": 15,
            "value": 0
        }]
    }]
}
```
