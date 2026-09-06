

# PROS Revenue Management Platform on AWS
<a name="pros-revenue-management"></a>

Publication date: **August 20, 2020 ([Diagram history](#pros-revenue-management-history))**

This reference architecture creates a highly available, secure, flexible, and cost-effective architecture on AWS. Use it to host a PROS application with two modules: Origin and Destination (O&D) and Group Revenue Management System (GRMS).

The PROS application manages revenue optimization for airlines. This architecture connects on-premises systems to AWS with redundant network paths. It provides automated failover for compute and database layers.

## PROS revenue management platform diagram
<a name="pros-revenue-management-diagram"></a>

![Architecture for AWS Direct Connect, Amazon S3, Amazon EC2, Amazon RDS, and AWS Key Management Service.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/pros-revenue-management/images/pros-revenue-management-platform-on-aws-ra.png)


The following steps describe the architecture:

1. Connect on-premises users and systems through [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/) as the primary connection. Use AWS Site-to-Site VPN as the secondary connection.

1. Use [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) for PROS applications to exchange files with upstream and downstream systems. Applications generate files after batch jobs and store them for retrieval.

1. The PROS application has an O&D module and a GRMS module. Access both modules only by private IP addresses. Connect Amazon VPCs (production and development) through [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/).

1. The O&D module primary node distributes traffic and jobs to worker nodes. Configure manual failover to a worker node. You can also automate failover through an Auto Scaling group and script integration. For worker node failover, automate with [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/) and [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/).

1. The GRMS module runs in active-passive mode. If the running [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) instance fails, a new instance is provisioned. Automate failover through an Auto Scaling group.

1. Both O&D and GRMS use [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/) for Oracle. Configure single-AZ (recovered from snapshot) or Multi-AZ (standby with failover). Use memory-optimized Amazon EC2 R5 instances for the O&D database.

1. AWS Key Management Service provides data-at-rest encryption at the database layer.

1. CloudWatch monitors the health of Amazon EC2 instances and Amazon RDS databases.

## Further reading
<a name="pros-revenue-management-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="pros-revenue-management-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#pros-revenue-management-history) | Reference architecture diagram first published. | August 20, 2020 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.