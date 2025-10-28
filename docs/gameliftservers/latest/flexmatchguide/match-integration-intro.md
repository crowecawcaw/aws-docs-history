# Preparing your game for FlexMatch

Use Amazon GameLift Servers FlexMatch to add player matchmaking functionality to your games. You can use FlexMatch
with a managed Amazon GameLift Servers hosting solution or as a standalone service with another hosting
solution. If you want to add FlexMatch to an Amazon GameLift Servers FleetIQ solution, use it as a standalone service.
For more information on how FlexMatch works, see [How Amazon GameLift Servers FlexMatch works](gamelift-match.md "gamelift-match.md").

Matchmaking solutions require the following work:

- Create a matchmaker with your custom matchmaking rules For more on creating the
  matchmaker, see [Buiding a Amazon GameLift Servers FlexMatch matchmaker](matchmaker-build.md "matchmaker-build.md").
- Update your game client to allow players to request a match.
- For games that use Amazon GameLift Servers hosting, update your game server to manage match data and
  optionally backfill empty slots on matches.
  The topics in this section cover how to add matchmaking support to your game clients and
  game servers.

See the roadmap for your preferred FlexMatch matchmaking solution:

- [Roadmap: Add matchmaking to a Amazon GameLift Servers hosting solution](match-tasks.md "match-tasks.md")
- [Roadmap: Create a standalone matchmaking solution with FlexMatch](match-tasks-safm.md "match-tasks-safm.md")
