

# Architecture of Crew Management System
<a name="crew-management-architecture"></a>

Publication date: **November 29, 2021 ([Diagram history](#crew-arch-history))**

This architecture focuses on Trip Update and Retrieve services. You can use AWS to create a highly available, secure, flexible, and cost-effective architecture for crew management systems.

This architecture extends the [Architecture for Airline Crew Management Systems](../crew-management-systems/crew-management-systems.html). It deploys across multiple Regions for high availability and reduced latency.

## Crew management architecture diagram
<a name="crew-arch-diagram"></a>

![Architecture for crew management using Amazon Elastic Kubernetes Service, Amazon Aurora, and AWS CloudFormation.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/crew-management-architecture/images/architecture_of_crew_management_ra.png)


The following steps describe the architecture:

1. Crew apps resolve domain names through [Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/) to the nearest region and [CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/) distribution. A regional [API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) provides access to read crew trip data. CloudFront serves static pages from [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

1. An [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/) Global Database provides high availability and low latency with Aurora Replicas. With read replica write forwarding, applications send writes to any Aurora Global Database replica.

1. Deploy the application in multiple Regions for high availability and reduced latency. Use [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/) for single-click deployment. Use a fully managed [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/) cluster for Trip Update and Retrieve services. Network Load Balancer routes traffic to Amazon EKS services.

1. Connect corporate users and systems by using [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/). A private API Gateway provides access to crew schedulers for update and read operations.

1. Use [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/) and monitoring tools to optimize operational health.

1. Use AWS cloud security services for at-rest, end-to-end encryption.

## Further reading
<a name="crew-arch-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="crew-arch-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#crew-arch-history) | Reference architecture diagram first published. | November 29, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.