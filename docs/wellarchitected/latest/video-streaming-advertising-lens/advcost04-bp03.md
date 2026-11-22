

# ADVCOST04-BP03 Store profiles in a single Region and replicate asynchronously

 Users are generally in one Region at a time, so their profiles update in only one Region. You can schedule replication a few times a day using serverless functions and workflow orchestration. This meets resiliency requirements while reducing the replicated write capacity that ongoing cross-region replication consumes. 

 **Desired outcome:** 
+  User profile data is stored in the Region closest to the user and replicated on a scheduled basis (not in real time) to secondary regions, reducing replicated write capacity consumption. 
+  The replication schedule is calibrated to your RPO requirements (typically 4–8 hours for user profiles, where slight targeting staleness is acceptable). 

 **Common anti-patterns:** 
+  Enabling ongoing real-time cross-Region replication (such as DynamoDB Global Tables) for profile data that only changes in one Region at a time, which pays ongoing replicated write charges in every replica Region for marginal freshness improvement. 
+  Replicating all profile data on every sync cycle rather than only changed records. 
+  Running replication on a single daily schedule, so a Regional failure occurring shortly before the next sync exceeds an acceptable recovery point objective (RPO). 
+  Implementing replication without error handling or retry logic, which allows failures that leave Regions out of sync without alerting operations teams. 
+  Never testing Regional failover with replicated data, so stale or missing data first surfaces during an actual incident. 
+  Adopting a self-managed pipeline without accounting for the inter-Region data transfer it introduces, which the managed feature doesn't charge for. 

 **Benefits of establishing this best practice:** 
+  Lower replicated write capacity consumption (rWCU or rWRU) compared to ongoing Global Tables replication for single-Region-active user patterns. 
+  Controlled RPO that meets resiliency requirements without over-engineering for real-time consistency that the workload doesn't need. 
+  Reduced complexity compared to managing bidirectional conflict resolution required by ongoing multi-Region writes. 
+  Replication work confined to known windows rather than running continuously, which makes cost timing predictable even though total cost still scales with the number of changed records. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 User profiles in real-time bidding (RTB) differ from most replicated datasets because a single user is active in one geographic region at a time. A person browsing from Frankfurt generates impressions that only the EU bidding infrastructure evaluates. Their profile updates (new segment memberships, recency signals, frequency caps) accumulate in the EU region. The US or APAC bidding nodes don't need those updates until the user physically travels, which for most users happens infrequently or never. 

 [DynamoDB Global Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html) replicate every write within seconds across all configured regions, and [DynamoDB does not charge cross-Region data transfer fees](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/global-tables-billing.html) for that replication. What you pay instead is a replicated write unit in every Region containing a replica, priced the same as a standard write unit: rWCU under provisioned capacity, rWRU under on-demand. For a 200-million-profile table where 5 percent of records change daily, 10 million daily changes are billed as replicated writes in each replica Region rather than as a transfer charge. Scheduled delta sync reduces that replicated write consumption by writing the same records as ordinary writes in one target Region on your own schedule. The saving is real but narrower than a transfer-cost argument would suggest, and there is a cost moving the other way. A self-managed cross-Region pipeline does incur inter-Region data transfer, charged on both sides, along with the orchestration and operational cost of running it. Adding a new replica Region to a global table is also billed as a table restore per gigabyte, a one-time charge separate from steady-state replication. 

 Scheduling replication changes your recovery point objective (RPO). With ongoing replication, a regional failure loses seconds of profile data. With a six hour sync schedule, you could lose up to six hours of profile updates. For advertising use cases, losing those few hours is usually acceptable. A stale frequency cap might cause a user to see one extra ad impression. A missing segment membership means a bid decision uses slightly outdated targeting data. Neither failure mode causes revenue loss on the same order as the replication cost savings. Organizations running campaigns with strict per-user frequency commitments (contractual caps, regulatory limits) should tighten their sync frequency or maintain ongoing replication for that subset of profile fields. 

 Delta replication syncs only records that changed since the last successful run. With a last\_modified attribute on each item, you can query for records newer than the previous sync timestamp, and application-level change flags let writers mark records as dirty. [DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html) provides a time-ordered log of item-level changes and captures every change regardless of write path, which makes it the most reliable source, but it offers no query-by-time interface. A shard iterator can start at the trim horizon, at the latest record, or at a given sequence number, and there is no timestamp option. A Streams-based design therefore must checkpoint sequence numbers per shard and resume after them, handling shard splits as the table scales, and it must consume the stream inside the 24-hour retention window. Where a scheduled job needs to ask for everything since a timestamp, either use the last\_modified path or land changes continuously into a stream that supports timestamp positioning and longer retention, then read that landing zone on your schedule. 

 Scheduled jobs fail and retry, so the replication has to be idempotent. If your replication function writes a batch to the secondary region and then crashes before recording completion, the next run must be safe to re-process the same records. Conditional writes (writing only if the target record's version is older than the source) help avoid stale overwrites during retries and help protect against out-of-order processing when multiple sync windows overlap during error recovery. 

 The data infrastructure team typically owns this replication pipeline. The pipeline operates independently of bid-serving code and follows its own operational cadence. Monitoring requires visibility into both the replication lag (time since last successful sync) and the write cost per sync cycle, because a regression in either metric indicates a problem. Growing lag threatens RPO, and growing cost suggests that something is writing more records than expected or that the delta detection is broken. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Store user profiles in the Region closest to users:** Partition profile storage by user geography. Configure bidding infrastructure to route lookups to the regional store. Avoid centralizing profiles in a single Region and serving lookups cross-region. 

1.  **Choose a change-detection mechanism that matches your schedule:** For a scheduled job that asks for everything since the last run, use a last\_modified attribute and query on it. For complete change capture, build a [DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html) consumer that persists the last processed sequence number per shard and resumes after it, handling shard splits, or land stream records continuously into [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) where timestamp positioning and longer retention are available. 

1.  **Implement delta replication using Step Functions and Lambda:** Create a Step Functions workflow triggered by EventBridge on a schedule (2–4 times per day). The workflow reads the changed records identified by your chosen mechanism, batches them and writes to the secondary region, updates the sync state marker, and sends an SNS notification on completion or failure. Use conditional writes in the secondary region for idempotency. 

1.  **Monitor replication lag and the write cost the pattern targets:** Publish replication completion time and record counts to CloudWatch, and alarm when replication lag exceeds your RPO target. In [Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-filtering.html), filter by Service and group by Usage type to compare REG-ReplWriteCapacityUnit-Hrs or REG-ReplWriteRequestUnits against the standard write units your scheduled pipeline consumes, and include the Lambda, Step Functions, and inter-Region transfer line items the self-managed path adds. Use the Cost and Usage Report for line-item detail. 

1.  **Test Regional failover against replicated data:** Exercise a failover to the secondary region on a regular schedule and confirm that bidding infrastructure reads the replicated profiles correctly. Verify that the observed data staleness matches the RPO your schedule implies, so the gap is a known quantity rather than an incident discovery. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Understanding Amazon DynamoDB billing for global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/global-tables-billing.html) 
+  [Change data capture for DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html) 
+  [Filtering data in AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-filtering.html) 

 **Related services:** 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 