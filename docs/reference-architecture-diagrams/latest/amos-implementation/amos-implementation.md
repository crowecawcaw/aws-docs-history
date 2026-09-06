

# AMOS Implementation on AWS
<a name="amos-implementation"></a>

Publication date: **April 19, 2022 ([Diagram history](#amos-implementation-history))**

This reference architecture shows how airlines can implement the Aircraft Maintenance and Engineering Operating System (AMOS) on AWS. Airlines use this architecture to achieve high availability, resiliency, and cost efficiency for Maintenance, Repair, and Overhaul (MRO) workloads. AMOS is an MRO management system that airlines and maintenance organizations use for aircraft maintenance operations.

Airlines that run AMOS on-premises often face challenges with hardware refresh cycles, limited disaster recovery options, and high total cost of ownership (TCO). This architecture provides a resilient deployment of AMOS across multiple Availability Zones with managed services for monitoring, patch management, and secure remote access.

## AMOS implementation diagram
<a name="amos-implementation-diagram"></a>

![Architecture for Amazon Elastic Compute Cloud deployment of AMOS with multi-AZ failover.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/amos-implementation/images/aws-reference-architecture-migration-airlines-amos-ra.png)


The following steps describe the architecture:

1. Create an [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/) to host [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) instances. Deploy production application and database instances to one Availability Zone. Deploy failover instances to another Availability Zone.

1. AMOS supports SAP Adaptive Server Enterprise (ASE), Oracle Database Standard Edition (SE) and Enterprise Edition (EE), and PostgreSQL. Use native replication tools for cross-AZ database replication.

1. AMOS is not designed for load-balanced environments. Replicate with a standby Amazon EC2 instance through the AMOS native solution. On failover, remap the primary Elastic Network Interface to the standby instance.

1. Deploy Amazon AppStream 2.0 for HTML5 browser access. Use AWS Directory Service for user authentication. Use [Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/) for DNS translation.

1. When direct connection to AMOS is required, connect through a secure channel. Use AWS Client VPN with [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/).

1. Use [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) for AMOS application binaries, database devices, web drivers, and backups.

1. Use [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/) for server and ecosystem monitoring.

1. Use [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/) for Amazon EC2 operating system patch management.

## Further reading
<a name="amos-implementation-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="amos-implementation-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#amos-implementation-history) | Reference architecture diagram first published. | April 19, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.