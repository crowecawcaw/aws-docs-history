# ADVSEC01-BP02 Restrict DSP access to allow only authorized SSPs

Provide a mechanism to control and manage third-party access to
each part of your cloud network environment.

## Implementation Guidance

Consider using
[AWS WAF](https://aws.amazon.com/waf/ "https://aws.amazon.com/waf/") to
allow access for authorized IPs for traffic that arrives at your
[Application Load Balancer](../../../elasticloadbalancing/latest/application/introduction.md "../../../elasticloadbalancing/latest/application/introduction.md"),
[Amazon API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/"), and Amazon CloudFront distributions. AWS WAF helps
protect your web applications against common web exploits that
may compromise security. Using AWS WAF rules, you can define a
set of inspection criteria and review when incoming requests
meets the set criteria. It is recommended to use AWS WAF rules
to inspect incoming traffic based on several factors like source
IP or originating geographic location.

Additionally, consider using AWS PrivateLink to restrict access to
your AWS services. AWS PrivateLink allows for the private connection
between your AWS VPCs and AWS services without exposing your
network traffic to the public internet. If you cannot use
AWS PrivateLink, consider using IAM to control access to your AWS
services.

## Resources

- [Configure
  security groups for your Classic Load Balancer](../../../elasticloadbalancing/latest/classic/elb-vpc-security-groups.md "../../../elasticloadbalancing/latest/classic/elb-vpc-security-groups.md")
- [How
  do I use AWS WAF to create IP set rules to restrict IPv4 and
  IPv6 access?](https://repost.aws/knowledge-center/waf-allow-my-ip-block-other-ip "https://repost.aws/knowledge-center/waf-allow-my-ip-block-other-ip")
- [Update
  the security groups for your Network Load Balancer](../../../elasticloadbalancing/latest/network/load-balancer-security-groups.md "../../../elasticloadbalancing/latest/network/load-balancer-security-groups.md")
- [Controlling
  access to Amazon Kinesis Data Streams resources using
  IAM](../../../streams/latest/dev/controlling-access.md "../../../streams/latest/dev/controlling-access.md")
- [Introducing
  Amazon API Gateway Private Endpoints](https://aws.amazon.com/blogs/compute/introducing-amazon-api-gateway-private-endpoints/ "https://aws.amazon.com/blogs/compute/introducing-amazon-api-gateway-private-endpoints/")
- [Use
  interface VPC endpoints for Amazon Kinesis Data Streams](../../../streams/latest/dev/vpc.md "../../../streams/latest/dev/vpc.md")
- [Private
  Amazon AppFlow flows](../../../appflow/latest/userguide/private-flows.md "../../../appflow/latest/userguide/private-flows.md")
- [Create
  a server in a virtual private cloud](../../../transfer/latest/userguide/create-server-in-vpc.md "../../../transfer/latest/userguide/create-server-in-vpc.md")
- [Configuring
  VPC endpoints as AWS Database Migration Service source and target endpoints](../../../dms/latest/userguide/CHAP_VPC_Endpoints.md "../../../dms/latest/userguide/CHAP_VPC_Endpoints.md")
- [Creating
  an interface VPC endpoint for AWS Data Exchange](../../../data-exchange/latest/userguide/vpc-interface-endpoints.md "../../../data-exchange/latest/userguide/vpc-interface-endpoints.md")
- [AWS PrivateLink for Amazon S3](../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md "../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md")
- [Considerations
  for AWS Glue VPC endpoints](../../../glue/latest/dg/vpc-interface-endpoints.md "../../../glue/latest/dg/vpc-interface-endpoints.md")
- [Amazon MSK multi-VPC private connectivity in a single Region](../../../msk/latest/developerguide/aws-access-mult-vpc.md "../../../msk/latest/developerguide/aws-access-mult-vpc.md")
- [Changing
  an Amazon MSK cluster's security group](../../../msk/latest/developerguide/change-security-group.md "../../../msk/latest/developerguide/change-security-group.md")
