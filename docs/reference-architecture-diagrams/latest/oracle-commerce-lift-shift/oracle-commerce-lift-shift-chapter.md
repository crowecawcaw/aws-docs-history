

# Oracle Commerce Lift-and-Shift to AWS
<a name="oracle-commerce-lift-shift-chapter"></a>

## Overview
<a name="oracle-lift-shift-overview"></a>

Legacy ecommerce websites face cost, elasticity, availability, and scalability challenges on-premises. You can use a lift-and-shift migration to move Oracle Commerce to AWS as a first step toward modernization. This approach gives you unlimited resources to scale your ecommerce website as needed.

This architecture deploys Oracle Commerce in a single AWS Region with multiple Availability Zones. It provides resilience, high availability, and improved performance for your production workload.

Publication date: May 14, 2021

![Oracle Commerce deployed in a single AWS Region and Amazon VPC across multiple Availability Zones, with Amazon CloudFront, Amazon Route 53, Elastic Load Balancing, AWS WAF, Oracle Commerce clusters, Oracle RAC databases, Amazon ElastiCache for Redis, and Amazon EFS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/oracle-commerce-lift-shift/images/oracle-commerce-lift-shift.png)


**Download:** [Architecture diagram (PDF)](samples/oracle-commerce-lift-shift.zip)

## Architecture
<a name="oracle-lift-shift-architecture"></a>

The following steps describe the architecture:

1. You deploy in a single Region and single Virtual Private Cloud (Amazon VPC). This mirrors an on-premises data center configuration.

1. You use multiple Availability Zones to provide resilience and high availability for the production workload.

1. An AWS Partner solution runs the production workload on Oracle RAC.

1. Elastic Load Balancing (ELB) distributes network traffic across multiple Availability Zones. This improves the scalability and availability of your applications.

1. [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/) provides a secure and programmable content delivery network (CDN).

1. [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/) protects the ecommerce website against common web exploits.

1. [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/) provides Domain Name System (DNS) configuration.

1. [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/) for Redis provides the caching mechanism for performance.

1. [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/) provides shared file storage. It is mounted to every Oracle Commerce instance.

1. [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/) provides application logging, monitoring, and alarms.

## Further reading
<a name="oracle-lift-shift-resources"></a>

For additional information, see the following resources:
+ [Three Steps for Modernizing Your DTC Ecommerce Website](https://aws.amazon.com/blogs/industries/three-steps-for-modernizing-your-dtc-ecommerce-website/)
+ [Running Oracle RAC on Amazon EC2 using FlashGrid](https://www.flashgrid.io/oracle-rac-on-aws/)

## Diagram history
<a name="oracle-lift-shift-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#oracle-lift-shift-history) | Reference architecture diagram first published. | May 14, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.