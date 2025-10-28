# Design a FlexMatch large-match rule

set

If your rule set creates matches that allow 41 to 200 players, you need to make some
adjustments to your rule set configuration. These adjustments optimize the match
algorithm so that it can build viable large matches while also keeping player wait times
short. As a result, large match rule sets replace time-consuming custom rules with
standard solutions that are optimized for common matchmaking priorities.

Here's how to determine if you need to optimize your rule set for large
matches:

1. For each team defined in your rule set, get the value of _maxPlayer_,
2. Add up all the _maxPlayer_ values. If the
   total exceeds 40, you've got a large match rule set.
   To optimize your rule set for large matches, make the adjustments described as
   follows. See the schema for a large match rule set in [Rule set schema for large matches](match-ruleset-schema-large.md "match-ruleset-schema-large.md")
   and rule set examples in [Example: Create a large match](match-examples-7.md "match-examples-7.md").
