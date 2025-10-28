# Define a queue's scope

Your game's player population might have groups of players who shouldn't play
together. For example, if you publish your game in two languages each language should
have it's own game servers.

To set up game session placement for your player population, create a separate queue
for each player segment. Scope each queue to place players into the correct game
servers. Some common ways to scope queues include:

- **By geographic locations.** When deploying your
  game servers in multiple geographic areas, you might build queues for players in
  each location to reduce player latency.
- **By build or script variations.** If you have
  more than one variation of your game server, you might be supporting player
  groups that can't play in the same game sessions. For example, game server
  builds or scripts might support different languages or device types.
- **By event types.** You might create a special
  queue to manage games for participants in tournaments or other special events.

## Design multiple queues

Depending on your game and players, you might want to create more than one game
session queue. When your game client service requests a new game session, it specifies
which game session queue to use. To help you determine whether to use multiple queues,
consider:

- Variations of your game server. You can create a separate queue for each
  variation of your game server. All fleets in a queue must deploy compatible game
  servers. This is because players who use the queue to join games must be able to
  play on any of the queue's game servers.
- Different player groups. You can customize how Amazon GameLift Servers places game sessions
  based on player group. For example, you might need queues customized for certain
  game modes that require a special instance type or runtime configuration. Or,
  you might want a special queue to manage placements for a tournament or other
  event.
- Game session queue metrics. You can set up queues based on how you want to
  collect game session placement metrics. For more information, see [Amazon GameLift Servers metrics for queues](monitoring-cloudwatch.md#gamelift-metrics-queue "monitoring-cloudwatch.md#gamelift-metrics-queue").
