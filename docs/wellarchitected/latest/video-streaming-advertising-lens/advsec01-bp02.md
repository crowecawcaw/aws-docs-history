

# ADVSEC01-BP02 Restrict DSP access to allow only authorized SSPs
<a name="advsec01-bp02"></a>

 Provide a mechanism to control and manage third-party access to each part of your cloud network environment. 

## Implementation Guidance
<a name="implementation-guidance-10"></a>

 Consider using [AWS WAF](https://aws.amazon.com/waf/) to allow access for authorized IPs for traffic that arrives at your [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Amazon API Gateway](https://aws.amazon.com/api-gateway/), and Amazon CloudFront distributions. AWS WAF helps protect your web applications against common web exploits that may compromise security. Using AWS WAF rules, you can define a set of inspection criteria and review when incoming requests meets the set criteria. It is recommended to use AWS WAF rules to inspect incoming traffic based on several factors like source IP or originating geographic location. 

 Additionally, consider using AWS PrivateLink to restrict access to your AWS services. AWS PrivateLink allows for the private connection between your AWS VPCs and AWS services without exposing your network traffic to the public internet. If you cannot use AWS PrivateLink, consider using IAM to control access to your AWS services. 

## Resources
<a name="resources-8"></a>
+  [Configure security groups for your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-vpc-security-groups.html) 
+  [How do I use AWS WAF to create IP set rules to restrict IPv4 and IPv6 access?](https://repost.aws/knowledge-center/waf-allow-my-ip-block-other-ip) 
+  [Update the security groups for your Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-security-groups.html) 
+  [Controlling access to Amazon Kinesis Data Streams resources using IAM](https://docs.aws.amazon.com/streams/latest/dev/controlling-access.html) 
+  [Introducing Amazon API Gateway Private Endpoints](https://aws.amazon.com/blogs/compute/introducing-amazon-api-gateway-private-endpoints/) 
+  [Use interface VPC endpoints for Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/vpc.html) 
+  [Private Amazon AppFlow flows](https://docs.aws.amazon.com/appflow/latest/userguide/private-flows.html) 
+  [Create a server in a virtual private cloud](https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html) 
+  [Configuring VPC endpoints as AWS Database Migration Service source and target endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_VPC_Endpoints.html) 
+  [Creating an interface VPC endpoint for AWS Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/vpc-interface-endpoints.html) 
+  [AWS PrivateLink for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html) 
+  [Considerations for AWS Glue VPC endpoints](https://docs.aws.amazon.com/glue/latest/dg/vpc-interface-endpoints.html) 
+  [Amazon MSK multi-VPC private connectivity in a single Region](https://docs.aws.amazon.com/msk/latest/developerguide/aws-access-mult-vpc.html) 
+  [Changing an Amazon MSK cluster's security group](https://docs.aws.amazon.com/msk/latest/developerguide/change-security-group.html) 