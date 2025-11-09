# IAM permissions required for KCL

consumer applications

You must add the following permissions to the IAM role or user associated with your
KCL consumer application.

Security best practices for AWS dictate the use of fine-grained permissions to
control access to different resources. AWS Identity and Access Management (IAM) lets you manage users
and user permissions in AWS. An IAM policy explicitly lists actions that are allowed
and the resources on which the actions are applicable.

The following table shows the minimum IAM permissions generally required for KCL
consumer applications:

| Minimum IAM permissions for KCL consumer applications | Service                                                                                                               | Actions                                                                                                                                                                                                                                                    | Resources (ARNs)                                                                                                                                                                                                   | Purpose |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| Amazon Kinesis Data Streams                           | `DescribeStream`<br>`DescribeStreamSummary`<br>`RegisterStreamConsumer`                                               | Kinesis data stream from which your KCL application will<br>process the data.`arn:aws:kinesis:region:account:stream/StreamName`                                                                                                                            | Before attempting to read records, the consumer checks if the data<br>stream exists, if it's active, and if the shards are contained in<br>the data stream.<br>Registers consumers to a shard.                     |
| Amazon Kinesis Data Streams                           | `GetRecords`<br>`GetShardIterator`<br>`ListShards`                                                                    | Kinesis data stream from which your KCL application will process the data.`arn:aws:kinesis:region:account:stream/StreamName`                                                                                                                               | Reads records from a shard.                                                                                                                                                                                        |
| Amazon Kinesis Data Streams                           | `SubscribeToShard`<br>`DescribeStreamConsumer`                                                                        | Kinesis data stream from which your KCL application will<br>process the data. Add this action only if you use enhanced fan-out<br>(EFO) consumers.<br>`arn:aws:kinesis:region:account:stream/StreamName/consumer/*`                                        | Subscribes to a shard for enhanced fan-out (EFO) consumers.                                                                                                                                                        |
| Amazon DynamoDB                                       | `CreateTable`<br>`DescribeTable`<br>`UpdateTable`<br>`Scan`<br>`GetItem`<br>`PutItem`<br>`UpdateItem`<br>`DeleteItem` | Lease table (metadata table in DynamoDB created by<br>KCL.<br>`arn:aws:dynamodb:region:account:table/KCLApplicationName`                                                                                                                                   | These actions are required for KCL to manag the lease table<br>created in DynamoDB.                                                                                                                                |
| Amazon DynamoDB                                       | `CreateTable`<br>`DescribeTable`<br>`Scan`<br>`GetItem`<br>`PutItem`<br>`UpdateItem`<br>`DeleteItem`                  | Worker metrics and coordinator state table (metadata tables in<br>DynamoDB) created by KCL.<br>`arn:aws:dynamodb:region:account:table/KCLApplicationName-WorkerMetricStats`<br>`arn:aws:dynamodb:region:account:table/KCLApplicationName-CoordinatorState` | Thess actions are required for KCL to manage the worker metrics<br>and coordinator state metadata tables in DynamoDB.                                                                                              |
| Amazon DynamoDB                                       | `Query`                                                                                                               | Global secondary index on the lease table.<br>`arn:aws:dynamodb:region:account:table/KCLApplicationName/index/*`                                                                                                                                           | This action is required for KCL to read the global secondary index<br>of the lease table created in DynamoDB.                                                                                                      |
| Amazon CloudWatch                                     | `PutMetricData`                                                                                                       | \*                                                                                                                                                                                                                                                         | Upload metrics to CloudWatch that are useful for monitoring the<br>application. The asterisk (\*) is used because there is no spcific<br>resource in CloudWatch on which the `PutMetricData` action is<br>invoked. |

###### Note

Replace "region," "account," "StreamName," and "KCLApplicationName" in the ARNs
with your own AWS Region, AWS account number, Kinesis data stream name, and
KCL application name respectively. KCL 3.x creates two more metadata tables
in DynamoDB. For details about DynamoDB metadata tables created by KCL, see [DynamoDB metadata tables and load balancing in
KCL](kcl-dynamoDB.md "kcl-dynamoDB.md"). If you use configurations
to customize names of the metadata tables created by KCL, use those
specified table names instead of KCL application name.

The following is an example policy document for a KCL consumer application.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kinesis:DescribeStream",
 "kinesis:DescribeStreamSummary",
 "kinesis:RegisterStreamConsumer",
 "kinesis:GetRecords",
 "kinesis:GetShardIterator",
 "kinesis:ListShards"
 ],
 "Resource": "arn:aws:kinesis:`us-east-1`:`123456789012`:stream/`STREAM_NAME`"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kinesis:SubscribeToShard",
 "kinesis:DescribeStreamConsumer"
 ],
 "Resource": "arn:aws:kinesis:`us-east-1`:`123456789012`:stream/`STREAM_NAME`/consumer/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:CreateTable",
 "dynamodb:DescribeTable",
 "dynamodb:UpdateTable",
 "dynamodb:GetItem",
 "dynamodb:UpdateItem",
 "dynamodb:PutItem",
 "dynamodb:DeleteItem",
 "dynamodb:Scan"
 ],
 "Resource": [
 "arn:aws:dynamodb:`us-east-1`:`123456789012`:table/`KCL_APPLICATION_NAME`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:CreateTable",
 "dynamodb:DescribeTable",
 "dynamodb:GetItem",
 "dynamodb:UpdateItem",
 "dynamodb:PutItem",
 "dynamodb:DeleteItem",
 "dynamodb:Scan"
 ],
 "Resource": [
 "arn:aws:dynamodb:`us-east-1`:`123456789012`:table/`KCL_APPLICATION_NAME-WorkerMetricStats`",
 "arn:aws:dynamodb:`us-east-1`:`123456789012`:table/`KCL_APPLICATION_NAME-CoordinatorState`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:Query"
 ],
 "Resource": [
 "arn:aws:dynamodb:`us-east-1`:`123456789012`:table/`KCL_APPLICATION_NAME`/index/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": "*"
 }
 ]
}`

```

Before you use this example policy, check the following items:

- Replace REGION with your AWS Region (for example,
  us-east-1).
- Replace ACCOUNT_ID with your AWS account ID.
- Replace STREAM_NAME with the name of your Kinesis data stream.
- Replace CONSUMER_NAME with the name of your consumer, typically your
  application name when using KCL.
- Replace KCL_APPLICATION_NAME with the name of your KCL application.
