

# AWS Distributed Perforce Architecture
<a name="aws-distributed-perforce-architecture"></a>

Publication date: **November 23, 2021 ([Diagram history](#diagram-history))**

This architecture shows how to deploy a hybrid multi-Region Perforce Helix Core architecture on AWS.

## AWS Distributed Perforce Architecture
<a name="diagram1"></a>

![Architecture diagram showing a distributed Perforce Helix Core deployment on AWS with hybrid and multi-Region connectivity.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/aws-distributed-perforce-architecture/images/aws-distributed-perforce-architecture.png)


1. Connect the corporate data center edge server to the AWS primary Region by using [https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) or AWS Site-to-Site VPN. Choose based on bandwidth and connection stability needs. Connect remote users by using AWS Client VPN or virtual workstations on AWS.

1. AWS Transit Gateway connects VPCs and on-premises networks through a central hub-and-spoke model. It simplifies complex peering relationships and encrypts data in transit.

1. If your depot is less than 16 TB, run Perforce on Amazon EBS GP3 volumes. For depots larger than 16 TB, store the Perforce depot in Amazon Elastic File System. Use Amazon EFS Standard-Infrequent Access for cost optimization.

1. [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) handles Amazon EFS backups. If you run Perforce on Amazon EBS only, EBS snapshots are the standard backup mechanism.

1. Edge Server high availability is not required, depending on recovery point objective and recovery time objective. Restoring from an EBS snapshot is a slower but more cost-effective solution.

1. Use a NAT gateway so that instances in a private subnet can connect to services outside your VPC. External services cannot initiate a connection with those instances.

1. Perforce commit-edge architecture offers the best overall performance with most commands running locally. The primary and replica/high availability servers run in separate Availability Zones for further high availability.

## Further reading
<a name="further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [ product page](https://aws.amazon.com/directconnect/)
+ [AWS Game Tech product page](https://aws.amazon.com/gametech/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | November 23, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.