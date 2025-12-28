# Log group-level subscription filters

You can use a subscription filter with Amazon Kinesis Data Streams, AWS Lambda, Amazon Data Firehose, or Amazon OpenSearch Service.
Logs sent to a service through a subscription filter are base64 encoded and compressed
with the gzip format. If you are using centralized logs with your AWS Organizations, you can
choose to emit the `@aws.account` and `@aws.region` system field
to identify which data comes from which accounts and regions in your organization. This
section provides examples you can follow to create a CloudWatch Logs subscription filter that
sends log data to Firehose, Lambda, Amazon Kinesis Data Streams, and OpenSearch Service.

###### Note

If you want to search your log data, see [Filter and
pattern syntax](FilterAndPatternSyntax.md "FilterAndPatternSyntax.md").

###### Examples

- [Example 1: Subscription filters with
  Amazon Kinesis Data Streams](#DestinationKinesisExample "#DestinationKinesisExample")
- [Example 2: Subscription filters with
  AWS Lambda](#LambdaFunctionExample "#LambdaFunctionExample")
- [Example 3: Subscription filters with
  Amazon Data Firehose](#FirehoseExample "#FirehoseExample")
- [Example 4: Subscription filters with
  Amazon OpenSearch Service](#OpenSearchExample "#OpenSearchExample")

## Example 1: Subscription filters with

Amazon Kinesis Data Streams

The following example associates a subscription filter with a log group containing
AWS CloudTrail events. The subscription filter delivers every logged activity made by
"Root" AWS credentials to a stream in Amazon Kinesis Data Streams called "RootAccess." For more
information about how to send AWS CloudTrail events to CloudWatch Logs, see [Sending CloudTrail Events to CloudWatch Logs](../../../awscloudtrail/latest/userguide/cw_send_ct_events.md "../../../awscloudtrail/latest/userguide/cw_send_ct_events.md")
in the _AWS CloudTrail User Guide_.

###### Note

Before you create the stream, calculate the volume of log data that will be
generated. Be sure to create a stream with enough shards to handle this volume.
If the stream does not have enough shards, the log stream will be throttled. For
more information about stream volume limits, see [Quotas and Limits](../../../streams/latest/dev/service-sizes-and-limits.md "../../../streams/latest/dev/service-sizes-and-limits.md").

Throttled deliverables are retried for up to 24 hours. After 24 hours, the
failed deliverables are dropped.

To mitigate the risk of throttling, you can take the following steps:

- Specify `random` for `distribution` when you
  create the subscription filter with [PutSubscriptionFilter](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutSubscriptionFilter.md#CWL-PutSubscriptionFilter-request-distribution "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutSubscriptionFilter.md#CWL-PutSubscriptionFilter-request-distribution") or [put-subscription-filter](https://awscli.amazonaws.com/v2/documentation/api/2.4.18/reference/logs/put-subscription-filter.html "https://awscli.amazonaws.com/v2/documentation/api/2.4.18/reference/logs/put-subscription-filter.html"). By default, the stream filter
  distribution is by log stream and this can cause throttling.
- Monitor your stream using CloudWatch metrics. This helps you identify any
  throttling and adjust your configuration accordingly. For example, the
  `DeliveryThrottling` metric can be used to track the
  number of log events for which CloudWatch Logs was throttled when
  forwarding data to the subscription destination. For more information
  about monitoring, see [Monitoring with CloudWatch metrics](CloudWatch-Logs-Monitoring-CloudWatch-Metrics.md "CloudWatch-Logs-Monitoring-CloudWatch-Metrics.md").
- Use the on-demand capacity mode for your stream in Amazon Kinesis Data Streams. On-demand
  mode instantly accommodates your workloads as they ramp up or down. More
  information about on-demand capacity mode, see [On-demand mode](../../../streams/latest/dev/how-do-i-size-a-stream.md#ondemandmode "../../../streams/latest/dev/how-do-i-size-a-stream.md#ondemandmode").
- Restrict your CloudWatch subscription filter pattern to match the capacity
  of your stream in Amazon Kinesis Data Streams. If you are sending too much data to the stream,
  you might need to reduce the filter size or adjust the filter
  criteria.

###### To create a subscription filter for Amazon Kinesis Data Streams

1. Create a destination stream using the following command:

```
`$` `C:\>`  aws kinesis create-stream --stream-name "RootAccess" --shard-count 1
```

2. Wait until the stream becomes Active (this might take a minute or two).
   You can use the following Amazon Kinesis Data Streams [describe-stream](../../../cli/latest/reference/kinesis/describe-stream.md "../../../cli/latest/reference/kinesis/describe-stream.md")
   command to check the **StreamDescription.StreamStatus**
   property. In addition, note the
   **StreamDescription.StreamARN** value, as you will need
   it in a later step:

```
`aws kinesis describe-stream --stream-name "RootAccess"`
```

The following is example output:

```
{
    "StreamDescription": {
        "StreamStatus": "ACTIVE",
        "StreamName": "RootAccess",
        "StreamARN": "arn:aws:kinesis:us-east-1:123456789012:stream/RootAccess",
        "Shards": [
            {
                "ShardId": "shardId-000000000000",
                "HashKeyRange": {
                    "EndingHashKey": "340282366920938463463374607431768211455",
                    "StartingHashKey": "0"
                },
                "SequenceNumberRange": {
                    "StartingSequenceNumber":
                    "49551135218688818456679503831981458784591352702181572610"
                }
            }
        ]
    }
}
```

3. Create the IAM role that will grant CloudWatch Logs permission to put data into
   your stream. First, you'll need to create a trust policy in a file (for
   example, `~/TrustPolicyForCWL-Kinesis.json`). Use a text
   editor to create this policy. Do not use the IAM console to create
   it.

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
        "StringLike": { "aws:SourceArn": "arn:aws:logs:`region`:`123456789012`:*" }
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
 "RoleId": "AAOIIAH450GAB4HC5F431",
 "CreateDate": "2015-05-29T13:46:29.431Z",
 "RoleName": "CWLtoKinesisRole",
 "Path": "/",
 "Arn": "arn:aws:iam::`123456789012`:role/CWLtoKinesisRole"
 }
}`
```

5. Create a permissions policy to define what actions CloudWatch Logs can do on your
   account. First, you'll create a permissions policy in a file (for example,
   `~/PermissionsForCWL-Kinesis.json`). Use a text
   editor to create this policy. Do not use the IAM console to create
   it.

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "kinesis:PutRecord",
      "Resource": "arn:aws:kinesis:`region`:`123456789012`:stream/RootAccess"
    }
  ]
}
```

6. Associate the permissions policy with the role using the following [put-role-policy](../../../cli/latest/reference/iam/put-role-policy.md "../../../cli/latest/reference/iam/put-role-policy.md")
   command:

```
`aws iam put-role-policy --role-name `CWLtoKinesisRole` --policy-name Permissions-Policy-For-CWL --policy-document file://~/`PermissionsForCWL-Kinesis.json``
```

7. After the stream is in **Active** state and you have
   created the IAM role, you can create the CloudWatch Logs subscription filter. The
   subscription filter immediately starts the flow of real-time log data from
   the chosen log group to your stream:

```
aws logs put-subscription-filter \
    --log-group-name "CloudTrail/logs" \
    --filter-name "RootAccess" \
    --filter-pattern "{$.userIdentity.type = Root}" \
    --destination-arn "arn:aws:kinesis:`region`:123456789012:stream/RootAccess" \
    --role-arn "arn:aws:iam::`123456789012`:role/`CWLtoKinesisRole`"
```

8. After you set up the subscription filter, CloudWatch Logs forwards all the incoming
   log events that match the filter pattern to your stream. You can verify that
   this is happening by grabbing a Amazon Kinesis Data Streams shard iterator and using the Amazon Kinesis Data Streams
   get-records command to fetch some Amazon Kinesis Data Streams records:

```
`aws kinesis get-shard-iterator --stream-name RootAccess --shard-id shardId-000000000000 --shard-iterator-type TRIM_HORIZON`
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

Note that you might need to make this call a few times before Amazon Kinesis Data Streams starts
to return data.

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
 "owner": "111111111111",
 "logGroup": "CloudTrail/logs",
 "logStream": "111111111111_CloudTrail/logs_us-east-1",
 "subscriptionFilters": [
 "Destination"
 ],
 "messageType": "DATA_MESSAGE",
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
 ]
}`
```

The key elements in the above data structure are the following:

**owner**

The AWS Account ID of the originating log data.

**logGroup**

The log group name of the originating log data.

**logStream**

The log stream name of the originating log data.

**subscriptionFilters**

The list of subscription filter names that matched with the
originating log data.

**messageType**

Data messages will use the "DATA_MESSAGE" type. Sometimes
CloudWatch Logs may emit Amazon Kinesis Data Streams records with a "CONTROL_MESSAGE" type,
mainly for checking if the destination is reachable.

**logEvents**

The actual log data, represented as an array of log event
records. The "id" property is a unique identifier for every log
event.

## Example 2: Subscription filters with

AWS Lambda

In this example, you'll create a CloudWatch Logs subscription filter that sends log data to
your AWS Lambda function.

###### Note

Before you create the Lambda function, calculate the volume of log data that
will be generated. Be sure to create a function that can handle this volume. If
the function does not have enough volume, the log stream will be throttled. For
more information about Lambda limits, see [AWS Lambda Limits](../../../lambda/latest/dg/limits.md "../../../lambda/latest/dg/limits.md").

###### To create a subscription filter for Lambda

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
    --zip-file fileb://`file-path`/helloWorld.zip \
    --role `lambda-execution-role-arn` \
    --handler helloWorld.handler \
    --runtime nodejs12.x
```

5. Grant CloudWatch Logs the permission to execute your function. Use the following
   command, replacing the placeholder account with your own account and the
   placeholder log group with the log group to process:

```
aws lambda add-permission \
    --function-name "`helloworld`" \
    --statement-id "`helloworld`" \
    --principal "logs.amazonaws.com" \
    --action "lambda:InvokeFunction" \
    --source-arn "arn:aws:logs:`region`:`123456789123`:log-group:`TestLambda`:*" \
    --source-account "`123456789012`"
```

6. Create a subscription filter using the following command, replacing the
   placeholder account with your own account and the placeholder log group with
   the log group to process:

```
aws logs put-subscription-filter \
    --log-group-name `myLogGroup` \
    --filter-name demo \
    --filter-pattern "" \
    --destination-arn arn:aws:lambda:`region`:`123456789123`:function:helloworld
```

7. (Optional) Test using a sample log event. At a command prompt, run the
   following command, which will put a simple log message into the subscribed
   stream.

To see the output of your Lambda function, navigate to the Lambda function
where you will see the output in /aws/lambda/helloworld:

```
aws logs put-log-events --log-group-name `myLogGroup` --log-stream-name `stream1` --log-events "[{\"timestamp\":`<CURRENT TIMESTAMP MILLIS>` , \"message\": \"`Simple Lambda Test`\"}]"
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
`{
 "owner": "123456789012",
 "logGroup": "CloudTrail",
 "logStream": "123456789012_CloudTrail_us-east-1",
 "subscriptionFilters": [
 "Destination"
 ],
 "messageType": "DATA_MESSAGE",
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
 ]
}`
```

The key elements in the above data structure are the following:

**owner**

The AWS Account ID of the originating log data.

**logGroup**

The log group name of the originating log data.

**logStream**

The log stream name of the originating log data.

**subscriptionFilters**

The list of subscription filter names that matched with the
originating log data.

**messageType**

Data messages will use the "DATA_MESSAGE" type. Sometimes
CloudWatch Logs may emit Lambda records with a "CONTROL_MESSAGE" type,
mainly for checking if the destination is reachable.

**logEvents**

The actual log data, represented as an array of log event
records. The "id" property is a unique identifier for every log
event.

## Example 3: Subscription filters with

Amazon Data Firehose

In this example, you'll create a CloudWatch Logs subscription that sends any incoming log
events that match your defined filters to your Amazon Data Firehose delivery stream. Data sent
from CloudWatch Logs to Amazon Data Firehose is already compressed with gzip level 6 compression, so you
do not need to use compression within your Firehose delivery stream. You can then use
the decompression feature in Firehose to automatically decompress the logs. For more
information, see [Send CloudWatch Logs to
Firehose](../../../logs/SubscriptionFilters.md#FirehoseExample "../../../logs/SubscriptionFilters.md#FirehoseExample").

###### Note

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
   specifying the trust policy file. Note of the returned
   **Role.Arn** value, as you will need it in a later
   step:

```
`aws iam create-role \
 --role-name FirehosetoS3Role \
 --assume-role-policy-document file://~/TrustPolicyForFirehose.json`

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
 "RoleId": "AAOIIAH450GAB4HC5F431",
 "CreateDate": "2015-05-29T13:46:29.431Z",
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

Note that Firehose automatically uses a prefix in YYYY/MM/DD/HH UTC time
format for delivered Amazon S3 objects. You can specify an extra prefix to be
added in front of the time format prefix. If the prefix ends with a forward
slash (/), it appears as a folder in the Amazon S3 bucket. 7. Wait until the stream becomes active (this might take a few minutes). You
can use the Firehose **describe-delivery-stream** command to
check the
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
 "DeliveryStreamARN": "arn:aws:firehose:`us-east-1:123456789012`:deliverystream/my-delivery-stream",
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
   specifying the trust policy file. Note of the returned
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

12. After the Amazon Data Firehose delivery stream is in active state and you have
    created the IAM role, you can create the CloudWatch Logs subscription filter. The
    subscription filter immediately starts the flow of real-time log data from
    the chosen log group to your Amazon Data Firehose delivery stream:

```
aws logs put-subscription-filter \
    --log-group-name "CloudTrail" \
    --filter-name "Destination" \
    --filter-pattern "{$.userIdentity.type = Root}" \
    --destination-arn "`arn:aws:firehose:`region`:`123456789012`:deliverystream/my-delivery-stream`" \
    --role-arn "`arn:aws:iam::`123456789012`:role/CWLtoKinesisFirehoseRole`"

```

13. After you set up the subscription filter, CloudWatch Logs will forward all the
    incoming log events that match the filter pattern to your Amazon Data Firehose delivery
    stream. Your data will start appearing in your Amazon S3 based on the time buffer
    interval set on your Amazon Data Firehose delivery stream. Once enough time has passed,
    you can verify your data by checking your Amazon S3 Bucket.

```
`aws s3api list-objects --bucket '`amzn-s3-demo-bucket2`' --prefix '`firehose/`'`
`{
 "Contents": [
 {
 "LastModified": "2015-10-29T00:01:25.000Z",
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
 "Key": "firehose/2015/10/29/00/my-delivery-stream-2015-10-29-00-35-40-7cc92023-7e66-49bc-9fd4-fc9819cc8ed3",
 "Owner": {
 "DisplayName": "cloudwatch-logs",
 "ID": "1ec9cf700ef6be062b19584e0b7d84ecc19237f87b6"
 },
 "Size": 5752
 }
 ]
}`
```

```
`aws s3api get-object --bucket '`amzn-s3-demo-bucket2`' --key 'firehose/2015/10/29/00/my-delivery-stream-2015-10-29-00-01-21-a188030a-62d2-49e6-b7c2-b11f1a7ba250' testfile.gz`

`{
 "AcceptRanges": "bytes",
 "ContentType": "application/octet-stream",
 "LastModified": "Thu, 29 Oct 2015 00:07:06 GMT",
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

## Example 4: Subscription filters with

Amazon OpenSearch Service

In this example, you'll create a CloudWatch Logs subscription that sends incoming log events
that match your defined filters to your OpenSearch Service domain.

###### To create a subscription filter for OpenSearch Service

1. Create an OpenSearch Service domain. For more information, see [Creating OpenSearch Service domains](../../../opensearch-service/latest/developerguide/createupdatedomains.md#createdomains "../../../opensearch-service/latest/developerguide/createupdatedomains.md#createdomains")
2. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
3. In the navigation pane, choose **Log groups**.
4. Select the name of the log group.
5. Choose **Actions**, **Subscription
   filters**, **Create Amazon OpenSearch Service subscription
   filter**.
6. Choose whether you want to stream to a cluster in this account or another
   account.
   - If you chose **This account**, select the domain
     that you created in step 1.
   - If you chose **Another account**, enter ARN and
     endpoint of that domain.

7. If you chose another account, provide the domain ARN and endpoint.
8. For Amazon OpenSearch Service cluster choose the name of the cluster where the log group
   data will be delivered
9. Choose a log format.
10. For **Subscription filter pattern**, enter the terms or
    pattern to find in your log events. This ensures that you send only the data
    that you're interested in to your OpenSearch Service cluster. For more information, see
    [Filter pattern syntax for
    metric filters](FilterAndPatternSyntaxForMetricFilters.md "FilterAndPatternSyntaxForMetricFilters.md").
11. (Optional) For **Select log data to test**, select a log
    stream and then choose **Test pattern** to verify that your
    search filter is returning the results you expect.
12. Choose **Start streaming**.
