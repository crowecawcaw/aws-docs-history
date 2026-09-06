

# WebSphere Commerce on AWS
<a name="websphere-commerce-on-aws"></a>

Publication date: **May 20, 2021 ([Diagram history](#wcs-history))**

With this architecture, you can lift and shift a legacy WebSphere Commerce (WCS) ecommerce website from on-premises to AWS. On-premises ecommerce platforms often struggle to scale during peak traffic periods. By migrating to AWS, you gain unlimited resources to scale when you need them. You use [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/) for content delivery, [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/) for security, and Elastic Load Balancing for traffic distribution.

For more information, see [Three Steps for Modernizing Your DTC Ecommerce Website](https://aws.amazon.com/blogs/industries/three-steps-for-modernizing-your-dtc-ecommerce-website/) on the AWS Blog.

## WebSphere Commerce diagram
<a name="wcs-diagram"></a>

![WebSphere Commerce deployed in a single AWS Region and Amazon VPC across multiple Availability Zones, with Amazon CloudFront as CDN, AWS WAF for security, Elastic Load Balancing, WebSphere Commerce clusters, and Oracle RAC or IBM Db2 databases.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/websphere-commerce-on-aws/images/websphere-commerce-on-aws.png)


The following steps describe the architecture:

1. A single AWS Region and single [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/) provide similar architecture to an on-premises data center setup.

1. Multiple Availability Zones provide resilience and separate the authoring workload from the live environment.

1. Out-of-the-box WebSphere Commerce clusters provide high availability and instance management through DMGR (deployment manager).

1. Use an AWS Partner solution to run the production workload on Oracle RAC. Alternatively, [create highly available IBM Db2 databases on AWS](https://aws.amazon.com/blogs/database/creating-highly-available-ibm-db2-databases-in-aws/).

1. Elastic Load Balancing distributes network traffic to improve the scalability and availability of your applications across multiple instances.

1. CloudFront provides a highly secure and programmable content delivery network (CDN).

1. AWS WAF protects the ecommerce website against common web exploits.

1. [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/) provides DNS configuration.

## Further reading
<a name="wcs-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="wcs-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#wcs-history) | Reference architecture diagram first published. | May 20, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.