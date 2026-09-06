

# Robotic Processing: Automation and VDI on AWS
<a name="robotic-processing-automation-vdi"></a>

Publication date: **December 7, 2021 ([Diagram history](#rpa-diagram-history))**

With this architecture, you can integrate UiPath for running robotics process automation (RPA) with VMware Cloud on AWS. You use [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/), [Amazon Relational Database Service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/) (Amazon RDS), [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html), and [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/) to support the automation infrastructure.

## Robotic processing automation and VDI architecture diagram
<a name="rpa-diagram"></a>

![Architecture diagram for UiPath robotics automation with VMware Cloud on AWS for virtual desktop infrastructure.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/robotic-processing-automation-vdi/images/robotic-processing-uipath-ra.png)


The following steps describe the architecture:

1. Deploy the Horizon View platform on VMware Cloud on AWS. Connect it with on-premises VMware Horizon in hybrid mode over VPN and [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/).

1. The UiPath database stores process and results queues on Amazon RDS with a read replica in a different Availability Zone.

1. Install UiPath Orchestrator on Amazon EC2 instances. Use load balancing across multiple Availability Zones.

1. Install UiPath robots in VMware Cloud on AWS Horizon virtual desktop infrastructure (VDI).

1. Use Amazon ElastiCache to cache session state and frequent queries for UiPath Orchestrator.

1. Send UiPath Orchestrator logs to Amazon OpenSearch Service for searching and analyzing data.

1. UiPath Orchestrator and robots connect through a cross-VPC elastic network interface (ENI).

1. Users log in to UiPath Orchestrator through VPN or Direct Connect. Requests pass through an Application Load Balancer.

1. (Optional) Use an RD gateway and NAT gateway for secure internet access to UiPath Orchestrator.

1. (Optional) Store UiPath nugget packages in [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/). Use [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/) and [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/) for auditing and monitoring.

## Further reading
<a name="rpa-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="rpa-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#rpa-diagram-history) | Reference architecture diagram first published. | December 7, 2021 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.