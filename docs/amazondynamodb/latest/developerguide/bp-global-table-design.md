# Using DynamoDB global tables

Global tables build on Amazon DynamoDB’s global footprint to provide you with a fully managed,
multi-Region, and multi-active database that can deliver fast and local, read and write
performance for massively scaled, global applications. Global tables replicate your DynamoDB tables
automatically across your choice of AWS Regions. No application changes are required because
global tables use existing DynamoDB APIs. There are no upfront costs or commitments for using
global tables, and you pay only for the resources you use.

This guide explains how to use DynamoDB global tables effectively. It provides key facts about
global tables, explains the feature’s primary use cases, describes the two consistency modes,
introduces a taxonomy of three different write models you should consider, walks through the
four main request routing choices you might implement, discusses ways to evacuate a Region
that’s live or a Region that’s offline, explains how to think about throughput capacity
planning, and provides a checklist of things to consider when you deploy global tables.

This guide fits into a larger context of AWS multi-Region deployments, as covered in the
[AWS Multi-Region Fundamentals](../../../prescriptive-guidance/latest/aws-multi-region-fundamentals/introduction.md "../../../prescriptive-guidance/latest/aws-multi-region-fundamentals/introduction.md") whitepaper and the [Data resiliency design patterns with
AWS](https://www.youtube.com/watch?v=7IA48SOX20c "https://www.youtube.com/watch?v=7IA48SOX20c") video.

###### Topics

- [Key facts about DynamoDB global table design](#bp-global-table-design.prescriptive-guidance.facts "#bp-global-table-design.prescriptive-guidance.facts")
- [Key facts about MREC](#bp-global-table-design-MREC-facts "#bp-global-table-design-MREC-facts")
- [Key facts about MRSC](#bp-global-table-design-MRSC-facts "#bp-global-table-design-MRSC-facts")
- [MREC DynamoDB global table use cases](#bp-global-table-design.prescriptive-guidance.usecases "#bp-global-table-design.prescriptive-guidance.usecases")
- [Write modes with DynamoDB global tables](bp-global-table-design.prescriptive-guidance.md "bp-global-table-design.prescriptive-guidance.md")
- [Routing strategies in DynamoDB](bp-global-table-design.prescriptive-guidance.md "bp-global-table-design.prescriptive-guidance.md")
- [Evacuation processes](bp-global-table-design.prescriptive-guidance.md "bp-global-table-design.prescriptive-guidance.md")
- [Throughput capacity planning for DynamoDB global tables](bp-global-table-design.prescriptive-guidance.md "bp-global-table-design.prescriptive-guidance.md")
- [Preparation checklist for DynamoDB global tables](bp-global-table-design.prescriptive-guidance.md "bp-global-table-design.prescriptive-guidance.md")
- [Conclusion and resources](#bp-global-table-design.prescriptive-guidance-resources-conclusion "#bp-global-table-design.prescriptive-guidance-resources-conclusion")

## Key facts about DynamoDB global table design

- There are two versions of global tables: the current version [Global Tables version 2019.11.21 (Current)](GlobalTables.md "GlobalTables.md") (sometimes called "V2"), and [Global tables version 2017.11.29 (Legacy)](globaltables.md "globaltables.md") (sometimes called "V1").
  This guide focuses exclusively on the current version.
- DynamoDB (without global tables) is a Regional service, which means that it is highly available
  and intrinsically resilient to failures of infrastructure, including the failure of an
  entire Availability Zone. A single-Region DynamoDB table is designed for 99.99%
  availability. For more information, see the [DynamoDB service-level agreement](https://aws.amazon.com/dynamodb/sla/ "https://aws.amazon.com/dynamodb/sla/")
  (SLA).
- A DynamoDB global table replicates its data between two or more Regions. A multi-Region DynamoDB
  table is designed for 99.999% availability. With proper planning, global tables can help
  create an architecture that is resilient to Regional failures.
- DynamoDB doesn’t have a global endpoint. All requests are made to a Regional endpoint that
  accesses the global table instance that’s local to that Region.
- Calls to DynamoDB should not go across Regions. The best practice is for an application that is
  homed to one Region to directly access only the local DynamoDB endpoint for its Region. If
  problems are detected within a Region (in the DynamoDB layer or in the surrounding stack),
  end user traffic should be routed to a different application endpoint that’s hosted in a
  different Region. Global tables ensure that the application homed in every Region has
  access to the same data.

### Consistency modes

When you create a global table, you configure its consistency mode. Global tables
support two consistency modes: multi-Region eventual consistency (MREC) and multi-Region
strong consistency (MRSC) which was introduced in June 2025.

If you don't specify a consistency mode when you create a global table, the global table
defaults to MREC. A global table can't contain replicas that are configured with different
consistency modes. You can't change a global table's consistency mode after its
creation.

## Key facts about MREC

- Global tables that use MRSC also employ an active-active replication model. From the
  perspective of DynamoDB, the table in each Region has equal standing to accept read and write
  requests. After receiving a write request, the local replica table replicates the write
  operation to other participating remote Regions in the background.
- Items are replicated individually. Items that are updated within a single transaction
  might not be replicated together.
- Each table partition in the source Region replicates its write operations in parallel
  with every other partition. The sequence of write operations within a remote Region might
  not match the sequence of write operations that happened within the source Region. For
  more information about table partitions, see the blog post [Scaling DynamoDB: How partitions, hot keys, and split for heat impact
  performance](https://aws.amazon.com/blogs/database/part-3-scaling-dynamodb-how-partitions-hot-keys-and-split-for-heat-impact-performance/ "https://aws.amazon.com/blogs/database/part-3-scaling-dynamodb-how-partitions-hot-keys-and-split-for-heat-impact-performance/").
- A newly written item is usually propagated to all replica tables within a second.
  Nearby Regions tend to propagate faster.
- Amazon CloudWatch provides a `ReplicationLatency` metric for each Region pair. It is
  calculated by looking at arriving items, comparing their arrival time with their initial
  write time, and computing an average. Timings are stored within CloudWatch in the source Region.
  Viewing the average and maximum timings can be useful for determining the average and
  worst-case replication lag. There is no SLA on this latency.
- If an individual item is updated at about the same time (within this
  `ReplicationLatency` window) in two different Regions, and the second write
  operation happens before the first write operation was replicated, there’s a potential for
  write conflicts. Global tables that use MREC resolve such conflicts by using a last writer
  wins mechanism, based on the timestamp of the write operations. The first operation
  “loses” to the second operation. These conflicts aren’t recorded in CloudWatch or
  AWS CloudTrail.
- Each item has a last write timestamp held as a private system property. The last
  writer wins approach is implemented by using a conditional write operation that requires
  the incoming item’s timestamp to be greater than the existing item’s timestamp.
- A global table replicates all items to all participating Regions. If you want to have
  different replication scopes, you can create multiple global tables and assign each table
  different participating Regions.
- The local Region accepts write operations even if the replica Region is offline or
  `ReplicationLatency` grows. The local table continues to attempt replicating
  items to the remote table until each item succeeds.
- In the unlikely event that a Region goes fully offline, when it comes back online
  later, all pending outbound and inbound replications will be retried. No special action is
  required to bring the tables back in sync. The _last writer wins_ mechanism ensures that the data eventually becomes consistent.
- You can add a new Region to a DynamoDB MREC table at any time. DynamoDB handles the
  initial sync and ongoing replication. You can also remove a Region (even the original
  Region), and this will delete the local table in that Region.

## Key facts about MRSC

- Global tables that use MRSC also employ an active-active replication model. From the
  perspective of DynamoDB, the table in each Region has equal standing to accept read and write
  requests. Item changes in an MRSC global table replica are **synchronously** replicated to at least one other Region before the write
  operation returns a successful response.
- Strongly consistent read operations on any MRSC replica always return the latest
  version of an item. Conditional write operations always evaluate the condition expression
  against the latest version of an item. Updates always operate against the latest version
  of an item.
- Eventually consistent read operations on an MRSC replica might not include changes
  that recently occurred in another Region, and might not even include changes that very
  recently occurred in the same Region.
- A write operation fails with a `ReplicatedWriteConflictException` exception
  when it attempts to modify an item that is already being modified in another Region. Write
  operations that fail with the `ReplicatedWriteConflictException` exception can
  be retried and will succeed if the item is no longer being modified in another
  Region.
- With MRSC, latencies are higher for write operations and for strongly consistent read
  operations. These operations require cross-Region communication. This communication can
  add latency that increases based on the round-trip latency between the Region being
  accessed and the nearest Region participating in the global table. For more information,
  see the AWS re:Invent 2024 presentation, [Multi-Region strong consistency with
  DynamoDB global tables](https://www.youtube.com/watch?v=R-nTs8ZD8mA "https://www.youtube.com/watch?v=R-nTs8ZD8mA"). Eventually consistent read operations experience
  no extra latency. There is an open source [tester
  tool](https://github.com/awslabs/amazon-dynamodb-tools/tree/main/tester "https://github.com/awslabs/amazon-dynamodb-tools/tree/main/tester") that lets you experimentally calculate these latencies with your
  Regions.
- Items are replicated individually. Global tables using MRSC do not support the
  transaction APIs.
- A MRSC global table must be deployed in exactly three Regions. You can configure a
  MRSC global table with three replicas, or with two replicas and one witness. A witness is
  a component of an MRSC global table that contains recent data written to global table
  replicas. A witness provides an optional alternative to a full replica while supporting
  MRSC's availability architecture. You can't perform read or write operations on a witness.
  A witness doesn't incur storage or write costs. A witness is located within a different
  Region from the two replicas.
- To create an MRSC global table, you add one replica and a witness, or add two replicas
  to an existing DynamoDB table that contains no data. You cannot add additional replicas to an
  existing MRSC global table. You can't delete a single replica or a witness from an MRSC
  global table. You can delete two replicas, or delete one replica and a witness, from an
  MRSC global table. The second scenario converts the remaining replica to a single-Region
  DynamoDB table.
- You can determine whether an MRSC global table has a witness configured, and which
  Region in which it's configured, from the output of the DescribeTable API. The witness is
  owned and managed by DynamoDB and doesn't appear in your AWS account in the Region where
  it's configured.
- MRSC global tables are available in the following Region sets:
  - US Region set: US East (N. Virginia), US East (Ohio), US West (Oregon)
  - EU Region set: Europe (Ireland), Europe (London), Europe (Paris), Europe
    (Frankfurt)
  - AP Region set: Asia Pacific (Tokyo), Asia Pacific (Seoul), and Asia Pacific
    (Osaka)

- MRSC global tables can't span Region sets. For example, an MRSC global table can't
  contain replicas from both US and EU Region sets.
- Time to Live (TTL) isn't supported for MRSC global tables.
- Local secondary indexes (LSIs) aren't supported for MRSC global tables.
- CloudWatch Contributor Insights information is only reported for the Region in which an
  operation occurred.
- The local Region accepts all read and write operations as long as there is a second
  Region that hosts a replica or witness to establish quorum. If a second Region isn't
  available, the local Region can only service eventually consistent reads.
- In the unlikely event that a Region goes fully offline, when it comes back online
  later, it will automatically catch up. Until it's caught up, write operations and
  strongly consistent read operations _only_ to the catching
  up Region will return errors while requests to other Regions will continue to perform normally.
  Eventually consistent read operations to the catching up Region will return the data that has
  so far been propagated into the Region, with usual local consistency behavior between the leader
  node and local replicas. No special action is required to bring the tables back in sync.

## MREC DynamoDB global table use cases

MREC global tables provides these benefits:

- **Lower-latency read operations.** Place a copy of the data
  closer to the end user to reduce network latency during read operations. The data is kept
  as fresh as the `ReplicationLatency` value.
- **Lower-latency write operations.** You can write to a nearby
  region to reduce network latency and the time taken to achieve the write. The write
  traffic must be carefully routed to ensure no conflicts. Techniques for routing are
  discussed in more detail in [Routing strategies in DynamoDB](bp-global-table-design.prescriptive-guidance.md "bp-global-table-design.prescriptive-guidance.md").
- **Seamless Region migration.** You can add a new Region
  and delete the old Region to migrate a deployment from one Region to another without
  downtime at the data layer.

MREC and MRSC global tables both provide this benefit:

- **Increased resiliency and disaster recovery.** If a Region
  has degraded performance or a full outage, you can evacuate it. To evacuate means moving
  away some or all requests going to that Region. Using global tables increases the [DynamoDB SLA](https://aws.amazon.com/dynamodb/sla/ "https://aws.amazon.com/dynamodb/sla/") for monthly uptime
  percentage from 99.99% to 99.999%. Using MREC supports a recovery point objective (RPO)
  and recovery time objective (RTO) measured in seconds. Using MRSC supports an RPO of
  zero.

For example, Fidelity Investments presented at re:Invent 2022 on how they use DynamoDB
global tables for their order management system. Their goal was to achieve reliably low
latency processing at a scale they couldn't achieve with on-premises processing while also
maintaining resilience to Availability Zone and Regional failures.

If your goal is resiliency and disaster recovery, MRSC tables have higher write
latencies and higher strongly consistent read latencies, but support an RPO of zero. MREC
global tables support an RPO equal to the replication delay between replicas, usually a
few seconds depending on the replica Regions.

## Conclusion and resources

DynamoDB global tables have very few controls but still require careful consideration. You must determine your write mode,
routing model, and evacuation processes. You must instrument your application across every Region and be ready to adjust your routing
or perform an evacuation to maintain global health. The reward is having a globally distributed dataset with low-latency read and write
operations that is designed for 99.999% availability.

For more information about DynamoDB global tables, see the following resources:

- [DynamoDB documentation](../../../dynamodb.md "../../../dynamodb.md")
- [Amazon
  Application Recovery Controller](https://aws.amazon.com/application-recovery-controller/ "https://aws.amazon.com/application-recovery-controller/")
- [Readiness check in ARC](../../../r53recovery/latest/dg/recovery-readiness.md "../../../r53recovery/latest/dg/recovery-readiness.md") (AWS documentation)
- [Route 53 routing policies](../../../Route53/latest/DeveloperGuide/routing-policy.md "../../../Route53/latest/DeveloperGuide/routing-policy.md")
- [AWS Global
  Accelerator](https://aws.amazon.com/global-accelerator/ "https://aws.amazon.com/global-accelerator/")
- [DynamoDB service-level
  agreement](https://aws.amazon.com/dynamodb/sla/ "https://aws.amazon.com/dynamodb/sla/")
- [AWS Multi-Region Fundamentals](../../../prescriptive-guidance/latest/aws-multi-region-fundamentals/introduction.md "../../../prescriptive-guidance/latest/aws-multi-region-fundamentals/introduction.md") (AWS whitepaper)
- [Data resiliency design
  patterns with AWS](https://www.youtube.com/watch?v=7IA48SOX20c "https://www.youtube.com/watch?v=7IA48SOX20c") (AWS re:Invent 2022 presentation)
- [How Fidelity
  Investments and Reltio modernized with Amazon DynamoDB](https://www.youtube.com/watch?v=QUpV5MDu4Ys&t=706s "https://www.youtube.com/watch?v=QUpV5MDu4Ys&t=706s") (AWS re:Invent 2022
  presentation)
- [Multi-Region
  design patterns and best practices](https://www.youtube.com/watch?v=ilgpzlE7Hds&t=1882s "https://www.youtube.com/watch?v=ilgpzlE7Hds&t=1882s") (AWS re:Invent 2022 presentation)
- [Disaster Recovery (DR) Architecture on AWS, Part III: Pilot Light and Warm
  Standby](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-iii-pilot-light-and-warm-standby/ "https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-iii-pilot-light-and-warm-standby/") (AWS blog post)
- [Use Region pinning to set a home Region for items in an Amazon DynamoDB global
  table](https://aws.amazon.com/blogs/database/use-region-pinning-to-set-a-home-region-for-items-in-an-amazon-dynamodb-global-table/ "https://aws.amazon.com/blogs/database/use-region-pinning-to-set-a-home-region-for-items-in-an-amazon-dynamodb-global-table/") (AWS blog post)
- [Monitoring Amazon DynamoDB for operational awareness](https://aws.amazon.com/blogs/database/monitoring-amazon-dynamodb-for-operational-awareness/ "https://aws.amazon.com/blogs/database/monitoring-amazon-dynamodb-for-operational-awareness/") (AWS blog post)
- [Scaling DynamoDB: How partitions, hot keys, and split for heat impact performance](https://aws.amazon.com/blogs/database/part-3-scaling-dynamodb-how-partitions-hot-keys-and-split-for-heat-impact-performance/ "https://aws.amazon.com/blogs/database/part-3-scaling-dynamodb-how-partitions-hot-keys-and-split-for-heat-impact-performance/")
  (AWS blog post)
- [Multi-Region strong
  consistency with DynamoDB global tables](https://www.youtube.com/watch?v=R-nTs8ZD8mA "https://www.youtube.com/watch?v=R-nTs8ZD8mA") (AWS re:Invent 2024
  presentation)
