# ADVPERF05-BP01 Establish private connections between your VPC and AWS services to improve performance

A private network not only enhances the overall stability and
security of your system, but it also improves the latency and user experience
for advertising customers.

## Implementation guidance

Use [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/") to establish private connections between your
VPC and AWS services, such as Amazon S3, Amazon DynamoDB, or
Amazon ElastiCache. This approach enhances security by avoiding
the public internet and improves performance by reducing network
hops and latency.

## Resources

- [Access
  AWS services through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md")
- [Simplify
  private connectivity to Amazon DynamoDB with AWS PrivateLink](https://aws.amazon.com/blogs/database/simplify-private-connectivity-to-amazon-dynamodb-with-aws-privatelink/ "https://aws.amazon.com/blogs/database/simplify-private-connectivity-to-amazon-dynamodb-with-aws-privatelink/")
- [AWS PrivateLink for Amazon S3](../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md "../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md")
- [AWS services that integrate with AWS PrivateLink](../../../vpc/latest/privatelink/aws-services-privatelink-support.md "../../../vpc/latest/privatelink/aws-services-privatelink-support.md")
