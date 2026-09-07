

# ADVCOST02-BP02 Use compression to reduce network traffic and storage costs
<a name="advcost02-bp02"></a>

 Using compression can reduce the amount of data transferred thus reducing network and storage costs. 

## Implementation guidance
<a name="implementation-guidance-60"></a>
+  Use GZIP compression before transferring data to [Amazon S3](https://aws.amazon.com/s3) to reduce traffic between Availability Zones and Regions, as well as traffic to the internet. 
+  Use snappy compression for [Amazon Kinesis](https://aws.amazon.com/kinesis/) Data Streams to reduce the amount of data stored and transferred. 
+  Implement HTTP/2 for [Application Load Balancers](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/), [Amazon API Gateway](https://aws.amazon.com/api-gateway/) compression, and [Amazon Managed Streaming for Apache Kafka (Amazon MSK)](https://aws.amazon.com/msk/). 
+  For databases, consider the following compression techniques to reduce storage costs: 
  +  Column-level compression 
  +  Table-level compression 
  +  Backup compression 
  +  Query result compression 
  +  Index compression 
+  Implement replication compression to reduce data transfer costs. 
+  Monitor the impact of compression on CPU utilization, and verify that the increased CPU costs do not exceed the network transfer costs saved. 

## Resources
<a name="resources-54"></a>
+  [Cost-Optimizing your AWS architectures by utilizing Amazon CloudFront features](https://aws.amazon.com/blogs/networking-and-content-delivery/cost-optimizing-your-aws-architectures-by-utilizing-amazon-cloudfront-features/) 
+  [Reduce network transfer time with connection compression in Amazon RDS for MySQL and Amazon RDS for MariaDB](https://aws.amazon.com/blogs/database/reduce-network-transfer-time-with-connection-compression-in-amazon-rds-for-mysql-and-amazon-rds-for-mariadb/) 
+  [Enable payload compression for an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-enable-compression.html) 
+  [Custom Amazon MSK configurations](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html) 
+  [Processing large records with Amazon Kinesis Data Streams](https://aws.amazon.com/blogs/big-data/processing-large-records-with-amazon-kinesis-data-streams/) 
+  [What is AWS Transfer Family?](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html) 