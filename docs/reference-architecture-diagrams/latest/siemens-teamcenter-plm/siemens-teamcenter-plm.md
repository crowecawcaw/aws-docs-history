

# Siemens Teamcenter Product Lifecycle Management on AWS
<a name="siemens-teamcenter-plm"></a>

Publication date: **March 8, 2024 ([Diagram history](#stp-diagram-history))**

With this architecture, you can deploy Siemens Teamcenter on AWS for high availability with Siemens Active Workspace and visualization. This solution uses [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/), [Amazon Relational Database Service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/), [Amazon Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/), [Amazon Elastic Block Store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/), [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/), and [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/).

## Siemens Teamcenter PLM architecture diagram
<a name="stp-diagram"></a>

![Architecture diagram for Siemens Teamcenter product lifecycle management on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/siemens-teamcenter-plm/images/siemens-teamcenter-ra.png)


The following steps describe the architecture:

1. End users connect to Teamcenter through HTTPS over the internet.

1. Application Load Balancer directs traffic to the Teamcenter Web tier on Amazon EC2.

1. Requests forward to the Teamcenter Enterprise Tier, which interacts with other servers and databases.

1. Teamcenter uses Amazon RDS for Oracle or Microsoft SQL Server on Amazon EC2 for structured product lifecycle management (PLM) data.

1. Teamcenter File Management System stores and retrieves files from Amazon EBS, Amazon EFS, or Amazon FSx for NetApp ONTAP.

1. Additional services include Active Workspace, Apache Solr, and Deployment Center.

1. Siemens license server instances deploy across three Availability Zones for high availability.

1. Data center users access environments through Direct Connect, VPN, or HTTPS.

1. IT teams connect through VPN for RDP, [Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/), or AWS Systems Manager access.

1. [AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/) on AWS or on premises provides admin authentication.

1. A monitoring server on Amazon EC2 monitors systems, networks, and infrastructure.

## Further reading
<a name="stp-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="stp-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#stp-diagram-history) | Reference architecture diagram first published. | March 8, 2024 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.