# Redo transport compression with RDS for Oracle

Use RDS for Oracle redo transport compression to improve the replication performance between your primary DB instance and standby replicas. This is particularly useful in environments that have limited network bandwidth or high-latency connections.

## Obtaining a license for redo transport compression

Redo transport compression is part of the [Oracle Advanced Compression](//www.oracle.com/database/advanced-compression/ "//www.oracle.com/database/advanced-compression/") option. To use redo transport compression, you need a valid license for the Oracle Advanced Compression option. For licensing information, contact your Oracle representative.

## Configuring redo transport compression

To configure redo transport compression, you can use the `rds.replica.redo_compression` parameter. This parameter is available for Oracle versions 19c and 21c.

The `rds.replica.redo_compression` parameter accepts the following values:

- `DISABLE` – Default value that disables redo transport compression.
- `ENABLE` – Value that enables redo transport compression through the default algorithm [ZLIB](https://zlib.net/ "https://zlib.net/").
- `ZLIB` – Value that explicitly enables redo transport compression using the ZLIB algorithm, which provides good compression ratios.
- `LZO` – Value that explicitly enables redo transport compression using the [LZO](https://www.oberhumer.com/opensource/lzo/ "https://www.oberhumer.com/opensource/lzo/") algorithm, which optimizes compression speed, particularly during decompression.

## Performance considerations for redo transport compression

Compression and decompression operations consume CPU resources on both the primary and standby instances. If you use redo transport compression, consider instance resource usage and network conditions.

## Related topics for redo transport compression

For more information on configuring redo transport compression, see the following resources:

- [DB parameter groups for
  Amazon RDS DB instances](USER_WorkingWithDBInstanceParamGroups.md "USER_WorkingWithDBInstanceParamGroups.md")
- [RedoCompression](https://docs.oracle.com/en/database/oracle/oracle-database/19/dgbkr/oracle-data-guard-broker-properties.html#GUID-5E6DDFD0-6196-48EB-94AF-21A1AFBB7DE1 "https://docs.oracle.com/en/database/oracle/oracle-database/19/dgbkr/oracle-data-guard-broker-properties.html#GUID-5E6DDFD0-6196-48EB-94AF-21A1AFBB7DE1") in the Oracle Database 19c release notes
