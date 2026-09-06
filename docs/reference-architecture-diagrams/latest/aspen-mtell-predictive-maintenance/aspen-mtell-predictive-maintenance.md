

# Predictive Maintenance on AWS using Aspen Mtell
<a name="aspen-mtell-predictive-maintenance"></a>

Publication date: **January 26, 2023 ([Diagram history](#amp-diagram-history))**

With this architecture, you can deploy AI and ML-powered predictive maintenance by using Aspen Mtell with [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/) or [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/). This solution provides early warnings of equipment failure from your assets, control automation systems, and historians. The architecture uses [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/), [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/), and [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/).

## Aspen Mtell predictive maintenance architecture diagram
<a name="amp-diagram"></a>

![Architecture diagram for predictive maintenance on AWS using Aspen Mtell.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/aspen-mtell-predictive-maintenance/images/aspen-mtell-predictive-maintenance-ra.png)


The following steps describe the architecture:

1. Aspen Connect connects data sources from your assets, automation systems, and historians into Aspen MES Collaborative through Direct Connect or Site-to-Site VPN.

1. Distribute data through Elastic Load Balancing (ELB) to Amazon EC2 instances running the Athena Historian Adapter across two Availability Zones.

1. In each Availability Zone, Aspen IP.21 Enterprise runs on Amazon EC2 instances in a private subnet to aggregate and manage data.

1. The Aspen Mtell Application Server persists data in SQL Server on Amazon EC2.

1. The Historian Adapter fetches data from remote historians. The EAM Adapter connects to EAM applications on premises or in the cloud.

1. A bastion host in the public subnet connects to private subnet instances for troubleshooting.

1. Aspen Mtell View runs on Amazon EC2 in an Auto Scaling group.

1. End users connect to Mtell View through a web browser. ELB behind an internet gateway directs traffic.

1. Aspen Cloud Connect delivers asset model and operational technology (OT) data to Amazon S3 for data lakes.

1. A CloudFormation template provides deployment of Aspen Mtell.

For more information about Aspen Mtell, see [Aspen Mtell product page](https://www.aspentech.com/en/products/apm/aspen-mtell) on the AspenTech website.

## Further reading
<a name="amp-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="amp-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#amp-diagram-history) | Reference architecture diagram first published. | January 26, 2023 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.