# GAMECOST03-BP02 Optimize databases for game backends

Games rely heavily on databases to store a wide range of critical
data, from player profiles and inventories to in-game micro
transactions and progression metrics. Databases also play a crucial
role in managing the social aspects of games, such as creating and
maintaining player groups, parties, and enforcing moderation
policies. As the player base of a game grows, the associated
database costs will inevitably rise to accommodate the increasing
data and usage demands.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

For game backends running on Amazon Aurora, there are several cost
optimization strategies that can be employed. One key
recommendation is to
[auto
scale your read replicas based on usage patterns](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.md "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.md"),
dynamically scaling the number of replicas up or down to handle
fluctuations in traffic. This means that you are paying for the
resources you truly need. Another optimization tactic is to
replace read replicas used for games analytics with DB snapshots
exports to Amazon S3, as the S3 storage service is generally more
affordable than provisioned Aurora database instances. For more
information, see
[Exporting
DB snapshot data to Amazon S3 for Amazon RDS](../../../AmazonRDS/latest/UserGuide/USER_ExportSnapshot.md "../../../AmazonRDS/latest/UserGuide/USER_ExportSnapshot.md").

Exploring the use of
[Reserved
DB instances for Amazon Aurora](../../../AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithReservedDBInstances.md "../../../AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithReservedDBInstances.md") for your core database
instances and transitioning to the
[Aurora
Serverless](../../../AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.md "../../../AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.md") configuration can also lead to substantial
long-term cost savings by providing more flexibility and
[granular
control over your resource utilization](https://www.youtube.com/watch?v=ecRje2wFO14 "https://www.youtube.com/watch?v=ecRje2wFO14").

Similarly, for game backends that use Amazon DynamoDB, employing
the
[DynamoDB
on-demand capacity mode](../../../amazondynamodb/latest/developerguide/on-demand-capacity-mode.md "../../../amazondynamodb/latest/developerguide/on-demand-capacity-mode.md") can be an effective choice,
especially for new or unpredictable workloads, as it allows you to
pay only for the resources you consume without the need to
over-provision. As your game traffic patterns become more stable
and predictable over time, you can then transition to the
[DynamoDB
provisioned capacity mode](../../../amazondynamodb/latest/developerguide/provisioned-capacity-mode.md "../../../amazondynamodb/latest/developerguide/provisioned-capacity-mode.md"), which can offer cost savings
through better capacity planning. Activating auto-scaling on your
DynamoDB tables is another key optimization, allowing the service
to dynamically adjust the provisioned capacity based on
fluctuations in traffic. Test your game's data structure in a
development environment before launch to find and remove
unnecessary
[local
secondary indexes (LSIs)](../../../amazondynamodb/latest/developerguide/LSI.md "../../../amazondynamodb/latest/developerguide/LSI.md") and
[global
secondary indexes (GSIs)](../../../amazondynamodb/latest/developerguide/GSI.md "../../../amazondynamodb/latest/developerguide/GSI.md"). This can lead to substantial cost
savings for game data storage and operations. Removing
[inefficient
Scan operations](../../../amazondynamodb/latest/developerguide/bp-query-scan.md "../../../amazondynamodb/latest/developerguide/bp-query-scan.md") from your game backend code in favor of
more targeted queries, purchasing
[Amazon DynamoDB reserved capacity](https://aws.amazon.com/dynamodb/reserved-capacity/ "https://aws.amazon.com/dynamodb/reserved-capacity/"), and leveraging
[DynamoDB
Streams with AWS Lambda triggers](../../../amazondynamodb/latest/developerguide/Streams.md "../../../amazondynamodb/latest/developerguide/Streams.md") to process game backend
events can further optimize your DynamoDB costs. For more
information, see
[Best
practices for querying and scanning data in DynamoDB](../../../amazondynamodb/latest/developerguide/bp-query-scan.md "../../../amazondynamodb/latest/developerguide/bp-query-scan.md").

By implementing these cost optimization strategies for both Amazon Aurora and DynamoDB, game developers and publishers can
significantly reduce their game backend databases spend.

### Implementation steps

- Use Aurora read replica auto-scaling and DB snapshot exports
  to Amazon S3 for cost-efficient handling of fluctuating
  traffic and analytics needs.
- Optimize DynamoDB costs by starting with on-demand capacity
  for new workloads, transitioning to provisioned capacity
  with auto-scaling for predictable traffic, and removing
  unused LSIs and GSIs.
- Avoid inefficient Scan operations in favor of targeted
  queries, use Reserved Instances or Reserved Capacity, and
  use DynamoDB Streams with AWS Lambda for event processing.
