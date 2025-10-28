# Customize the match

algorithm

FlexMatch optimizes the default algorithm for most games to get players into acceptable
matches with minimal wait time. You can customize the algorithm and adjust matchmaking
for your game.

The following is the default FlexMatch matchmaking algorithm:

1. FlexMatch places all open matchmaking tickets and backfill tickets in a ticket
   pool.
2. FlexMatch randomly groups tickets in the pool into one or more batches. As the
   ticket pool gets larger, FlexMatch forms additional batches to maintain optimal
   batch size.
3. FlexMatch sorts the tickets by age, within each batch.
4. FlexMatch builds a match based on the oldest ticket of each batch.
   To customize the match algorithm, add an `algorithm` component to your rule
   set schema. See [FlexMatch rule set schema](match-ruleset-schema.md "match-ruleset-schema.md") for the complete reference information.

Use the following optional customizations to impact different stages of your
matchmaking process.

- [Add pre-batch
  sorting](#match-rulesets-components-algorithm-presort "#match-rulesets-components-algorithm-presort")
- [Form batches based on batchDistance attributes](match-rules-reference-ruletype.md#match-rules-reference-ruletype-batchdistance "match-rules-reference-ruletype.md#match-rules-reference-ruletype-batchdistance")
- [Prioritize backfill
  tickets](#match-rulesets-components-algorithm-backfill "#match-rulesets-components-algorithm-backfill")
- [Favor older tickets
  with expansions](#match-rulesets-components-algorithm-expansion "#match-rulesets-components-algorithm-expansion")

## Add pre-batch

sorting

You can sort the ticket pool before forming batches. This type of customization is
most effective with games with large tickets pools. Pre-batch sorting can help speed
up the matchmaking process and increase player uniformity in defined
characteristics.

Define Pre-batch sorting methods using the algorithm property
`batchingPreference`. The default setting is
`random`.

Options for customizing pre-batch sorting include:

- **Sort by player attributes.** Provide a list
  of player attributes to pre-sort the ticket pool.

To sort by player attributes, set `batchingPreference` to
`sorted`, and define your list of player attributes in
`sortByAttributes`. To use an attribute, first declare the
attribute in the `playerAttributes` component of the rule set.

In the following example, FlexMatch sorts the ticket pool based on players'
preferred game map and then by player skill. The resulting batches are more
likely to contain similarly skilled players who want to use the same
map.

```
"algorithm": {
    "batchingPreference": "sorted",
    "sortByAttributes": ["map", "player_skill"],
    "strategy": "exhaustiveSearch"
},
```

- **Sort by latency.** Create matches with the
  lowest available latency or quickly create matches with acceptable latency.
  This customization is useful for rule sets forming large matches of more
  than 40 players.

Set the algorithm property `strategy` to `balanced`.
The balanced strategy limits the available types of rule statements. For
more information, see [Design a FlexMatch large-match rule
set](match-design-rulesets-large.md "match-design-rulesets-large.md").

FlexMatch sorts tickets based on players' reported latency data in one of the
following ways:

    + *Lowest latency locations.* The ticket pool is
     pre-sorted by the locations where players report their lowest
     latency values. FlexMatch then batches tickets with low latency in the
     same locations, creating a better game play experience. It also
     reduces the number of tickets in each batch, so matchmaking can take
     longer. To use this customization, set
     `batchingPreference` to `fastestRegion`,
     as shown in the following example.



    ```
    "algorithm": {
        "batchingPreference": "fastestRegion",
        "strategy": "balanced"
    },
    ```
    + *Acceptable latency matches quickly.* The
     ticket pool is pre-sorted by locations where players report
     acceptable latency value. This forms fewer batches containing more
     tickets. With more tickets in each batch, finding acceptable matches
     is faster. To use this customization, set the property
     `batchingPreference` to`largestPopulation`, as shown in the following
     example.



    ```
    "algorithm": {
        "batchingPreference": "largestPopulation",
        "strategy": "balanced"
    },
    ```

###### Note

The default value for the balanced strategy is
`largestPopulation`.

## Prioritize backfill

tickets

If your game implements auto-backfill or manual backfill, you can customize how
FlexMatch processes matchmaking tickets based on request type. The request type can be
a new match or backfill request. By default, FlexMatch treats both types of requests
the same.

Backfill prioritization impacts how FlexMatch handles tickets after it batches them.
Backfill prioritization requires rule sets to use the exhaustive search strategy.

FlexMatch doesn't match multiple backfill tickets together.

To change prioritization for backfill tickets, set the property
`backfillPriority`.

- **Match backfill tickets first.** This option
  tries to match backfill tickets before creating new matches. This means that
  incoming players have a higher chance of joining an existing game.

It's best to use this if your game uses auto-backfill. Auto-backfill is
often used in games with short game sessions and high player turnaround.
Auto-backfill helps these games form minimum viable matches and get them
started while FlexMatch searches for more players to fill open slots.

Set the `backfillPriority` to `high`.

```
"algorithm": {
    "backfillPriority": "high",
    "strategy": "exhaustiveSearch"
},
```

- **Match backfill tickets last.** This option
  ignores backfill tickets until it evaluates all other tickets. This means
  that FlexMatch backfills incoming players into existing games when it can't
  match them into new games.

This option is useful when you want to use backfill as a last-chance
option to get players into a game, such as when there aren't enough players
to form a new match.

Set `backfillPriority` to `low`.

```
"algorithm": {
    "backfillPriority": "low",
    "strategy": "exhaustiveSearch"
},
```

## Favor older tickets

with expansions

Expansion rules relax match criteria when matches are difficult to complete. Amazon GameLift Servers
applies expansion rules when tickets in a partially completed match reach a certain
age. The creation timestamps of the tickets determine when Amazon GameLift Servers applies the rules;
by default, FlexMatch tracks the timestamp of the most recently matched ticket.

To change when FlexMatch applies expansion rules, set the property
`expansionAgeSelection` as follows:

- **Expand based on newest tickets.** This
  option applies expansion rules based on the newest ticket added to the
  potential match. Each time FlexMatch matches a new ticket, the time clock is
  reset. With this option, resulting matches tend to be higher quality but
  take longer to match; match requests might time out before completing if
  they take too long to match. Set `expansionAgeSelection` to
  `newest`. `newest` is default.
- **Expand based on oldest tickets.** This
  option applies expansion rules based on the oldest ticket in the potential
  match. With this option, FlexMatch applies expansions faster, which improves
  wait times for the earliest matched players, but lowers the match quality
  for all players. Set `expansionAgeSelection` to
  `oldest`.

```
"algorithm": {
    "expansionAgeSelection": "oldest",
    "strategy": "exhaustiveSearch"
},
```
