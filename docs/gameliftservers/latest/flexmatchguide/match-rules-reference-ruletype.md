# FlexMatch rule types

## Batch distance

rule

```
batchDistance
```

Batch distance rules measure the difference between two attribute values. You can use
the batch distance rule type with both large and small matches. There are two types of
batch distance rules:

- _Compare numerical attribute values_. For example, a batch
  distance rule of this type might require that all players in a match be within
  two skill levels of each other. For this type, define a maximum distance between
  the `batchAttribute` of all tickets.
- _Compare string attribute values_. For example, a batch
  distance rule of this type might require that all players in a match request the
  same game mode. For this type, define a `batchAttribute` value that
  FlexMatch uses to form batches.

**Batch distance rule properties**

- **`batchAttribute`** – The
  player attribute value used to form batches.
- **`maxDistance`** – The maximum
  distance value for a successful match. Used to compare numerical
  attributes.
- **`partyAggregation`** – The
  value that determines how FlexMatch handles tickets with multiple players
  (parties). Valid options include the minimum (`min`), maximum
  (`max`), and average (`avg`) values for a ticket's
  players. The default is `avg`.

Examples

```
{
  "name":"SimilarSkillRatings",
  "description":"All players must have similar skill ratings",
  "type":"batchDistance",
  "batchAttribute":"SkillRating",
  "maxDistance":"500"
}
```

```
{
  "name":"SameGameMode",
  "description":"All players must have the same game mode",
  "type":"batchDistance",
  "batchAttribute":"GameMode"
}
```

## Comparison rule

```
comparison
```

Comparison rules compare a player attribute value to another value. There are two
types of comparison rules:

- _Compare to reference value_. For example, a comparison
  rule of this type might require that matched players have a certain skill level
  or greater. For this type, specify a player attribute, reference value, and a
  comparison operation.
- _Compare across players_. For example, a comparison rule of
  this type might require that all players in the match use different characters.
  For this type, specify a player attribute and either the equal (`=`)
  or not-equal (`!=`) comparison operation. Don't specify a reference
  value.

###### Note

Batch distance rules are more efficient for comparing player attributes. To reduce
matchmaking latency, use a batch distance rule when possible.

**Comparison rule properties**

- **`measurements`** – The player
  attribute value to compare.
- **`referenceValue`** – The
  value to compare the measurement to for a prospective match.
- **`operation`** – The value
  that determines how to compare the measurement to the reference value. Valid
  operations include: `<`, `<=`, `=`,
  `!=`, `>`, `>=`.
- **`partyAggregation`** – The
  value that determines how FlexMatch handles tickets with multiple players
  (parties). Valid options include the minimum (`min`), maximum
  (`max`), and average (`avg`) values for a ticket's
  players. The default is `avg`.

## Distance rule

```
distance
```

Distance rules measure the difference between two number values, such as the distance
between player skill levels. For example, a distance rule might require that all players
have played the game for at least 30 hours.

###### Note

Batch distance rules are more efficient for comparing player attributes. To reduce
matchmaking latency, use a batch distance rule when possible.

**Distance rule properties**

- **`measurements`** – The player
  attribute value to measure distance for. This must be an attribute with a
  numerical value.
- **`referenceValue`** – The
  numerical value to measure distance against for a prospective match.
- **`minDistance`/`maxDistance`** – The
  minimum or maximum distance value for a successful match.
- **`partyAggregation`** – The
  value that determines how FlexMatch handles tickets with multiple players
  (parties). Valid options include the minimum (`min`), maximum
  (`max`), and average (`avg`) values for a ticket's
  players. The default is `avg`.

## Collection rule

```
collection
```

Collection rules compare a group of player attribute values to those of other players
in the batch or to a reference value. A collection can contain attribute values for
multiple players, a player attribute as a string list, or both. For example, a
collection rule might look at the characters that the players in a team choose. The rule
might then require the team to have at least one of a certain character.

**Collection rule properties**

- **`measurements`** – The
  collection of player attribute values to compare. The attribute values must be
  string lists.
- **`referenceValue`** – The
  value (or collection of values) to use to compare measurements for a prospective
  match.
- **`operation`** – The value
  that determines how to compare a collection of measurements. Valid operations
  include the following:
  - `intersection` – This operation measures the number
    of values that are the same in all players' collections. For an example
    of a rule that uses the intersection operation, see [Example: Use explicit sorting to find best
    matches](match-examples-4.md "match-examples-4.md").
  - `contains` – This operation measures the number of
    player attribute collections that contain the specified reference value.
    For an example of a rule that uses the contains operation, see [Example: Set team-level requirements and latency
    limits](match-examples-3.md "match-examples-3.md").
  - `reference_intersection_count` – This operation
    measures the number of items in a player attribute collection that match
    items in the reference value collection. You can use this operation to
    compare multiple different player attributes. For an example of a rule
    that compares multiple player attribute collections, see [Example: Find intersections across multiple player
    attributes](match-examples-5.md "match-examples-5.md").

- **`minCount`/`maxCount`**
  – The minimum or maximum count value for a successful match.
- **`partyAggregation`** – The
  value that determines how FlexMatch handles tickets with multiple players
  (parties). For this value, you can use `union` to combine the player
  attributes of all players in the party. Or, you can use
  `intersection` to use player attributes that the party has in
  common. The default is `union`.

## Compound rule

```
compound
```

Compound rules use logical statements to form matches of 40 or fewer players. You can
use multiple compound rules in a single rule set. When using multiple compound rules,
all compound rules must be true to form a match.

You can't expand a compound rule using [expansion rules](match-rulesets-components-algorithm.md#match-rulesets-components-algorithm-expansion "match-rulesets-components-algorithm.md#match-rulesets-components-algorithm-expansion"), but
you can expand underlying or supporting rules.

**Compound rule properties**

- **`statement`** – The logic
  used to combine individual rules to form the compound rule. The rules that you
  specify in this property must have been defined earlier in your rule set. You
  can't use `batchDistance` rules in a compound rule.

This property supports the following logical operators:

    + `and` – The expression is true if the two provided
     arguments are true.
    + `or` – The expression is true if either of the two
     provided arguments are true.
    + `not` – Reverses the outcome of the argument in the
     expression.
    + `xor` – The expression is true if only one of the
     arguments is true.

###### Example

The following example matches players of varying skill levels based on the game
mode that they select.

```
{
    "name": "CompoundRuleExample",
    "type": "compound",
    "statement": "or(and(SeriousPlayers, VeryCloseSkill), and(CasualPlayers, SomewhatCloseSkill))"
}
```

## Latency rule

```
latency
```

Latency rules measure player latency per location. A latency rule ignores any location
with a latency higher than the maximum. A player must have a latency value below the
maximum in at least one location for the latency rule to accept them. You can use this
rule type with large matches by specifying the `maxLatency` property.

**Latency rule properties**

- **`maxLatency`** – The maximum
  acceptable latency value for a location. If a ticket has no locations with
  latency under the maximum, then the ticket doesn't match the latency
  rule.
- **`maxDistance`** – The maximum
  value between the latency of each ticket and the distance reference
  value.
- **`distanceReference`** – The
  latency value to compare ticket latency with. Tickets within the maximum
  distance of the distance reference value result in a successful match. Valid
  options include the minimum (`min`) and average (`avg`)
  player latency values.
- **`partyAggregation`** – The
  value that determines how FlexMatch handles tickets with multiple players
  (parties). Valid options include the minimum (`min`), maximum
  (`max`), and average (`avg`) values for a ticket's
  players. The default is `avg`.

###### Note

A queue can place a game session in a Region that doesn't match a latency rule.
For more information about latency policies for queues, see [Create a player latency policy](../developerguide/queues-design.md#queues-design-latency "../developerguide/queues-design.md#queues-design-latency").

## Absolute sort rule

```
absoluteSort
```

Absolute sort rules sort a batch of matchmaking tickets based on a specified player
attribute compared to the first ticket added to the batch.

**Absolute sort rule properties**

- **`sortDirection`** – The order
  to sort the matchmaking tickets in. Valid options include `ascending`
  and `descending`.
- **`sortAttribute`** – The
  player attribute to sort tickets by.
- **`mapKey`** – The options to
  sort the player attribute if it's a map. Valid options include:
  - `minValue` – The key with the lowest value is
    first.
  - `maxValue` – The key with the highest value is
    first.

- **`partyAggregation`** – The
  value that determines how FlexMatch handles tickets with multiple players
  (parties). Valid options include the minimum (`min`) player
  attribute, the maximum (`max`) player attribute, and the average
  (`avg`) of all player attributes for players in the party. The
  default is `avg`.

Example

The following example rule sorts players by skill level and averages the skill
level of parties.

```
{
    "name":"AbsoluteSortExample",
    "type":"absoluteSort",
    "sortDirection":"ascending",
    "sortAttribute":"skill",
    "partyAggregation":"avg"
}
```

## Distance sort rule

```
distanceSort
```

Distance sort rules sort a batch of matchmaking tickets based on the distance of a
specified player attribute from the first ticket added to the batch.

**Distance sort rule properties**

- **`sortDirection`** – The
  direction to sort matchmaking tickets. Valid options include
  `ascending` and `descending`.
- **`sortAttribute`** – The
  player attribute to sort tickets by.
- **`mapKey`** – The options to
  sort the player attribute if it's a map. Valid options include:
  - `minValue` – For the first ticket added to the
    batch, find the key with the lowest value.
  - `maxValue` – For the first ticket added to the
    batch, find the key with the highest value.

- **`partyAggregation`** – The
  value that determines how FlexMatch handles tickets with multiple players
  (parties). Valid options include the minimum (`min`), maximum
  (`max`), and average (`avg`) values for a ticket's
  players. The default is `avg`.
