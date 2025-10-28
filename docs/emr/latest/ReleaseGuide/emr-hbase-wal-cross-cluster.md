# EMR WAL cross-cluster replication

From EMR 7.5, EMR WAL supports HBase cross-cluster replication of write-ahead logs. This topic shows
you how to enable the feature and check that it's working. For more details about cluster-replication,
see [Cluster Replication](https://hbase.apache.org/book.html#_cluster_replication "https://hbase.apache.org/book.html#_cluster_replication") in the Apache HBase documentation.

###### Note

There is extra read cost associated with write-ahead logs, because the replication process reads data from the local EMR WAL. For more details
about cost, refer to [About Amazon EMR Releases](emr-hbase-wal-metrics.md "emr-hbase-wal-metrics.md").

## Cross-cluster replication setup

In order to have the same user experience, enabling the replication feature on EMR WAL is the same as with native HBase write-ahead
logs. The procedure that follows shows a simple example. For more information, see the HBase documentation at [Cluster Replication](https://hbase.apache.org/book.html#_cluster_replication "https://hbase.apache.org/book.html#_cluster_replication").

1. Start a primary cluster, which is the replication source, with EMR WAL enabled. To enable write-ahead logs, see [Enabling Amazon EMR WAL](emr-hbase-wal-enabling.md "emr-hbase-wal-enabling.md"). Additionally, start a peer cluster. For this peer cluster, you can choose to enable EMR WAL or not.
2. On both clusters, create a table:

```
HBASE_CMD="sudo -u hbase hbase"
echo "create 'test_replication_table',{NAME => 'CF'}" | $HBASE_CMD shell
```

3. Add peer setup on the primary cluster and enable table replication. During the peer addition, it needs the peer cluster master node
   hostname, which is **PEER_DNS**.

```
HBASE_CMD="sudo -u hbase hbase"
PEER_DNS="ip-10-1-1-0.ec2.com"
PEER_NAME="aws"
TABLE_NAME="test_replication_table"

## Create peering with the destination cluster
echo "add_peer '$PEER_NAME', CLUSTER_KEY => '$PEER_DNS:2181:/hbase'" | $HBASE_CMD shell

## List peers in the primary cluster to confirm peer setup
echo "list_peers" | $HBASE_CMD shell

## Enable table replication
echo "enable_table_replication '$TABLE_NAME'" | $HBASE_CMD shell

```

## Confirming cross cluster replication

After performing the setup steps, replication is enabled between the primary cluster and peer cluster. A test follows that confirms
replication is working.

1. Add data on the primary cluster and verify the data replicated to the peer cluster.

```
## Write on primary cluster with HBase CLI

put 'test_replication_table', 'aaa', 'CF:a', 'aaa_a1'
put 'test_replication_table', 'bbb', 'CF:b', 'bbb_b1'
put 'test_replication_table', 'ccc', 'CF:c', 'ccc_c1'

```

2. Confirm successful replication on the peer cluster. In this case, you should see replicated data written
   from the primary to the peer cluster.

```
### Scan on peer cluster with HBase CLI

scan 'test_replication_table'
```
