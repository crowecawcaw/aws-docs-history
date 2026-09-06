

# Microservices-based Headless DTC Website with Infosys Equinox on AWS
<a name="dtc-website-infosys-equinox"></a>

Publication date: **2021 ([Diagram history](#dtc-history))**

With this architecture, you can build a microservices-based headless direct-to-consumer (DTC) website. Headless applications let brand owners loosely couple brand websites with a unified commerce engine that is extensible and durable. Infosys is an AWS partner with a DTC platform, [Infosys Equinox](https://www.infosys.com/about/alliances/amazon.html), running on AWS to provide comprehensive capabilities across the commerce lifecycle.

## Architecture diagram
<a name="dtc-diagram"></a>

![DTC website architecture with Amazon CloudFront, AWS WAF, Amazon EKS, and Infosys Equinox unified commerce on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/dtc-website-infosys-equinox/images/microservice-dtc-with-skava-on-AWS-ra.png)


The following steps describe the architecture:

1. [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/) provides a highly secure, programmable content delivery network (CDN).

1. [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/) is the web application firewall that protects the ecommerce website against common web exploits.

1. [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/) provides domain name service (DNS) configuration.

1. Lambda@Edge improves performance for dynamic content processing.

1. [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) stores static content (HTML, image, video).

1. Consumer packaged goods (CPG) brand websites are implemented with your choice of technologies by using [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), AWS AppSync, or applications running on [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/).

1. Infosys Equinox Unified Commerce is built with [Spring Boot](https://spring.io/projects/spring-boot), [Hibernate](https://hibernate.org/), and [Hystrix](https://github.com/Netflix/Hystrix) running on [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/). It provides essential DTC features for high availability and scalability.

1. An analytics and management layer provides ad hoc reporting, monitoring, security, and data protection.

1. Fulfillment partner integration handles order picking, packing, and shipping.

1. Your choice of a dedicated connection ([AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/)) or AWS Site-to-Site VPN secures data in transit.

1. Business users and existing business intelligence (BI) and ERP systems on the corporate network handle day-to-day activities.

## Further reading
<a name="dtc-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="dtc-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#dtc-history) | Reference architecture diagram first published. | January 1, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.