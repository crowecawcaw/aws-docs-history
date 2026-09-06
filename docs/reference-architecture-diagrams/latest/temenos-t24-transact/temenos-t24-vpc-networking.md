

# Temenos T24 Transact: Amazon VPC and networking
<a name="temenos-t24-vpc-networking"></a>

Publication date: **November 12, 2021 ([Diagram history](#t24-vpc-history))**

With this architecture, you can deploy Temenos T24 with Amazon VPC isolation and secure network access. The solution uses [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) private endpoints for on-premises connectivity and [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html) for container compute.

## Temenos T24 Amazon VPC and networking diagram
<a name="t24-vpc-diagram"></a>

![Reference architecture diagram showing Temenos T24 Amazon VPC and networking by using Amazon API Gateway, AWS Fargate, and Amazon VPC endpoints.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/temenos-t24-transact/images/temenos-t24-vpc-networking.png)


The following steps describe the networking and access components for this architecture:

1. Use [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/), [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/), and [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) for security and performance for internet usage.

1. Use Amazon API Gateway private endpoints for secure on-premises access through a VPN or [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/).

1. Restrict access to the Amazon VPC to only through the Amazon API Gateway VpcLink resource.

1. Run [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/) containers on AWS Fargate. You can also run your containers on [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/), or a combination of both AWS Fargate and Amazon EC2.

1. Access AWS services from within the Amazon VPC through endpoints. This removes the need for internet access.

## Further reading
<a name="t24-vpc-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="t24-vpc-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](temenos-t24-service.md#t24-svc-history) | Reference architecture diagram first published. | November 12, 2021 | 
| [Initial publication](#t24-vpc-history) | Reference architecture diagram first published. | November 12, 2021 | 
| [Initial publication](temenos-t24-availability-zones.md#t24-az-history) | Reference architecture diagram first published. | November 12, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.