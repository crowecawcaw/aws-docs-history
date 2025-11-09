# Deploy hosting fleets for Amazon GameLift Servers

Deploying hosting resources involves creating and configuring the compute infrastructure that will run your game servers. Amazon GameLift Servers offers several fleet types to match different hosting needs, from fully managed AWS Cloud resources to hybrid solutions that combine cloud and on-premises infrastructure.

Choose the fleet type that best fits your requirements for cost, control, scalability, and geographic distribution. You can also combine multiple fleet types in a single hosting solution to optimize for different scenarios or player populations.

## Fleet characteristics

An Amazon GameLift Servers fleet is a collection of computing resources that run your game servers and
host game sessions for players. Fleets can vary in the type of compute resources you use
and how the fleet is managed. A fleet's size—the number of game sessions and
players that it can support—depends on the number of compute resources that you
give it. All Amazon GameLift Servers fleets have the following characteristics:

- The game server processes that run on all fleets are integrated with the
  server SDK for Amazon GameLift Serversand communicate with the Amazon GameLift Servers service in the same way. Game servers
  report their availability to host game sessions and players, respond to prompts
  to start or stop game sessions, and other interactions.
- Amazon GameLift Servers handles game session placement for all fleets in the same way. Amazon GameLift Servers keeps
  track of a fleet's game server status and chooses from available game servers to
  host a new game session. This process is used whether your game places game
  sessions on a single fleet or uses a [game session
  queue](queues-intro.md "queues-intro.md") to balance hosting across multiple fleets. With a queue, you
  can also customize placement decisions to consider factors such as resource cost
  and latency.
- All fleets support the use of a FlexMatch matchmaker in collaboration with a game
  session placement queue. The Amazon GameLift Servers service receives player match requests, forms
  the matches, and passes them to the game session queue to find available game
  servers.
- Amazon GameLift Servers collects a wide range of fleet metrics. These include status metrics for computes and
  server processes, as well as usage metrics for game sessions and player activity.
  See the complete list of available metrics at [Monitor Amazon GameLift Servers with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

###### Topics

- [Decision guide: Choose a hosting option](fleets-decision-guide.md "fleets-decision-guide.md")
- [Amazon GameLift Servers managed EC2 fleets](fleets-intro-managed.md "fleets-intro-managed.md")
- [Amazon GameLift Servers managed container fleets](fleets-intro-containers.md "fleets-intro-containers.md")
- [Amazon GameLift Servers Anywhere fleets](fleets-intro-anywhere.md "fleets-intro-anywhere.md")
- [Build a hybrid hosting solution](hybrid-solution-guide.md "hybrid-solution-guide.md")
