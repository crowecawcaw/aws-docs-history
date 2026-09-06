

# Couchbase on AWS Local Zones for Low Latency Edge Use Case
<a name="couchbase-local-zones"></a>

Publication date: **December 25, 2021 ([Diagram history](#diagram-history))**

This architecture shows how to deploy Couchbase Server and Couchbase Sync Gateway on AWS Local Zones for a low latency edge use case. It extends [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) from the parent region into multiple AWS Local Zones.

## Couchbase on AWS Local Zones architecture
<a name="diagram1"></a>

![Architecture diagram showing Couchbase Server and Sync Gateway deployment on AWS Local Zones with replication to the parent region.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/couchbase-local-zones/images/couchbase-local-zones.png)


The following components describe this architecture:

1. Amazon VPC extends from the parent region into multiple AWS Local Zones.

1. Couchbase metrics and logs route to [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) for centralized log management and alerts.

1. [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) uses geolocation-based routing to route clients to the nearest AWS Local Zone or the parent Region.

1. Couchbase Server backups store directly to an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket.

1. Couchbase Server multi-Availability Zone deployment provides high availability and automatic failover. Couchbase Server in the private subnet connects to the internet using NAT Gateway.

1. A bastion host in the public subnet provides access to Couchbase Server from an external network.

1. VPC endpoints enable private connections between VPC and AWS services without requiring access over the internet.

1. Couchbase Sync Gateway multi-Availability Zone deployment with Application Load Balancer provides high availability and automatic failover.

1. An edge cluster consisting of Couchbase Server and Couchbase Sync Gateway deploys on an AWS Local Zone.

1. Inter-Sync Gateway Replication between the Couchbase cluster in the parent region and the edge cluster in the AWS Local Zone uses private IP addresses within the VPC.

1. Couchbase Lite clients such as mobile, desktop, and embedded devices run an embedded NoSQL database and provide low latency data sync with the edge cluster Sync Gateway over the internet.

## Further reading
<a name="further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | December 25, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.