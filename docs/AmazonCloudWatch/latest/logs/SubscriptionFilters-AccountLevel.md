# Account-level subscription

filters

###### Important

There is a risk of causing an infinite recursive loop with subscription filters
that can lead to a large increase in ingestion billing if not addressed. To mitigate
this risk, we recommend that you use selection criteria in your account-level
subscription filters to exclude log groups that ingest log data from resources that
are part of the subscription delivery workflow. For more information on this problem
and determining which log groups to exclude, see [Log recursion prevention](Subscriptions-recursion-prevention.md "Subscriptions-recursion-prevention.md").

You can set an account-level subscription policy that includes a subset of log groups
in the account. The account subscription policy can work with Amazon Kinesis Data Streams, AWS Lambda, or
Amazon Data Firehose. Logs sent to a service through an account-level subscription policy are
base64 encoded and compressed with the gzip format. This section provides examples you
can follow to create an account-level subscription for Amazon Kinesis Data Streams, Lambda, and Firehose.

###### Note

To view a list of all subscription filter policies in your account, use the
`describe-account-policies` command with a value of
`SUBSCRIPTION_FILTER_POLICY` for the `--policy-type`
parameter. For more information, see [describe-account-policies¶](../../../cli/latest/reference/logs/describe-account-policies.md "../../../cli/latest/reference/logs/describe-account-policies.md").

###### Examples

- [Example 1: Subscription
  filters with Amazon Kinesis Data Streams](#DestinationKinesisExample-AccountLevel "#DestinationKinesisExample-AccountLevel")
- [Example 2: Subscription filters
  with AWS Lambda](#LambdaFunctionExample-AccountLevel "#LambdaFunctionExample-AccountLevel")
- [Example 3: Subscription filters with
  Amazon Data Firehose](#FirehoseExample-AccountLevel "#FirehoseExample-AccountLevel")

## Example 1: Subscription

filters with Amazon Kinesis Data Streams

Before you create a Amazon Kinesis Data Streams data stream to use with an account-level subscription
policy, calculate the volume of log data that will be generated. Be sure to create a
stream with enough shards to handle this volume. If a stream doesn't have enough
shards, it is throttled. For more information about stream volume limits, see [Quotas and Limits](../../../streams/latest/dev/service-sizes-and-limits.md "../../../streams/latest/dev/service-sizes-and-limits.md") in the Amazon Kinesis Data Streams documentation.

###### Warning

Because the log events of multiple log groups are forwarded to the
destination, there is a risk of throttling. Throttled deliverables are retried
for up to 24 hours. After 24 hours, the failed deliverables are dropped.

To mitigate the risk of throttling, you can take the following steps:

- Monitor your Amazon Kinesis Data Streams stream with CloudWatch metrics. This helps you identify
  throttling and adjust your configuration accordingly. For example, the
  `DeliveryThrottling` metric tracks the number of log
  events for which CloudWatch Logs was throttled when forwarding data to the
  subscription destination. For more information, see [Monitoring with CloudWatch metrics](CloudWatch-Logs-Monitoring-CloudWatch-Metrics.md "CloudWatch-Logs-Monitoring-CloudWatch-Metrics.md").
- Use the on-demand capacity mode for your stream in Amazon Kinesis Data Streams. On-demand
  mode instantly accommodates your workloads as they ramp up or down. For
  more information, see [On-demand mode](../../../streams/latest/dev/how-do-i-size-a-stream.md#ondemandmode "../../../streams/latest/dev/how-do-i-size-a-stream.md#ondemandmode").
- Restrict your CloudWatch Logs subscription filter pattern to match the capacity
  of your stream in Amazon Kinesis Data Streams. If you are sending too much data to the stream,
  you might need to reduce the filter size or adjust the filter
  criteria.

The following example uses an account-level subscription policy to forward all log
events to a stream in Amazon Kinesis Data Streams. The filter pattern matches any log events with the text
`Test` and forwards them to the stream in Amazon Kinesis Data Streams.

###### To create an account-level subscription policy for Amazon Kinesis Data Streams

1. Create a destination stream using the following command:

```
`$` `C:\>`  aws kinesis create-stream —stream-name "TestStream" —shard-count 1
```

2. Wait a few minutes for the stream to become active. You can verify whether
   the stream is active by using the [describe-stream](../../../cli/latest/reference/kinesis/describe-stream.md "../../../cli/latest/reference/kinesis/describe-stream.md")
   command to check the **StreamDescription.StreamStatus**
   property.

```
`aws kinesis describe-stream --stream-name "TestStream"`
```

The following is example output:

```
{
    "StreamDescription": {
        "StreamStatus": "ACTIVE",
        "StreamName": "TestStream",
        "StreamARN": "arn:aws:kinesis:`region`:123456789012:stream/TestStream",
        "Shards": [
            {
                "ShardId": "shardId-000000000000",
                "HashKeyRange": {
                    "EndingHashKey": "EXAMPLE8463463374607431768211455",
                    "StartingHashKey": "0"
                },
                "SequenceNumberRange": {
                    "StartingSequenceNumber":
                    "EXAMPLE688818456679503831981458784591352702181572610"
                }
            }
        ]
    }
}
```

3. Create the IAM role that will grant CloudWatch Logs permission to put data into
   your stream. First, you'll need to create a trust policy in a file (for
   example, `~/TrustPolicyForCWL-Kinesis.json`). Use a text
   editor to create this policy.

This policy includes a `aws:SourceArn` global condition context
key to help prevent the confused deputy security problem. For more
information, see [Confused deputy prevention](Subscriptions-confused-deputy.md "Subscriptions-confused-deputy.md").

```
{
  "Statement": {
    "Effect": "Allow",
    "Principal": { "Service": "logs.amazonaws.com" },
    "Action": "sts:AssumeRole",
    "Condition": {
        "StringLike": { "aws:SourceArn": "arn:aws:logs:`region`:123456789012:*" }
     }
   }
}
```

4. Use the **create-role** command to create the IAM role,
   specifying the trust policy file. Note the returned
   **Role.Arn** value, as you will also need it for a
   later step:

```
`aws iam create-role --role-name `CWLtoKinesisRole` --assume-role-policy-document file://~/`TrustPolicyForCWL-Kinesis.json``
```

The following is an example of the output.

```
`{
 "Role": {
 "AssumeRolePolicyDocument": {
 "Statement": {
 "Action": "sts:AssumeRole",
 "Effect": "Allow",
 "Principal": {
 "Service": "logs.amazonaws.com"
 },
 "Condition": {
 "StringLike": {
 "aws:SourceArn": { "arn:aws:logs:`region`:`123456789012`:*" }
 }
 }
 }
 },
 "RoleId": "EXAMPLE450GAB4HC5F431",
 "CreateDate": "2023-05-29T13:46:29.431Z",
 "RoleName": "CWLtoKinesisRole",
 "Path": "/",
 "Arn": "arn:aws:iam::`123456789012`:role/CWLtoKinesisRole"
 }
}`
```

5. Create a permissions policy to define what actions CloudWatch Logs can do on your
   account. First, you'll create a permissions policy in a file (for example,
   `~/PermissionsForCWL-Kinesis.json`). Use a text
   editor to create this policy. Don't use the IAM console to create
   it.

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "kinesis:PutRecord",
      "Resource": "arn:aws:kinesis:`region`:`123456789012`:stream/TestStream"
    }
  ]
}
```

6. Associate the permissions policy with the role using the following [put-role-policy](../../../cli/latest/reference/iam/put-role-policy.md "../../../cli/latest/reference/iam/put-role-policy.md")
   command:

```
`aws iam put-role-policy --role-name `CWLtoKinesisRole` --policy-name Permissions-Policy-For-CWL --policy-document file://~/`PermissionsForCWL-Kinesis.json``
```

7. After the stream is in the **Active** state and you have
   created the IAM role, you can create the CloudWatch Logs subscription filter policy.
   The policy immediately starts the flow of real-time log data to your stream.
   In this example, all log events that contain the string `ERROR`
   are streamed, except those in the log groups named
   `LogGroupToExclude1` and
   `LogGroupToExclude2`.

```
aws logs put-account-policy \
    --policy-name "ExamplePolicy" \
    --policy-type "SUBSCRIPTION_FILTER_POLICY" \
    --policy-document '{"RoleArn":"arn:aws:iam::`123456789012`:role/CWLtoKinesisRole", "DestinationArn":"arn:aws:kinesis:`region`:`123456789012`:stream/TestStream", "FilterPattern": "Test", "Distribution": "Random"}' \
    --selection-criteria 'LogGroupName NOT IN ["LogGroupToExclude1", "LogGroupToExclude2"]' \
    --scope "ALL"
```

8. After you set up the subscription filter, CloudWatch Logs forwards all the incoming
   log events that match the filter pattern and selection criteria to your
   stream.

The `selection-criteria` field is optional, but is important
for excluding log groups that can cause an infinite log recursion from a
subscription filter. For more information about this issue and determining
which log groups to exclude, see [Log recursion prevention](Subscriptions-recursion-prevention.md "Subscriptions-recursion-prevention.md"). Currently, NOT IN
is the only supported operator for `selection-criteria`.

You can verify that the flow of log events by by using a Amazon Kinesis Data Streams shard
iterator and using the Amazon Kinesis Data Streams `get-records` command to fetch some
Amazon Kinesis Data Streams records::

```
`aws kinesis get-shard-iterator --stream-name TestStream --shard-id shardId-000000000000 --shard-iterator-type TRIM_HORIZON`
```

```
`{
 "ShardIterator":
 "AAAAAAAAAAFGU/kLvNggvndHq2UIFOw5PZc6F01s3e3afsSscRM70JSbjIefg2ub07nk1y6CDxYR1UoGHJNP4m4NFUetzfL+wev+e2P4djJg4L9wmXKvQYoE+rMUiFq+p4Cn3IgvqOb5dRA0yybNdRcdzvnC35KQANoHzzahKdRGb9v4scv+3vaq+f+OIK8zM5My8ID+g6rMo7UKWeI4+IWiK2OSh0uP"
}`
```

```
`aws kinesis get-records --limit 10 --shard-iterator "AAAAAAAAAAFGU/kLvNggvndHq2UIFOw5PZc6F01s3e3afsSscRM70JSbjIefg2ub07nk1y6CDxYR1UoGHJNP4m4NFUetzfL+wev+e2P4djJg4L9wmXKvQYoE+rMUiFq+p4Cn3IgvqOb5dRA0yybNdRcdzvnC35KQANoHzzahKdRGb9v4scv+3vaq+f+OIK8zM5My8ID+g6rMo7UKWeI4+IWiK2OSh0uP"`
```

You might need to use this command a few times before Amazon Kinesis Data Streams starts to
return data.

You should expect to see a response with an array of records. The
**Data** attribute in a Amazon Kinesis Data Streams record is base64 encoded
and compressed with the gzip format. You can examine the raw data from the
command line using the following Unix commands:

```
echo -n "<Content of Data>" | base64 -d | zcat
```

The base64 decoded and decompressed data is formatted as JSON with the
following structure:

```
`{
 "messageType": "DATA_MESSAGE",
 "owner": "123456789012",
 "logGroup": "Example1",
 "logStream": "logStream1",
 "subscriptionFilters": [
 "ExamplePolicy"
 ],
 "logEvents": [
 {
 "id": "31953106606966983378809025079804211143289615424298221568",
 "timestamp": 1432826855000,
 "message": "{\"eventVersion\":\"1.03\",\"userIdentity\":{\"type\":\"Root\"}"
 },
 {
 "id": "31953106606966983378809025079804211143289615424298221569",
 "timestamp": 1432826855000,
 "message": "{\"eventVersion\":\"1.03\",\"userIdentity\":{\"type\":\"Root\"}"
 },
 {
 "id": "31953106606966983378809025079804211143289615424298221570",
 "timestamp": 1432826855000,
 "message": "{\"eventVersion\":\"1.03\",\"userIdentity\":{\"type\":\"Root\"}"
 }
 ],
 "policyLevel": "ACCOUNT_LEVEL_POLICY"
}`
```

The key elements in the data structure are the following:

**messageType**

Data messages will use the "DATA_MESSAGE" type. Sometimes
CloudWatch Logs might emit Amazon Kinesis Data Streams records with a "CONTROL_MESSAGE" type,
mainly for checking if the destination is reachable.

**owner**

The AWS Account ID of the originating log data.

**logGroup**

The log group name of the originating log data.

**logStream**

The log stream name of the originating log data.

**subscriptionFilters**

The list of subscription filter names that matched with the
originating log data.

**logEvents**

The actual log data, represented as an array of log event
records. The "id" property is a unique identifier for every log
event.

**policyLevel**

The level at which the policy was enforced.
"ACCOUNT_LEVEL_POLICY" is the `policyLevel` for an
account-level subscription filter policy.

## Example 2: Subscription filters

with AWS Lambda

In this example, you'll create a CloudWatch Logs account-level subscription filter policy
that sends log data to your AWS Lambda function.

###### Warning

Before you create the Lambda function, calculate the volume of log data that
will be generated. Be sure to create a function that can handle this volume. If
the function can't handle the volume, the log stream will be throttled. Because
the log events of either all log groups or a subset of the account's log groups
are forwarded to the destination, there is a risk of throttling. For more
information about Lambda limits, see [AWS Lambda Limits](../../../lambda/latest/dg/limits.md "../../../lambda/latest/dg/limits.md").

###### To create an account-level subscription filter policy for Lambda

1. Create the AWS Lambda function.

Ensure that you have set up the Lambda execution role. For more
information, see [Step 2.2: Create an IAM Role (execution role)](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md") in the
_AWS Lambda Developer Guide_. 2. Open a text editor and create a file named
`helloWorld.js` with the following contents:

```
var zlib = require('zlib');
exports.handler = function(input, context) {
    var payload = Buffer.from(input.awslogs.data, 'base64');
    zlib.gunzip(payload, function(e, result) {
        if (e) {
            context.fail(e);
        } else {
            result = JSON.parse(result.toString());
            console.log("Event Data:", JSON.stringify(result, null, 2));
            context.succeed();
        }
    });
};
```

3. Zip the file helloWorld.js and save it with the name
   `helloWorld.zip`.
4. Use the following command, where the role is the Lambda execution role you
   set up in the first step:

```
aws lambda create-function \
    --function-name helloworld \
    --zip-file fileb://file-path/helloWorld.zip \
    --role lambda-execution-role-arn \
    --handler helloWorld.handler \
    --runtime nodejs18.x
```

5. Grant CloudWatch Logs the permission to execute your function. Use the following
   command, replacing the placeholder account with your own account.

```
aws lambda add-permission \
    --function-name "helloworld" \
    --statement-id "helloworld" \
    --principal "logs.amazonaws.com" \
    --action "lambda:InvokeFunction" \
    --source-arn "arn:aws:logs:`region`:`123456789012`:log-group:*" \
    --source-account "123456789012"
```

6. Create an account-level subscription filter policy using the following
   command, replacing the placeholder account with your own account. In this
   example, all log events that contain the string `ERROR` are
   streamed, except those in the log groups named
   `LogGroupToExclude1` and
   `LogGroupToExclude2`.

```
aws logs put-account-policy \
    --policy-name "ExamplePolicyLambda" \
    --policy-type "SUBSCRIPTION_FILTER_POLICY" \
    --policy-document '{"DestinationArn":"arn:aws:lambda:`region`:`123456789012`:function:helloWorld", "FilterPattern": "Test", "Distribution": "Random"}' \
    --selection-criteria 'LogGroupName NOT IN ["LogGroupToExclude1", "LogGroupToExclude2"]' \
    --scope "ALL"
```

After you set up the subscription filter, CloudWatch Logs forwards all the incoming
log events that match the filter pattern and selection criteria to your
stream.

The `selection-criteria` field is optional, but is important
for excluding log groups that can cause an infinite log recursion from a
subscription filter. For more information about this issue and determining
which log groups to exclude, see [Log recursion prevention](Subscriptions-recursion-prevention.md "Subscriptions-recursion-prevention.md"). Currently, NOT IN
is the only supported operator for `selection-criteria`. 7. (Optional) Test using a sample log event. At a command prompt, run the
following command, which will put a simple log message into the subscribed
stream.

To see the output of your Lambda function, navigate to the Lambda function
where you will see the output in /aws/lambda/helloworld:

```
aws logs put-log-events --log-group-name Example1 --log-stream-name logStream1 --log-events "[{\"timestamp\":`CURRENT TIMESTAMP MILLIS` , \"message\": \"Simple Lambda Test\"}]"
```

You should expect to see a response with an array of Lambda. The
**Data** attribute in the Lambda record is base64
encoded and compressed with the gzip format. The actual payload that Lambda
receives is in the following format `{ "awslogs": {"data":
 "BASE64ENCODED_GZIP_COMPRESSED_DATA"} }` You can examine the raw
data from the command line using the following Unix commands:

```
echo -n "<BASE64ENCODED_GZIP_COMPRESSED_DATA>" | base64 -d | zcat
```

The base64 decoded and decompressed data is formatted as JSON with the
following structure:

```
{
    "messageType": "DATA_MESSAGE",
    "owner": "123456789012",
    "logGroup": "Example1",
    "logStream": "logStream1",
    "subscriptionFilters": [
        "ExamplePolicyLambda"
    ],
    "logEvents": [
        {
            "id": "31953106606966983378809025079804211143289615424298221568",
            "timestamp": 1432826855000,
            "message": "{\"eventVersion\":\"1.03\",\"userIdentity\":{\"type\":\"Root\"}"
        },
        {
            "id": "31953106606966983378809025079804211143289615424298221569",
            "timestamp": 1432826855000,
            "message": "{\"eventVersion\":\"1.03\",\"userIdentity\":{\"type\":\"Root\"}"
        },
        {
            "id": "31953106606966983378809025079804211143289615424298221570",
            "timestamp": 1432826855000,
            "message": "{\"eventVersion\":\"1.03\",\"userIdentity\":{\"type\":\"Root\"}"
        }
    ],
    "policyLevel": "ACCOUNT_LEVEL_POLICY"
}
```

###### Note

The account-level subscription filter will not be applied to the
destination Lambda function’s log group. This is to prevent an infinite
log recursion that can lead to an increase in ingestion billing. For
more information about this problem, see [Log recursion prevention](Subscriptions-recursion-prevention.md "Subscriptions-recursion-prevention.md") .

The key elements in the data structure are the following:

**messageType**

Data messages will use the "DATA_MESSAGE" type. Sometimes
CloudWatch Logs might emit Amazon Kinesis Data Streams records with a "CONTROL_MESSAGE" type,
mainly for checking if the destination is reachable.

**owner**

The AWS Account ID of the originating log data.

**logGroup**

The log group name of the originating log data.

**logStream**

The log stream name of the originating log data.

**subscriptionFilters**

The list of subscription filter names that matched with the
originating log data.

**logEvents**

The actual log data, represented as an array of log event
records. The "id" property is a unique identifier for every log
event.

**policyLevel**

The level at which the policy was enforced.
"ACCOUNT_LEVEL_POLICY" is the `policyLevel` for an
account-level subscription filter policy.

## Example 3: Subscription filters with

Amazon Data Firehose

In this example, you'll create a CloudWatch Logs account-level subscription filter policy
that sends incoming log events that match your defined filters to your Amazon Data Firehose
delivery stream. Data sent from CloudWatch Logs to Amazon Data Firehose is already compressed with gzip
level 6 compression, so you do not need to use compression within your Firehose
delivery stream. You can then use the decompression feature in Firehose to
automatically decompress the logs. For more information, see [Writing to Kinesis Data Firehose Using CloudWatch Logs](../../../firehose/latest/dev/writing-with-cloudwatch-logs.md "../../../firehose/latest/dev/writing-with-cloudwatch-logs.md").

###### Warning

Before you create the Firehose stream, calculate the volume of log data that will
be generated. Be sure to create a Firehose stream that can handle this volume. If
the stream cannot handle the volume, the log stream will be throttled. For more
information about Firehose stream volume limits, see [Amazon Data Firehose Data Limits](../../../firehose/latest/dev/limits.md "../../../firehose/latest/dev/limits.md").

###### To create a subscription filter for Firehose

1. Create an Amazon Simple Storage Service (Amazon S3) bucket. We recommend that you use a bucket that
   was created specifically for CloudWatch Logs. However, if you want to use an existing
   bucket, skip to step 2.

Run the following command, replacing the placeholder Region with the
Region you want to use:

```
aws s3api create-bucket --bucket `amzn-s3-demo-bucket2` --create-bucket-configuration LocationConstraint=`region`
```

The following is example output:

```
`{
 "Location": "/`amzn-s3-demo-bucket2`"
}`
```

2. Create the IAM role that grants Amazon Data Firehose permission to put data into
   your Amazon S3 bucket.

For more information, see [Controlling Access with
Amazon Data Firehose](../../../firehose/latest/dev/controlling-access.md "../../../firehose/latest/dev/controlling-access.md") in the _Amazon Data Firehose Developer Guide_.

First, use a text editor to create a trust policy in a file
`~/TrustPolicyForFirehose.json` as follows:

```
{
  "Statement": {
    "Effect": "Allow",
    "Principal": { "Service": "firehose.amazonaws.com" },
    "Action": "sts:AssumeRole"
    }
}
```

3. Use the **create-role** command to create the IAM role,
   specifying the trust policy file. Keep a note of the returned
   **Role.Arn** value, as you will need it in a later
   step:

```
aws iam create-role \
 --role-name FirehosetoS3Role \
 --assume-role-policy-document file://~/TrustPolicyForFirehose.json

`{
 "Role": {
 "AssumeRolePolicyDocument": {
 "Statement": {
 "Action": "sts:AssumeRole",
 "Effect": "Allow",
 "Principal": {
 "Service": "firehose.amazonaws.com"
 }
 }
 },
 "RoleId": "EXAMPLE50GAB4HC5F431",
 "CreateDate": "2023-05-29T13:46:29.431Z",
 "RoleName": "`FirehosetoS3Role`",
 "Path": "/",
 "Arn": "arn:aws:iam::`123456789012`:role/`FirehosetoS3Role`"
 }
}`
```

4. Create a permissions policy to define what actions Firehose can do on your
   account. First, use a text editor to create a permissions policy in a file
   `~/PermissionsForFirehose.json`:

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
          "s3:AbortMultipartUpload",
          "s3:GetBucketLocation",
          "s3:GetObject",
          "s3:ListBucket",
          "s3:ListBucketMultipartUploads",
          "s3:PutObject" ],
      "Resource": [
          "arn:aws:s3:::`amzn-s3-demo-bucket2`",
          "arn:aws:s3:::`amzn-s3-demo-bucket2`/*" ]
    }
  ]
}
```

5. Associate the permissions policy with the role using the following
   put-role-policy command:

```
aws iam put-role-policy --role-name `FirehosetoS3Role` --policy-name `Permissions-Policy-For-Firehose` --policy-document `file://~/PermissionsForFirehose`.json
```

6. Create a destination Firehose delivery stream as follows, replacing the
   placeholder values for **RoleARN** and
   **BucketARN** with the role and bucket ARNs that you
   created:

```
aws firehose create-delivery-stream \
   --delivery-stream-name 'my-delivery-stream' \
   --s3-destination-configuration \
  '{"RoleARN": "arn:aws:iam::`123456789012`:role/FirehosetoS3Role", "BucketARN": "`arn:aws:s3:::amzn-s3-demo-bucket2`"}'

```

NFirehose automatically uses a prefix in YYYY/MM/DD/HH UTC time format for
delivered Amazon S3 objects. You can specify an extra prefix to be added in front
of the time format prefix. If the prefix ends with a forward slash (/), it
appears as a folder in the Amazon S3 bucket. 7. Wait a few minutes for the stream becomes active. You can use the Firehose
**describe-delivery-stream** command to check the
**DeliveryStreamDescription.DeliveryStreamStatus**
property. In addition, note the
**DeliveryStreamDescription.DeliveryStreamARN** value,
as you will need it in a later step:

```
`aws firehose describe-delivery-stream --delivery-stream-name "`my-delivery-stream`"`
`{
 "DeliveryStreamDescription": {
 "HasMoreDestinations": false,
 "VersionId": "1",
 "CreateTimestamp": 1446075815.822,
 "DeliveryStreamARN": "arn:aws:firehose:`us-east-1`:`123456789012`:deliverystream/my-delivery-stream",
 "DeliveryStreamStatus": "ACTIVE",
 "DeliveryStreamName": "`my-delivery-stream`",
 "Destinations": [
 {
 "DestinationId": "destinationId-000000000001",
 "S3DestinationDescription": {
 "CompressionFormat": "UNCOMPRESSED",
 "EncryptionConfiguration": {
 "NoEncryptionConfig": "NoEncryption"
 },
 "RoleARN": "delivery-stream-role",
 "BucketARN": "arn:aws:s3:::`amzn-s3-demo-bucket2`",
 "BufferingHints": {
 "IntervalInSeconds": 300,
 "SizeInMBs": 5
 }
 }
 }
 ]
 }
}`
```

8. Create the IAM role that grants CloudWatch Logs permission to put data into your
   Firehose delivery stream. First, use a text editor to create a trust policy in
   a file `~/TrustPolicyForCWL.json`:

This policy includes a `aws:SourceArn` global condition context
key to help prevent the confused deputy security problem. For more
information, see [Confused deputy prevention](Subscriptions-confused-deputy.md "Subscriptions-confused-deputy.md").

```
{
  "Statement": {
    "Effect": "Allow",
    "Principal": { "Service": "logs.amazonaws.com" },
    "Action": "sts:AssumeRole",
    "Condition": {
         "StringLike": {
             "aws:SourceArn": "arn:aws:logs:`region`:`123456789012`:*"
         }
     }
  }
}
```

9. Use the **create-role** command to create the IAM role,
   specifying the trust policy file. Make a note of the returned
   **Role.Arn** value, as you will need it in a later
   step:

```
`aws iam create-role \
--role-name `CWLtoKinesisFirehoseRole` \
--assume-role-policy-document `file://~/TrustPolicyForCWL.json``

`{
 "Role": {
 "AssumeRolePolicyDocument": {
 "Statement": {
 "Action": "sts:AssumeRole",
 "Effect": "Allow",
 "Principal": {
 "Service": "logs.amazonaws.com"
 },
 "Condition": {
 "StringLike": {
 "aws:SourceArn": "arn:aws:logs:`region`:`123456789012`:*"
 }
 }
 }
 },
 "RoleId": "`AAOIIAH450GAB4HC5F431`",
 "CreateDate": "2015-05-29T13:46:29.431Z",
 "RoleName": "`CWLtoKinesisFirehoseRole`",
 "Path": "/",
 "Arn": "`arn:aws:iam::123456789012:role/CWLtoKinesisFirehoseRole`"
 }
}`
```

10. Create a permissions policy to define what actions CloudWatch Logs can do on your
    account. First, use a text editor to create a permissions policy file (for
    example, `~/PermissionsForCWL.json`):

```
{
    "Statement":[
      {
        "Effect":"Allow",
        "Action":["firehose:PutRecord"],
        "Resource":[
            "arn:aws:firehose:`region`:`account-id`:deliverystream/`delivery-stream-name`"]
      }
    ]
}
```

11. Associate the permissions policy with the role using the put-role-policy
    command:

```
aws iam put-role-policy --role-name `CWLtoKinesisFirehoseRole` --policy-name `Permissions-Policy-For-CWL` --policy-document `file://~/PermissionsForCWL.json`
```

12. After the Amazon Data Firehose delivery stream is in the active state and you have
    created the IAM role, you can create the CloudWatch Logs account-level subscription
    filter policy. The policy immediately starts the flow of real-time log data
    from the chosen log group to your Amazon Data Firehose delivery stream:

```
aws logs put-account-policy \
    --policy-name "ExamplePolicyFirehose" \
    --policy-type "SUBSCRIPTION_FILTER_POLICY" \
    --policy-document '{"RoleArn":"arn:aws:iam::`123456789012`:role/CWLtoKinesisFirehoseRole", "DestinationArn":"arn:aws:firehose:`us-east-1`:`123456789012`:deliverystream/delivery-stream-name", "FilterPattern": "Test", "Distribution": "Random"}' \
    --selection-criteria 'LogGroupName NOT IN ["LogGroupToExclude1", "LogGroupToExclude2"]' \
    --scope "ALL"
```

13. After you set up the subscription filter, CloudWatch Logs forwards the incoming log
    events that match the filter pattern to your Amazon Data Firehose delivery
    stream.

The `selection-criteria` field is optional, but is important
for excluding log groups that can cause an infinite log recursion from a
subscription filter. For more information about this issue and determining
which log groups to exclude, see [Log recursion prevention](Subscriptions-recursion-prevention.md "Subscriptions-recursion-prevention.md"). Currently, NOT IN
is the only supported operator for `selection-criteria`.

Your data will start appearing in your Amazon S3 based on the time buffer
interval set on your Amazon Data Firehose delivery stream. Once enough time has passed,
you can verify your data by checking your Amazon S3 Bucket.

```
`aws s3api list-objects --bucket '`amzn-s3-demo-bucket2`' --prefix '`firehose/`'`
`{
 "Contents": [
 {
 "LastModified": "2023-10-29T00:01:25.000Z",
 "ETag": "\"a14589f8897f4089d3264d9e2d1f1610\"",
 "StorageClass": "STANDARD",
 "Key": "firehose/2015/10/29/00/my-delivery-stream-2015-10-29-00-01-21-a188030a-62d2-49e6-b7c2-b11f1a7ba250",
 "Owner": {
 "DisplayName": "cloudwatch-logs",
 "ID": "1ec9cf700ef6be062b19584e0b7d84ecc19237f87b5"
 },
 "Size": 593
 },
 {
 "LastModified": "2015-10-29T00:35:41.000Z",
 "ETag": "\"a7035b65872bb2161388ffb63dd1aec5\"",
 "StorageClass": "STANDARD",
 "Key": "firehose/2023/10/29/00/my-delivery-stream-2023-10-29-00-35-40-EXAMPLE-7e66-49bc-9fd4-fc9819cc8ed3",
 "Owner": {
 "DisplayName": "cloudwatch-logs",
 "ID": "EXAMPLE6be062b19584e0b7d84ecc19237f87b6"
 },
 "Size": 5752
 }
 ]
}`
```

```
`aws s3api get-object --bucket '`amzn-s3-demo-bucket2`' --key 'firehose/2023/10/29/00/my-delivery-stream-2023-10-29-00-01-21-a188030a-62d2-49e6-b7c2-b11f1a7ba250' testfile.gz`

`{
 "AcceptRanges": "bytes",
 "ContentType": "application/octet-stream",
 "LastModified": "Thu, 29 Oct 2023 00:07:06 GMT",
 "ContentLength": 593,
 "Metadata": {}
}`
```

The data in the Amazon S3 object is compressed with the gzip format. You can
examine the raw data from the command line using the following Unix
command:

```
zcat testfile.gz
```
