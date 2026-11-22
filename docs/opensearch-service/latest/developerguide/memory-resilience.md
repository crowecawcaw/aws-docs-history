

# Resilience in Amazon OpenSearch Memory

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between Availability Zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures. 

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

Amazon OpenSearch Memory is a Regional service. It stores the events and memories of each space redundantly across multiple Availability Zones in the Region where you created the space, and it continues to serve requests if an Availability Zone becomes unavailable. You don't configure replication or failover yourself.

OpenSearch Memory doesn't replicate a space to other Regions, and it doesn't provide backups or exports of a space's data. If your application must keep working when a Region is unavailable, keep the events that you send to OpenSearch Memory in your own durable store as well, so that you can create a space in another Region and resend them.