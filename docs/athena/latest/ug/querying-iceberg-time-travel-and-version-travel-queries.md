# Perform time

travel and version travel queries

Each Apache Iceberg table maintains a versioned manifest of the Amazon S3 objects that it
contains. Previous versions of the manifest can be used for time travel and version travel
queries.

Time travel queries in Athena query Amazon S3 for historical data from a consistent snapshot as
of a specified date and time. Version travel queries in Athena query Amazon S3 for historical data
as of a specified snapshot ID.

## Time travel queries

To run a time travel query, use `FOR TIMESTAMP AS OF
 `timestamp``after the table name in the
`SELECT` statement, as in the following example.

```
SELECT * FROM iceberg_table FOR TIMESTAMP AS OF `timestamp`
```

The system time to be specified for traveling is either a timestamp or timestamp with
a time zone. If not specified, Athena considers the value to be a timestamp in UTC
time.

The following example time travel queries select CloudTrail data for the specified date and
time.

```
SELECT * FROM iceberg_table FOR TIMESTAMP AS OF TIMESTAMP '2020-01-01 10:00:00 UTC'
```

```
SELECT * FROM iceberg_table FOR TIMESTAMP AS OF (current_timestamp - interval '1' day)
```

## Version travel queries

To execute a version travel query (that is, view a consistent snapshot as of a
specified version), use `FOR VERSION AS OF
 `version``after the table name in the
`SELECT` statement, as in the following example.

```
SELECT * FROM [`db_name`.]`table_name` FOR VERSION AS OF `version`
```

The `version` parameter is the `bigint` snapshot
ID associated with an Iceberg table version.

The following example version travel query selects data for the specified
version.

```
SELECT * FROM iceberg_table FOR VERSION AS OF 949530903748831860
```

###### Note

The `FOR SYSTEM_TIME AS OF` and `FOR SYSTEM_VERSION AS OF`
clauses in Athena engine version 2 have been replaced by the `FOR TIMESTAMP AS OF` and
`FOR VERSION AS OF` clauses in Athena engine version 3.

### Retrieve the snapshot

ID

You can use the Java [SnapshotUtil](https://iceberg.apache.org/javadoc/1.6.0/org/apache/iceberg/util/SnapshotUtil.html "https://iceberg.apache.org/javadoc/1.6.0/org/apache/iceberg/util/SnapshotUtil.html") class provided by Iceberg to retrieve the Iceberg snapshot
ID, as in the following example.

```
import org.apache.iceberg.Table;
import org.apache.iceberg.aws.glue.GlueCatalog;
import org.apache.iceberg.catalog.TableIdentifier;
import org.apache.iceberg.util.SnapshotUtil;

import java.text.SimpleDateFormat;
import java.util.Date;

Catalog catalog = new GlueCatalog();

Map<String, String> properties = new HashMap<String, String>();
properties.put("warehouse", "s3://amzn-s3-demo-bucket/`my-folder`");
catalog.initialize("my_catalog", properties);

Date date = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss").parse("2022/01/01 00:00:00");
long millis = date.getTime();

TableIdentifier name = TableIdentifier.of("db", "table");
Table table = catalog.loadTable(name);
long oldestSnapshotIdAfter2022 = SnapshotUtil.oldestAncestorAfter(table, millis);
```

## Combine time and

version travel

You can use time travel and version travel syntax in the same query to specify
different timing and versioning conditions, as in the following example.

```
SELECT table1.*, table2.* FROM
  [`db_name`.]`table_name` FOR TIMESTAMP AS OF (current_timestamp - interval '1' day) AS table1
  FULL JOIN
  [`db_name`.]`table_name` FOR VERSION AS OF 5487432386996890161 AS table2
  ON table1.ts = table2.ts
  WHERE (table1.id IS NULL OR table2.id IS NULL)
```
