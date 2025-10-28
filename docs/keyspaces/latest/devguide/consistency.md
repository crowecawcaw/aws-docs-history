# Supported Apache Cassandra read and write consistency levels and associated costs

The topics in this section describe which Apache Cassandra consistency levels are supported for read and write operations in Amazon Keyspaces (for Apache Cassandra).

###### Topics

- [Write consistency levels](#WriteConsistency "#WriteConsistency")
- [Read consistency levels](#ReadConsistency "#ReadConsistency")
- [Unsupported consistency levels](#UnsupportedConsistency "#UnsupportedConsistency")

## Write consistency levels

Amazon Keyspaces replicates all write
operations three times across multiple Availability Zones for durability and high
availability. Writes are durably stored before they are acknowledged using the
`LOCAL_QUORUM` consistency level. For each 1 KB write, you are billed 1
write capacity unit (WCU) for tables using provisioned capacity mode or 1 write request unit (WRU)
for tables using on-demand mode.

You can use `cqlsh` to set the consistency for all queries in the current
session to `LOCAL_QUORUM` using the following code.

```
CONSISTENCY LOCAL_QUORUM;
```

To configure the consistency level programmatically, you can set the consistency with
the appropriate Cassandra client drivers. For example, the 4.x version Java drivers allow you
to set the consistency level in the `app config` file as shown
below.

```
basic.request.consistency = LOCAL_QUORUM
```

If you're using a 3.x version Java Cassandra driver, you can specify the consistency level for the session by adding
`.withQueryOptions(new QueryOptions().setConsistencyLevel(ConsistencyLevel.LOCAL_QUORUM)` as shown in the following
code example.

```
Session session = Cluster.builder()
                      .addContactPoint(endPoint)
                      .withPort(portNumber)
                      .withAuthProvider(new SigV4AuthProvider("us-east-1"))
                      .withSSL()
                      .withQueryOptions(new QueryOptions().setConsistencyLevel(ConsistencyLevel.LOCAL_QUORUM)
                      .build()
                      .connect();
```

To configure the consistency level for specific write operations, you can define the consistency
when you call `QueryBuilder.insertInto` with a `setConsistencyLevel` argument
when you're using the Java driver.

## Read consistency levels

Amazon Keyspaces supports three read
consistency levels: `ONE`, `LOCAL_ONE`, and `LOCAL_QUORUM`. During a
`LOCAL_QUORUM` read, Amazon Keyspaces returns a response reflecting the most recent updates
from all prior successful write operations. Using the consistency level `ONE` or `LOCAL_ONE`
can improve the performance and availability of your read requests, but the response might not reflect the results of a
recently completed write.

For each 4 KB read using `ONE` or `LOCAL_ONE` consistency,
you are billed 0.5 read capacity units (RCUs) for tables using provisioned capacity mode
or 0.5 read request units (RRUs) for tables using on-demand mode. For each 4 KB read
using `LOCAL_QUORUM` consistency, you are billed 1 read capacity unit (RCU)
for tables using provisioned capacity mode or 1 read request units (RRU) for tables
using on-demand mode.

Billing based on read consistency and read capacity throughput mode per table for
each 4 KB of reads| Consistency level | Provisioned | On-demand |
| --- | --- | --- |
| `ONE` | 0.5 RCUs | 0.5 RRUs |
| `LOCAL_ONE` | 0.5 RCUs | 0.5 RRUs |
| `LOCAL_QUORUM` | 1 RCU | 1 RRU | To specify a different consistency for read operations, call `QueryBuilder.select` with a `setConsistencyLevel` argument when you're using the Java driver. ## Unsupported consistency levels The following consistency levels are not supported by Amazon Keyspaces and will result in exceptions. Unsupported consistency levels| Apache Cassandra | Amazon Keyspaces |
| --- | --- | | `EACH_QUORUM` | Not supported |
| `QUORUM` | Not supported | | `ALL` | Not supported |
| `TWO` | Not supported | | `THREE` | Not supported |
| `ANY` | Not supported | | `SERIAL` | Not supported |
| `LOCAL_SERIAL` | Not supported |
