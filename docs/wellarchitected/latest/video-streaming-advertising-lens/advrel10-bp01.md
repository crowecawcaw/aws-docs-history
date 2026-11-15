

# ADVREL10-BP01 Design independent failure domains for linear log ingestion and digital event streams with reliable convergence
<a name="advrel10-bp01"></a>

 Linear TV log files (typically batch-delivered hourly or daily from broadcast traffic systems) and digital ad event streams (real-time impression data) must converge for unified reporting. A failure in one pipeline should never corrupt or halt the other. 

 **Desired outcome:** 
+  Linear log ingestion and digital event streaming operate as fully independent pipelines with separate compute, storage, and error handling. 
+  A failure in either pipeline doesn't block, corrupt, or delay the other. 
+  Unified reporting gracefully indicates partial data availability when one source is delayed. 

 **Common anti-patterns:** 
+  Coupling linear and digital pipelines into a single ETL job, a malformed linear log file blocks digital event processing 
+  Using a shared database writer for both streams without isolation, deadlocks or write saturation in one channel cascade to the other 
+  No schema versioning on linear log formats, upstream broadcast system format changes break the ingestion pipeline without raising an error 
+  Reporting dashboards that fail entirely when one data source is unavailable rather than showing partial results with clear indicators 

 **Benefits of establishing this best practice:** 
+  Independent failure domains help maintain high availability for each pipeline independently. 
+  Unified reporting remains available with partial data indicators when one source is delayed, maintaining advertiser and publisher confidence in the system even during partial outages. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Linear logs arrive in batches from broadcast traffic systems well after broadcast, whereas digital events stream in close to real time. A single pipeline forces both into a shared timing model, and coupled designs fail on that mismatch. 

 A failure domain is a boundary that keeps a fault inside it from escaping to neighbors. Coupled pipelines share one domain, so a malformed linear log can stall digital processing. A shared database writer can saturate under one channel and block the other. Independent domains remove that shared fate by giving each pipeline its own compute and storage, so a fault in one leaves the other running. 

 Use scheduled convergence to break the dependency by reading whatever each source has produced at execution time. This reduces freshness but keeps the convergence process isolated from source availability and delayed logs. 

 The most dangerous failure is stale data that still reads as current. A coupled report shows old numbers without explanation, so consumers can't tell delay from correctness. A "data pending" marker makes the delay visible so advertisers and publishers can trust the reports. Schema ownership is a second organizational risk. Broadcast traffic systems sit upstream and change their log formats without notice, so unversioned schemas let those changes break ingestion. Broadcast and data teams need a shared schema contract with an explicit owner. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy linear log ingestion as a fully independent pipeline:** Create separate S3 buckets for linear and digital data. Deploy separate Lambda functions, Kinesis Firehose delivery streams, and AWS Glue ETL jobs for each pipeline. Use AWS Glue Schema Registry for both pipelines with schema evolution alerts. Confirm no shared resources between pipelines. 

1.  **Configure dedicated Kinesis shards for digital event streaming:** Create a separate Kinesis Data Stream for digital ad events with partition keys by publisher ID. Confirm this stream has no dependencies on linear pipeline resources. 

1.  **Implement convergence layer on scheduled interval:** Deploy a Glue or Athena job on a 30-minute EventBridge schedule that joins linear and digital data from the data lake. The job reads whatever data is available at scheduled execution time without waiting for either pipeline. Use data freshness timestamps to flag stale sources in output reports. 

1.  **Add data freshness indicators to unified reports:** Tag each reporting dimension with lastLinearUpdateTimestamp and lastDigitalUpdateTimestamp. Display a "data pending" indicator in dashboards when either source hasn't updated within its SLA. Configure downstream reports to display partial totals with appropriate annotations. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL01-BP01 Use loosely-coupled architectures to enable graceful recovery from failures](advrel01-bp01.md) 
+  [ADVREL04-BP04 Design your workloads to withstand failures of individual components](advrel04-bp04.md) 

 **Related documents:** 
+  [Guidance for Building an Advertising Data Lake for Publishers on AWS](https://aws.amazon.com/solutions/guidance/building-an-advertising-data-lake-for-publishers-on-aws/) 
+  [AWS Glue Schema Registry](https://docs.aws.amazon.com/glue/latest/dg/schema-registry.html) 

 **Related services:** 
+  [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) 
+  [Amazon Data Firehose](https://aws.amazon.com/kinesis/data-firehose/) 
+  [AWS Glue](https://aws.amazon.com/glue/) 
+  [Amazon Athena](https://aws.amazon.com/athena/) 