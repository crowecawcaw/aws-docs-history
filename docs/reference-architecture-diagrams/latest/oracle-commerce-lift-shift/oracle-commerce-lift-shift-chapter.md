# Oracle Commerce Lift-and-Shift to AWS

## Overview

Legacy ecommerce websites face cost, elasticity, availability, and scalability challenges
on-premises. You can use a lift-and-shift migration to move Oracle Commerce to
AWS as a first step toward modernization. This approach gives you unlimited resources to
scale your ecommerce website as needed.

This architecture deploys Oracle Commerce in a single AWS Region with
multiple Availability Zones. It provides resilience, high availability, and improved
performance for your production workload.

Publication date: May 14, 2021

![Oracle Commerce deployed in a single AWS Region and Amazon VPC across multiple Availability Zones, with Amazon CloudFront, Amazon Route 53, Elastic Load Balancing, AWS WAF, Oracle Commerce clusters, Oracle RAC databases, Amazon ElastiCache for Redis, and Amazon EFS.](images/oracle-commerce-lift-shift.png)

**Download:** [Architecture diagram (PDF)](samples/oracle-commerce-lift-shift.zip.md "samples/oracle-commerce-lift-shift.zip.md")

## Architecture

The following steps describe the architecture:

1. You deploy in a single Region and single Virtual Private Cloud (Amazon VPC). This mirrors
   an on-premises data center configuration.
2. You use multiple Availability Zones to provide resilience and high availability for
   the production workload.
3. An AWS Partner solution runs the production workload on Oracle
   RAC.
4. Elastic Load Balancing (ELB) distributes network traffic across multiple Availability
   Zones. This improves the scalability and availability of your applications.
5. [Amazon CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide.md "../../../AmazonCloudFront/latest/DeveloperGuide.md")
   provides a secure and programmable content delivery network (CDN).
6. [AWS WAF](../../../waf/latest/developerguide.md "../../../waf/latest/developerguide.md") protects the
   ecommerce website against common web exploits.
7. [Amazon Route 53](../../../Route53/latest/DeveloperGuide.md "../../../Route53/latest/DeveloperGuide.md")
   provides Domain Name System (DNS) configuration.
8. [Amazon ElastiCache](../../../AmazonElastiCache/latest/red-ug.md "../../../AmazonElastiCache/latest/red-ug.md") for
   Redis provides the caching mechanism for performance.
9. [Amazon EFS](../../../efs/latest/ug.md "../../../efs/latest/ug.md") provides shared file
   storage. It is mounted to every Oracle Commerce instance.
10. [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md")
    provides application logging, monitoring, and alarms.

## Further reading

For additional information, see the following resources:

- [Three Steps for Modernizing Your DTC Ecommerce Website](https://aws.amazon.com/blogs/industries/three-steps-for-modernizing-your-dtc-ecommerce-website/ "https://aws.amazon.com/blogs/industries/three-steps-for-modernizing-your-dtc-ecommerce-website/")
- [Running Oracle RAC on Amazon EC2 using
  FlashGrid](https://www.flashgrid.io/oracle-rac-on-aws/ "https://www.flashgrid.io/oracle-rac-on-aws/")

## Diagram history

To receive updates about this reference architecture diagram, subscribe to the RSS
feed.

| Change              | Description                                     | Date         |
| ------------------- | ----------------------------------------------- | ------------ |
| Initial publication | Reference architecture diagram first published. | May 14, 2021 |

###### RSS subscription requirement

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you
are using.
