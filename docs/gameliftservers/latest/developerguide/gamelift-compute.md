# Choose compute resources for a managed fleet

For Amazon GameLift Servers managed hosting, including managed EC2 and managed containers, the service
deploys your game servers to fleets of computing resources in the AWS Cloud. When you
create a managed fleet, you want to configure the hosting resources to best suit your game.
This topic discusses key decision points when choosing and configuring your game hosting
fleets.

###### Note

If you're building a hybrid solution with both Anywhere and Amazon GameLift Servers managed fleets, use these topics to
design managed fleets to supplement your own self-managed resources. See
[Deploy hosting fleets for Amazon GameLift Servers](fleets-intro.md "fleets-intro.md").

###### Topics

- [Geographic locations](#gamelift-compute-location "#gamelift-compute-location")
- [Operating systems](#gamelift-compute-os "#gamelift-compute-os")
- [Instance types](#gamelift-compute-instance "#gamelift-compute-instance")
- [On-Demand Instances versus Spot
  Instances](#gamelift-compute-spot "#gamelift-compute-spot")
- [Service quotas](#gamelift-service-limits "#gamelift-service-limits")

## Geographic locations

Consider where you plan to deploy your game servers. In general, you want to put your
game servers as close as possible to your players to deliver the best possible player
experience. For Amazon GameLift Servers managed hosting, you can choose to put game servers in any of
the supported AWS Regions and Local Zones. If you're building a hybrid solution, consider
how managed fleet deployment can supplement the locations of your self-managed
Amazon GameLift Servers Anywhere fleets.

For most development and testing scenarios, deploying to a single location makes
sense. As you prepare for launch and beyond, there are many reasons to deploy across
multiple geographic locations. These include supporting a widespread group of players
and improving overall game hosting resilience and reliability. Multiple locations can
also boost player experience by speeding up game session placement and enabling more
choices when optimizing placements for latency and cost.

For a list of locations that are supported by Amazon GameLift Servers and more information about
locations for all fleet types, see [Amazon GameLift Servers service locations](gamelift-regions.md "gamelift-regions.md").

Multi-location fleets

A single managed fleet can deploy resources to multiple locations. You can manually
set capacity for each individual location in a multi-location fleet.

Advantages of using a multi-location fleet:

- Simplified fleet deployment and management – You supply the game server
  software and fleet configuration, and Amazon GameLift Servers deploys it to fleet instances
  across multiple locations (build once, deploy anywhere). In a production fleet,
  you can view and manage all locations in a fleet instead of having to manage
  multiple fleets each located in a different region.
- Local Zone availability – If you want to use a Local Zone you must create a
  multi-location fleet with an AWS Region home location and Local Zones as remote
  locations. Local Zones are extensions of AWS Regions that can deliver even lower
  latency to areas and customers that need it. You can add a Local Zone to any
  multi-location fleet; you don't need to include the Local Zone's parent AWS Region.
- Compatibility with game session queues – You can build game session
  placement queues with one or more multi-location fleets. This approach gives the
  queue flexibility when prioritizing and choosing locations to host a new game
  session.
- Efficient resource utilization – With auto-scaling turned on, Amazon GameLift Servers
  can better optimize capacity scaling across all locations in a fleet.

Tips for using multi-location fleets:

- Check for quotas on the number of locations per AWS Region or fleet. See
  [Amazon GameLift Servers service quotas](../../../general/latest/gr/gamelift.md#limits_gamelift "../../../general/latest/gr/gamelift.md#limits_gamelift").
- Not all instance types are available in all locations. Depending on your
  chosen locations, you might have limited instance type options. The Amazon GameLift Servers
  console provides useful tools to help you find the right balance of locations
  and instance types.
- Consider using [UDP ping beacons](reference-udp-ping-beacons.md "reference-udp-ping-beacons.md") to collect player latency
  data for all your fleet locations. Amazon GameLift Servers can use this data to optimize game
  sessions for low latency and prevent players from joining sessions with
  unacceptably high latency. These special endpoints accept UDP messages instead
  of traditional ICMP pings, providing accurate latency measurements to help you
  select optimal fleet locations.

## Operating systems

All instances in a managed fleet are deployed with an Amazon machine image (AMI) that
provides a complete runtime environment for your game server software. For managed EC2
fleets, you specify the game server build's operating system when you upload the build
to Amazon GameLift Servers. For managed container fleets, you specify the operating system in the
container group definition. For more information about the latest AMI versions, see
[Amazon GameLift Servers AMI versions](reference-ec2-ami-version-history.md "reference-ec2-ami-version-history.md").

AMI versions are regularly updated. When you create a new fleet, Amazon GameLift Servers assigns the
latest available version of the AMI you selected for your game build. All instances that
are deployed in that fleet use the same version. To keep your AMI version up to date
with the latest security and software updates, you need to regularly replace your
fleets. As a best practice, we recommend replacing your managed fleets every 30 days to
maintain the runtime environment for your game servers. For guidance, see [Security best practices for Amazon GameLift Servers](security-best-practices.md "security-best-practices.md").

## Instance types

A managed fleet's instance type determines the kind of hardware that is deployed for
all fleet instances, and instance types are generally available in various sizes. All
Amazon GameLift Servers managed fleet use Amazon EC2 instances, and support a wide range of instance types that
offer different combinations of computing power, memory, storage, and networking
capabilities. The availability of instance types varies depending on the locations you
choose.

The Amazon GameLift Servers console provides useful tools to help you find the right instance types for
your game build and your deployment locations. For managed container fleets, the console
also offers guidance on your game's CPU power and memory requirements.

When choosing from available instance types for your game, consider:

- The compute architecture of your game server: x64 or Arm (AWS Graviton).

###### Note

Graviton Arm instances require a server build for a Linux AMI.
Server SDK 5.1.1 or newer is required for C++ and C#. Server SDK 5.0 or newer is required for Go.
These instances do not provide out-of-the-box support for Mono installation on Amazon Linux 2023 (AL2023) or Amazon Linux 2 (AL2).

- The computing, memory, and storage requirements of your game server build.
- The size of your instance type. In addition to meeting the requirements of
  your game server software executables, larger instance type sizes can run
  multiple game server processes and/or containers on each instance. Factors to
  consider include cost (is it cheaper to run a few large instances or many small
  instances). Also consider how game session capacity might be impacted by adding
  or removing instances during fleet scaling events or when shutting down
  unhealthy instances. If each instance runs many game server processes
  concurrently, adding or removing an instance can significantly affect ame
  hosting capacity.

For more information about instance types, see [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/").

## On-Demand Instances versus Spot

Instances

Amazon EC2 On-Demand Instances and Spot Instances offer the same hardware and performance,
but they differ in availability and cost.

###### On-Demand Instances

You can acquire an On-Demand Instance when you need it and keep it for as long as
you want. On-Demand Instances have a fixed cost, meaning you pay only for the amount
of time that you use them. There are no long-term commitments.

###### Spot Instances

Spot Instances can offer a cost-efficient alternative to On-Demand Instances by
utilizing unused AWS computing capacity. Spot Instance prices fluctuate based on
the supply and demand for each instance type in each location. AWS can reclaim
Spot Instances with a two-minute notification whenever it needs the capacity back,
and game sessions actively running on a reclaimed instance are interrupted.

Amazon GameLift Servers offers several tools to help mitigate the likelihood of Spot interruptions
to your game sessions. A spot viability algorithm tracks instance type historical data
to anticipate when the risk of interruption reaches a critical point and avoids placing
new game sessions on Spot Instances of that type. If an interruption does occur, your
game servers can use the notification to gracefully end a game session for
players.

Game hosting with Spot fleets must use a queue for game session placement. A queue is
able to prioritize game session placements based on Spot fleet viability, cost, and
other factors. See these topics for more information about how to take advantage of Spot
for your game server hosting:

- [Reduce game hosting costs with Spot fleets](fleets-spot.md "fleets-spot.md")
- [Build a queue for Spot Instances](spot-tasks.md "spot-tasks.md")

## Service quotas

You can view default service quotas for Amazon GameLift Servers and current quota status for your
AWS account using the following tools:

- For general service quota information for Amazon GameLift Servers, see [Amazon GameLift Servers
  endpoints and quotas](../../../general/latest/gr/gamelift.md "../../../general/latest/gr/gamelift.md") in the
  _AWS General Reference_.
- For a list of available instance types per location for your account, open the
  [Service quotas](https://console.aws.amazon.com/gamelift/service-quotas "https://console.aws.amazon.com/gamelift/service-quotas")
  page of the Amazon GameLift Servers console. This page also displays your account's current usage
  for each instance type in each location.
- For a list of your account's current quotas for instance types per Region, run
  the AWS Command Line Interface (AWS CLI) command [`describe-ec2-instance-limits`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-ec2-instance-limits.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-ec2-instance-limits.html"). This command returns
  the number of active instances that you have in your default Region (or in
  another Region that you specify).

As you prepare to launch you game, fill out a launch questionnaire in the
[Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/ "https://console.aws.amazon.com/gamelift/"). The Amazon GameLift Servers team uses the launch questionnaire to determine the correct
quotas and limits for your game.
