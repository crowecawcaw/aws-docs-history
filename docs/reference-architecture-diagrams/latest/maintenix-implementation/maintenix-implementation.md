

# IFS Maintenix Software Implementation on AWS
<a name="maintenix-implementation"></a>

Publication date: **March 24, 2022 ([Diagram history](#maintenix-history))**

You can use AWS to create a highly available, secure, flexible, and cost-effective architecture to host [IFS Maintenix Aviation Maintenance Management Software](https://www.ifs.com/en/products/aviation-maintenance). This architecture connects on-premises systems to AWS with multiple networking options.

This architecture deploys IFS Maintenix software servers across two Availability Zones. It uses [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/) for the database tier and [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/) for data replication to your data warehouse.

## IFS Maintenix implementation diagram
<a name="maintenix-diagram"></a>

![Architecture for IFS Maintenix on AWS using Amazon Elastic Compute Cloud, Amazon RDS, and AWS Transit Gateway.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/maintenix-implementation/images/maintenix-migration-airlines-ra.png)


The following steps describe the architecture:

1. Connect on-premises routers securely with high availability to a [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/). Use [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/), AWS Site-to-Site VPN, and [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/).

1. Deploy Maintenix software servers into [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) instances across two Availability Zones with Auto Scaling groups.

1. Deploy an Oracle database by using [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/) configured with Multi-AZ for high availability with a failover standby instance.

1. Turn on Change Data Capture (CDC) with [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/). Push changes to your data warehouse for analytical processing.

1. Provide access to the application tier for corporate-network users. Route requests through a private Application Load Balancer through AWS Transit Gateway into the Amazon EC2 Auto Scaling group.

1. Allow internet-connected users to access the application tier through a public Application Load Balancer. Use [Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/) for domain name resolution. Protect the Application Load Balancer with [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/).

1. Configure the Integration and Reporting tiers for internal access only. Make them accessible from the application tier Auto Scaling group and from on-premises through private Application Load Balancers.

## Further reading
<a name="maintenix-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="maintenix-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#maintenix-history) | Reference architecture diagram first published. | March 24, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.