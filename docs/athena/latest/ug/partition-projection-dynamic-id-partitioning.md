# Use dynamic ID partitioning

When your data is partitioned by a property with high cardinality or when the values
cannot be known in advance, you can use the `injected` projection type.
Examples of such properties are user names, and IDs of devices or products. When you use
the `injected` projection type to configure a partition key, Athena uses
values from the query itself to compute the set of partitions that will be read.

For Athena to be able to run a query on a table that has a partition key configured
with the `injected` projection type, the following must be true:

- Your query must include at least one value for the partition key.
- The value(s) must be literals or expressions that can be evaluated without
  reading any data.
  If any of these criteria are not met, your query fails with the following
  error:

**`CONSTRAINT_VIOLATION: For the injected projected partition column
 `column_name`, the WHERE clause must contain only
 static equality conditions, and at least one such condition must be
 present.`**

## When to use the `injected` projection type

Imagine you have a data set that consists of events from IoT devices, partitioned
on the devices' IDs. This data set has the following characteristics:

- The device IDs are generated randomly.
- New devices are provisioned frequently.
- There are currently hundreds of thousands of devices, and in the future
  there will be millions.

This data set is difficult to manage using traditional metastores. It is difficult
to keep the partitions in sync between the data storage and the metastore, and
filtering partitions can be slow during query planning. But if you configure a table
to use partition projection and use the `injected` projection type, you
have two advantages: you don't have to manage partitions in the metastore, and your
queries don't have to look up partition metadata.

The following `CREATE TABLE` example creates a table for the device
event data set just described. The table uses the injected projection type.

```
CREATE EXTERNAL TABLE device_events (
  event_time TIMESTAMP,
  data STRING,
  battery_level INT
)
PARTITIONED BY (
  device_id STRING
)
LOCATION "s3://amzn-s3-demo-bucket/`prefix`/"
TBLPROPERTIES (
  "projection.enabled" = "true",
  "projection.device_id.type" = "injected",
  "storage.location.template" = "s3://amzn-s3-demo-bucket/`prefix`/${device_id}"
)
```

The following example query looks up the number of events received from three
specific devices over the course of 12 hours.

```
SELECT device_id, COUNT(*) AS events
FROM device_events
WHERE device_id IN (
  '4a770164-0392-4a41-8565-40ed8cec737e',
  'f71d12cf-f01f-4877-875d-128c23cbde17',
  '763421d8-b005-47c3-ba32-cc747ab32f9a'
)
AND event_time BETWEEN TIMESTAMP '2023-11-01 20:00' AND TIMESTAMP '2023-11-02 08:00'
GROUP BY device_id
```

When you run this query, Athena sees the three values for the
`device_id` partition key and uses them to compute the partition
locations. Athena uses the value for the `storage.location.template`
property to generate the following locations:

- `s3://amzn-s3-demo-bucket/`prefix`/4a770164-0392-4a41-8565-40ed8cec737e`
- `s3://amzn-s3-demo-bucket/`prefix`/f71d12cf-f01f-4877-875d-128c23cbde17`
- `s3://amzn-s3-demo-bucket/`prefix`/763421d8-b005-47c3-ba32-cc747ab32f9a`

If you leave out the `storage.location.template` property from the
partition projection configuration, Athena uses Hive-style partitioning to project
partition locations based on the value in `LOCATION` (for example,
`s3://amzn-s3-demo-bucket/`prefix`/device_id=4a770164-0392-4a41-8565-40ed8cec737e`).
