

# GAMECOST03-BP02 Optimize databases for game backends
<a name="gamecost03-bp02"></a>

 Games rely heavily on databases to store a wide range of critical data, from player profiles and inventories to in-game micro transactions and progression metrics. Databases also play a crucial role in managing the social aspects of games, such as creating and maintaining player groups, parties, and enforcing moderation policies. As the player base of a game grows, the associated database costs will inevitably rise to accommodate the increasing data and usage demands. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance-76"></a>

 For game backends running on Amazon Aurora, there are several cost optimization strategies that can be employed. One key recommendation is to [auto scale your read replicas based on usage patterns](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.AutoScaling.html), dynamically scaling the number of replicas up or down to handle fluctuations in traffic. This means that you are paying for the resources you truly need. Another optimization tactic is to replace read replicas used for games analytics with DB snapshots exports to Amazon S3, as the S3 storage service is generally more affordable than provisioned Aurora database instances. For more information, see [Exporting DB snapshot data to Amazon S3 for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ExportSnapshot.html). 

 Exploring the use of [Reserved DB instances for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithReservedDBInstances.html) for your core database instances and transitioning to the [Aurora Serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html) configuration can also lead to substantial long-term cost savings by providing more flexibility and [granular control over your resource utilization](https://www.youtube.com/watch?v=ecRje2wFO14). 

 Similarly, for game backends that use Amazon DynamoDB, employing the [DynamoDB on-demand capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html) can be an effective choice, especially for new or unpredictable workloads, as it allows you to pay only for the resources you consume without the need to over-provision. As your game traffic patterns become more stable and predictable over time, you can then transition to the [DynamoDB provisioned capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/provisioned-capacity-mode.html), which can offer cost savings through better capacity planning. Activating auto-scaling on your DynamoDB tables is another key optimization, allowing the service to dynamically adjust the provisioned capacity based on fluctuations in traffic. Test your game's data structure in a development environment before launch to find and remove unnecessary [local secondary indexes (LSIs)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LSI.html) and [global secondary indexes (GSIs)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html). This can lead to substantial cost savings for game data storage and operations. Removing [inefficient Scan operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-query-scan.html) from your game backend code in favor of more targeted queries, purchasing [Amazon DynamoDB reserved capacity](https://aws.amazon.com/dynamodb/reserved-capacity/), and leveraging [DynamoDB Streams with AWS Lambda triggers](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.Lambda.html) to process game backend events can further optimize your DynamoDB costs. For more information, see [Best practices for querying and scanning data in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-query-scan.html). 

 By implementing these cost optimization strategies for both Amazon Aurora and DynamoDB, game developers and publishers can significantly reduce their game backend databases spend. 

### Implementation steps
<a name="implementation-steps-68"></a>
+  Use Aurora read replica auto-scaling and DB snapshot exports to Amazon S3 for cost-efficient handling of fluctuating traffic and analytics needs. 
+  Optimize DynamoDB costs by starting with on-demand capacity for new workloads, transitioning to provisioned capacity with auto-scaling for predictable traffic, and removing unused LSIs and GSIs. 
+  Avoid inefficient Scan operations in favor of targeted queries, use Reserved Instances or Reserved Capacity, and use DynamoDB Streams with AWS Lambda for event processing. 