For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Writes

You can collect time series data from connected devices, IT systems, and industrial
equipment, and write it into Timestream for Live Analytics. Timestream for Live Analytics enables you to write data
points from a single time series and/or data points from many series in a single write
request when the time series belong to the same table. For your convenience,
Timestream for Live Analytics offers you with a flexible schema that auto detects the column names and
data types for your Timestream for Live Analytics tables based on the dimension names and the data types
of the measure values you specify when invoking writes into the database. You can also
write batches of data into Timestream for Live Analytics.

###### Note

Timestream for Live Analytics supports eventual consistency semantics for reads. This means that
when you query data immediately after writing a batch of data into Timestream for Live Analytics,
the query results might not reflect the results of a recently completed write
operation. The results may also include some stale data. Similarly, while writing
time series data with one or more new dimensions, a query can return a partial
subset of columns for a short period of time. If you repeat these query requests
after a short time, the results should return the latest data.

You can write data using the [AWS SDKs](getting-started-sdks.md "getting-started-sdks.md"),
[AWS CLI](Tools.md "Tools.md"), or through [AWS Lambda](Lambda.md "Lambda.md"), [AWS IoT Core](IOT-Core.md "IOT-Core.md"), [Amazon Managed Service for Apache Flink](ApacheFlink.md "ApacheFlink.md"), [Amazon Kinesis](Kinesis.md "Kinesis.md"), [Amazon MSK](MSK.md "MSK.md"), and [Open source Telegraf](Telegraf.md "Telegraf.md").

###### Topics

- [Data types](#writes.data-types "#writes.data-types")
- [No upfront schema definition](#writes.no-upfront-schema "#writes.no-upfront-schema")
- [Writing data (inserts and
  upserts)](#writes.writing-data-inserts-upserts "#writes.writing-data-inserts-upserts")
- [Eventual consistency for
  reads](#writes.eventual-consistency "#writes.eventual-consistency")
- [Batching writes with WriteRecords
  API](writes.md "writes.md")
- [Batch load](batch-load-how.md "batch-load-how.md")
- [Choosing between the WriteRecords API
  operation and batch load](writes.md "writes.md")

## Data types

Timestream for Live Analytics supports the following data types for writes.

| Data type | Description                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BIGINT    | Represents a 64-bit signed integer.                                                                                                                                                                                                                                                                                                                                                                           |
| BOOLEAN   | Represents the two truth values of logic, namely, true, and<br>false.                                                                                                                                                                                                                                                                                                                                         |
| DOUBLE    | 64-bit variable-precision implementing the IEEE Standard 754<br>for Binary Floating-Point Arithmetic.<br>NoteThere are query language functions for<br>`Infinity` and `NaN` double values<br>which can be used in queries. But you cannot write those<br>values to Timestream.                                                                                                                                |
| VARCHAR   | Variable length character data with an optional maximum<br>length. The maximum limit is 2 KB.                                                                                                                                                                                                                                                                                                                 |
| MULTI     | Data type for multi-measure records. This data type includes<br>one or more measures of type `BIGINT`,<br>`BOOLEAN`, `DOUBLE`,<br>`VARCHAR`, and `TIMESTAMP`.                                                                                                                                                                                                                                                 |
| TIMESTAMP | Represents an instance in time using nanosecond precision<br>time in UTC, tracking the time since Unix time. This data type<br>is currently supported only for multi-measure records (i.e.<br>within measure values of type `MULTI`).<br>``YYYY`-`MM`-`DD`<br>`hh`:`mm`:`ss`.`sssssssss``<br>Writes support timestamps in the range `1970-01-01<br>00:00:00.000000000` to `2262-04-11<br>23:47:16.854775807`. |

## No upfront schema definition

Before sending data into Amazon Timestream for Live Analytics, you must create a database and a
table using the AWS Management Console, Timestream for Live Analytics SDKs, or the Timestream for Live Analytics API operations.
For more information, see [Create a database](console_timestream.md#console_timestream.db.using-console "console_timestream.md#console_timestream.db.using-console") and [Create a table](console_timestream.md#console_timestream.table.using-console "console_timestream.md#console_timestream.table.using-console"). While creating the
table, you do not need to define the schema up front. Amazon Timestream for Live Analytics
automatically detects the schema based on the measures and dimensions of the data
points being sent, so you no longer need to alter your schema offline to adapt it to
your rapidly changing time series data.

## Writing data (inserts and

upserts)

The write operation in Amazon Timestream for Live Analytics enables you to insert and
_upsert_ data. By default, writes in Amazon Timestream for Live Analytics follow
the _first writer wins_ semantics, where data is stored as append
only and duplicate records are rejected. While the first writer wins semantics
satisfies the requirements of many time series applications, there are scenarios
where applications need to update existing records in an idempotent manner and/or
write data with the last writer wins semantics, where the record with the highest
version is stored in the service. To address these scenarios, Amazon Timestream for Live Analytics
provides the ability to upsert data. Upsert is an operation that inserts a record
into the system when the record does not exist, or updates the record when one
exists. When the record is updated, it is updated in an idempotent manner.

There isn't a record level operation for deletion. But tables and databases can be
deleted.

**Writing data into the memory store and the magnetic
store**

Amazon Timestream for Live Analytics offers the ability to directly write data into the memory store
and the magnetic store. The memory store is optimized for high throughput data
writes and the magnetic store is optimized for lower throughput writes of late
arrival data.

Late-arriving data is data with a timestamp earlier than the current time and
outside the memory store retention period. You must explicitly enable the ability to
write late-arriving data into the magnetic store by enabling magnetic store writes
for the table. Also, `MagneticStoreRejectedDataLocation` is defined when
a table is created. To write to the magnetic store, callers of
`WriteRecords` must have `S3:PutObject` permissions to the
S3 bucket specified in `MagneticStoreRejectedDataLocation`during table
creation. For more information, see [CreateTable](API_CreateTable.md "API_CreateTable.md"),
[WriteRecords](API_WriteRecords.md "API_WriteRecords.md"), and [PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md").

**Writing data with single-measure records and multi-measure
records**

Amazon Timestream for Live Analytics offers the ability to write data using two types of records,
namely, single-measure records and multi-measure records.

**Single-measure records**

Single-measure records enable you to send a single measure per record. When data
is sent to Timestream for Live Analytics using this format, Timestream for Live Analytics creates one table row per
record. This means that if a device emits 4 metrics and each metric is sent as a
single-measure record, Timestream for Live Analytics will create 4 rows in the table to store this
data, and the device attributes will be repeated for each row. This format is
recommended in cases when you want to monitor a single metric from an application or
when your application does not emit multiple metrics at the same time.

**Multi-measure records**

With multi-measure records, you can store multiple measures in a single table row,
instead of storing one measure per table row. Multi-measure records therefore enable
you to migrate your existing data from relational databases to Amazon Timestream for Live Analytics
with minimal changes.

You can also batch more data in a single write request than single-measure
records. This increases data write throughput and performance, and also reduces the
cost of data writes. This is because batching more data in a write request enables
Amazon Timestream for Live Analytics to identify more repeatable data in a single write request (where
applicable), and charge only once for repeated data.

###### Topics

- [Multi-measure
  records](#writes.writing-data-multi-measure "#writes.writing-data-multi-measure")
- [Writing data with a timestamp
  that exists in the past or in the future](#writes.timestamp-past-future "#writes.timestamp-past-future")

### Multi-measure

records

With multi-measure records, you can store your time-series data in a more
compact format in the memory and magnetic store, which helps lower data storage
costs. Also, the compact data storage lends itself to writing simpler queries
for data retrieval, improves query performance, and lowers the cost of
queries.

Furthermore, multi-measure records also support the TIMESTAMP data type for
storing more than one timestamp in a time-series record. TIMESTAMP attributes in
a multi-measure record support timestamps in future or past. Multi-measure
records therefore help improve performance, cost, and query
simplicity—and offer more flexibility for storing different types of
correlated measures.

###### Benefits

The following are the benefits of using multi-measure records.

- Performance and cost –
  Multi-measure records enable you to write multiple time-series measures
  in a single write request. This increases the write throughput and also
  reduces the cost of writes. With multi-measure records, you can store
  data in a more compact manner, which helps lower the data storage costs.
  The compact data storage of multi-measure records results in less data
  being processed by queries. This is designed to improve the overall
  query performance and help lower the query cost.
- Query simplicity – With
  multi-measure records, you do not need to write complex common table
  expressions (CTEs) in a query to read multiple measures with the same
  timestamp. This is because the measures are stored as columns in a
  single table row. Multi-measure records therefore enable writing simpler
  queries.
- Data modeling flexibility – You
  can write future timestamps into Timestream for Live Analytics by using the TIMESTAMP
  data type and multi-measure records. A multi-measure record can have
  multiple attributes of TIMESTAMP data type, in addition to the time
  field in a record. TIMESTAMP attributes, in a multi-measure record, can
  have timestamps in the future or the past and behave like the time field
  except that Timestream for Live Analytics does not index on the values of type TIMESTAMP
  in a multi-measure record.

###### Use cases

You can use multi-measure records for any time-series application that
generates more than one measurement from the same device at any given time.
The following are some example applications.

- A video streaming platform that generates hundreds of metrics at a
  given time.
- Medical devices that generate measurements such as blood oxygen
  levels, heart rate, and pulse.
- Industrial equipment such as oil rigs that generate metrics,
  temperature, and weather sensors.
- Other applications that are architected with one or more
  microservices.

#### Example: Monitoring

the performance and health of a video streaming application

Consider a video streaming application that is running on 200 EC2
instances. You want to use Amazon Timestream for Live Analytics to store and analyze the
metrics being emitted from the application, so you can understand the
performance and health of your application, quickly identify anomalies,
resolve issues, and discover optimization opportunities.

We will model this scenario with single-measure records and multi-measure
records, and then compare/contrast both approaches. For each approach, we
make the following assumptions.

- Each EC2 instance emits four measures (video_startup_time,
  rebuffering_ratio, video_playback_failures, and average_frame_rate)
  and four dimensions (device_id, device_type, os_version, and region)
  per second.
- You want to store 6 hours of data in the memory store and 6 months
  of data in the magnetic store.
- To identify anomalies, you've set up 10 queries that run every
  minute to identify any unusual activity over the past few minutes.
  You've also built a dashboard with eight widgets that display the
  last 6 hours of data, so that you can effectively monitor your
  application. This dashboard is accessed by five users at any given
  time and is auto-refreshed every hour.

##### Using single

measure records

**Data modeling**: With single measure
records, we will create one record for each of the four measures (video
startup time, rebuffering ratio, video playback failures, and average
frame rate). Each record will have the four dimensions (device_id,
device_type, os_version, and region) and a timestamp.

**Writes**: When you write data into
Amazon Timestream for Live Analytics, the records are constructed as follows.

```
public void writeRecords() {
    System.out.println("Writing records");
    // Specify repeated values for all records
    List<Record> records = new ArrayList<>();
    final long time = System.currentTimeMillis();

    List<Dimension> dimensions = new ArrayList<>();

    final Dimension device_id = new Dimension().withName("device_id").withValue("12345678");
    final Dimension device_type = new Dimension().withName("device_type").withValue("iPhone 11");
    final Dimension os_version = new Dimension().withName("os_version").withValue("14.8");
    final Dimension region = new Dimension().withName("region").withValue("us-east-1");

    dimensions.add(device_id);
    dimensions.add(device_type);
    dimensions.add(os_version);
    dimensions.add(region);

    Record videoStartupTime = new Record()
        .withDimensions(dimensions)
        .withMeasureName("video_startup_time")
        .withMeasureValue("200")
        .withMeasureValueType(MeasureValueType.BIGINT)
        .withTime(String.valueOf(time));
    Record rebufferingRatio = new Record()
        .withDimensions(dimensions)
        .withMeasureName("rebuffering_ratio")
        .withMeasureValue("0.5")
        .withMeasureValueType(MeasureValueType.DOUBLE)
        .withTime(String.valueOf(time));
    Record videoPlaybackFailures = new Record()
        .withDimensions(dimensions)
        .withMeasureName("video_playback_failures")
        .withMeasureValue("0")
        .withMeasureValueType(MeasureValueType.BIGINT)
        .withTime(String.valueOf(time));
    Record averageFrameRate = new Record()
        .withDimensions(dimensions)
        .withMeasureName("average_frame_rate")
        .withMeasureValue("0.5")
        .withMeasureValueType(MeasureValueType.DOUBLE)
        .withTime(String.valueOf(time));

    records.add(videoStartupTime);
    records.add(rebufferingRatio);
    records.add(videoPlaybackFailures);
    records.add(averageFrameRate);

    WriteRecordsRequest writeRecordsRequest = new WriteRecordsRequest()
        .withDatabaseName(DATABASE_NAME)
        .withTableName(TABLE_NAME)
        .withRecords(records);

    try {
      WriteRecordsResult writeRecordsResult = amazonTimestreamWrite.writeRecords(writeRecordsRequest);
      System.out.println("WriteRecords Status: " + writeRecordsResult.getSdkHttpMetadata().getHttpStatusCode());
    } catch (RejectedRecordsException e) {
      System.out.println("RejectedRecords: " + e);
      for (RejectedRecord rejectedRecord : e.getRejectedRecords()) {
        System.out.println("Rejected Index " + rejectedRecord.getRecordIndex() + ": "
            + rejectedRecord.getReason());
      }
      System.out.println("Other records were written successfully. ");
    } catch (Exception e) {
      System.out.println("Error: " + e);
    }
  }
```

When you store single-measure records, the data is logically
represented as follows.

| Time                           | device_id | device_type | os_version | region    | measure_name            | measure_value::bigint | measure_value::double |
| ------------------------------ | --------- | ----------- | ---------- | --------- | ----------------------- | --------------------- | --------------------- |
| 2021-09-07 21:48:44 .000000000 | 12345678  | iPhone 11   | 14.8       | us-east-1 | video_startup_time      | 200                   |                       |
| 2021-09-07 21:48:44 .000000000 | 12345678  | iPhone 11   | 14.8       | us-east-1 | rebuffering_ratio       |                       | 0.5                   |
| 2021-09-07 21:48:44 .000000000 | 12345678  | iPhone 11   | 14.8       | us-east-1 | video_playback_failures | 0                     |                       |
| 2021-09-07 21:48:44 .000000000 | 12345678  | iPhone 11   | 14.8       | us-east-1 | average_frame_rate      |                       | 0.85                  |
| 2021-09-07 21:53:44 .000000000 | 12345678  | iPhone 11   | 14.8       | us-east-1 | video_startup_time      | 500                   |                       |
| 2021-09-07 21:53:44 .000000000 | 12345678  | iPhone 11   | 14.8       | us-east-1 | rebuffering_ratio       |                       | 1.5                   |
| 2021-09-07 21:53:44 .000000000 | 12345678  | iPhone 11   | 14.8       | us-east-1 | video_playback_failures | 10                    |                       |
| 2021-09-07 21:53:44 .000000000 | 12345678  | iPhone 11   | 14.8       | us-east-1 | average_frame_rate      |                       | 0.2                   |

**Queries**: You can write a query that
retrieves all of the data points with the same timestamp received over
the past 15 minutes as follows.

```
with cte_video_startup_time as ( SELECT time, device_id, device_type, os_version, region, measure_value::bigint as video_startup_time FROM table where time >= ago(15m) and measure_name=”video_startup_time”),
cte_rebuffering_ratio as ( SELECT time, device_id, device_type, os_version, region, measure_value::double as rebuffering_ratio FROM table where time >= ago(15m) and measure_name=”rebuffering_ratio”),
cte_video_playback_failures as ( SELECT time, device_id, device_type, os_version, region, measure_value::bigint as video_playback_failures FROM table where time >= ago(15m) and measure_name=”video_playback_failures”),
cte_average_frame_rate as ( SELECT time, device_id, device_type, os_version, region, measure_value::double as average_frame_rate FROM table where time >= ago(15m) and measure_name=”average_frame_rate”)
SELECT a.time, a.device_id, a.os_version, a.region, a.video_startup_time, b.rebuffering_ratio, c.video_playback_failures, d.average_frame_rate FROM cte_video_startup_time a, cte_buffering_ratio b, cte_video_playback_failures c, cte_average_frame_rate d WHERE
a.time = b.time AND a.device_id = b.device_id AND a.os_version = b.os_version AND a.region=b.region AND
a.time = c.time AND a.device_id = c.device_id AND a.os_version = c.os_version AND a.region=c.region AND
a.time = d.time AND a.device_id = d.device_id AND a.os_version = d.os_version AND a.region=d.region
```

**Workload cost**: The cost of this
workload is estimated to be $373.23 per month with single-measure
records

##### Using

multi-measure records

**Data modeling**: With multi-measure
records, we will create one record that contains all four measures
(video startup time, rebuffering ratio, video playback failures, and
average frame rate), all four dimensions (device_id, device_type,
os_version, and region), and a timestamp.

**Writes**: When you write data into
Amazon Timestream for Live Analytics, the records are constructed as follows.

```
public void writeRecords() {
    System.out.println("Writing records");
    // Specify repeated values for all records
    List<Record> records = new ArrayList<>();
    final long time = System.currentTimeMillis();

    List<Dimension> dimensions = new ArrayList<>();

    final Dimension device_id = new Dimension().withName("device_id").withValue("12345678");
    final Dimension device_type = new Dimension().withName("device_type").withValue("iPhone 11");
    final Dimension os_version = new Dimension().withName("os_version").withValue("14.8");
    final Dimension region = new Dimension().withName("region").withValue("us-east-1");

    dimensions.add(device_id);
    dimensions.add(device_type);
    dimensions.add(os_version);
    dimensions.add(region);

    Record videoMetrics = new Record()
        .withDimensions(dimensions)
        .withMeasureName("video_metrics")
        .withTime(String.valueOf(time));
        .withMeasureValueType(MeasureValueType.MULTI)
        .withMeasureValues(
          new MeasureValue()
        	.withName("video_startup_time")
        	.withValue("0")
        	.withValueType(MeasureValueType.BIGINT),
        	new MeasureValue()
		.withName("rebuffering_ratio")
        	.withValue("0.5")
        	.withType(MeasureValueType.DOUBLE),
          new MeasureValue()
        	.withName("video_playback_failures")
        	.withValue("0")
        	.withValueType(MeasureValueType.BIGINT),
		 new MeasureValue()
         	.withName("average_frame_rate")
        	.withValue("0.5")
        	.withValueType(MeasureValueType.DOUBLE))

    records.add(videoMetrics);

    WriteRecordsRequest writeRecordsRequest = new WriteRecordsRequest()
        .withDatabaseName(DATABASE_NAME)
        .withTableName(TABLE_NAME)
        .withRecords(records);

    try {
      WriteRecordsResult writeRecordsResult = amazonTimestreamWrite.writeRecords(writeRecordsRequest);
      System.out.println("WriteRecords Status: " + writeRecordsResult.getSdkHttpMetadata().getHttpStatusCode());
    } catch (RejectedRecordsException e) {
      System.out.println("RejectedRecords: " + e);
      for (RejectedRecord rejectedRecord : e.getRejectedRecords()) {
        System.out.println("Rejected Index " + rejectedRecord.getRecordIndex() + ": "
            + rejectedRecord.getReason());
      }
      System.out.println("Other records were written successfully. ");
    } catch (Exception e) {
      System.out.println("Error: " + e);
    }
  }

```

When you store multi-measure records, the data is logically
represented as follows.

| Time                           | device_id | device_type | os_version | region    | measure_name  | video_startup_time | rebuffering_ratio | video\_ playback_failures | average_frame_rate |
| ------------------------------ | --------- | ----------- | ---------- | --------- | ------------- | ------------------ | ----------------- | ------------------------- | ------------------ |
| 2021-09-07 21:48:44 .000000000 | 12345678  | iPhone 11   | 14.8       | us-east-1 | video_metrics | 200                | 0.5               | 0                         | 0.85               |
| 2021-09-07 21:53:44 .000000000 | 12345678  | iPhone 11   | 14.8       | us-east-1 | video_metrics | 500                | 1.5               | 10                        | 0.2                |

**Queries**: You can write a query that
retrieves all of the data points with the same timestamp received over
the past 15 minutes as follows.

```
SELECT time, device_id, device_type, os_version, region, video_startup_time, rebuffering_ratio, video_playback_failures, average_frame_rate FROM table where time >= ago(15m)
```

**Workload cost**: The cost of workload
is estimated to be $127.43 with multi-measure records.

###### Note

In this case, using multi-measure records reduces the overall
estimated monthly spend by 2.5x, with the data writes cost reduced
by 3.3x, the storage cost reduced by 3.3x, and the query cost
reduced by 1.2x.

### Writing data with a timestamp

that exists in the past or in the future

Timestream for Live Analytics offers the ability to write data with a timestamp that lies
outside of the memory store retention window through a couple different
mechanisms.

- Magnetic store writes – You can
  write late-arriving data directly into the magnetic store through
  magnetic store writes. To use magnetic store writes, you must first
  enable magnetic store writes for a table. You can then ingest data into
  the table using the same mechanism used for writing data into the memory
  store. Amazon Timestream for Live Analytics will automatically write the data into the
  magnetic store based on its timestamp.

###### Note

The write-to-read latency for the magnetic store can be up to 6
hours, unlike writing data into the memory store, where the
write-to-read latency is in the sub-second range.

- TIMESTAMP data type for measures
  – You can use the TIMESTAMP data type to store data from the
  past, present, or future. A multi-measure record can have multiple
  attributes of TIMESTAMP data type, in addition to the time field in a
  record. TIMESTAMP attributes, in a multi-measure record, can have
  timestamps in the future or the past and behave like the time field
  except that Timestream for Live Analytics does not index on the values of type TIMESTAMP
  in a multi-measure record.

###### Note

The TIMESTAMP data type is supported only for multi-measure
records.

## Eventual consistency for

reads

Timestream for Live Analytics supports eventual consistency semantics for reads. This means that
when you query data immediately after writing a batch of data into Timestream for Live Analytics,
the query results might not reflect the results of a recently completed write
operation. If you repeat these query requests after a short time, the results should
return the latest data.
