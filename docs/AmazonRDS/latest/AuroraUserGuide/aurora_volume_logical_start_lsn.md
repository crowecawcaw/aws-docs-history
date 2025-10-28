# aurora_volume_logical_start_lsn

Returns the log sequence number (LSN) used for identifying the beginning of a record
in the logical write-ahead log (WAL) stream of the Aurora cluster volume.

## Syntax

```
aurora_volume_logical_start_lsn()
```

## Arguments

None

## Return type

`pg_lsn`

## Usage notes

This function identifies the beginning of the record in the logical WAL stream for
a given Aurora cluster volume. You can use this function while performing major
version upgrade using logical replication and Aurora fast cloning to determine the
LSN at which a snapshot or database clone is taken. You can then use logical
replication to continuously stream the newer data recorded after the LSN and
synchronize the changes from publisher to subscriber.

For more information on using logical replication for a major version upgrade, see
[Using logical replication to perform a major version upgrade for Aurora PostgreSQL](AuroraPostgreSQL.md "AuroraPostgreSQL.md").

This function is available on the following versions of Aurora PostgreSQL:

- 15.2 and higher 15 versions
- 14.3 and higher 14 versions
- 13.6 and higher 13 versions
- 12.10 and higher 12 versions
- 11.15 and higher 11 versions
- 10.20 and higher 10 versions

## Examples

You can obtain the log sequence number (LSN) using the following query:

```
`postgres=>` SELECT aurora_volume_logical_start_lsn();
            `aurora_volume_logical_start_lsn
---------------
0/402E2F0
(1 row)`
```
