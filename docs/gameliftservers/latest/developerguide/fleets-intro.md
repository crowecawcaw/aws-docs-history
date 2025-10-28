# Setting up a hosting fleet with Amazon GameLift Servers

In this section, you'll find information about designing, building, and maintaining
Amazon GameLift Servers fleets to host your game servers. See [Amazon GameLift Servers hosting options](gamelift-intro-flavors.md#gamelift-intro-flavors-hosting "gamelift-intro-flavors.md#gamelift-intro-flavors-hosting") to learn more about the hosting solutions that Amazon GameLift Servers offers, including those that use
managed EC2 fleets, self-managed Anywhere fleets for your on-premises hardware, and a hybrid
solution that uses both.

###### Topics

- [Fleet characteristics](#fleets-intro-common "#fleets-intro-common")
- [How Amazon GameLift Servers fleet creation works](#fleets-creation-workflow "#fleets-creation-workflow")
- [Amazon GameLift Servers managed EC2 fleets](fleets-intro-managed.md "fleets-intro-managed.md")
- [Amazon GameLift Servers managed container fleets](fleets-intro-containers.md "fleets-intro-containers.md")
- [Amazon GameLift Servers Anywhere fleets](fleets-intro-anywhere.md "fleets-intro-anywhere.md")
- [Abstract an Amazon GameLift Servers fleet designation with an alias](aliases-intro.md "aliases-intro.md")

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

## How Amazon GameLift Servers fleet creation works

When you request a new fleet, Amazon GameLift Servers starts a workflow to create the fleet resource. As
it completes each step of the workflow, Amazon GameLift Servers updates the fleet's status and emits a
series of events to communicate progress toward fleet creation.

Amazon GameLift Servers uses two types of events. Fleet state transition events mark when the fleet
status changes. Fleet creation events provide additional markers to help with debugging
creation issues. You can track all events using the Amazon GameLift Servers console or by calling the
Amazon GameLift Servers API operation [DescribeFleetEvents](../apireference/API_DescribeFleetEvents.md "../apireference/API_DescribeFleetEvents.md"). You can also track fleet and location status using
[DescribeFleetAttributes](../apireference/API_DescribeFleetAttributes.md "../apireference/API_DescribeFleetAttributes.md") or [DescribeFleetLocationAttributes](../apireference/API_DescribeFleetLocationAttributes.md "../apireference/API_DescribeFleetLocationAttributes.md").
