# Design a queue for Spot Instances

You can take advantage of significant savings in hosting costs by using Spot fleets. For
more details, see [On-Demand Instances versus Spot
Instances](gamelift-compute.md#gamelift-compute-spot "gamelift-compute.md#gamelift-compute-spot"). To add Spot
fleets to your hosting solution, you need to configure a game session queue with a
combination of Spot fleets and On-Demand fleets. Amazon GameLift Servers uses a queue during the game
session placement process to search across multiple fleets and find the best available hosts
for new game sessions. This topic provides guidance on how to start using Spot
fleets.

Are you using FlexMatch for matchmaking? You can use the following steps to add Spot fleets
to your existing game session queues for matchmaking placements.

1. **Determine the destinations for your game session
   queue.**

Managing game session placement with a queue is best practice, and it's required
when using Spot Instances. Because Spot Instances might not always be available when
you need them, you need to design a resilient queue that includes both Spot fleets
and On-Demand fleets to offer backup capacity. You can keep your On-Demand fleets
scaled down until they're needed. To design your queue, consider the
following:

    * Locations – If possible, your Spot fleets and On-Demand fleets
     should be in the same Region as the players. Position both Spot resources
     and On-Demand resources in each location that you want to support.
     Multi-location fleets support both Spot and On-Demand instances.
    * Instance types – Consider your game server's hardware requirements
     and availability of instances in the locations you choose.

To try a queue that optimizes Spot availability and resiliency, see [Tutorial: Create an Amazon GameLift Servers queue with Spot Instances](tutorial-queues-spot.md "tutorial-queues-spot.md"). For Spot
design best practices, see [Best practices for Amazon GameLift Servers game session queues](queues-design.md#queues-best-practices "queues-design.md#queues-best-practices"). 2. **Create the fleets for your Spot-optimized queue.**

Based on your queue design, create fleets to deploy your game servers to your
desired locations and instance types. See [Create an Amazon GameLift Servers managed EC2 fleet](fleets-creating.md "fleets-creating.md") for help creating and configuring new
fleets. 3. **Create your game session queue.**

Add the fleet destinations, configure the game session placement process, and
define placement priorities. See [Create a game session queue](queues-creating.md "queues-creating.md") for help creating and configuring the new
queue. 4. **Update your game client service to use the
queue.**

When your game client uses a queue to request resources, the queue avoids
resources with a high chance of interruption and selects the location that matches
your defined priorities. For help implementing game session placements in your game
client, see [Create game sessions](gamelift-sdk-client-api.md#gamelift-sdk-client-api-create "gamelift-sdk-client-api.md#gamelift-sdk-client-api-create"). 5. **Update your game server to handle a Spot
interruption.**

AWS can interrupt Spot Instances with a 2 minute notification, when it needs the
capacity back. Set up your game server to handle interruption to minimize player
impact.

Before AWS reclaims a Spot Instance, it sends a termination notification. Amazon GameLift Servers
passes the notification to all affected server processes by invoking the Amazon GameLift Servers
Server SDK callback function `onProcessTerminate()`. Implement this
callback to end the game session or move the game session and players to a new
instance. See [Respond to a server process shutdown
notification](gamelift-sdk-server-api.md#gamelift-sdk-server-terminate "gamelift-sdk-server-api.md#gamelift-sdk-server-terminate") for help implementing
`onProcessTerminate()`.

###### Note

AWS makes every effort to provide the notification before it reclaims an
instance, but it's possible that AWS reclaims the Spot Instance before the
warning arrives. Prepare your game server to handle unexpected
interruptions. 6. **Review the performance of your Spot fleets and
queues.**

View Amazon GameLift Servers metrics in the Amazon GameLift Servers console or with Amazon CloudWatch to review performance.
For more information about Amazon GameLift Servers metrics, see [Monitor Amazon GameLift Servers with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md"). Key metrics include:

    * Interruption rate – Use the `InstanceInterruptions` and
     `GameSessionInterruptions` metrics to track the number and
     frequency of Spot-related interruptions for instances and game sessions.
     Game sessions that are reclaimed by AWS have a status of
     `TERMINATED` and a status reason of
     `INTERRUPTED`.
    * Queue effectiveness – Track placement success rates, average wait
     time, and queue depth to confirm that Spot fleets don't impact your queue
     performance.
    * Fleet usage – Monitor data on instances, game sessions and player
     sessions. Usage for your On-Demand fleets can be an indicator that queues
     are avoiding placements into your Spot fleets to avoid disruption.

## Best practices for queues with Spot fleets

If your queue includes Spot fleets, set up a resilient queue. This takes advantage of
cost savings with Spot fleets while minimizing the effect of game session interruptions.
For help with correctly building fleets and game session queues for use with Spot
fleets, see [Tutorial: Create an Amazon GameLift Servers queue with Spot Instances](tutorial-queues-spot.md "tutorial-queues-spot.md").
For more information about Spot instances, see [Design a queue for Spot Instances](spot-tasks.md "spot-tasks.md").

In addition to the general best practices in the previous section, consider these
Spot-specific best practices:

- **Create at least one On-Demand fleet in each
  location.** On-Demand fleets provide backup game servers for your
  players. You can keep your backup fleets scaled down until they're needed, and
  use auto scaling to increase On-Demand capacity when Spot fleets are
  unavailable.
- **Select different instance types across multiple Spot
  fleets in a location.** If one Spot Instance type becomes
  temporarily unavailable, the interruption affects only one Spot fleet in the
  location. Best practice is to choose widely available instance types, and use
  instance types in the same family (for example, m5.large, m5.xlarge,
  m5.2xlarge). Use the [Amazon GameLift Servers
  console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/") to view historical pricing data for instance types.
