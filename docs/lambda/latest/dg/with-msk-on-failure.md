# Capturing discarded batches for an Amazon MSK event source

To retain records of failed event source mapping invocations, add a destination to your function's event source mapping.
Each record sent to the destination is a JSON document containing metadata about the failed invocation. For Amazon S3 destinations, Lambda also sends the entire invocation record along with the
metadata. You can configure any Amazon SNS topic, Amazon SQS queue, or S3 bucket as a destination.

With Amazon S3 destinations, you can use the [Amazon S3 Event Notifications](../../../index.md "../../../index.md") feature to receive notifications when objects are uploaded to
your destination S3 bucket. You can also configure S3 Event Notifications to invoke another Lambda function to perform automated processing on failed batches.

Your execution role must have permissions for the destination:

- **For SQS destinations:** [sqs:SendMessage](../../../AWSSimpleQueueService/latest/APIReference/API_SendMessage.md "../../../AWSSimpleQueueService/latest/APIReference/API_SendMessage.md")
- **For SNS destinations:** [sns:Publish](../../../sns/latest/api/API_Publish.md "../../../sns/latest/api/API_Publish.md")
- **For S3 bucket destinations:** [s3:PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md") and [s3:ListBucket](../../../AmazonS3/latest/API/ListObjectsV2.md "../../../AmazonS3/latest/API/ListObjectsV2.md")
  You must deploy a VPC endpoint for your on-failure destination service inside your Amazon MSK cluster VPC.

Additionally, if you configured a KMS key on your destination, Lambda needs the following
permissions depending on the destination type:

- If you've enabled encryption with your own KMS key for an S3 destination,
  [kms:GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") is required.
  If the KMS key and S3 bucket destination are in a different account from your Lambda function
  and execution role, configure the KMS key to trust the execution role to allow
  kms:GenerateDataKey.
- If you've enabled encryption with your own KMS key for SQS destination,
  [kms:Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") and
  [kms:GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") are
  required. If the KMS key and SQS queue destination are in a different account from your
  Lambda function and execution role, configure the KMS key to trust the execution role to
  allow kms:Decrypt, kms:GenerateDataKey,
  [kms:DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md"), and
  [kms:ReEncrypt](../../../kms/latest/APIReference/API_ReEncrypt.md "../../../kms/latest/APIReference/API_ReEncrypt.md").
- If you've enabled encryption with your own KMS key for SNS destination,
  [kms:Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") and
  [kms:GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") are
  required. If the KMS key and SNS topic destination are in a different account from your
  Lambda function and execution role, configure the KMS key to trust the execution role to
  allow kms:Decrypt, kms:GenerateDataKey,
  [kms:DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md"), and
  [kms:ReEncrypt](../../../kms/latest/APIReference/API_ReEncrypt.md "../../../kms/latest/APIReference/API_ReEncrypt.md").

## Configuring on-failure destinations for an Amazon MSK event source mapping

To configure an on-failure destination using the console, follow these steps:

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Choose a function.
3. Under **Function overview**, choose **Add destination**.
4. For **Source**, choose **Event source mapping invocation**.
5. For **Event source mapping**, choose an event source that's configured
   for this function.
6. For **Condition**, select **On failure**. For event
   source mapping invocations, this is the only accepted condition.
7. For **Destination type**, choose the destination type that Lambda sends
   invocation records to.
8. For **Destination**, choose a resource.
9. Choose **Save**.

You can also configure an on-failure destination using the AWS CLI. For example, the following
[create-event-source-mapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-event-source-mapping.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-event-source-mapping.html") command adds an event source mapping with an SQS on-failure destination to
`MyFunction`:

```
aws lambda create-event-source-mapping \
--function-name "MyFunction" \
--event-source-arn arn:aws:kafka:us-east-1:123456789012:cluster/vpc-2priv-2pub/751d2973-a626-431c-9d4e-d7975eb44dd7-2 \
--destination-config '{"OnFailure": {"Destination": "arn:aws:sqs:us-east-1:123456789012:dest-queue"}}'
```

The following [update-event-source-mapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-event-source-mapping.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-event-source-mapping.html") command adds an S3 on-failure destination to the event source associated with the input `uuid`:

```
aws lambda update-event-source-mapping \
--uuid f89f8514-cdd9-4602-9e1f-01a5b77d449b \
--destination-config '{"OnFailure": {"Destination": "arn:aws:s3:::dest-bucket"}}'
```

To remove a destination, supply an empty string as the argument to the
`destination-config` parameter:

```
aws lambda update-event-source-mapping \
--uuid f89f8514-cdd9-4602-9e1f-01a5b77d449b \
--destination-config '{"OnFailure": {"Destination": ""}}'
```

### Security best practices for Amazon S3 destinations

Deleting an S3 bucket that's configured as a destination without removing the destination from your function's configuration can create a security risk. If another
user knows your destination bucket's name, they can recreate the bucket in their AWS account. Records of failed invocations will be sent to their bucket, potentially
exposing data from your function.

###### Warning

To ensure that invocation records from your function can't be sent to an S3 bucket in another AWS account, add a condition to your function's execution role
that limits `s3:PutObject` permissions to buckets in your account.

The following example shows an IAM policy that limits your function's `s3:PutObject` permissions to buckets in your account. This policy also gives Lambda
the `s3:ListBucket` permission it needs to use an S3 bucket as a destination.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3BucketResourceAccountWrite",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::*/*",
                "arn:aws:s3:::*"
            ],
            "Condition": {
                "StringEquals": {
                    "s3:ResourceAccount": `"111122223333"`
                }
            }
        }
    ]
}
```

To add a permissions policy to your function's execution role using the AWS Management Console or AWS CLI, refer to the instructions in the following procedures:

Console

###### To add a permissions policy to a function's execution role (console)

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Select the Lambda function whose execution role you want to modify.
3. In the **Configuration** tab, select **Permissions**.
4. In the **Execution role** tab, select your function's **Role name** to open the role's IAM console page.
5. Add a permissions policy to the role by doing the following:
   1. In the **Permissions policies** pane, choose **Add permissions** and select **Create inline policy**.
   2. In **Policy editor**, select **JSON**.
   3. Paste the policy you want to add into the editor (replacing the existing JSON), and then choose **Next**.
   4. Under **Policy details**, enter a **Policy name**.
   5. Choose **Create policy**.

AWS CLI

###### To add a permissions policy to a function's execution role (CLI)

1. Create a JSON policy document with the required permissions and save it in a local directory.
2. Use the IAM `put-role-policy` CLI command to add the permissions to your function's execution role. Run the following command from the
   directory you saved your JSON policy document in and replace the role name, policy name, and policy document with your own values.

```
`aws iam put-role-policy \
--role-name `my_lambda_role` \
--policy-name LambdaS3DestinationPolicy \
--policy-document file://`my_policy.json``
```

### SNS and SQS example invocation record

The following example shows what Lambda sends to an SNS topic or SQS queue destination for a
failed Kafka event source invocation. Each of the keys under `recordsInfo` contains
both the Kafka topic and partition, separated by a hyphen. For example, for the key
`"Topic-0"`, `Topic` is the Kafka topic, and `0` is the
partition. For each topic and partition, you can use the offsets and timestamp data to find
the original invocation records.

```
{
    "requestContext": {
        "requestId": "316aa6d0-8154-xmpl-9af7-85d5f4a6bc81",
        "functionArn": "arn:aws:lambda:us-east-1:123456789012:function:myfunction",
        "condition": "RetryAttemptsExhausted" | "MaximumPayloadSizeExceeded",
        "approximateInvokeCount": 1
    },
    "responseContext": { // null if record is MaximumPayloadSizeExceeded
        "statusCode": 200,
        "executedVersion": "$LATEST",
        "functionError": "Unhandled"
    },
    "version": "1.0",
    "timestamp": "2019-11-14T00:38:06.021Z",
    "KafkaBatchInfo": {
        "batchSize": 500,
        "eventSourceArn": "arn:aws:kafka:us-east-1:123456789012:cluster/vpc-2priv-2pub/751d2973-a626-431c-9d4e-d7975eb44dd7-2",
        "bootstrapServers": "...",
        "payloadSize": 2039086, // In bytes
        "recordsInfo": {
            "Topic-0": {
                "firstRecordOffset": "49601189658422359378836298521827638475320189012309704722",
                "lastRecordOffset": "49601189658422359378836298522902373528957594348623495186",
                "firstRecordTimestamp": "2019-11-14T00:38:04.835Z",
                "lastRecordTimestamp": "2019-11-14T00:38:05.580Z",
            },
            "Topic-1": {
                "firstRecordOffset": "49601189658422359378836298521827638475320189012309704722",
                "lastRecordOffset": "49601189658422359378836298522902373528957594348623495186",
                "firstRecordTimestamp": "2019-11-14T00:38:04.835Z",
                "lastRecordTimestamp": "2019-11-14T00:38:05.580Z",
            }
        }
    }
}
```

### S3 destination example invocation record

For S3 destinations, Lambda sends the entire invocation record along with the metadata
to the destination. The following example shows that Lambda sends to an S3 bucket destination
for a failed Kafka event source invocation. In addition to all of the fields from the previous
example for SQS and SNS destinations, the `payload` field contains the original
invocation record as an escaped JSON string.

```
{
    "requestContext": {
        "requestId": "316aa6d0-8154-xmpl-9af7-85d5f4a6bc81",
        "functionArn": "arn:aws:lambda:us-east-1:123456789012:function:myfunction",
        "condition": "RetryAttemptsExhausted" | "MaximumPayloadSizeExceeded",
        "approximateInvokeCount": 1
    },
    "responseContext": { // null if record is MaximumPayloadSizeExceeded
        "statusCode": 200,
        "executedVersion": "$LATEST",
        "functionError": "Unhandled"
    },
    "version": "1.0",
    "timestamp": "2019-11-14T00:38:06.021Z",
    "KafkaBatchInfo": {
        "batchSize": 500,
        "eventSourceArn": "arn:aws:kafka:us-east-1:123456789012:cluster/vpc-2priv-2pub/751d2973-a626-431c-9d4e-d7975eb44dd7-2",
        "bootstrapServers": "...",
        "payloadSize": 2039086, // In bytes
        "recordsInfo": {
            "Topic-0": {
                "firstRecordOffset": "49601189658422359378836298521827638475320189012309704722",
                "lastRecordOffset": "49601189658422359378836298522902373528957594348623495186",
                "firstRecordTimestamp": "2019-11-14T00:38:04.835Z",
                "lastRecordTimestamp": "2019-11-14T00:38:05.580Z",
            },
            "Topic-1": {
                "firstRecordOffset": "49601189658422359378836298521827638475320189012309704722",
                "lastRecordOffset": "49601189658422359378836298522902373528957594348623495186",
                "firstRecordTimestamp": "2019-11-14T00:38:04.835Z",
                "lastRecordTimestamp": "2019-11-14T00:38:05.580Z",
            }
        }
    },
    "payload": "<Whole Event>" // Only available in S3
}
```

###### Tip

We recommend enabling S3 versioning on your destination bucket.
