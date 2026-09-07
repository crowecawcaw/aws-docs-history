

# ADVSUS03-BP01 Use caching techniques to prevent frequent data access
<a name="advsus03-bp01"></a>

 Implement caching techniques to store frequently accessed data in cache, preventing repeated data retrieval and thereby reducing computing time and energy consumption for advertising workloads. 

## Implementation guidance 
<a name="implementation-guidance-69"></a>
+  Implement caching strategies for advertising content and data to minimize frequent data access and reduce computing time and energy consumption. 
+  Use AWS caching services like [Amazon ElastiCache](https://aws.amazon.com/elasticache/) (for in-memory caching) and [Amazon CloudFront](https://aws.amazon.com/cloudfront/) (for content delivery network caching) to store frequently accessed data closer to the consumers, reducing latency and compute requirements. 
+  Consider using [AWS Lambda@Edge](https://aws.amazon.com/lambda/edge/) and CloudFront Functions to run lightweight logic at edge locations, minimizing the need for data transfer to centralized servers and reducing overall energy consumption. 

## Key AWS services
<a name="key-aws-services-40"></a>
+  [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) (for optimizing data transfer over the AWS Cloud) 
+  [AWS Graviton processors](https://aws.amazon.com/ec2/graviton/) (for energy-efficient compute instances) 