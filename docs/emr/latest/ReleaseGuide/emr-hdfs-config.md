# HDFS configuration

The following table describes the default Hadoop Distributed File System (HDFS)
parameters and their settings. You can change these values using the
`hdfs-site` configuration classification. For more information, see [Configure applications](emr-configure-apps.md "emr-configure-apps.md").

###### Warning

1. Setting `dfs.replication` to 1 on clusters with fewer than
   four nodes can lead to HDFS data loss if a single node goes down. If
   your cluster has HDFS storage, we recommend that you configure the
   cluster with at least four core nodes for production workloads to avoid
   data loss.
2. Amazon EMR will not allow clusters to scale core nodes below
   `dfs.replication`. For example, if `dfs.replication
= 2`, the minimum number of core nodes is 2.
3. When you use managed Scaling, auto-scaling, or choose to manually
   resize your cluster, we recommend that you set
   `dfs.replication` to `2` or higher.

| Parameter         | Definition                                                                                                                                                                                                                                                         | Default value                                                                                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dfs.block.size`  | The size of HDFS blocks. When operating on data stored in HDFS, the split size is generally the size of an HDFS block. Larger numbers provide less task granularity, but also put less strain on the cluster `NameNode`.                                           | 134217728 (128 MB)                                                                                                                                                  |
| `dfs.replication` | The number of copies of each block to store for durability. Amazon EMR sets this value based on the number of core nodes the cluster is provisioned with. Adjust the value to meet your needs. To overwrite the default value, use the `hdfs-site` classification. | `1` for clusters that are provisioned with less than four core nodes `2` for clusters that are provisioned with less than ten core nodes `3` for all other clusters |
