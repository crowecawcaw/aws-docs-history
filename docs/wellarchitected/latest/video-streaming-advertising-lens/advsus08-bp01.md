

# ADVSUS08-BP01 Optimize privacy workload processing patterns and resource allocation for sustainability
<a name="advsus08-bp01"></a>

 For privacy-enhanced collaboration, advertising workloads have specific sustainability considerations for combining first and third-party customer data directly. 

## Implementation guidance
<a name="implementation-guidance-advsus08-bp01"></a>
+  Schedule intensive privacy computations during periods of lower carbon intensity. 
+  Use batch processing for data cleansing and matching operations. 
+  Implement efficient data compression and formatting using formats such as Parquet. 
+  Leverage AWS Graviton processors for energy-efficient computing. 
+  Use serverless architectures for matching operations where possible. 
+  Implement auto scaling based on actual collaboration workload patterns. 
+  Configure Regional data aggregation before central processing to reduce transfer needs. 

## Key AWS services
<a name="aws-key-services-5"></a>
+  AWS Lambda 
+  AWS Graviton Processors 
+  AWS Auto Scaling 

## Resources
<a name="resources-advsus08-bp01"></a>
+  [Hardware and services](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/hardware-and-services.html) 
+  [AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/optimization.html) 