# Customize a game session queue

This topic describes how to customize your game session queues to make the best possible
decisions about game session placement. For more information about game session queues and
how they work, see [Managing game session placement with Amazon GameLift Servers queues](queues-intro.md "queues-intro.md").

These Amazon GameLift Servers features require queues:

- [Matchmaking with FlexMatch](../flexmatchguide/match-tasks.md "../flexmatchguide/match-tasks.md")
- [Design a queue for Spot Instances](spot-tasks.md "spot-tasks.md")

###### Topics

- [Best practices for Amazon GameLift Servers game session queues](#queues-best-practices "#queues-best-practices")
- [Define a queue's scope](queues-design-scope.md "queues-design-scope.md")
- [Build a multi-location queue](queues-design-multiregion.md "queues-design-multiregion.md")
- [Prioritize game session placement](queues-design-priority.md "queues-design-priority.md")
- [Evaluate queue metrics](queues-design-metrics.md "queues-design-metrics.md")
- [Design a queue for Spot Instances](spot-tasks.md "spot-tasks.md")

## Best practices for Amazon GameLift Servers game session queues

A game session queue contains a list of fleets where Amazon GameLift Servers can place new game sessions.
Each fleet can have hosting resources deployed in multiple geographic locations. When choosing a
placement, the queue selects a fleet and a fleet location based on a set of priorities
that you set for the fleet.

Consider the following guidelines and best practices:

- **Add fleets in locations that cover your
  players.** You can add fleets and aliases in any available
  location. Location is important if you're making placements based on reported
  player latency.
- **Use aliases for all fleets.** Assign an alias
  to each fleet in a queue, and use the alias names when setting destinations in
  your queue.
- **Use the same or a similar game build or script for all
  fleets.** The queue might put players into game sessions on any
  fleet in the queue. Players must be able to play in any game session on any
  fleet.
- **Create fleets in at least two locations.** By
  having game servers hosted in at least one other location, you mitigate the
  impact of Regional outages on your players. You can keep your backup fleets
  scaled down, and use auto scaling to increase capacity if usage
  increases.
- **Prioritize your game session placement.** A
  queue prioritizes placement choices based on several elements, including
  destination list order.
- **Create your queue in the same location as your client
  service.** By putting your queue in a location near your client
  service, you can minimize communication latency.
- **Use fleets with multiple locations.** Use the
  queue filter configuration to prevent the queue from placing game sessions in
  specified locations. You can use at least two multi-location fleets with
  different home locations to mitigate the impact of game placements during a
  Regional outage.
- **Use the same TLS certificate setting for all
  fleets.** Game clients that connect to game sessions in your fleets
  must have compatible communication protocols.
