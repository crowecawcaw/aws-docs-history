# Customize match algorithm

for large matches

Add an algorithm component to the rule set, if one doesn't already exist. Set the
following properties.

- `strategy` (required) – Set the `strategy`
  property to “balanced”. This setting triggers FlexMatch to do additional
  post-match checks to find the optimal team balance based on a specified
  player attribute, which is defined in the `balancedAttribute`
  property. The balanced strategy replaces the need for custom rules to build
  evenly matched teams.
- `balancedAttribute` (required) – Identify a player
  attribute to use when balancing the teams in a match. This attribute must
  have a numerical data type (double or integer). For example, if you choose
  to balance on player skill, FlexMatch tries to assign players so that all teams
  have aggregate skill levels that are as evenly matched as possible. The
  balancing attribute must be declared in the rule set's player attributes.
- `batchingPreference` (optional) – Choose how much
  emphasis you want to put on forming the lowest latency matches possible for
  your players. This setting affects how match tickets are sorted prior to
  building matches. Options include:

      + Largest population. FlexMatch allows matches using all tickets in the
       pool that have acceptable latency values in at least one location in
       common. As a result, the potential ticket pool tends to be large,
       which makes it easier to fill matches more quickly. Players might be
       placed in games with acceptable, but not always optimal, latency. If
       the `batchingPreference` property isn't set, this is the
       default behavior when `strategy` is set to
       "balanced".
      + Fastest location. FlexMatch pre-sorts all tickets in the pool based on
       where they report the lowest latency values. As a result, matches
       tend to be formed with players that report low latency in the same
       locations. At the same time, the potential ticket pool for each match
       is smaller, which can increase the time needed to fill a match. In
       addition, because a higher priority is placed on latency, players in
       matches may vary more widely with regard to the balancing
       attribute.

  The following example configures the match algorithm to behave as follows: (1)
  Pre-sort the ticket pool to group tickets by location where they have acceptable
  latency values; (2) Form batches of sorted tickets for matching; (3) Create matches
  with tickets in a batch and balance the teams to even out the average player
  skill.

```
"algorithm": {
    "strategy": "balanced",
    "balancedAttribute": "player_skill",
    "batchingPreference": "largestPopulation"
},
```
