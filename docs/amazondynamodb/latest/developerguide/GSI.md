# Managing Global Secondary Indexes in DynamoDB

This section describes how to create, modify, and delete global secondary indexes in
Amazon DynamoDB.

###### Topics

- [Creating a table with Global Secondary Indexes](#GSI.Creating "#GSI.Creating")
- [Describing the Global Secondary Indexes on a table](#GSI.Describing "#GSI.Describing")
- [Adding a Global Secondary Index to an existing table](#GSI.OnlineOps.Creating "#GSI.OnlineOps.Creating")
- [Deleting a Global Secondary Index](#GSI.OnlineOps.Deleting "#GSI.OnlineOps.Deleting")
- [Modifying a Global Secondary Index during
  creation](#GSI.OnlineOps.Creating.Modify "#GSI.OnlineOps.Creating.Modify")

## Creating a table with Global Secondary Indexes

To create a table with one or more global secondary indexes, use the
`CreateTable` operation with the `GlobalSecondaryIndexes`
parameter. For maximum query flexibility, you can create up to 20
global secondary indexes (default quota) per table.

You must specify one attribute to act as the index partition key. You can optionally
specify another attribute for the index sort key. It is not necessary for either of
these key attributes to be the same as a key attribute in the table. For example, in the
_GameScores_ table (see [Using Global Secondary Indexes in DynamoDB](GSI.md "GSI.md")), neither `TopScore` nor `TopScoreDateTime` are key attributes.
You could create a global secondary index with a partition key of `TopScore` and a sort key of
`TopScoreDateTime`. You might use such an index to determine whether
there is a correlation between high scores and the time of day a game is played.

Each index key attribute must be a scalar of type `String`,
`Number`, or `Binary`. (It cannot be a document or a set.) You
can project attributes of any data type into a global secondary index. This includes scalars, documents,
and sets. For a complete list of data types, see [Data types](HowItWorks.md#HowItWorks.DataTypes "HowItWorks.md#HowItWorks.DataTypes").

If using provisioned mode, you must provide `ProvisionedThroughput`
settings for the index, consisting of `ReadCapacityUnits` and
`WriteCapacityUnits`. These provisioned throughput settings are separate
from those of the table, but behave in similar ways. For more information, see [Provisioned throughput considerations for Global Secondary Indexes](GSI.md#GSI.ThroughputConsiderations "GSI.md#GSI.ThroughputConsiderations").

Global secondary indexes inherit the read/write capacity mode from the base table.
For more information, see [Considerations when switching capacity modes in DynamoDB](bp-switching-capacity-modes.md "bp-switching-capacity-modes.md").

###### Note

When creating a new GSI, it can be important to check if
your choice of partition key is producing uneven or narrowed distribution of data or
traffic across the new index’s partition key values. If this occurs, you could be
seeing backfill and write operations occurring at the same time and throttling
writes to the base table. The service takes measures to minimize the potential for
this scenario, but has no insight into the shape of customer data with respect to
the index partition key, the chosen projection, or the sparseness of the index
primary key.

If you suspect that your new global secondary index might have narrow or skewed
data or traffic distribution across partition key values, consider the following
before adding new indexes to operationally important tables.

- It might be safest to add the index at a time when your application is
  driving the least amount of traffic.
- Consider enabling CloudWatch Contributor Insights on your base table and
  indexes. This will give you valuable insight into your traffic
  distribution.
- Watch `WriteThrottleEvents`, `ThrottledRequests`, and
  `OnlineIndexPercentageProgress` CloudWatch metrics throughout the
  process. Adjust the provisioned write capacity as required to complete the
  backfill in a reasonable time without any significant throttling effects on
  your ongoing operations. `OnlineIndexConsumedWriteCapacity` and
  `OnlineThrottleEvents` are expected to show 0 during index backfill.
- Be prepared to cancel the index creation if you experience operational
  impact due to write throttling.

## Describing the Global Secondary Indexes on a table

To view the status of all the global secondary indexes on a table, use the
`DescribeTable` operation. The `GlobalSecondaryIndexes`
portion of the response shows all of the indexes on the table, along with the current
status of each ( `IndexStatus`).

The `IndexStatus` for a global secondary index will be one of the following:

- `CREATING` — The index is currently being created, and is not
  yet available for use.
- `ACTIVE` — The index is ready for use, and applications can
  perform `Query` operations on the index.
- `UPDATING` — The provisioned throughput settings of the index
  are being changed.
- `DELETING` — The index is currently being deleted, and can no
  longer be used.

When DynamoDB has finished building a global secondary index, the index status changes from
`CREATING` to `ACTIVE`.

## Adding a Global Secondary Index to an existing table

To add a global secondary index to an existing table, use the `UpdateTable` operation with
the `GlobalSecondaryIndexUpdates` parameter. You must provide the
following:

- An index name. The name must be unique among all the indexes on the
  table.
- The key schema of the index. You must specify one attribute for the index
  partition key; you can optionally specify another attribute for the index sort
  key. It is not necessary for either of these key attributes to be the same as a
  key attribute in the table. The data types for each schema attribute must be
  scalar: `String`, `Number`, or `Binary`.
- The attributes to be projected from the table into the index:
  - `KEYS_ONLY` — Each item in the index consists only of
    the table partition key and sort key values, plus the index key values.
  - `INCLUDE` — In addition to the attributes described
    in `KEYS_ONLY`, the secondary index includes other
    non-key attributes that you specify.
  - `ALL` — The index includes all of the attributes from
    the source table.

- The provisioned throughput settings for the index, consisting of
  `ReadCapacityUnits` and `WriteCapacityUnits`. These
  provisioned throughput settings are separate from those of the table.

You can only create one global secondary index per `UpdateTable`
operation.

###### Important

When creating a Global Secondary Index (GSI), write operations to the base table
can be throttled if the GSI activity resulting from writes to the base table exceeds
the GSI's provisioned write capacity. This throttling affects all write operations,
from indexing process to potentially disrupting your production workloads. For more
information, see [Troubleshooting throttling in Amazon DynamoDB](TroubleshootingThrottling.md "TroubleshootingThrottling.md").

### Phases of index creation

When you add a new global secondary index to an existing table, the table continues to be available
while the index is being built. However, the new index is not available for Query
operations until its status changes from `CREATING` to
`ACTIVE`.

###### Note

Global secondary index creation does not use Application Auto Scaling. Increasing the `MIN` Application Auto Scaling
capacity will not decrease the creation time of the global secondary index.

Behind the scenes, DynamoDB builds the index in two phases:

**Resource Allocation**

DynamoDB allocates the compute and storage resources that are needed for
building the index.

During the resource allocation phase, the `IndexStatus`
attribute is `CREATING` and the `Backfilling`
attribute is false. Use the `DescribeTable` operation to
retrieve the status of a table and all of its secondary indexes.

While the index is in the resource allocation phase, you can't delete
the index or delete its parent table. You also can't modify the
provisioned throughput of the index or the table. You cannot add or
delete other indexes on the table. However, you can modify the
provisioned throughput of these other indexes.

**Backfilling**

For each item in the table, DynamoDB determines which set of attributes
to write to the index based on its projection (`KEYS_ONLY`,
`INCLUDE`, or `ALL`). It then writes these
attributes to the index. During the backfill phase, DynamoDB tracks the
items that are being added, deleted, or updated in the table. The
attributes from these items are also added, deleted, or updated in the
index as appropriate.

During the backfilling phase, the `IndexStatus` attribute
is set to `CREATING`, and the `Backfilling`
attribute is true. Use the `DescribeTable` operation to
retrieve the status of a table and all of its secondary indexes.

While the index is backfilling, you cannot delete its parent table.
However, you can still delete the index or modify the provisioned
throughput of the table and any of its global secondary indexes.

###### Note

During the backfilling phase, some writes of violating items might
succeed while others are rejected. After backfilling, all writes to
items that violate the new index's key schema are rejected. We
recommend that you run the Violation Detector tool after the backfill phase
finishes to detect and resolve any key violations that might have
occurred. For more information, see [Detecting and correcting index key
violations in DynamoDB](GSI.OnlineOps.md "GSI.OnlineOps.md").

While the resource allocation and backfilling phases are in progress, the index is
in the `CREATING` state. During this time, DynamoDB performs read operations
on the table. You are not charged for read operations from the base table to
populate the global secondary index.

When the index build is complete, its status changes to `ACTIVE`. You
can't `Query` or `Scan` the index until it is
`ACTIVE`.

###### Note

In some cases, DynamoDB can't write data from the table to the index because of
index key violations. This can occur if:

- The data type of an attribute value does not match the data type of an
  index key schema data type.
- The size of an attribute exceeds the maximum length for an index key
  attribute.
- An index key attribute has an empty String or empty Binary attribute
  value.
  Index key violations do not interfere with global secondary index creation. However, when the
  index becomes `ACTIVE`, the violating keys are not present in the
  index.

DynamoDB provides a standalone tool for finding and resolving these issues. For
more information, see [Detecting and correcting index key
violations in DynamoDB](GSI.OnlineOps.md "GSI.OnlineOps.md").

### Adding a Global Secondary Index to a large

table

The time required for building a global secondary index depends on several factors, such as the
following:

- The size of the table
- The number of items in the table that qualify for inclusion in the
  index
- The number of attributes projected into the index
- Write activity on the main table during index builds

If you are adding a global secondary index to a very large table, it might take a long time for the
creation process to complete. To monitor progress and determine whether the index
has sufficient write capacity, consult the following Amazon CloudWatch metrics:

- `OnlineIndexPercentageProgress`

For more information about CloudWatch metrics related to DynamoDB, see [DynamoDB metrics](metrics-dimensions.md#dynamodb-metrics "metrics-dimensions.md#dynamodb-metrics").

###### Important

You may need to allowlist very large tables before creating or updating a
Global Secondary Index. Please reach out to AWS Support to allowlist your
tables.

While an index is being backfilled, DynamoDB uses internal system capacity to read
from the table. This is to minimize the impact of the index creation and to assure
that your table does not run out of read capacity.

## Deleting a Global Secondary Index

If you no longer need a global secondary index, you can delete it using the `UpdateTable`
operation.

You can delete only one global secondary index per `UpdateTable`
operation.

While the global secondary index is being deleted, there is no effect on any read or write activity in
the parent table. While the deletion is in progress, you can still modify the
provisioned throughput on other indexes.

###### Note

- When you delete a table using the `DeleteTable` action, all of
  the global secondary indexes on that table are also deleted.
- Your account will not be charged for the delete operation of the
  global secondary index.

## Modifying a Global Secondary Index during

creation

While an index is being built, you can use the `DescribeTable` operation to
determine what phase it is in. The description for the index includes a Boolean
attribute, `Backfilling`, to indicate whether DynamoDB is currently loading the
index with items from the table. If `Backfilling` is true, the resource
allocation phase is complete and the index is now backfilling.

During the backfilling phase, you can delete the index that is being created. During
this phase, you can't add or delete other indexes on the table.

###### Note

For indexes that were created as part of a `CreateTable` operation, the
`Backfilling` attribute does not appear in the
`DescribeTable` output. For more information, see [Phases of index creation](#GSI.OnlineOps.Creating.Phases "#GSI.OnlineOps.Creating.Phases").
