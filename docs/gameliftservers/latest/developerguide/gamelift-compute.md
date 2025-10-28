# Choose compute resources for a managed fleet

To deploy your game servers and host game sessions in the cloud, Amazon GameLift Servers provides
managed fleets that use [Amazon Elastic Compute Cloud (Amazon EC2) resources](../../../AWSEC2/latest/UserGuide/Instances.md "../../../AWSEC2/latest/UserGuide/Instances.md") called
_instances_. Use the following topics to help decide what type of EC2
instances you want to use for your managed hosting solution and how to configure them to run
your game server software.

###### Note

If you plan to use hosting resources that you own, either on-premises hardware or
other cloud-based hosting, consider options for hybrid hosting with Amazon GameLift Servers Anywhere. See
[Setting up a hosting fleet with Amazon GameLift Servers](fleets-intro.md "fleets-intro.md").

###### Topics

- [Fleet location](#gamelift-compute-location "#gamelift-compute-location")
- [On-Demand Instances versus Spot
  Instances](#gamelift-compute-spot "#gamelift-compute-spot")
- [Operating systems](#gamelift-compute-os "#gamelift-compute-os")
- [Instance types](#gamelift-compute-instance "#gamelift-compute-instance")
- [Service quotas](#gamelift-service-limits "#gamelift-service-limits")

## Fleet location

Consider the geographic locations where you plan to deploy your game servers. Instance
type availability varies by AWS Region and Local Zone.

For multi-location fleets, instance availability and quotas depend on a combination of
the fleet's home Region and selected remote locations. For more information about fleet
locations, see [Amazon GameLift Servers service locations](gamelift-regions.md "gamelift-regions.md").

Consider using [UDP ping beacons](reference-udp-ping-beacons.md "reference-udp-ping-beacons.md") to collect network latency data
in various geographical locations to anticipate the latency between player devices and
potential fleet locations. These special endpoints accept UDP messages instead of
traditional ICMP pings, providing accurate latency measurements to help you select
optimal fleet locations.

For Amazon GameLift Servers Anywhere fleets, you determine the location of your physical
hardware. For more information about custom locations, see [Locations for Amazon GameLift Servers Anywhere](gamelift-regions.md#gamelift-regions-anywhere "gamelift-regions.md#gamelift-regions-anywhere").

## On-Demand Instances versus Spot

Instances

Amazon EC2 On-Demand Instances and Spot Instances offer the same hardware and performance,
but they differ in availability and cost.

###### On-Demand Instances

You can acquire an On-Demand Instance when you need it, and keep it for as long as
you want. On-Demand Instances have a fixed cost, meaning you pay for the amount of
time that you use them, and there are no long-term commitments.

###### Spot Instances

Spot Instances can offer a cost-efficient alternative to On-Demand Instances by
utilizing unused AWS computing capacity. Spot Instance prices fluctuate based on
the supply and demand for each instance type in each location. AWS can interrupt
Spot Instances whenever it needs the capacity back. Amazon GameLift Servers uses queues and the FleetIQ
algorithm to determine that AWS is going to interrupt a Spot Instance, it puts the
instance in a recycling state. Then, when there are no active game sessions on the
instance, Amazon GameLift Servers tries to replace it.

For more information about how to use Spot Instances, see [Design a queue for Spot Instances](spot-tasks.md "spot-tasks.md").

## Operating systems

Amazon GameLift Servers instances support game server builds that run on Microsoft Windows or Amazon Linux. When
you upload a game build to Amazon GameLift Servers, specify the operating system for the game. When you
create an Amazon EC2 fleet to deploy the game build, Amazon GameLift Servers automatically sets up instances
with the build's operating system. For more information about supported game server
operating systems, see [Get Amazon GameLift Servers development tools](gamelift-supported.md "gamelift-supported.md").

When using a Amazon GameLift Servers Anywhere fleet, you can use any operating system that
your hardware supports. Amazon GameLift Servers Anywhere fleets require you to deploy your game build to
the hardware while using Amazon GameLift Servers to manage your resources in one place.

## Instance types

An Amazon EC2 fleet's instance type determines the kind of hardware that the instances use.
Different instance types offer different combinations of computing power, memory,
storage, and networking capabilities.

When choosing from available instance types for your game, consider:

- The compute architecture of your game server: x64 or Arm (AWS Graviton).

###### Note

Graviton Arm instances require an Amazon GameLift Servers server build on Linux OS.
Server SDK 5.1.1 or newer is required for C++ and C#.
Server SDK 5.0 or newer is required for Go.
These instances provide no out-of-the-box support for Mono installation on Amazon Linux 2023 (AL2023) or Amazon Linux 2 (AL2).

- The computing, memory, and storage requirements of your game server build.
- The number of server processes that you plan to run per instance.

By using a larger instance type, you may be able to run multiple server processes on
each instance. This can reduce the number of instances required to meet player demand.

For more information:

- About instance types, see [Amazon EC2 Instance
  Types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/").
- About running multiple processes per instance, see [Manage how Amazon GameLift Servers launches game servers](fleets-multiprocess.md "fleets-multiprocess.md").

## Service quotas

To see the default service quotas for Amazon GameLift Servers, and the current quotas for your
AWS account, do the following:

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
