

# ADVREL10-BP02 Implement resilient cross-system measurement pipelines with data reconciliation guarantees
<a name="advrel10-bp02"></a>

 Cross-system measurement combines linear TV panel data with digital impression-level data. If pipelines lose data, produce duplicates, or fail to reconcile, advertisers lose confidence in the measurement. 

 **Desired outcome:** 
+  At-least-once processing for all measurement events with automated reconciliation that detects discrepancies within 24 hours. 
+  Reports are available within SLA even during source delays, using clearly labeled partial data. 
+  Replay capability makes processing failures recoverable rather than a source of permanently lost measurement data. 

 **Common anti-patterns:** 
+  Processing measurement events exactly-once without idempotency, infrastructure retries cause inflated impression counts that erode advertiser trust 
+  No reconciliation process between linear log totals and digital event counts, discrepancies accumulate unnoticed until quarterly audits reveal large gaps 
+  Single measurement pipeline serving both real-time dashboards and audited reports, real-time approximations contaminate audited data 
+  No replay capability for measurement events, a 2-hour processing failure results in permanently lost measurement data 

 **Benefits of establishing this best practice:** 
+  Resilient measurement with reconciliation guarantees helps maintain industry measurement compliance standards (e.g., MRC accreditation requirements), preserves advertiser confidence in cross-system reach and frequency metrics, and helps protect against revenue disputes caused by measurement discrepancies. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Linear panels produce statistical projections while digital census counting produces exact impression tallies. The two never match perfectly. Some variance is expected model behavior, while other variance signals a failure. The reconciliation layer must tell them apart, because confusing the two produces false alarms or missed data loss. 

 Use at-least-once delivery because distributed pipelines can't guarantee exactly-once. Retries re-deliver events, so implement idempotency by recognizing each event on its second arrival. Without idempotency, retries inflate impression counts, and inflated counts erode advertiser trust faster than missing data. 

 Use separate paths for real-time and audited data. Real-time measurement drives pacing and values speed over precision. Audited measurement drives billing and values correctness over speed. One pipeline serving both mixes real-time approximations into audited records, which become billing discrepancies days later. 

 Deduplication holds state across a rolling window, and an immutable archive prevents early deletion. Both choices raise storage and processing spend, but a processing outage becomes recoverable instead of final. Accreditation such as MRC defines minimum retention and accuracy expectations, and the team owning reconciliation owns those obligations. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Implement idempotent event processing with DynamoDB deduplication:** Assign a unique eventId to each measurement event (bid event, impression, and conversion). Before processing, perform a conditional DynamoDB write using attribute\_not\_exists(eventId). Only proceed with processing if the write succeeds (event hasn't been processed before). This helps avoid duplicate counting during Kinesis consumer retries. 

1.  **Maintain immutable event archive in S3 with Object Lock:** Write all raw measurement events to S3 in append-only format with Object Lock governance mode. Set retention period aligned to regulatory requirements (minimum 1 year for advertising measurement). This archive is the canonical source for replay operations. 

1.  **Deploy daily reconciliation between linear and digital totals:** Create an AWS Glue job triggered daily that compares: linear log total impressions per campaign compared to digital measurement total impressions per campaign. Flag campaigns where discrepancy exceeds your compliance threshold. Store reconciliation results in S3 and publish discrepancy metrics to CloudWatch. 

1.  **Implement replay pipeline for failed processing:** Create an EventBridge rule that triggers a Lambda function to replay failed events from the S3 archive. The Lambda reads from the archive, re-processes events using the same idempotent logic, and verifies completion. Schedule replay attempts for failed batches at T\+1 hour, T\+4 hours, and T\+24 hours. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL08-BP01 Implement redundant ad verification systems with automated failover mechanisms](advrel08-bp01.md) 
+  [ADVREL08-BP02 Establish reliable data collection and validation pipelines for measurement accuracy](advrel08-bp02.md) 

 **Related documents:** 
+  [Making retries safe with idempotent APIs, Amazon Builders Library](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-apis/) 

 **Related services:** 
+  [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [AWS Glue](https://aws.amazon.com/glue/) 
+  [Amazon EMR](https://aws.amazon.com/emr/) 