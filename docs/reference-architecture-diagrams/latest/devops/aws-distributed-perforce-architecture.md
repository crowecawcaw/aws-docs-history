

# Distributed Perforce architecture on AWS

Publication date: **November 23, 2021 ([Diagram history](diagram-history.md))**

With this architecture, you can deploy a hybrid multi-Region Perforce Helix Core architecture on AWS.

## Distributed Perforce architecture on AWS diagram
<a name="aws-distributed-perforce-architecture-diagram"></a>

![Hybrid, multi-Region Perforce Helix Core deployment on AWS with commit and edge servers in private subnets.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/devops/images/aws-distributed-perforce-architecture.png)


The following steps describe the architecture:

1. Connect the corporate data center edge server to the AWS primary Region by using [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/) or AWS Site-to-Site VPN. Choose based on bandwidth and connection stability needs. Connect remote users by using AWS Client VPN or virtual workstations on AWS.

1. AWS Transit Gateway connects VPCs and on-premises networks through a central hub-and-spoke model. It simplifies complex peering relationships and encrypts data in transit.

1. If your depot is less than 16 TB, run Perforce on Amazon EBS gp3 volumes. For depots larger than 16 TB, store the Perforce depot in Amazon Elastic File System. Use Amazon EFS Standard-Infrequent Access for cost optimization.

1. [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/) handles Amazon EFS backups. If you run Perforce on Amazon EBS only, Amazon EBS snapshots are the standard backup mechanism.

1. Edge Server high availability is not required, depending on recovery point objective and recovery time objective. Restoring from an Amazon EBS snapshot is a slower but more cost-effective solution.

1. Use a NAT gateway so that instances in a private subnet can connect to services outside your VPC. External services cannot initiate a connection with those instances.

1. Perforce commit-edge architecture offers the best overall performance with most commands running locally. The primary and replica/high availability servers run in separate Availability Zones for further high availability.

## Further reading
<a name="aws-distributed-perforce-architecture-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS Direct Connect product page](https://aws.amazon.com/directconnect/)
+ [AWS Game Tech product page](https://aws.amazon.com/gametech/)