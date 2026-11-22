

# ADVCOST02-BP02 Use compression to reduce network traffic and storage costs

 Compression reduces the amount of data you transfer and store, which lowers network and storage costs. Advertising workloads handle large volumes of bid events, impression logs, and creative assets, so applying compression consistently across data paths lowers costs at scale. 

 **Desired outcome:** 
+  Compression is applied across all major advertising data paths (API responses, log storage, message queues, and data lake ingestion) with measurable reductions in data transfer and storage costs. 
+  The CPU overhead of compression is monitored to confirm that increased CPU costs don't exceed the network transfer and storage costs saved. 

 **Common anti-patterns:** 
+  Transferring uncompressed bid request and response payloads between services, inflating network costs at scale. 
+  Storing raw, uncompressed log and event data in S3 without considering columnar or compressed formats. 
+  Neglecting to enable compression on managed services (CloudFront, API Gateway, Kinesis) that support it natively. 

 **Benefits of establishing this best practice:** 
+  Reduced data transfer costs, particularly for cross-region or internet-facing traffic in RTB architectures. 
+  Lower storage costs for bid logs, impression data, and analytics datasets. 
+  Potential latency improvements from smaller message sizes over the network. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Compression trades CPU cycles for a smaller data volume. That trade is worth making when network transfer or storage costs exceed the cost of the extra compute, which is usually the case for advertising workloads that move billions of bid events daily across Availability Zones, Regions, and the public internet. The trade reverses only when compression runs on already CPU-constrained instances during peak bidding windows, where the added latency can push bid responses past exchange deadlines (typically 100 ms or less). 

 Real-time paths (bid responses, inter-service RPCs, and streaming ingestion) need algorithms that compress and decompress in microseconds with modest ratios, such as LZ4 and Snappy. Batch and storage paths (log archival, data lake writes, and analytics datasets) benefit from higher-ratio algorithms like ZSTD or gzip, where the decompression penalty spreads across fewer, larger read operations. A high-ratio algorithm on a latency-critical path adds milliseconds per request that compound across millions of daily bid cycles. 

 For stored data, the format you choose matters as much as the compression algorithm. Columnar formats like [Apache Parquet](https://docs.aws.amazon.com/athena/latest/ug/columnar-storage.html) reach much better compression ratios than row-oriented JSON because similar values cluster together within columns. A raw JSON impression log that costs $X per month in Amazon S3 storage might cost $X/10 as compressed Parquet. Query engines like [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is-athena.html) and [Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-using-spectrum.html) skip irrelevant columns entirely, which reduces both scan costs and query duration. 

 Several managed services support compression, so the service absorbs the CPU overhead instead of your application. [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html) compresses responses at the edge, [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-gzip-compression-decompression.html) compresses API responses, and [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) compresses stored indices. 

 If you do not monitor it, compression gets less effective over time. Schema changes, new event types, or shifts in bid payload structure can reduce compression ratios without any explicit configuration change. A field that once held repetitive categorical values might start carrying high-entropy identifiers after a partner integration change. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enable compression on managed services that support it natively:** Configure gzip or Brotli compression on Amazon CloudFront distributions and API Gateway responses. Enable gzip compression on Amazon OpenSearch Service domains. These options need little configuration and reduce data transfer with minimal CPU overhead. 

1.  **Store data in compressed columnar formats in the advertising data lake:** Convert log and event data to Apache Parquet or ORC with Snappy or ZSTD compression before writing to Amazon S3. This reduces storage costs and improves query performance with Amazon Athena and Amazon Redshift Spectrum. Parquet with Snappy compression typically achieves 5–10x size reduction compared to raw JSON. 

1.  **Apply payload compression to inter-service communication:** Use gzip or LZ4 for real-time messages on Amazon Kinesis or Amazon MSK where low latency is critical. Use ZSTD or Snappy for batch processing where higher compression ratios are beneficial. For Amazon MSK and Kafka-compatible producers, set the producer property compression.type (for example, snappy). For Kinesis, apply compression in the producer application before putting records, because the Kinesis Producer Library doesn't expose a compression setting. 

1.  **Monitor compression effectiveness against CPU overhead:** Track data transfer volumes before and after compression using AWS Cost Explorer and CloudWatch metrics. Monitor CPU utilization on compression-enabled services to confirm that CPU costs are lower than the savings from reduced data transfer. Adjust compression level settings if CPU costs approach transfer savings. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Cost-Optimizing your AWS architectures by utilizing Amazon CloudFront features](https://aws.amazon.com/blogs/networking-and-content-delivery/cost-optimizing-your-aws-architectures-by-utilizing-amazon-cloudfront-features/) 
+  [Enable payload compression for an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-gzip-compression-decompression.html) 
+  [Reduce network transfer time with connection compression in Amazon RDS for MySQL and Amazon RDS for MariaDB](https://aws.amazon.com/blogs/database/reduce-network-transfer-time-with-connection-compression-in-amazon-rds-for-mysql-and-amazon-rds-for-mariadb/) 
+  [Custom Amazon MSK configurations](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html) 
+  [Processing large records with Amazon Kinesis Data Streams](https://aws.amazon.com/blogs/big-data/processing-large-records-with-amazon-kinesis-data-streams/) 
+  [What is AWS Transfer Family?](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html) 

 **Related services:** 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 
+  [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) 
+  [Amazon MSK](https://aws.amazon.com/msk/) 