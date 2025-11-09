Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Getting started with streaming ingestion from Amazon Kinesis Data Streams

This topic describes how to consume streaming data from Kinesis Data Streams using a materialized view.

Setting up Amazon Redshift streaming ingestion involves creating an external schema that
maps to the streaming data source and creating a materialized view that references
the external schema. Amazon Redshift streaming ingestion supports Kinesis Data Streams as a source. As such,
you must have a Kinesis Data Streams source available before configuring streaming ingestion. If
you don't have a source, follow the instructions in the Kinesis documentation at [Getting Started with Amazon Kinesis Data Streams](../../../streams/latest/dev/getting-started.md "../../../streams/latest/dev/getting-started.md")
or create one on the console using the instructions at [Creating a Stream via the AWS
Management Console](../../../streams/latest/dev/how-do-i-create-a-stream.md "../../../streams/latest/dev/how-do-i-create-a-stream.md").

Amazon Redshift streaming ingestion uses a materialized view, which is updated directly from the stream when `REFRESH` is run. The materialized view
maps to the stream data source. You can perform filtering and aggregations on the stream data as part of the materialized-view definition. Your
streaming ingestion materialized view (the _base_ materialized view) can reference only one stream, but you
can create additional materialized views that join with the base materialized view and with other materialized views or tables.

###### Note

_Streaming ingestion and Amazon Redshift Serverless_ - The configuration steps in this topic apply
both to provisioned Amazon Redshift clusters and to Amazon Redshift Serverless. For more information, see [Streaming ingestion behavior and data types](materialized-view-streaming-ingestion.md#materialized-view-streaming-ingestion-limitations "materialized-view-streaming-ingestion.md#materialized-view-streaming-ingestion-limitations").

Assuming you have a Kinesis Data Streams stream available, the first step is to define a schema
in Amazon Redshift with `CREATE EXTERNAL SCHEMA` and to reference a Kinesis Data Streams
resource. Following that, to access data in the stream, define the
`STREAM` in a materialized view. You can store stream records in the
semi-structured `SUPER` format, or define a schema that results in data
converted to Redshift data types. When you query the materialized view,
the returned records are a point-in-time view of the stream.

1. Create an IAM role with a trust policy that allows your Amazon Redshift cluster or Amazon Redshift Serverless workgroup to assume
   the role. For information about how to configure the trust policy for the IAM role, see [Authorizing Amazon Redshift to access other AWS services on your behalf](../mgmt/authorizing-redshift-service.md "../mgmt/authorizing-redshift-service.md"). After it is created, the role
   should have the following IAM policy, which provides permission for communication with the Amazon Kinesis data stream.

**IAM policy for an unencrypted stream from Kinesis Data Streams**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReadStream",
 "Effect": "Allow",
 "Action": [
 "kinesis:DescribeStreamSummary",
 "kinesis:GetShardIterator",
 "kinesis:GetRecords",
 "kinesis:ListShards",
 "kinesis:DescribeStream"
 ],
 "Resource": "arn:aws:kinesis:*:`111122223333`:stream/*"
 },
 {
 "Sid": "ListStream",
 "Effect": "Allow",
 "Action": "kinesis:ListStreams",
 "Resource": "*"
 }
 ]
}`

```

**IAM policy for an encrypted stream from Kinesis Data Streams**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReadStream",
 "Effect": "Allow",
 "Action": [
 "kinesis:DescribeStreamSummary",
 "kinesis:GetShardIterator",
 "kinesis:GetRecords",
 "kinesis:ListShards",
 "kinesis:DescribeStream"
 ],
 "Resource": "arn:aws:kinesis:*:`111122223333`:stream/*"
 },
 {
 "Sid": "DecryptStream",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": "arn:aws:kms:us-east-1:`111122223333`:key/1234abcd-12ab-34cd-56ef-1234567890ab"
 },
 {
 "Sid": "ListStream",
 "Effect": "Allow",
 "Action": "kinesis:ListStreams",
 "Resource": "*"
 }
 ]
}`

```

2. Check your VPC and verify that your Amazon Redshift cluster or Amazon Redshift Serverless has a route to get to
   the Kinesis Data Streams endpoints over the internet using a NAT gateway or internet
   gateway. If you want traffic between Redshift and Kinesis Data Streams to remain within
   the AWS network, consider using a Kinesis Interface VPC Endpoint. For more
   information, see [Using Amazon Kinesis Data Streams
   Kinesis Data Streams with Interface VPC Endpoints](../../../streams/latest/dev/vpc.md "../../../streams/latest/dev/vpc.md").
3. In Amazon Redshift, create an external schema to map the data from Kinesis to a schema.

```
CREATE EXTERNAL SCHEMA kds
FROM KINESIS
IAM_ROLE { default | 'iam-role-arn' };
```

Streaming ingestion for Kinesis Data Streams doesn't require an authentication type. It uses the IAM role
defined in the `CREATE EXTERNAL SCHEMA` statement for making Kinesis Data Streams requests.

Optional: Use the REGION keyword to specify the region where the Amazon Kinesis Data Streams or Amazon MSK stream resides.

```
CREATE EXTERNAL SCHEMA kds
FROM KINESIS
REGION 'us-west-2'
IAM_ROLE { default | 'iam-role-arn' };
```

In this sample, the region specifies the location of the source stream. The IAM_ROLE is a sample. 4. Create a materialized view to consume the stream data. With a statement like the following, if a record can't be parsed, it causes an error. Use a command like this if you don't
want error records to be skipped.

```
CREATE MATERIALIZED VIEW my_view AUTO REFRESH YES AS
SELECT *
FROM kds.my_stream_name;
```

Kinesis stream names are case sensitive and can contain both uppercase and
lowercase letters. To ingest from streams with uppercase names, you can set
the configuration `enable_case_sensitive_identifier` to
`true` at the database level. For more information, see
[Names and identifiers](r_names.md "r_names.md") and
[enable_case_sensitive_identifier](r_enable_case_sensitive_identifier.md "r_enable_case_sensitive_identifier.md").

To turn on auto refresh, use `AUTO REFRESH YES`. The default behavior is manual refresh. Note when you use CAN_JSON_PARSE, it's possible that records
that can't be parsed are skipped.

Metadata columns include the following:

| Metadata column               | Data type                   | Description                                                                              |
| ----------------------------- | --------------------------- | ---------------------------------------------------------------------------------------- |
| approximate_arrival_timestamp | timestamp without time zone | The approximate time that the record was inserted into the Kinesis stream                |
| partition_key                 | varchar(256)                | The key used by Kinesis to assign the record to a shard                                  |
| shard_id                      | char(20)                    | The unique identifier of the shard within the stream from which the record was retrieved |
| sequence_number               | varchar(128)                | The unique identifier of the record from the Kinesis shard                               |
| refresh_time                  | timestamp without time zone | The time the refresh started                                                             |
| kinesis_data                  | varbyte                     | The record from the Kinesis stream                                                       |

It's important to note if you have business logic in your materialized view definition that business-logic errors can cause streaming
ingestion to be blocked in some cases. This might lead to you having to drop and re-create the materialized view. To avoid this, we
recommend that you keep your logic as simple as possible and perform most of your business-logic checks on the data
after it's ingested. 5. Refresh the view, which invokes Redshift to read from the stream and load data into the materialized view.

```
REFRESH MATERIALIZED VIEW my_view;
```

6. Query data in the materialized view.

```
select * from my_view;
```
