

# Document history for AWS PrivateLink
<a name="doc-history"></a>

The following table describes the releases for AWS PrivateLink.

| Change | Description | Date | 
| --- |--- |--- |
| [Access resources and service networks](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-resources.html) | AWS PrivateLink supports accessing resources and service networks across VPC and account boundaries. | December 1, 2024 | 
| [Cross-Region access](#doc-history) | A service provider can host a service in one Region and make it available in a set of AWS Regions. A service consumer selects a service Regions when creating an endpoint. | November 26, 2024 | 
| [Designated IP addresses](#doc-history) | You can specify the IP addresses for your endpoint network interfaces when you create or modify your VPC endpoint. | August 17, 2023 | 
| [IPv6 support](#doc-history) | You can configure your Gateway Load Balancer endpoint services and Gateway Load Balancer endpoints to support both IPv4 and IPv6 addresses or only IPv6 addresses. | December 12, 2022 | 
| [Contributor Insights](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-cloudwatch-metrics.html#privatelink-contributor-insights) | You can use built-in Contributor Insights rules to identify specific endpoints that are the top contributors to the CloudWatch metrics for AWS PrivateLink. | August 18, 2022 | 
| [IPv6 support](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html#endpoint-service-ip-address-type) | Service providers can enable their endpoint service to accept IPv6 requests, even if their backend services support only IPv4. If an endpoint service accepts IPv6 requests, service consumers can enable IPv6 support for their interface endpoints so that they can access the endpoint service over IPv6. | May 11, 2022 | 
| [CloudWatch metrics](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-cloudwatch-metrics.html) | AWS PrivateLink publishes CloudWatch metrics for your interface endpoints, Gateway Load Balancer endpoints, and endpoint services. | January 27, 2022 | 
| [Gateway Load Balancer endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-gateway-load-balancer.html) | You can create a Gateway Load Balancer endpoint in your VPC to route traffic to a VPC endpoint service that you've configured using a Gateway Load Balancer. | November 10, 2020 | 
| [VPC endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) | You can attach an IAM policy to an interface VPC endpoint for an AWS service to control access to the service. | March 23, 2020 | 
| [Condition keys for VPC endpoints and endpoint services](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-iam.html) | You can use EC2 condition keys to control access to VPC endpoints and endpoint services. | March 6, 2020 | 
| [Tag VPC endpoints and endpoint services on creation](#doc-history) | You can add tags when you create VPC endpoints and endpoint services. | February 5, 2020 | 
| [Private DNS names](#doc-history) | You can access AWS PrivateLink based services from within your VPC using private DNS names. | January 6, 2020 | 
| [VPC endpoint services](#doc-history) | You can create your own endpoints services and enable other AWS accounts and users to connect to your service through an interface VPC endpoint. You can offer your endpoint services for subscription in the AWS Marketplace. | November 28, 2017 | 
| [Interface VPC endpoints for AWS services](#doc-history) | You can create an interface endpoint to connect to AWS services that integrate with AWS PrivateLink without using an internet gateway or NAT device. | November 8, 2017 | 
| [VPC endpoints for DynamoDB](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-ddb.html) | You can create a gateway VPC endpoint to access Amazon DynamoDB from your VPC without using an internet gateway or NAT device. | August 16, 2017 | 
| [VPC endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html) | You can create a gateway VPC endpoint to access Amazon S3 from your VPC without using an internet gateway or NAT device. | May 11, 2015 | 