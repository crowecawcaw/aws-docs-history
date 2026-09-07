

# ADVPERF05-BP01 Establish private connections between your VPC and AWS services to improve performance
<a name="advperf05-bp01"></a>

 A private network not only enhances the overall stability and security of your system, but it also improves the latency and user experience for advertising customers. 

## Implementation guidance
<a name="implementation-guidance-51"></a>

 Use [AWS PrivateLink](https://aws.amazon.com/privatelink/) to establish private connections between your VPC and AWS services, such as Amazon S3, Amazon DynamoDB, or Amazon ElastiCache. This approach enhances security by avoiding the public internet and improves performance by reducing network hops and latency. 

## Resources
<a name="resources-46"></a>
+  [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) 
+  [Simplify private connectivity to Amazon DynamoDB with AWS PrivateLink](https://aws.amazon.com/blogs/database/simplify-private-connectivity-to-amazon-dynamodb-with-aws-privatelink/) 
+  [AWS PrivateLink for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html) 
+  [AWS services that integrate with AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/aws-services-privatelink-support.html) 