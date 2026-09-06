

# Digital River for CPG, B2B, and DTC on AWS
<a name="digital-river-cpg"></a>

Publication date: **March 28, 2022 ([Diagram history](#dr-history))**

With this architecture, consumer packaged goods (CPG) companies manage all online commerce activities. As CPG companies move to various sales channels domestically and worldwide, they need robust solutions to reduce friction in ecommerce operations. Digital River provides an all-in-one solution that runs on AWS for order-to-cash processes.

## Digital River commerce platform diagram
<a name="dr-diagram"></a>

![Store devices and mobile apps connecting through AWS edge services to a headless ecommerce layer, integrated with Digital River SaaS on Amazon Elastic Container Service.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/digital-river-cpg/images/digital-river-cpg.png)


The following steps describe the architecture:

1. Use [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/) for faster content delivery. Static content is served through CloudFront. Lambda@Edge provides edge computing for dynamic content. Shield and AWS WAF provide website security.

1. Choose either [https://docs.aws.amazon.com/directconnect/latest/UserGuide/](https://docs.aws.amazon.com/directconnect/latest/UserGuide/) or AWS Site-to-Site VPN for data security in transit.

1. Build the business-to-business (B2B) or direct-to-consumer (DTC) ecommerce website frontend by using AWS services such as [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/appsync/latest/devguide/), [management portal](https://docs.aws.amazon.com/amplify/latest/userguide/), and Lambda. Serve the frontend through AWS edge locations.

1. Create the headless ecommerce application and data layer with [API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/), Lambda, [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/), and [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/). This shared microservices layer interacts with storefronts, fulfillment partners, and Digital River.

1. The Digital River multi-tenant SaaS layer provides core commerce functionality. It runs on AWS services such as Amazon Relational Database Service, [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/), Elastic Load Balancing, [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/), and [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/).

1. Fulfillment partners interact with the headless ecommerce layer for fulfillment requests, order status updates, and return processes.

1. The application layer integrates with existing internal and third-party applications on corporate networks. Business users and existing business intelligence (BI) and enterprise resource planning (ERP) systems support day-to-day activities.

1. AWS Outposts adds AWS compute and storage capability at stores by using 1U and 2U form factors.

## Further reading
<a name="dr-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="dr-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#dr-history) | Reference architecture diagram first published. | March 28, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.