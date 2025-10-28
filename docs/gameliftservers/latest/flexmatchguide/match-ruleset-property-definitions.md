# FlexMatch rule set property

definitions

This section defines each property in the rule set schema. For additional help with
creating a rule set, see [Build a FlexMatch rule set](match-rulesets.md "match-rulesets.md").

**`name`**

A descriptive label for the rule set. This value is not associated with the
name assigned to the Amazon GameLift Servers [MatchmakingRuleSet resource](../../../gamelift/latest/apireference/API_MatchmakingRuleSet.md "../../../gamelift/latest/apireference/API_MatchmakingRuleSet.md"). This value is included in the
matchmaking data describing a completed match, but it not used by any Amazon GameLift Servers
processes.

Allowed values: String

Required? No

**`ruleLanguageVersion`**

The version of the FlexMatch property expression language being used.

Allowed values: "1.0"

Required? Yes

**`playerAttributes`**

A collection of player data that is included in matchmaking requests and is
used in the matchmaking process. You can also declare attributes here to have
the player data included in the matchmaking data that is passed to game servers,
even if the data is not used in the matchmaking process.

Required? No

**`name`**

A unique name for player attribute to be used by matchmaker. This
name must match the player attribute name that is referenced in
matchmaking requests.

Allowed values: String

Required? Yes

**`type`**

The data type of the player attribute value.

Allowed values: "string", "number", "string_list",
"string_number_map"

Required? Yes

**`default`**

A default value to use when a matchmaking request does not provide
one for a player.

Allowed values: Any value allowed for the player attribute.

Required? No

**`algorithm`**

Optional configuration settings to customize the matchmaking process.

Required? No

**`strategy`**

The method to use when building matches. If this property is not
set, the default behavior is "exhaustiveSearch".

Allowed values:

- "exhaustiveSearch" – Standard matching method.
  FlexMatch forms a match around the oldest ticket in a batch by
  evaluating other tickets in the pool based a set of custom
  match rules. This strategy is used for matches of 40 players
  or fewer. When using this strategy,
  `batchingPreference` should be set to either
  "random" or "sorted".
- "balanced" – Method that's optimized to form large
  matches quickly. This strategy is used only for matches of
  41 to 200 players. It forms matches by pre-sorting the
  ticket pool, building potential matches and assigning
  players to teams, and then balancing each team in a match
  using a specified player attribute. For example, this
  strategy can be used to equalize the average skill levels of
  all teams in a match. When using this strategy,
  `balancedAttribute` must be set, and
  `batchingPreference` should be set to either
  "largestPopulation" or "fastestRegion". Most custom rule
  types are not recognized with this strategy.

Required? Yes

**`batchingPreference`**

The pre-sorting method to use before grouping tickets for match
building. Pre-sorting the ticket pool causes tickets to be batched
together based on a specific characteristic, which tends to increase
uniformity across players in the final matches.

Allowed values:

- "random" – Valid only with `strategy` =
  "exhaustiveSearch". No pre-sorting is done; tickets in the
  pool are randomly batched. This is the default behavior for
  an exhaustive search strategy.
- "sorted" – Valid only with `strategy` =
  "exhaustiveSearch". The ticket pool is pre-sorted based on
  the player attributes listed in
  `sortbyAttributes`.
- "largestPopulation" – Valid only with
  `strategy` = "balanced". The ticket pool is
  pre-sorted by regions where players are reporting acceptable
  latency levels. This is the default behavior for a balanced
  strategy.
- "fastestRegion" – Valid only with
  `strategy` = "balanced". The ticket pool is
  pre-sorted by regions where players are reporting their
  lowest latency levels. Resulting matches take longer to
  complete, but latency for all players tends to be
  low.

Required? Yes

**`balancedAttribute`**

The name of a player attribute to use when building large matches
with the balanced strategy.

Allowed values: Any attribute declared in
`playerAttributes` with `type` =
"number".

Required? Yes, if `strategy` = "balanced".

**`sortByAttributes`**

A list of player attributes to use when pre-sorting the ticket
pool prior to batching. This property is only used when pre-sorting
with the exhaustive search strategy. The order of the attribute list
determines sort order. FlexMatch uses standard sorting convention for
alpha and numeric values.

Allowed values: Any attribute declared in
`playerAttributes`.

Required? Yes, if `batchingPreference` =
"sorted".

**`backfillPriority`**

The prioritization method for matching backfill tickets. This
property determines when FlexMatch processes the backfill tickets in a
batch. It is only used when pre-sorting with the exhaustive search
strategy. If this property is not set, the default behavior is
"normal".

Allowed values:

- "normal" – A ticket's request type (backfill or new
  match) is not considered when forming matches.
- "high" – A ticket batch is sorted by request type
  (and then by age), and FlexMatch attempts to match backfill
  tickets first.
- "low" – A ticket batch is sorted by request type
  (and then by age), and FlexMatch attempts to match non-backfill
  tickets first.

Required? No

**`expansionAgeSelection`**

The method for calculating the wait time for a match rule
expansion. Expansions are used to relax match requirements if a
match hasn't been completed after a certain amount of time passes.
Wait time is calculated based on the age of tickets that are already
in the partially filled match. If this property is not set, the
default behavior is "newest".

Allowed values:

- "newest" – Expansion wait time is calculated based
  on the ticket with the most recent creation timestamp in the
  partially completed match. Expansions tend to be triggered
  more slowly, because one newer ticket can restart the wait
  time clock.
- "oldest" – Expansion wait time is calculated based
  on the ticket with the oldest creation timestamp in the
  match. Expansions tend to be triggered more quickly.

Required? No

**`teams`**

The configuration of teams in a match. Provide a team name and size range for
each team. A rule set must define at least one team.

**`name`**

A unique name for the team. Team names can be referred to in rules
and expansions. On a successful match, players are assigned by team
name in the matchmaking data.

Allowed values: String

Required? Yes

**`maxPlayers`**

The maximum number of players that can be assigned to the
team.

Allowed values: Number

Required? Yes

**`minPlayers`**

The minimum number of players that must be assigned to the team
before the match is viable.

Allowed values: Number

Required? Yes

**`quantity`**

The number of teams of this type to create in a match. Teams with
quantities greater than 1 are designated with an appended number
("Red_1", "Red_2", etc.). If this property is not set, the default
value is "1".

Allowed values: Number

Required? No

**`rules`**

A collection of rule statements that define how to evaluate players for a
match.

Required? No

**`name`**

A unique name for the rule. All rules in a rule set must have
unique names. Rule names are referenced in event logs and metrics
that track activity related to the rule.

Allowed values: String

Required? Yes

**`description`**

A text description for the rule. This information can be used to
identify the purpose of a rule. It is not used in the matchmaking
process.

Allowed values: String

Required? No

**`type`**

The type of rule statement. Each rule type has additional
properties that must be set. For more details on the structure and
use of each rule type, see [FlexMatch rule types](match-rules-reference-ruletype.md "match-rules-reference-ruletype.md").

Allowed values:

- "absoluteSort" – Sorts using an explicit sorting
  method that orders tickets in a batch based on whether a
  specified player attribute compares to the oldest ticket in
  the batch.
- "collection" – Evaluates the values in a
  collection, such as a player attribute that's a collection,
  or a set of values for multiple players.
- "comparison" – Compares two values.
- "compound" – Defines a compound matchmaking rule
  using a logical combination of other rules in the rule set.
  Supported only for matches of 40 or fewer players.
- "distance" – Measures the distance between number
  values.
- "batchDistance" – Measures the difference between
  an attribute value and uses it to group match
  requests.
- "distanceSort" – Sorts using an explicit sorting
  method that orders tickets in a batch based on how a
  specified player attribute with a numerical value compares
  to the oldest ticket in the batch.
- "latency" – Evaluates the regional latency data
  that is reported for a matchmaking request.

Required? Yes

**`expansions`**

Rules for relaxing match requirements over time when a match cannot be
completed. Set up expansions as a series of steps that apply gradually in order
to make matches easier to find. By default, FlexMatch calculates wait time based on
the age of the newest ticket added to a match. You can change how expansion wait
times are calculated using the algorithm property
`expansionAgeSelection`.

Expansion wait times are absolute values, so each step should have a wait time
longer than the previous step. For example, to schedule a gradual series of
expansion, you might use wait times of 30 seconds, 40 seconds, and 50 seconds.
Wait times cannot exceed the maximum time allowed for a match request, which is
set in the matchmaking configuration.

Required? No

**`target`**

The rule set element to be relaxed. You can relax team size
properties or any rule statement property. The syntax is
"<component name>[<rule/team name>].<property name>". For
example, to change team minimum sizes: `teams[Red,
 Yellow].minPlayers`. To change the minimum skill
requirement in a comparison rule statement named "minSkill":
`rules[minSkill].referenceValue`.

Required? Yes

**`steps`**

**`waitTimeSeconds`**

The length of time, in seconds, to wait before
applying the new value for the target rule set element.

Required? Yes

**`value`**

The new value for the target rule set element.
