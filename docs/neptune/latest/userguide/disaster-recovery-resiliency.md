# Building resilient and disaster-tolerant Amazon Neptune deployments

The AWS global infrastructure is built around AWS Regions and Availability
Zones. AWS Regions provide multiple physically separated and isolated
Availability Zones, which are connected with low-latency, high-throughput,
and highly redundant networking. With Availability Zones, you can design and
operate applications and databases that automatically fail over between
Availability Zones without interruption. Availability Zones are more highly
available, fault tolerant, and scalable than traditional single or multiple
data center infrastructures.

An Amazon Neptune DB cluster can only be created in an Amazon VPC that has at
least two subnets in at least two Availability Zones. By distributing your
cluster instances across at least two Availability Zones, Neptune helps ensure
that there are instances available in your DB cluster in the unlikely event
of an Availability Zone failure. The cluster volume for your Neptune DB
cluster always spans three Availability Zones to provide durable storage
with less possibility of data loss.

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").
