# Write-ahead logs (WAL) for Amazon EMR

With Amazon EMR 6.15 and higher, you can write your Apache HBase write-ahead logs (WAL) to the
Amazon EMR WAL. With lower Amazon EMR releases, when you create a cluster with the **HBase on
Amazon S3** option, WAL is the only Apache HBase component that gets stored in the
local disk for clusters, and you can store other components such as the root directory,
store files (HFiles), table metadata, and data on Amazon S3.

You can use Amazon EMR WAL to recover data that didn't flush to Amazon S3. To fully back up your
HBase clusters, opt in to use the Amazon EMR WAL service. Behind the scenes,
`RegionServer` writes your HBase write-ahead logs (WAL) to the WAL for
Amazon EMR.

In the event that your cluster or the AZ becomes unhealthy or unavailable, you can create
a new cluster, point it to the same S3 root directory and Amazon EMR WAL workspace, and
automatically recover the data in WAL within a few minutes. For more information, see [Restoring from Amazon EMR WAL](emr-hbase-wal-restoring.md "emr-hbase-wal-restoring.md").

Starting with Amazon EMR releases 7.3.0 and higher,
Amazon EMR creates multiple EMR WALs for each server and groups multiple HBase regions into one Amazon EMR WAL. Doing so
enhances Apache HBase WAL to improve log utilization and optimize costs. To configure the number of Amazon EMR WAL
instances per HBase `RegionServer`, use the parameter `hbase.wal.regiongrouping.numgroups`.
By default, this parameter is set to 2. There are two system tables that are not included in any WAL group: _meta_ and _masterstore_. These tables always
use their own individual WALs.

If you run a release lower than Amazon EMR 7.3.0, we recommend that you manually disable the tables in the old HBase cluster to
make sure that all data in the Amazon EMR WAL flushes
to Amazon S3. Then, delete the old Amazon EMR WAL, terminate the old cluster, and set up a new cluster that runs the latest release.
If you run into issues and can't disable the tables on the old cluster, you can directly terminate the old cluster
and set `emr.wal.multiplex.migrate` to `true`. on the new cluster. If set to true, HBase will attempt
to replay the data from old Amazon EMR WAL instances during HBase region initialization and delete the old WALs after replay.
This replay process incurs additional costs for reads. After migration, we recommend that you configure the cluster
and set `emr.wal.multiplex.migrate` to `false`. Alternatively, you can remove the parameter
to speed up HBase region initialization.

###### Note

Amazon EMR WAL deletes the data after HBase flushes it. If HBase doesn't flush the data, Amazon EMR WAL
retains the data for a maximum of 30 days. After 30 days, Amazon EMR WAL automatically deletes the data.
Amazon EMR keeps WAL instances for up to 30 days from when you terminate an EMR cluster.
However, if you launch a new WAL-enabled cluster from the same S3 root directory within those 30 days, Amazon EMR
won't delete any of the WAL instances from your previous cluster.
For more information, see [Restoring from Amazon EMR WAL](emr-hbase-wal-restoring.md "emr-hbase-wal-restoring.md").

The following sections describe how to set up and use Amazon EMR WAL with your HBase-enabled
EMR cluster.

###### Topics

- [Amazon EMR WAL workspaces](emr-hbase-wal-workspaces.md "emr-hbase-wal-workspaces.md")
- [Required permissions for Amazon EMR WAL](emr-hbase-wal-permissions.md "emr-hbase-wal-permissions.md")
- [Enabling Amazon EMR WAL](emr-hbase-wal-enabling.md "emr-hbase-wal-enabling.md")
- [Restoring from Amazon EMR WAL](emr-hbase-wal-restoring.md "emr-hbase-wal-restoring.md")
- [Using security configurations with Amazon EMR
  WAL](emr-hbase-wal-security.md "emr-hbase-wal-security.md")
- [Access Amazon EMR WAL through
  AWS PrivateLink](emr-hbase-wal-privatelink.md "emr-hbase-wal-privatelink.md")
- [Understanding Amazon EMR WAL pricing and
  metrics](emr-hbase-wal-metrics.md "emr-hbase-wal-metrics.md")
- [Tagging WAL workspaces](emr-hbase-wal-tagging.md "emr-hbase-wal-tagging.md")
- [EMR WAL cross-cluster replication](emr-hbase-wal-cross-cluster.md "emr-hbase-wal-cross-cluster.md")
- [Considerations and Regions for Amazon EMR
  WAL](emr-hbase-wal-considerations.md "emr-hbase-wal-considerations.md")
- [Amazon EMR WAL (EMRWAL) CLI reference](emrwalcli-ref.md "emrwalcli-ref.md")
