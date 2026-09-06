

# Temenos WealthSuite Front Office on AWS: Amazon VPC and networking
<a name="temenos-wealthsuite-vpc-networking"></a>

Publication date: **January 6, 2023 ([Diagram history](#tw-vpc-history))**

With this architecture, you can deploy Temenos WealthSuite with Amazon VPC isolation and secure network access. The solution uses [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) private endpoints, [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/) containers on [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html) or [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/), and [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/) for on-premises connectivity.

## Temenos WealthSuite Amazon VPC and networking diagram
<a name="tw-vpc-diagram"></a>

![Reference architecture diagram showing Temenos WealthSuite Amazon VPC and networking by using Amazon API Gateway, Amazon EKS, AWS Fargate, and AWS Direct Connect.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/temenos-wealthsuite-front-office/images/temenos-wealthsuite-vpc-networking.png)


The following steps describe the networking and access components for this architecture:

1. Use [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/), [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/), and [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) for security and performance for internet usage.

1. Use Amazon API Gateway private endpoints for secure on-premises access through a VPN or AWS Direct Connect.

1. Restrict access to the Amazon VPC to only through the Amazon API Gateway VpcLink resource.

1. Run Amazon EKS containers on AWS Fargate, Amazon EC2, or a combination of both.

1. Extend this architecture to three Availability Zones for additional resilience.

1. Access AWS services from within the Amazon VPC through endpoints. This removes the need for internet access.

1. Enhance database availability by using [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/) Multi-AZ.

## Further reading
<a name="tw-vpc-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="tw-vpc-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](temenos-wealthsuite-overview.md#tw-ov-history) | Reference architecture diagram first published. | January 6, 2023 | 
| [Initial publication](#tw-vpc-history) | Reference architecture diagram first published. | January 6, 2023 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.