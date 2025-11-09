# Add FlexMatch matchmaking to Amazon GameLift Servers

Use Amazon GameLift Servers FlexMatch to add player matchmaking functionality to your Amazon GameLift Servers hosted games. You
can use FlexMatch with either custom game servers or Amazon GameLift Servers Realtime.

FlexMatch pairs the matchmaking service with a customizable rules engine. You design how to
match players together based on player attributes and game modes that make sense for your
game. FlexMatch manages the nuts and bolts of evaluating players who are looking for a game,
forming matches with one or more teams, and starting game sessions to host the matches.

To use the full FlexMatch service, you must have your hosting resources set up with queues.
Amazon GameLift Servers uses queues to locate the best possible hosting locations for games across multiple
regions and computing types. In particular, Amazon GameLift Servers queues can use latency data, when provided
by game clients, to place game sessions so that players experience the lowest possible
latency when playing.

For more information on FlexMatch including detailed help with integrating matchmaking into
your games, see these [Amazon GameLift Servers FlexMatch Developer Guide](../../../gamelift/latest/flexmatchguide.md "../../../gamelift/latest/flexmatchguide.md")
topics:

- [How Amazon GameLift Servers FlexMatch works](../../../gamelift/latest/flexmatchguide/match-intro.md "../../../gamelift/latest/flexmatchguide/match-intro.md")
- [FlexMatch integration steps](../../../gamelift/latest/flexmatchguide/match-tasks.md "../../../gamelift/latest/flexmatchguide/match-tasks.md")
