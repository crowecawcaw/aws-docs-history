

# ADVCOST04-BP01 Consider lower-cost storage for older user profile data
<a name="advcost04-bp01"></a>

 Recent user profile data drives bid evaluation, so the last 30 days belong in high-performance storage. Archiving older profiles to low-cost object storage can reduce costs. High-performance database storage costs substantially more per gigabyte than object storage, making tiered storage effective for large-scale user profile stores. 

 **Desired outcome:** 
+  Recent user profile data (last 30 days) is stored in high-performance DynamoDB for sub-millisecond bid-path access. 
+  Older profile data transitions to S3 with S3 Intelligent-Tiering, reducing storage costs while maintaining accessibility for analytics. 
+  DynamoDB TTL automatically expires old profile records, limiting indefinite accumulation. 

 **Common anti-patterns:** 
+  Storing all historical profile data indefinitely in DynamoDB, so provisioned or on-demand pricing keeps applying to data that is rarely or never queried during bid evaluation. 
+  Keeping all archived data in S3 Standard storage class regardless of access frequency, which forgoes cost savings from Infrequent Access or Glacier tiers. 
+  Deleting old profile data entirely rather than archiving it, so the ability to perform historical analysis, compliance audits, or model retraining is lost. 
+  Manually managing data movement between tiers instead of automating with TTL, lifecycle policies, and scheduled export jobs. 
+  Using a single S3 storage class for all archived data without analyzing retrieval patterns to determine the appropriate tier. 

 **Benefits of establishing this best practice:** 
+  DynamoDB costs remain proportional to active working set size rather than growing unbounded with total data volume. 
+  S3 Intelligent-Tiering and lifecycle policies automatically optimize storage costs based on actual access patterns. 
+  Bid evaluation latency remains low because DynamoDB only contains the most relevant, recent data. 
+  Historical data remains available for analytics, model training, and compliance without paying high-performance storage rates. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Profile value drops off quickly after a record is created. The most recent 30 days of behavioral signals drive bid evaluation, whereas older records serve only offline analytics, model retraining, or compliance retention. Keeping all historical data in [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) means paying per-GB rates that are 10 to 20 times higher than equivalent [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) storage. The cost gap widens linearly with audience size because profile volume grows whereas the active working set stays fixed at the retention window. 

 Because DynamoDB serves profile queries at single-digit millisecond latency, every record you remove disappears from the bid path unless the application reads it from S3. Define a clear contract about which data paths need real-time access and which tolerate seconds or minutes of retrieval delay. 

 DynamoDB TTL deletes expired items at no cost and without consuming write capacity, but it introduces a race condition. Records disappear permanently after TTL executes, so any archival pipeline must capture items before expiration. If the export pipeline lags behind TTL processing, data can be lost. Teams that rely on periodic full-table exports rather than streaming pipelines are especially vulnerable because export frequency might not keep pace with TTL deletions during traffic spikes. 

 Choosing an S3 storage class trades storage cost against retrieval cost. [S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html) moves objects between frequent and infrequent tiers automatically and charges a small monitoring fee per object. Use it by default when archive access patterns are unpredictable, such as one-off analytics queries or periodic model retraining. When profiles have a predictable lifecycle (retain 90 days for compliance, then deep archive), prefer static S3 Lifecycle rules to avoid the per-object monitoring overhead. 

 The team owning DynamoDB tables and the team consuming archived data for analytics often differ. Schema mismatches emerge when the archival format (JSON export from DynamoDB) doesn't match what the analytics team expects (columnar Parquet in a data lake). Define the archive schema as a shared contract early to avoid costly reformatting pipelines later. Make the retention window length (30, 60, or 90 days) a tunable parameter driven by campaign performance data. Optimal recency varies by advertiser vertical and audience segment. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Configure DynamoDB TTL to expire profiles beyond the retention window:** Set a TTL attribute on profile items using epoch time of last activity \+ retention window (30–90 days). Enable TTL on the table. TTL deletions occur at no additional cost and don't consume write capacity. Monitor TimeToLiveDeletedItemCount to confirm TTL is pruning records at the expected rate. 

1.  **Export profiles to S3 before TTL expiration for analytics retention:** Use DynamoDB Export to S3 or a DynamoDB Streams-based pipeline to write expiring items to S3 in Parquet format before TTL deletes them. Configure S3 Intelligent-Tiering on the archive bucket to automatically move infrequently accessed profiles to lower-cost tiers. 

1.  **Configure S3 Lifecycle policies for long-term archival:** For profiles that must be retained beyond the operational window for compliance (typically 1 year), configure S3 Lifecycle rules to transition to Glacier Instant Retrieval after 90 days and Glacier Deep Archive after 1 year. 

## Resources
<a name="resources"></a>

 **Related services:** 
+  [Amazon DynamoDB TTL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html) 
+  [Amazon S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) 