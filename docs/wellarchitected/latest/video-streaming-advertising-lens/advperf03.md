

# Data storage selection

 The advertising industry generates large volumes of data from user interactions, campaigns, and real-time bidding, and efficient storage is essential for handling that data. AWS offers many purpose-built storage services. When you understand what your advertising workload requires and choose the services that match, you improve bid latency, analytics freshness, and storage cost. 


|  ADVPERF03: How do you select and configure storage services to meet the performance and cost requirements of your advertising workload?  | 
| --- | 
| [ADVPERF03-BP01 Choose appropriate block storage options to power your advertising workload](advperf03-bp01.md) | 
| [ADVPERF03-BP02 Use object storage to store and analyze raw data from ad servers, DSPs, and DMPs](advperf03-bp02.md) | 
| [ADVPERF03-BP03 Use a cloud file system to store shared data between applications](advperf03-bp03.md) | 
| [ADVPERF03-BP04 Use single-zone high-performance object storage for latency-sensitive ad serving and model artifact retrieval](advperf03-bp04.md) | 

## Capability intent
<a name="advperf03-capability-intent"></a>
+  Every component in your advertising stack uses the EBS volume type (GP3, io2, and Instance Store) that matches its specific performance, durability, and cost profile. 
+  Object storage ([Amazon S3](https://aws.amazon.com/s3/)) is partitioned and tiered to match the access patterns of different advertising data categories (hot bid logs, warm campaign reports, cold compliance archives). 
+  Shared file storage ([Amazon EFS](https://aws.amazon.com/efs/)) is sized and tiered for the distributed advertising workloads that need it (log processing pipelines, configuration management). 
+  Latency-sensitive advertising data (model artifacts, ad creative assets, intermediate audience data) is served from [Amazon S3 Express One Zone](https://aws.amazon.com/s3/storage-classes/express-one-zone/) with single-digit-millisecond access times. 

## Common issues to watch for
<a name="advperf03-common-issues-to-watch-for"></a>
+  Storing all advertising data under a single S3 prefix regardless of access frequency or performance requirements, creating request rate bottlenecks on high-throughput ingestion paths. 
+  Using EBS GP2 volumes (older generation with burst-based IOPS) for latency-sensitive advertising databases that need consistent IOPS delivery. 
+  Failing to implement S3 lifecycle policies, allowing bid log archives and expired campaign creative assets to accumulate at premium storage rates. 
+  Storing latency-sensitive model artifacts used in bid evaluation in S3 Standard cross-AZ rather than in S3 Express One Zone colocate with compute, adding tens of milliseconds of retrieval latency to every model load. 
+  Serving all file storage from a single EFS mount target in one Availability Zone, creating a single point of failure and adding cross-AZ latency for instances in other zones. 