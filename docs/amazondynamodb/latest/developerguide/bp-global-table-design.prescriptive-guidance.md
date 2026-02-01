# Preparation

checklist for DynamoDB global tables

Use the following checklist for decisions and tasks when you deploy global tables.

- Determine if your use case benefits more from an MRSC or MREC consistency mode. Do you
  need strong consistency, even with the higher latency and other tradeoffs?
- Determine how many and which Regions should participate in the global table. If you plan to
  use MRSC, decide if you want the third Region to be a replica or a witness.
- Determine your application’s write mode. This is not the same as the consistency mode. For
  more information, see [Write modes with DynamoDB global tables](bp-global-table-design.prescriptive-guidance.md "bp-global-table-design.prescriptive-guidance.md").
- Plan your [Routing
  strategies in DynamoDB](bp-global-table-design.prescriptive-guidance.md "bp-global-table-design.prescriptive-guidance.md") strategy, based on your write mode.
- Define your
  [Evacuation
  processes](bp-global-table-design.prescriptive-guidance.md "bp-global-table-design.prescriptive-guidance.md"), based on your
  consistency mode, write mode, and routing strategy.
- Capture metrics on the health, latency, and errors across each Region. For a list of DynamoDB metrics, see the AWS blog post [Monitoring Amazon DynamoDB for Operational Awareness](https://aws.amazon.com/blogs/database/monitoring-amazon-dynamodb-for-operational-awareness/ "https://aws.amazon.com/blogs/database/monitoring-amazon-dynamodb-for-operational-awareness/") for a list of metrics to observe. You should also use [synthetic canaries](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md") (artificial requests designed to detect failures, named after the canary in the coal mine), as well as live observation of customer traffic. Not all issues will appear in the DynamoDB metrics.
- If you're using MREC, set alarms for any sustained increase in
  `ReplicationLatency`. An increase might indicate an accidental misconfiguration
  in which the global table has different write settings in different Regions, which leads
  to failed replicated requests and increased latencies. It could also indicate that there
  is a Regional disruption. A [good example](https://aws.amazon.com/blogs/database/monitoring-amazon-dynamodb-for-operational-awareness/ "https://aws.amazon.com/blogs/database/monitoring-amazon-dynamodb-for-operational-awareness/") is to generate an alert if the recent average exceeds 180,000
  milliseconds. You might also watch for `ReplicationLatency` dropping to 0,
  which indicates stalled replication.
- Assign sufficient maximum read and write settings for each global table.
- Identify the reasons for evacuating a Region in advance. If the decision involves human
  judgment, document all considerations. This work should be done carefully in advance, not
  under stress.
- Maintain a runbook for every action that must take place when you evacuate a Region. Usually
  very little work is involved for the global tables, but moving the rest of the stack might be
  complex.

###### Note

With failover procedures, it's best practice to rely only on data plane operations and not on
control plane operations, because some control plane operations could be degraded during
Region failures.

For more information, see the AWS blog post [Build resilient applications with Amazon DynamoDB global tables: Part 4](https://aws.amazon.com/blogs/database/part-4-build-resilient-applications-with-amazon-dynamodb-global-tables/ "https://aws.amazon.com/blogs/database/part-4-build-resilient-applications-with-amazon-dynamodb-global-tables/").

- Test all aspects of the runbook periodically, including Region evacuations. An untested runbook
  is an unreliable runbook.
- Consider using [AWS Resilience Hub](../../../resilience-hub/latest/userguide/what-is.md "../../../resilience-hub/latest/userguide/what-is.md") to evaluate the resilience of your entire application (including
  global tables). It provides a comprehensive view of your overall application portfolio
  resilience status through its dashboard.
- Consider using ARC readiness checks to evaluate the current configuration of your application
  and track any deviances from best practices.
- When you write health checks for use with Route 53 or Global Accelerator, make a set of calls
  that cover the full database flow. If you limit your check to confirm only that the DynamoDB
  endpoint is up, you won’t be able to cover many failure modes such as AWS Identity and Access Management (IAM)
  configuration errors, code deployment problems, failure in the stack outside DynamoDB, higher
  than average read or write latencies, and so on.

## Frequently Asked Questions (FAQ) for deploying global tables

**What is the pricing for global tables?**

- A write operation in a traditional DynamoDB table is priced in write capacity units (WCUs,
  for provisioned tables) or write request units (WRUs) for on-demand tables. If you write a 5
  KB item, it incurs a charge of 5 units. A write to a global table is priced in replicated
  write capacity units (rWCUs, for provisioned tables) or replicated write request units
  (rWRUs, for on-demand tables). rWCUs and rWRUs are priced the same as WGUs and WRUs.
- rWCU and rWRU changes are incurred in every Region where the item is written
  directly or written through replication. Cross-Region data transfer fees apply.
- Writing to a global secondary index (GSI) is considered a local write operation and
  uses regular write units.
- There is no reserved capacity available for rWCUs or rWRUs at this time. Purchasing
  reserved capacity for WCUs can be beneficial for tables where GSIs consume write
  units.
- When you add a new Region to a global table, DynamoDB bootstraps the new Region
  automatically and charges you as if it were a table restore, based on the GB size of the
  table. It also charges cross-Region data transfer fees.

**Which Regions does global tables support?**

[Global Tables version 2019.11.21 (Current)](GlobalTables.md "GlobalTables.md") supports
all AWS Regions for MREC tables and the following Region sets for MRSC tables:

- US Region set: US East (N.Virginia), US East (Ohio), US West (Oregon)
- EU Region set: Europe (Ireland), Europe (London), Europe (Paris), Europe
  (Frankfort)
- AP Region set: Asia Pacific (Tokyo), Asia Pacific (Seoul), and Asia Pacific
  (Osaka)

**How are GSIs handled with global tables?**

In [Global Tables version 2019.11.21 (Current)](GlobalTables.md "GlobalTables.md"), when you create a GSI in one Region
it’s automatically created in
other participating Regions and automatically backfilled.

**How do I stop replication of a global table?**

- You can delete a replica table the same way you would delete any other table.
  Deleting the global table stops replication to that Region and deletes the table copy
  kept in that Region. However, you can't stop replication while keeping copies of the
  table as independent entities, nor can you pause replication.
- An MRSC table must be deployed in exactly three Regions. To delete the replicas you
  must delete all the replicas and the witness so that the MRSC table becomes a local
  table.

**How do DynamoDB Streams interact with global tables?**

- Each global table produces an independent stream based on all its write operations,
  wherever they started from. You can choose to consume the DynamoDB stream in one Region or
  in all Regions (independently). If you want to process local but not replicated write
  operations, you can add your own Region attribute to each item to identify the writing
  Region. You can then use a Lambda event filter to call the Lambda function only for write
  operations in the local Region. This helps with insert and update operations, but not
  delete operations.
- Global tables that are configured for multi-Region eventual consistency (MREC
  tables) replicate changes by reading those changes from a DynamoDB stream on a replica
  table and applying that change to all other replica tables. Therefore, DynamoDB is enabled
  by default on all replicas in an MREC global table and cannot be disabled on those
  replicas. The MREC replication process can combine multiple changes in a short period of
  time into a single replicated write operation. As a result, each replica's stream might
  contain slightly different records. DynamoDB Streams records on MREC replicas are always ordered on
  a per-item basis, but ordering between items might differ between replicas.
- Global tables that are configured for multi-Region strong consistency (MRSC tables)
  don’t use DynamoDB Streams for replication, so this feature isn’t enabled by default on MRSC
  replicas. You can enable DynamoDB Streams on an MRSC replica. DynamoDB Streams records on MRSC replicas are
  identical for every replica and are always ordered on a per-item basis, but ordering
  between items might differ between replicas.

**How do global tables handle transactions?**

- Transactional operations on MRSC tables will generate errors.
- Transactional operations on MREC tables provide atomicity, consistency, isolation,
  and durability (ACID) guarantees only within the Region where the write operation
  originally occurred. Transactions are not supported across Regions in global tables. For
  example, if you have an MREC global table with replicas in the US East (Ohio) and US
  West (Oregon) Regions and perform a `TransactWriteItems` operation in the US
  East (Ohio) Region, you might observe partially completed transactions in the US West
  (Oregon) Region as changes are replicated. Changes are replicated to other Regions only
  after they have been committed in the source Region.

**How do global tables interact with the DynamoDB Accelerator cache (DAX)?**

Global tables bypass DAX by updating DynamoDB directly, so DAX isn’t aware that it’s
holding stale data. The DAX cache is refreshed only when the cache’s TTL expires.

**Do tags on tables propagate?**

No, tags do not automatically propagate.

**Should I backup tables in all Regions or just one?**

The answer depends on the purpose of the backup.

- If you want to ensure data durability, DynamoDB already provides that safeguard. The
  service ensures durability.
- If you want to keep a snapshot for historical records (for example, to meet
  regulatory requirements), backing up in one Region should suffice. You can copy the
  backup to additional Regions by using AWS Backup.
- If you want to recover erroneously deleted or modified data, use [DynamoDB point-in-time recovery (PITR)](PointInTimeRecovery_Howitworks.md "PointInTimeRecovery_Howitworks.md") in
  one Region.

**How do I deploy global tables using CloudFormation?**

- CloudFormation represents a DynamoDB table and a global table as two separate resources:
  `AWS::DynamoDB::Table` and `AWS::DynamoDB::GlobalTable`. One
  approach is to create all tables that can potentially be global by using the
  `GlobalTable` construct of keeping them as standalone tables initially, and
  add Regions later if necessary.
- In CloudFormation, each global table is controlled by a single stack, in a single
  Region, regardless of the number of replicas. When you deploy your template, CloudFormation
  creates and updates all replicas as part of a single stack operation. You should not
  deploy the same [AWS::DynamoDB::GlobalTable](../../../AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.md") resource in multiple Regions. This will result in
  errors and is unsupported. If you deploy your application template in multiple Regions,
  you can use conditions to create the `AWS::DynamoDB::GlobalTable` resource in
  a single Region. Alternatively, you can choose to define your
  `AWS::DynamoDB::GlobalTable` resources in a stack that’s separate from your
  application stack, and make sure that it’s deployed to a single Region.
- If you have a regular table and you want to convert it to a global table while
  keeping it managed by CloudFormation then set the deletion policy to `Retain`,
  remove the table from the stack, convert the table to a global table in the console, and
  then import the global table as a new resource to the stack. For more information, see
  the [AWS
  GitHub repository](https://github.com/aws-samples/amazon-dynamodb-table-to-global-table-cdk "https://github.com/aws-samples/amazon-dynamodb-table-to-global-table-cdk").
- Cross-account replication is not supported at this time.
