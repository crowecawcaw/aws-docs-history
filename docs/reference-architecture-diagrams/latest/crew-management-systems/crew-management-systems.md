

# Architecture for Airline Crew Management Systems
<a name="crew-management-systems"></a>

Publication date: **June 11, 2021 ([Diagram history](#crew-systems-history))**

You can use AWS to create a highly available, secure, flexible, and cost-effective architecture for airline crew management systems. This architecture connects corporate users to crew applications through multiple networking options.

This architecture uses [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/) for container orchestration. It stores crew data in [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/) and provides business intelligence through [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html).

## Airline crew management systems diagram
<a name="crew-systems-diagram"></a>

![Architecture for airline crew management using Amazon Elastic Kubernetes Service, Amazon Aurora, and Amazon Quick Sight.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/crew-management-systems/images/crew-management-systems-aws-ra.png)


The following steps describe the architecture:

1. Connect corporate users and systems to crew management on AWS. Use [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/) as primary and AWS Site-to-Site VPN as secondary.

1. [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/) provides user authentication and access control to crew applications.

1. Crew apps resolve domain names through [Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/) to [API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) and [CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/). API Gateway provides access to the application tier. CloudFront serves static pages and assets from [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/). [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/) protects these resources.

1. The application tier has a private Application Load Balancer for crew management microservices. Connect the Application Load Balancer to an [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/) cluster across two Availability Zones.

1. [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/) PostgreSQL-Compatible Edition provides high availability with Aurora Replicas. Store data copies across multiple Availability Zones.

1. Use AWS cloud security services for at-rest, end-to-end encryption. Protect credentials and private keys.

1. Use [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/) and monitoring tools to optimize operational health.

1. Create a data lake with Amazon S3 and Amazon S3 Glacier for crew management data. Use the data lake for reporting, visualization, and advanced analytics.

1. Use [Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) for business intelligence on crew planning, training statistics, and crew utilization.

## Further reading
<a name="crew-systems-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="crew-systems-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#crew-systems-history) | Reference architecture diagram first published. | June 11, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.