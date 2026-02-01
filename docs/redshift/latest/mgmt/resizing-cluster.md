Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Resizing a cluster

As your data warehousing capacity and performance needs change, you can resize your
cluster to make the best use of Amazon Redshift's computing and storage options.

When you resize a cluster, you specify a number of nodes or node type that is
different from the current configuration of the cluster. While the cluster is in the
process of resizing, you cannot run any write or read/write queries on the cluster; you
can run only read queries.

For more information about resizing clusters, including walking through the process
of resizing clusters using different approaches, see Resizing a cluster.

###### To resize a cluster

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**.
3. Choose the cluster to resize.
4. For **Actions**, choose **Resize**. The
   **Resize cluster** page appears.
5. Follow the instructions on the page. You can resize the cluster now, once at a
   specific time, or increase and decrease the size of your cluster on a
   schedule.
6. Depending on your choices, choose **Resize now** or
   **Schedule resize**.
   If you have reserved nodes, you can upgrade to RA3 reserved nodes. You can do this
   when you use the console to restore from a snapshot or to perform an elastic resize. You
   can use the console to guide you through this process. For more information about
   upgrading to RA3 nodes, see [Upgrading to RA3
   node types](working-with-clusters.md#rs-upgrading-to-ra3 "working-with-clusters.md#rs-upgrading-to-ra3").

When you perform a resize operation to upgrade from a DC2.large node type to an
RA3.large node type, Amazon Redshift automatically converts interleaved sort keys to compound
sort keys. This conversion enables access to the concurrency scaling feature, which does
not support queries on tables with interleaved sort keys. While this automatic
conversion ensures compatibility with RA3 features, it may impact your existing query
performance patterns.

If you want to maintain interleaved sort keys after upgrading to RA3 nodes, you can
recreate your tables with the desired sort key configuration after the resize operation
completes. However, choosing this option means you won't be able to use concurrency
scaling for these tables.

A resize operation comes in two types:

- **Elastic resize** – You can add nodes to
  or remove nodes from your cluster. You can also change the node type, such as
  from DC2 nodes to RA3 nodes. An elastic resize typically completes quickly,
  taking ten minutes on average. For this reason, we recommend it as a first
  option. When you perform an elastic resize, it redistributes data slices, which
  are partitions that are allocated memory and disk space in each node. Elastic
  resize is appropriate when you:
  - _Add or reduce nodes in an existing cluster, but you don't
    change the node type_ – This is commonly called an
    _in-place_ resize. When you perform this type of
    resize, some running queries complete successfully, but others can be
    dropped as part of the
    operation.
  - _Change the node type for a cluster_ – When
    you change the node type, a snapshot is created and data is
    redistributed from the source cluster to a cluster comprised of the new
    node type. On completion, running queries are dropped. Like the
    _in-place_ resize, it completes quickly.

- **Classic resize** – You can change the
  node type, number of nodes, or both, in a similar manner to elastic resize.
  Classic resize takes more time to complete, but it can be useful in cases where
  the change in node count or the node type to migrate to doesn't fall within the
  bounds for elastic resize. This can apply, for instance, when the change in node
  count is really large.

###### Topics

- [Elastic resize](#elastic-resize "#elastic-resize")
- [Classic resize](#classic-resize-faster "#classic-resize-faster")

## Elastic resize

An elastic resize operation, when you add or remove nodes of the same type, has
the following stages:

1. Elastic resize takes a cluster snapshot.
   No-backup tables are only supported for DC2 nodes. For all
   other types of cluster, no-backup tables are included in the
   snapshot. For more information, see
   [Excluding tables from snapshots](working-with-snapshots.md#snapshots-no-backup-tables "working-with-snapshots.md#snapshots-no-backup-tables").
   If your cluster doesn't have a recent
   snapshot, because you disabled automated snapshots, the backup operation can
   take longer. (To minimize the time before the resize operation begins, we
   recommend that you enable automated snapshots or create a manual snapshot
   before starting the resize.) When you
   start an elastic resize and a snapshot operation is in progress, the resize
   can fail if the snapshot operation doesn't complete within a few
   minutes. For more information, see [Amazon Redshift snapshots and backups](working-with-snapshots.md "working-with-snapshots.md").
2. The operation migrates cluster metadata. The cluster is unavailable for a
   few minutes. The majority of queries are temporarily paused and connections
   are held open. It is possible, however, for some queries to be dropped. This
   stage is short.
3. Session connections are reinstated and queries resume.
4. Elastic resize redistributes data to node slices, in the background. The
   cluster is available for read and write operations, but some queries can
   take longer to run.
5. After the operation completes, Amazon Redshift sends an event notification.

When you use elastic resize to change the node type, it works similarly to when
you add or subtract nodes of the same type. First, a snapshot is created. A new
target cluster is provisioned with the latest data from the snapshot, and data is
transferred to the new cluster in the background. During this period, data is read
only.
When
the resize nears completion, Amazon Redshift updates the endpoint to point to the new cluster
and all connections to the source cluster are dropped.

It's unlikely that an elastic resize would fail. However, in the case of a
failure, rollback happens automatically in the majority of cases without needing any
manual intervention.

If you have reserved nodes, for example DC2 reserved nodes, you can upgrade to RA3
reserved nodes when you perform a resize. You can do this when you perform an
elastic resize or use the console to restore from a snapshot. The console guides you
through this process. For more information about upgrading to RA3 nodes, see [Upgrading to
RA3 node types](working-with-clusters.md#rs-upgrading-to-ra3 "working-with-clusters.md#rs-upgrading-to-ra3").

Elastic resize doesn't sort tables or reclaims disk space, so it isn't a
substitute for a vacuum operation.
For more information, see [Vacuuming
tables](../dg/t_Reclaiming_storage_space202.md "../dg/t_Reclaiming_storage_space202.md").

Elastic resize has the following constraints:

- _Elastic resize and data sharing clusters_ - When you
  add or subtract nodes on a cluster that's a producer for data sharing, you
  can’t connect to it from consumers while Amazon Redshift migrates cluster metadata.
  Similarly, if you perform an elastic resize and choose a new node type, data
  sharing is unavailable while connections are dropped and transferred to the
  new target cluster. In both types of elastic resize, the producer is
  unavailable for several minutes.
- _Data transfer from a shared snapshot_ - To run an
  elastic resize on a cluster that is transferring data from a shared
  snapshot, at least one backup must be available for the cluster. You can
  view your backups on the Amazon Redshift console snapshots list, the
  `describe-cluster-snapshots` CLI command, or the
  `DescribeClusterSnapshots` API operation.
- _Platform restriction_ - Elastic resize is available
  only for clusters that use the EC2-VPC platform. For more information, see
  [Use EC2 to create your cluster](working-with-clusters.md#cluster-platforms "working-with-clusters.md#cluster-platforms").
- _Storage considerations_ - Make sure that your new node
  configuration has enough storage for existing data. You may have to add
  additional nodes or change configuration.
- _Source vs target cluster size_ - The number of nodes
  and node type that it's possible to resize to with elastic resize is
  determined by the number of nodes in the source cluster and the node type
  chosen for the resized cluster. To determine the possible configurations
  available, you can use the console. Or you can use the
  `describe-node-configuration-options` AWS CLI command with the
  `action-type resize-cluster` option. For more information
  about the resizing using the Amazon Redshift console, see [Resizing a cluster](resizing-cluster.md "resizing-cluster.md").

The following example CLI command describes the configuration options
available. In this example, the cluster named `mycluster` is a
`dc2.large` 8-node cluster.

```
aws redshift describe-node-configuration-options --cluster-identifier mycluster --region eu-west-1 --action-type resize-cluster
```

This command returns an option list with recommended node types, number of
nodes, and disk utilization for each option. The configurations returned can
vary based on the specific input cluster. You can choose one of the returned
configurations when you specify the options of the
`resize-cluster` CLI command.

- _Ceiling on additional nodes_ - Elastic resize has
  limits on the nodes that you can add to a cluster. For example, a dc2
  cluster supports elastic resize up to double the number of nodes. To
  illustrate, you can add a node to a 4-node dc2.8xlarge cluster to make it a
  five-node cluster, or add more nodes until you reach eight.

###### Note

The growth and reduction limits are based on the original node type
and the number of nodes in the original cluster or its last classic
resize. If an elastic resize will exceed the growth or reduction limits,
use a classic resize.

With some ra3 node types, you can increase the number of nodes up to four
times the existing count. Specifically, suppose that your cluster consists
of ra3.4xlarge or ra3.16xlarge nodes. You can then use elastic resize to
increase the number of nodes in an 8-node cluster to 32. Or you can pick a
value below the limit. (Keep in mind that the ability to grow the cluster by
4x depends on the source cluster size.) If your cluster has ra3.xlplus
nodes, the limit is double.

All ra3 node types support a decrease in the number of nodes to a quarter
of the existing count. For example, you can decrease the size of a cluster
with ra3.4xlarge nodes from 12 nodes to 3, or to a number above the
minimum.

The following table lists growth and reduction limits for each node type
that supports elastic resize.

| Original node type | Growth limit                         | Reduction limit                                                   |
| ------------------ | ------------------------------------ | ----------------------------------------------------------------- |
| ra3.16xlarge       | 4x (from 4 to 16 nodes, for example) | To one quarter of the number (from 16 to 4 nodes,<br>for example) |
| ra3.4xlarge        | 4x                                   | To one quarter of the number                                      |
| ra3.xlplus         | 2x (from 4 to 8 nodes, for example)  | To one quarter of the number                                      |
| ra3.large          | 2x                                   | To one half of the number                                         |
| dc2.8xlarge        | 2x                                   | To one half of the number (from 16 to 8 nodes, for<br>example)    |
| dc2.large          | 2x                                   | To one half of the number                                         |

###### Note

**Choosing legacy node types when you resize an RA3
cluster** – If you attempt to resize from a cluster
with RA3 nodes to another node type, such as DC2
,
a validation warning message appears in the console, and the resize
operation won't complete. This occurs because resize to legacy node
types isn't supported. This is to prevent a customer from resizing to a
node type that's deprecated or soon to be deprecated. This applies for
both elastic resize and classic resize.

## Classic resize

Classic resize handles use cases where the change in cluster size or node type
isn't supported by elastic resize. When you perform a classic resize, Amazon Redshift creates a
target cluster and migrates your data and metadata to it from the source cluster.

### Classic resize to RA3 can provide

better availability

Classic resize has been enhanced when the target node type is RA3. It does
this by using a backup and restore operation between the source and target
cluster. When the resize begins, the source cluster restarts and is unavailable
for a few minutes. After that, the cluster is available for read and write
operations while the resize continues in the background.

#### Checking your

cluster

To ensure you have the best performance and results when you perform a
classic resize to an RA3 cluster, complete this checklist. When you don't
follow the checklist, you may not get some of the benefits of classic
resizing with RA3 nodes, such as the ability to do read and write
operations.

1. The size of the data must be below 2 petabytes. (A petabyte is
   equal to 1,000 terabytes.) To validate the size of your data, create
   a snapshot and check its size. You can also run the following query
   to check the size:

```
SELECT
sum(case when lower(diststyle) like ('%key%') then size else 0 end) distkey_blocks,
sum(size) as total_blocks,
((distkey_blocks/(total_blocks*1.00)))*100 as Blocks_need_redist
FROM svv_table_info;
```

The `svv_table_info` table is visible only to
superusers. 2. Before you initiate a classic resize, make sure you have a manual
snapshot that is no more than 10 hours old. If not, take a
snapshot. 3. The snapshot used to perform the classic resize can't be used for
a table restore or other purpose. 4. The cluster must be in a VPC.

#### Sorting and distribution operations

that result from classic resize to RA3

During classic resize to RA3, tables with KEY distribution that are
migrated as EVEN distribution are converted back to their original
distribution style.
The
duration of this is dependent on the size of the data and how busy your
cluster is. Query workloads are given higher priority to run over data
migration. For more information, see [Distribution styles](../dg/c_choosing_dist_sort.md "../dg/c_choosing_dist_sort.md").
Both reads and writes to the database work during this migration process,
but it can take longer for queries to complete. However, concurrency scaling
can boost performance during this time by adding resources for query
workloads. You can see the progress of data migration by viewing results
from the [SYS_RESTORE_STATE](../dg/SYS_RESTORE_STATE.md "../dg/SYS_RESTORE_STATE.md") and [SYS_RESTORE_LOG](../dg/SYS_RESTORE_LOG.md "../dg/SYS_RESTORE_LOG.md") views.
More information about monitoring follows.

After the cluster is fully resized, the following sort behavior
occurs:

- If the resize results in the cluster having more slices, KEY
  distribution tables become partially unsorted, but EVEN tables
  remain sorted. Additionally, the information about how much data is
  sorted may not be up to date, directly following the resize. After
  key recovery, automatic vacuum sorts the table over time.
- If the resize results in the cluster having fewer slices, both KEY
  distribution and EVEN distribution tables become partially unsorted.
  Automatic vacuum sorts the table over time.

For more information about automatic table vacuum, see [Vacuuming
tables](../dg/t_Reclaiming_storage_space202.md "../dg/t_Reclaiming_storage_space202.md"). For more information about slices in compute nodes, see
[Data
warehouse system architecture](../dg/c_high_level_system_architecture.md "../dg/c_high_level_system_architecture.md").

#### Classic resize steps when the

target cluster is RA3

Classic resize consists of the following steps, when the target cluster
type is RA3 and you've met the prerequisites detailed in the previous
section.

1. Migration initiates from the source cluster to the target cluster.
   When the new, target cluster is provisioned, Amazon Redshift sends an event
   notification that the resize has started. It restarts your existing
   cluster, which closes all connections. If your existing cluster is a
   datasharing producer cluster, connections with consumer clusters are
   also closed. The restart takes a few minutes.
2. After the restart, the database is available for reads and writes.
   Additionally, data sharing resumes, which takes an additional few
   minutes.
3. Data is migrated to the target cluster. When the target node type
   is RA3, reads and writes are available during data migration.
4. When the resize process nears completion, Amazon Redshift updates the
   endpoint to the target cluster, and all connections to the source
   cluster are dropped. The target cluster becomes the producer for
   data sharing.
5. The resize completes. Amazon Redshift sends an event notification.

You can view the resize progress on the Amazon Redshift console. The time it takes
to resize a cluster depends on the amount of data.

###### Note

**Choosing legacy node types when you resize an RA3
cluster** – If you attempt to resize from a cluster
with RA3 nodes to another node type, such as DC2
,
a validation warning message appears in the console, and the resize
operation won't complete. This occurs because resize to legacy node
types isn't supported. This is to prevent a customer from resizing to a
node type that's deprecated or soon to be deprecated. This applies for
both elastic resize and classic resize.

#### Monitoring a classic resize when the

target cluster is RA3

To monitor a classic resize of a provisioned cluster in progress,
including KEY distribution, use
[SYS_RESTORE_STATE](../dg/SYS_RESTORE_STATE.md "../dg/SYS_RESTORE_STATE.md"). It
shows the percentage completed for the table being converted. You must be a
super user to access the
data.

Drop tables that you don't need when you perform a classic resize. When
you do this, existing tables can be distributed more quickly.

### Classic resize steps when the target

cluster isn't RA3

Classic resize consists of the following, when the target node type is
anything other than RA3, like DC2, for instance.

1. Migration initiates from the source cluster to the target cluster.
   When the new, target cluster is provisioned,
   Amazon Redshift sends an event notification that the resize has started. It
   restarts your existing cluster, which closes all connections. If your
   existing cluster is a datasharing producer cluster, connections with
   consumer clusters are also closed. The restart takes a few
   minutes.

Note that any database relation, such as a table or materialized view,
created with `BACKUP NO` is not retained during the classic
resize. For more information, see [CREATE
MATERIALIZED VIEW](../dg/materialized-view-create-sql-command.md "../dg/materialized-view-create-sql-command.md"). 2. Following the restart, the database is available as read only. Data
sharing resumes, which takes an additional few minutes. 3. Data is migrated to the target cluster. The database remains read
only. 4. When the resize process nears completion, Amazon Redshift updates the endpoint to
the target cluster, and all connections to the source cluster are
dropped. The target cluster becomes the producer for data
sharing. 5. The resize completes. Amazon Redshift sends an event notification.

You can view the resize progress on the Amazon Redshift console. The time it takes to
resize a cluster depends on the amount of data.

###### Note

It can take days or possibly weeks to resize a cluster with a large amount
of data when the target cluster isn't RA3, or it doesn't meet the
prerequisites for an RA3 target cluster detailed in the previous
section.

Also note that used storage capacity for the cluster can go up after a
classic resize. This is normal system behavior when the cluster has
additional data slices that result from the classic resize. This use of
additional capacity can occur even when the number of nodes in the cluster
stays the same.

### Elastic resize vs classic

resize

The following table compares behavior between the two resize types.

| Behavior                             | Elastic resize                                                                                                                                                                                                                           | Classic resize                                                                                                                                             | Comments                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **System data<br>retention**         | Elastic resize retains system log data.                                                                                                                                                                                                  | Classic resize doesn't retain system tables and data.                                                                                                      | If you have audit logging enabled in your source cluster, you<br>can continue to access the logs in Amazon S3 or in CloudWatch, following a<br>resize. You can keep or delete these logs as your data policies<br>specify.                                                                                                                  |
| **Changing node types**              | Elastic resize, when the node type doesn't change:<br>In-place resize, and most queries are held.<br>Elastic resize, with a new node type selected: A new<br>cluster is created. Queries are dropped as the resize<br>process completes. | Classic Resize: A new cluster is created. Queries are dropped<br>during the resize process.                                                                |                                                                                                                                                                                                                                                                                                                                             |
| **Session and query<br>retention**   | Elastic resize retains sessions and queries when the node<br>type is the same in the source cluster and target. If you choose<br>a new node type, queries are dropped.                                                                   | Classic resize doesn't retain sessions and queries. Queries<br>are dropped.                                                                                | When queries are dropped, you can expect some performance<br>degradation. It's best to perform a resize operation during a<br>period of light use.                                                                                                                                                                                          |
| **Cancelling a resize<br>operation** | You can't cancel an elastic resize.                                                                                                                                                                                                      | You can cancel a classic resize operation before it<br>completes by choosing **Cancel resize**<br>from the cluster details in the Amazon Redshift console. | The amount of time it takes to cancel a resize depends<br>on the stage of the resize operation when you cancel. When<br>you do this, the cluster isn't available until the<br>cancel operation completes. If the resize operation is in<br>the final stage, you can't cancel.<br>For classic resize to an RA3 cluster, you can't<br>cancel. |

### Scheduling a

resize

You can schedule resize operations for your cluster to scale up to anticipate
high use or to scale down for cost savings. Scheduling works for both elastic
resize and classic resize. You can set up a schedule on the Amazon Redshift console. For
more information, see [Resizing a cluster](resizing-cluster.md "resizing-cluster.md"), under **Managing clusters using
the console**. You can also use AWS CLI or Amazon Redshift API operations to
schedule a resize. For more information, see [create-scheduled-action](../../../cli/latest/reference/redshift/create-scheduled-action.md "../../../cli/latest/reference/redshift/create-scheduled-action.md") in the _AWS CLI Command Reference_
or [CreateScheduledAction](../APIReference/API_CreateScheduledAction.md "../APIReference/API_CreateScheduledAction.md") in the
_Amazon Redshift API Reference_.

### Snapshot,

restore, and resize

[Elastic
resize](#elastic-resize "#elastic-resize") is the fastest method to resize an Amazon Redshift cluster. If
elastic resize isn't an option for you and you require near-constant write
access to your cluster, use the snapshot and restore operations with classic
resize as described in the following section. This approach requires that any
data that is written to the source cluster after the snapshot is taken must be
copied manually to the target cluster after the switch. Depending on how long
the copy takes, you might need to repeat this several times until you have the
same data in both clusters. Then you can make the switch to the target cluster.
This process might have a negative impact on existing queries until the full set
of data is available in the target cluster. However, it minimizes the amount of
time that you can't write to the database.

The snapshot, restore, and classic resize approach uses the following process:

1. Take a snapshot of your existing cluster. The existing cluster is the
   source cluster.
2. Note the time that the snapshot was taken. Doing this means that you
   can later identify the point when you need to rerun extract, transact,
   load (ETL) processes to load any post-snapshot data into the target
   database.
3. Restore the snapshot into a new cluster. This new cluster is the
   target cluster. Verify that the sample data exists in the target
   cluster.
4. Resize the target cluster. Choose the new node type, number of nodes,
   and other settings for the target cluster.
5. Review the loads from your ETL processes that occurred after you took
   a snapshot of the source cluster. Be sure to reload the same data in the
   same order into the target cluster. If you have ongoing data loads,
   repeat this process several times until the data is the same in both the
   source and target clusters.
6. Stop all queries running on the source cluster. To do this, you can
   reboot the cluster, or you can log on as a superuser and use the [PG_CANCEL_BACKEND](../dg/PG_CANCEL_BACKEND.md "../dg/PG_CANCEL_BACKEND.md")
   and the [PG_TERMINATE_BACKEND](../dg/PG_TERMINATE_BACKEND.md "../dg/PG_TERMINATE_BACKEND.md") commands. Rebooting the cluster is the
   easiest way to make sure that the cluster is unavailable.
7. Rename the source cluster. For example, rename it from
   `examplecluster` to `examplecluster-source`.
8. Rename the target cluster to use the name of the source cluster before
   the rename. For example, rename the target cluster from preceding to
   `examplecluster`. From this point on, any applications
   that use the endpoint containing `examplecluster` connect to
   the target cluster.
9. Delete the source cluster after you switch to the target cluster, and
   verify that all processes work as expected.

Alternatively, you can rename the source and target clusters before reloading
data into the target cluster. This approach works if you don't require that
any dependent systems and reports be immediately up to date with those for the
target cluster. In this case, step 6 moves to the end of the process described
preceding.

The rename process is only required if you want applications to continue using
the same endpoint to connect to the cluster. If you don't require this, you
can instead update any applications that connect to the cluster to use the
endpoint of the target cluster without renaming the cluster.

There are a couple of benefits to reusing a cluster name. First, you
don't need to update application connection strings because the endpoint
doesn't change, even though the underlying cluster changes. Second, related
items such as Amazon CloudWatch alarms and Amazon Simple Notification Service (Amazon SNS) notifications are tied to
the cluster name. This tie means that you can continue using the same alarms and
notifications that you set up for the cluster. This continued use is primarily a
concern in production environments where you want the flexibility to resize the
cluster without reconfiguring related items, such as alarms and notifications.
