# Configure game session placement

Game session placement is the process of finding available game servers to host new game sessions. Amazon GameLift Servers uses game session queues to intelligently place game sessions across your fleets, taking into account factors like player latency, fleet capacity, and cost optimization.

A well-configured game session queue ensures that players are connected to the best available game server, providing optimal performance while making efficient use of your hosting resources. Queues can span multiple fleets and AWS Regions to provide global coverage and redundancy.

A game session queue is the primary mechanism that Amazon GameLift Servers uses to search for available game servers
and choose them to host new game sessions. Queues offers a far more efficient way to process large numbers
of game session requests and find placements for them across multiple fleets of hosting resources.
If your hosting solution uses more than one fleet, and you're processing high volumes of requests,
you probably need a queue.

When your game wants to start a new game session for players, it sends a placement request
to the Amazon GameLift Servers service, which funnels it to the queue. The queue's configuration determines
when and how the requests are processed. When processing a placement request, Amazon GameLift Servers searches
a set of fleets for a game server to host the game session. Placement succeeds when Amazon GameLift Servers
finds an available game server and prompts it to start a game session.

###### Topics

- [Queue characteristics](#queues-intro-characteristics "#queues-intro-characteristics")
- [Best practices for Amazon GameLift Servers game session queues](#queues-best-practices "#queues-best-practices")
- [Create a game session queue](queues-creating.md "queues-creating.md")
- [Set up event notification for game session
  placement](queue-notification.md "queue-notification.md")

## Queue characteristics

An Amazon GameLift Servers game session queue is an AWS cloud resource. You can create a queue in any
AWS Region that Amazon GameLift Servers supports (see [Amazon GameLift Servers service locations](gamelift-regions.md "gamelift-regions.md")). Game session placement requests are sent to
that location and processed there.

Automating game session placement with queues offers significant benefits for both game
developers and players. These include:

- **Queues deliver the "best possible" placement.**
  When processing game session placement requests, a queue uses the Amazon GameLift Servers FleetIQ
  algorithm to prioritize placements based on a set of defined preferences,
  including cost, location, and player latency.
- **Queues support Spot fleets to help reduce game hosting
  costs.** You can configure your queues with AWS Spot fleets,
  which often offer significantly lower hosting costs, as well as On-Demand
  fleets. Because low cost is one of the key criteria for placements, queues can
  always take advantage of differences in cost.
- **Queues can place new games faster during high
  demand.** By configuring a queue with multiple fleets, you're
  providing more flexible options for game session placement. But additional
  fleets also provide backup capacity as needed when demand increases. For any
  placement request, if Amazon GameLift Servers can't place a game session in the most preferred
  location, it automatically moves on to evaluate other locations.
- **Queues can make game server availability more
  resilient.** Outages can happen. With a multi-fleet queue, a
  slowdown or outage doesn't have to affect player access to your game. By
  configuring your queue with fleets that have capacity in different AWS Regions and availability zones,
  you can help make sure that players can always find a game session to join.
- **Get metrics on game session placements and queue
  performance.** Amazon GameLift Servers emits queue metrics, including statistics on
  placement successes and failures, the number of requests in the queue, and
  average time that requests spend in the queue. You can view these metrics in the
  Amazon GameLift Servers console or in CloudWatch.

To get started by creating a basic starter queue, see [Create a game session queue](queues-creating.md "queues-creating.md").

###### Topics

- [Best practices for Amazon GameLift Servers game session queues](#queues-best-practices "#queues-best-practices")
- [Create a game session queue](queues-creating.md "queues-creating.md")
- [Set up event notification for game session
  placement](queue-notification.md "queue-notification.md")

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
