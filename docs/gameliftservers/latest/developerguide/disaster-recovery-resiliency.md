# Resilience in Amazon GameLift Servers

If you're using Amazon GameLift Servers FleetIQ as a standalone feature with Amazon EC2, see [Security in Amazon EC2](../../../AWSEC2/latest/UserGuide/ec2-security.md "../../../AWSEC2/latest/UserGuide/ec2-security.md") in the
_Amazon EC2 User Guide_.

The AWS global infrastructure is built around AWS Regions and
Availability Zones. AWS Regions provide multiple physically separated and isolated
Availability Zones, which are connected with low-latency, high-throughput, and highly
redundant networking. With Availability Zones, you can design and operate applications and
databases that automatically fail over between zones without interruption. Availability
Zones are more highly available, fault tolerant, and scalable than traditional single or
multiple data center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS global
infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

In addition to the AWS global infrastructure, Amazon GameLift Servers offers the following features to
help support your data resiliency needs:

- **Multi-region queues** – Amazon GameLift Servers game session
  queues are used to place new game sessions with available hosting resources. Queues
  that span multiple Regions are able to redirect game session placements in the event
  of a regional outage. For more information and best practices on creating game
  session queues, see [Customize a game session queue](queues-design.md "queues-design.md").
- **Automatic capacity scaling** – Maintain the
  health and availability of your hosting resources by using Amazon GameLift Servers scaling tools.
  These tools provide a range of options that let you adjust fleet capacity to fit the
  needs of your game and players. For more information on scaling, see [Scaling game hosting capacity with Amazon GameLift Servers](fleets-manage-capacity.md "fleets-manage-capacity.md").
- **Distribution across instances** – Amazon GameLift Servers
  distributes incoming traffic across multiple instances, depending on fleet size. As
  a best practice, games in production should have multiple instances to maintain
  availability in case an instance becomes unhealthy or unresponsive.
- **Amazon S3 storage** – Game server builds and
  scripts that are uploaded to Amazon GameLift Servers are stored in Amazon S3 using the Standard storage
  class, which uses multiple data center replications to increase resilience. Game
  session logs are also stored in Amazon S3 using the Standard storage class.
