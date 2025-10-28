# Configuring MySQL binary logging for Multi-AZ DB clusters

Binary logging in Amazon RDS for MySQL Multi-AZ DB clusters records all database changes to support
replication, point-in-time recovery, and auditing. In Multi-AZ DB clusters, binary logs synchronize
secondary nodes with the primary node, ensuring data consistency across Availability Zones
and enabling seamless failovers.

To optimize binary logging, Amazon RDS supports binary log transaction compression, which
reduces the storage requirements for binary logs and improves replication efficiency.

###### Topics

- [Binary log transaction compression for
  Multi-AZ DB clusters](#USER_Binlog.MultiAZ.compression "#USER_Binlog.MultiAZ.compression")
- [Configuring binary log transaction
  compression for Multi-AZ DB clusters](#USER_Binlog.MultiAZ.configuring "#USER_Binlog.MultiAZ.configuring")

## Binary log transaction compression for

Multi-AZ DB clusters

Binary log transaction compression uses the zstd algorithm to reduce the size of
transaction data stored in binary logs. When enabled, the MySQL database engine
compresses transaction payloads into a single event, minimizing I/O and storage
overhead. This feature improves database performance, reduces binary log size, and
optimizes resource use for managing and replicating logs in Multi-AZ DB clusters.

Amazon RDS provides binary log transaction compression for RDS for MySQL Multi-AZ DB clusters through the
following parameters:

- `binlog_transaction_compression` – When enabled
  (`1`), the database engine compresses transaction payloads and
  writes them to the binary log as a single event. This reduces storage usage and
  I/O overhead. The parameter is disabled by default.
- `binlog_transaction_compression_level_zstd` – Configures the
  zstd compression level for binary log transactions. Higher values increase the
  compression ratio, reducing storage requirements further but increasing CPU and
  memory usage for compression. The default value is 3, with a range of
  1-22.

These parameters let you fine-tune binary log compression based on workload
characteristics and resource availability. For more information, see [Binary Log Transaction Compression](https://dev.mysql.com/doc/refman/8.4/en/binary-log-transaction-compression.html "https://dev.mysql.com/doc/refman/8.4/en/binary-log-transaction-compression.html") in the MySQL documentation.

Binary log transaction compression has the following main benefits:

- Compression decreases the size of binary logs, particularly for workloads with
  large transactions or high write volumes.
- Smaller binary logs reduce network and I/O overhead, enhancing replication
  performance.
- The `binlog_transaction_compression_level_zstd` parameter provides
  control over the trade-off between compression ratio and resource
  consumption.

## Configuring binary log transaction

compression for Multi-AZ DB clusters

To configure binary log transaction compression for an RDS for MySQL Multi-AZ DB cluster, modify the relevant cluster parameter settings to match your workload
requirements.

###### To enable binary log transaction compression

1. Modify the DB cluster parameter group to set the
   `binlog_transaction_compression` parameter to
   `1`.
2. (Optional) Adjust the value of the
   `binlog_transaction_compression_level_zstd` parameter
   based on your workload requirements and resource availability.
   For more information, see [Modifying parameters in a DB cluster parameter group](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

To configure binary log transaction compression using the AWS CLI, use the
[modify-db-cluster-parameter-group](../../../cli/latest/reference/rds/modify-db-cluster-parameter-group.md "../../../cli/latest/reference/rds/modify-db-cluster-parameter-group.md") command.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster-parameter-group \
  --db-cluster-parameter-group-name `your-cluster-parameter-group` \
  --parameters "ParameterName=binlog_transaction_compression,ParameterValue=1,ApplyMethod=pending-reboot"
```

For Windows:

```
aws rds modify-db-cluster-parameter-group ^
  --db-cluster-parameter-group-name `your-cluster-parameter-group` ^
  --parameters "ParameterName=binlog_transaction_compression,ParameterValue=1,ApplyMethod=pending-reboot"
```

To configure binary log transaction compression using the Amazon RDS API, use the
[`ModifyDBClusterParameterGroup`](../APIReference/API_ModifyDBClusterParameterGroup.md "../APIReference/API_ModifyDBClusterParameterGroup.md") operation.
