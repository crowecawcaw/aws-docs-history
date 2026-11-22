

# ADVREL08-BP02 Establish reliable data collection and validation pipelines for measurement accuracy

 Build reliable data collection and validation pipelines with real-time monitoring, automated reconciliation, and recovery procedures to maintain measurement accuracy in advertising systems. 

 **Desired outcome:** 
+  Measurement events are collected with at-least-once delivery guarantees and deduplicated before processing. 
+  Data quality checks run at each pipeline stage to catch anomalies before they propagate to reporting. 
+  Failed measurement events are processed from dead-letter queues rather than discarded. 

 **Common anti-patterns:** 
+  Collecting measurement events without at-least-once delivery guarantees, so events are lost on failure. 
+  Discarding failed events instead of routing them to a dead-letter queue for reprocessing. 
+  Running data quality checks only at the end, so anomalies propagate to reporting before detection. 
+  No reconciliation against third-party provider totals, so collection drift accumulates undetected. 

 **Benefits of establishing this best practice:** 
+  At-least-once collection with deduplication supports measurement completeness without double counting. 
+  Stage-by-stage data quality checks catch anomalies before they reach reporting. 
+  Dead-letter queue processing recovers failed events rather than losing them. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 The longer an error remains, the higher its corresponding cost for correction. Once an event enters the Kinesis pipeline, it spreads to aggregation, reporting, and billing. Fixing it there requires a full AWS Glue ETL reprocessing run and possible advertiser billing adjustments. Validate close to collection to help avoid such steadily rising costs. 

 At-least-once delivery accepts duplicates in exchange for never losing an event. Pair it with DynamoDB-backed deduplication to remove the duplicates the guarantee allows. Together, they give completeness without double counting. 

 Accept events to S3 and route validation failures to an SQS dead-letter queue. Store the original events in an S3 bucket to preserve valid data when a client is misconfigured, and use a dead-letter queue to block invalid events from moving downstream undetected. 

 A KCL consumer can fail without raising an alarm, and small persistent losses cause measurement drift over time. Reconciliation against third-party totals eventually exposes the drift, but by then some data might be unrecoverable. Assign an owner to the reconciliation cadence who acts on its findings. Add stage-by-stage data quality checks so that owner detects anomalies earlier than a final check would. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy Kinesis Data Streams for measurement event collection:** Create Kinesis shards sized for your peak measurement event throughput (each shard handles 1,000 records/second). Configure Kinesis Consumer Library (KCL) with automatic checkpoint management. Set ShardIteratorType to TRIM\_HORIZON during recovery scenarios so that no events are missed. 

1.  **Implement dead-letter queue processing for all measurement consumers:** Configure DLQ on all SQS queues and Kinesis stream consumers. Set DLQ depth alarms at 100 messages (immediate investigation required). Deploy Lambda functions that process DLQ messages on a 15-minute schedule, attempting reprocessing with exponential backoff. Generate reports on DLQ processing for data loss tracking. 

1.  **Run automated reconciliation between measurement sources:** Deploy a daily AWS Glue job that compares measurement totals from your collection pipeline against third-party verification provider reports. Flag discrepancies exceeding 2% for investigation. Store reconciliation results in S3 and publish summary metrics to CloudWatch for trend analysis. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL08-BP01 Implement redundant ad verification systems with automated failover mechanisms](advrel08-bp01.md) 
+  [ADVREL02-BP02 Implement a caching strategy](advrel02-bp02.md) 

 **Related documents:** 
+  [Avoiding insurmountable queue backlogs - Amazon Builders' Library](https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/) 
+  [Making retries safe with idempotent APIs - Amazon Builders' Library](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-apis/) 

 **Related services:** 
+  [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) 
+  [Amazon SQS](https://aws.amazon.com/sqs/) 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [AWS Glue](https://aws.amazon.com/glue/) 
+  [Amazon EMR](https://aws.amazon.com/emr/) 