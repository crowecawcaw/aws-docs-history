Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Ingesting streaming data using Kinesis

This procedure demonstrates how to ingest data from a Kinesis stream named _ev_station_data_, which contains
consumption data from different EV charging stations, in JSON format. The schema is well defined. The example
shows how to store the data as raw JSON and also how to convert the JSON data to Amazon Redshift data types as it's ingested.

**Producer setup**

1. Using Amazon Kinesis Data Streams, follow the steps to create a stream named `ev_station_data`. Choose **On-demand** for
   the **Capacity mode**. For more information, see [Creating a Stream via the AWS Management Console](../../../streams/latest/dev/how-do-i-create-a-stream.md "../../../streams/latest/dev/how-do-i-create-a-stream.md").
2. The [Amazon Kinesis Data Generator](https://awslabs.github.io/amazon-kinesis-data-generator/web/producer.html? "https://awslabs.github.io/amazon-kinesis-data-generator/web/producer.html?") can help you generate
   test data for use with your stream. Follow the steps detailed in the tool to get started, and use the following data template
   for generating your data:

```
{

   "_id" : "{{random.uuid}}",
   "clusterID": "{{random.number(
        {   "min":1,
            "max":50
        }
    )}}",
    "connectionTime": "{{date.now("YYYY-MM-DD HH:mm:ss")}}",
    "kWhDelivered": "{{commerce.price}}",
    "stationID": "{{random.number(
        {   "min":1,
            "max":467
        }
    )}}",
      "spaceID": "{{random.word}}-{{random.number(
        {   "min":1,
            "max":20
        }
    )}}",

   "timezone": "America/Los_Angeles",
   "userID": "{{random.number(
        {   "min":1000,
            "max":500000
        }
    )}}"
}
```

Each JSON object in the stream data has the following properties:

```
{
    "_id": "12084f2f-fc41-41fb-a218-8cc1ac6146eb",
    "clusterID": "49",
    "connectionTime": "2022-01-31 13:17:15",
    "kWhDelivered": "74.00",
    "stationID": "421",
    "spaceID": "technologies-2",
    "timezone": "America/Los_Angeles",
    "userID": "482329"
}
```

**Amazon Redshift setup**

These steps show you how to configure the materialized view to ingest data.

1. Create an external schema to map the data from Kinesis to a Redshift
   object.

```
CREATE EXTERNAL SCHEMA evdata FROM KINESIS
IAM_ROLE 'arn:aws:iam::0123456789:role/redshift-streaming-role';
```

For information about how to configure the IAM role, see [Getting started with streaming ingestion from Amazon Kinesis Data Streams](materialized-view-streaming-ingestion-getting-started.md "materialized-view-streaming-ingestion-getting-started.md"). 2. Create a materialized view to consume the stream data. The following example shows how to
define a materialized view to ingest the JSON formatted data from a Kinesis
stream.

First, store stream records in semi-structured SUPER format. In this example, the JSON source is stored in Redshift without converting to Redshift types.

```
CREATE MATERIALIZED VIEW ev_station_data AS
    SELECT approximate_arrival_timestamp,
    partition_key,
    shard_id,
    sequence_number,
    case when can_json_parse(kinesis_data) then json_parse(kinesis_data) else null end as payload,
    case when not can_json_parse(kinesis_data) then kinesis_data else null end as failed_payload
    FROM evdata."ev_station_data" ;
```

**Query the stream**

1. Enable case sensitive SUPER attributes using the command below. Amazon Redshift
   is case insensitive by default, so in order to access case sensitive SUPER
   attributes, you need to enable this functionality.

```
SET enable_case_sensitive_super_attribute to TRUE;
```

2. Refresh the materialized view with the following command in order to pull data
   from the stream.

```
REFRESH MATERIALIZED VIEW ev_station_data;
```

3. Query the refreshed materialized view to get usage statistics.

```
SELECT e.payload.connectionTime::date as connectiontime
,SUM(e.payload.kWhDelivered::decimal(10,2)) AS Energy_Consumed
,count(distinct e.payload.userID) AS #Users
from ev_station_data as e
group by connectiontime
order by 1 desc;
```

4. View results.

```
connectiontime        energy_consumed    #users
2022-02-08                 4139          10
2022-02-09                 5571          10
2022-02-10                 8697          20
2022-02-11                 4408          10
2022-02-12                 4257          10
2022-02-23                 6861          10
```
