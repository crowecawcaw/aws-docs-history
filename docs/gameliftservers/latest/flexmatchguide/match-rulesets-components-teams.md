# Define match teams

Describe the structure and size of the teams for a match. Each match must have at
least one team, and you can define as many teams as you want. Your teams can have the
same number of players or be asymmetric. For example, you might define a single-player
monster team and a hunters team with 10 players.

FlexMatch processes match requests as either small match or large match, based on how the
rule set defines team sizes. Potential matches of up to 40 players are small matches,
matches with more than 40 players are large matches. To determine a rule set's potential
match size, add up the _maxPlayer_ settings for all
teams defined in the rule set.

- _name_ (required) – Assign each team a
  unique name. You use this name in rules and expansions, and FlexMatch references
  for the matchmaking data in a game session.
- _maxPlayers_ (required) – Specify the
  maximum number of players to assign to the team.
- _minPlayers_ (required) – Specify the
  minimum number of players to assign to the team.
- _quantity_ (optional) – Specify the
  number of team to make with this definition. When FlexMatch creates a match, it
  gives these teams the provided name with an appended number. For example
  `Red-Team1`, `Red-Team2`, and `Red-Team3`.
  FlexMatch attempts to fill teams to the maximum player size but does create teams with
  fewer players. If you want all teams in the match to be equally sized, you can create a
  rule for that. See the [FlexMatch rule set examples](match-examples.md "match-examples.md")
  topic for an example of an `EqualTeamSizes` rule.
