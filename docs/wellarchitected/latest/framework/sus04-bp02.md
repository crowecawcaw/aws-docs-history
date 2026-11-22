

# SUS04-BP02 Select appropriate file formats, compression, and software implementation

 Choose file formats, encodings, compression techniques, and software implementations that minimize the storage and processing resources your workload consumes while maintaining required functionality. 

 **Desired outcome:** 
+  You minimize the resources used to store, transport, and process data. 
+  You choose file formats and compression based on how the data is written, read, and consumed. 
+  You store data in formats that balance storage efficiency, processing performance, and accessibility for your workload, reducing storage needs and making processing more efficient. 
+  You process data efficiently, favoring efficient algorithms and considering how the data is consumed downstream. 

 **Common anti-patterns:** 
+  Using general-purpose formats (such as CSV or JSON) for all data regardless of size or access patterns, and neglecting to consider file format and encoding options such as Parquet for analytical workloads [[1]](https://parquet.apache.org/). 
+  Applying the same compression technique to all data without considering its characteristics and decompression volumes. 
+  Ignoring column-oriented formats for analytical workloads. 
+  Using inefficient serialization/deserialization methods that consume excessive CPU. 
+  Failing to compress data before network transmission. 
+  Ignoring code efficiency and the impact of frameworks and dependencies on resource consumption. 
+  Overlooking algorithmic complexity (Big O notation) when implementing data processing tasks. 
+  Choosing pre-built implementations without evaluating their efficiency for your specific use case. 
+  Failing to conduct performance profiling and offset testing to identify optimization opportunities. 

 **Benefits of establishing this best practice:** 
+  Lowers the required share on hardware related impacts, from raw material extraction to end of life treatment (Scope 3 emissions). 
+  Lowers the required share on energy for operating infrastructure (Scope 2 emissions). 
+  Minimizes data transfer volume and network resource requirements. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Optimizing file formats and compression requires analyzing your data characteristics, access patterns, and processing needs. By selecting the right combination of formats and compression techniques, you can significantly reduce storage requirements and improve processing efficiency on the data. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Identify the most appropriate storage service for the intended use case. 

1.  Analyze your data characteristics and access patterns. For data in S3 buckets, consider performing an [S3 storage class analysis](https://aws.amazon.com/blogs/storage/analyze-access-patterns-and-use-the-most-cost-effective-amazon-s3-storage-class/). 

   1.  Identify your primary data usage patterns (transactional, analytical, and archive). 

   1.  Assess your data structure and typical query operations. 

   1.  Evaluate your performance and availability requirements. 

1.  Select appropriate file formats for your use cases. 

   1.  Evaluate columnar formats such as [Apache Parquet](https://parquet.apache.org/) or [ORC](https://orc.apache.org/) for analytical workloads, which can significantly reduce storage requirements and improve query performance by allowing [column-level operations](https://docs.aws.amazon.com/athena/latest/ug/columnar-storage.html). 

   1.  Consider binary formats such as [protocol buffers](https://protobuf.dev/) or [Apache Avro](https://avro.apache.org) for data serialization. 

   1.  Use specialized formats for specific domains (for example, [GLTF](https://www.khronos.org/gltf/) for 3D assets or [WebP](https://developers.google.com/speed/webp) for images). 

1.  Index your data appropriately for the access patterns. 

   1.  Choose the right [Amazon DynamoDB partition key](https://aws.amazon.com/blogs/database/choosing-the-right-dynamodb-partition-key/) to support your query types. 

   1.  Design Amazon Aurora tables to best suit your [usage patterns](https://www.amazon.science/publications/amazon-aurora-design-considerations-for-high-throughput-cloud-native-relational-databases). 

1.  Implement efficient compression techniques. 

   1.  Select compression algorithms based on data characteristics and access patterns. 

   1.  Consider column-level encoding for analytical formats. 

   1.  Use tiered compression strategies based on data age and access frequency. 

1.  Optimize for AWS service integration. 

   1.  Use [formats](https://docs.aws.amazon.com/athena/latest/ug/compression-formats.html) that work efficiently with Amazon Athena and [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format.html). 

   1.  Implement [S3 Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html) for efficient data uploads. 

   1.  Configure [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html) to serve compressed files. 

1.  Take samples of data and process that data instead of processing all data where it fits the business case (for example, you can take [samples with AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-console-sampling.html#xray-console-config)). 

1.  Monitor and optimize data operations. 

   1.  Track storage usage and query performance across different formats. 

   1.  Evaluate compression ratios and processing overhead. 

   1.  Continuously refine your format and compression strategies based on results. 

1.  Optimize code efficiency and implementation. 

   1.  Evaluate the impact of frameworks and dependencies on resource consumption. 

   1.  Consider algorithmic complexity (Big O notation) when implementing data processing tasks. 

   1.  Choose language implementations which maximize the level of parallelism. 

   1.  Use updated third-party libraries that use optimizations such as parallelism and hardware-level instructions. 

   1.  Conduct performance profiling to identify bottlenecks and optimization opportunities. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SUS04-BP01 Eliminate unnecessary data](sus04-bp01.md) 

 **Related documents:** 
+  [Use compression in Athena](https://docs.aws.amazon.com/athena/latest/ug/compression-formats.html) 
+  [Data format options for inputs and outputs in AWS Glue for Spark](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format.html) 
+  [It's Not Easy Being Green: On the Energy Efficiency of Programming Languages](https://arxiv.org/pdf/2410.05460) 
+  [Best practice 10.3 – Utilize compression techniques to both decrease storage requirements and enhance I/O efficiency](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-10.3---use-file-compression-to-reduce-number-of-files-and-to-improve-file-io-efficiency..html) 

 **Related videos:** 
+  [AWS re:Invent 2022 - Building modern data architectures on AWS](https://www.youtube.com/watch?v=Uk2CqEt5f0o) 
+  [AWS re:Invent 2024 - Build and optimize a data lake on Amazon S3 (STG323)](https://www.youtube.com/watch?v=SIGpBvmlick) 

 **Related examples:** 
+  [AWS Modern Data Architecture Immersion Day](https://catalog.workshops.aws/modern-data-architecture/en-US) 
+  [Use columnar storage formats](https://docs.aws.amazon.com/athena/latest/ug/columnar-storage.html) 