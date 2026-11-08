

# Performance tiers
<a name="BulkPutItems.Tiers"></a>

Bulk put items offers two performance tiers at different price points. Accelerated provides a higher throughput target than Standard, which allows an operation to complete faster. You specify the tier when you start the operation by setting the [PerformanceTier](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_StartBulkPutItems.html#DDB-StartBulkPutItems-request-PerformanceTier) parameter to `STANDARD` or `ACCELERATED`. If you do not specify a tier, the operation defaults to `STANDARD`.

## Standard performance tier
<a name="BulkPutItems.Tiers.Standard"></a>

**Standard** is the default and the right choice for most bulk put items operations. It is an option designed to optimize costs, suited to operations where completion time is flexible. Common use cases include background population of existing tables and periodic data enrichment. The Standard performance tier is available in all commercial AWS Regions and in the AWS GovCloud (US) Regions.

## Accelerated performance tier
<a name="BulkPutItems.Tiers.Accelerated"></a>

**Accelerated** is designed for workloads where completion time is more rigid and targets higher throughput than Standard, so large operations can finish faster. Common use cases include data migrations, recovery scenarios that must finish quickly, and recurring bulk put items operations that must finish within a time window.

The Accelerated performance tier is available in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Melbourne), Canada (Central), Europe (Ireland), Europe (London), Europe (Frankfurt), Europe (Zurich), Europe (Milan), Europe (Spain), Europe (Stockholm), South America (São Paulo), AWS GovCloud (US-West).

The following table shows estimated completion times for the Accelerated performance tier in supported AWS Regions. Actual times depend on the factors described following the table.


| Number of 1 KB items written | Estimated completion time | 
| --- | --- | 
| 10 million | Less than 10 minutes | 
| 100 million | Less than 1 hour | 
| 1 billion | 2–4 hours | 

These estimates assume the following conditions:
+ A well-scaled table
+ Writes uniformly distributed across a high-cardinality partition key space
+ No global secondary indexes (GSIs) or local secondary indexes (LSIs)
+ Input split across multiple similarly sized S3 objects

## Factors that affect throughput
<a name="BulkPutItems.Tiers.Factors"></a>

Actual throughput at either performance tier is affected by table scale, item size, key distribution, the number of global and local secondary indexes that writes propagate to, and available system capacity.

**Note**  
Initial bulk put items operations may outpace table scaling. As DynamoDB scales the table, successive operations may be required to reach optimal throughput.