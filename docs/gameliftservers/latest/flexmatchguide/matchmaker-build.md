# Buiding a Amazon GameLift Servers FlexMatch matchmaker

This section describes the key elements of a matchmaker and how to
create and customize one for your game. This includes setting up a matchmaking configuration
and a matchmaking rule set.

Creating your matchmaker is the first step in the FlexMatch roadmaps:

- [Roadmap: Add matchmaking to a Amazon GameLift Servers hosting solution](match-tasks.md "match-tasks.md")
- [Roadmap: Create a standalone matchmaking solution with FlexMatch](match-tasks-safm.md "match-tasks-safm.md")
  A FlexMatch matchmaker does the work of building a game match. It manages the pool of
  matchmaking requests received, processes and selects players to
  find the best possible player groups, and forms teams for a match. For games that use Amazon GameLift Servers for hosting,
  it also places and starts a game session for the match.

FlexMatch pairs the matchmaking service with a customizable rules engine. This lets you
design how to match players together based on player attributes and game modes that make
sense for your game, and rely on FlexMatch to manage the nuts and bolts of forming player
groups and placing them into games. See more details about custom matchmaking in [FlexMatch rule set examples](match-examples.md "match-examples.md").

After forming a match, FlexMatch provides the match data for game session placement.
For games that use Amazon GameLift Servers for hosting, FlexMatch sends a game session placement request with matched
players to the a game session queue. The queue searches for available hosting resources on
your Amazon GameLift Servers fleets and starts a new game session for the match. For games that use another hosting
solution, FlexMatch provides the match data for you to provide to your own game session placement component.

For a detailed description of how a FlexMatch matchmaker processes the matchmaking requests
it receives, see [FlexMatch matchmaking process](gamelift-match-howitworks.md "gamelift-match-howitworks.md").

###### Topics

- [Design a FlexMatch matchmaker](match-configuration.md "match-configuration.md")
- [Build a FlexMatch rule set](match-rulesets.md "match-rulesets.md")
- [Create a matchmaking configuration](match-create-configuration.md "match-create-configuration.md")
- [Set up FlexMatch event notifications](match-notification.md "match-notification.md")
