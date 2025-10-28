# Error handling (error action)

When AWS IoT receives a message from a device, the rules engine checks to see if the
message matches a rule. If so, the rule's query statement is evaluated and the rule's
actions are activated, passing the query statement's result.

If a problem occurs when activating an action, the rules engine activates an error
action, if one is specified for the rule. This might happen when:

- A rule doesn't have permission to access an Amazon S3 bucket.
- A user error causes DynamoDB provisioned throughput to be exceeded.

###### Note

The error handling covered in this topic is for [rule actions](iot-rule-actions.md "iot-rule-actions.md"). To debug SQL issues, including external functions, you can
set up AWS IoT logging. For more information, see [Configure AWS IoT logging](configure-logging.md "configure-logging.md").

## Error action message format

A single message is generated per rule and message. For example, if two rule
actions in the same rule fail, the error action receives one message that contains
both errors.

The error action message looks like the following example.

```
{
  "ruleName": "TestAction",
  "topic": "testme/action",
  "cloudwatchTraceId": "7e146a2c-95b5-6caf-98b9-50e3969734c7",
  "clientId": "iotconsole-1511213971966-0",
  "base64OriginalPayload": "ewogICJtZXNzYWdlIjogIkhlbGxvIHZyb20gQVdTIElvVCBjb25zb2xlIgp9",
  "failures": [
    {
      "failedAction": "S3Action",
      "failedResource": "us-east-1-s3-verify-user",
      "errorMessage": "Failed to put S3 object. The error received was The specified bucket does not exist (Service: Amazon S3; Status Code: 404; Error Code: NoSuchBucket; Request ID: 9DF5416B9B47B9AF; S3 Extended Request ID: yMah1cwPhqTH267QLPhTKeVPKJB8BO5ndBHzOmWtxLTM6uAvwYYuqieAKyb6qRPTxP1tHXCoR4Y=). Message arrived on: error/action, Action: s3, Bucket: us-east-1-s3-verify-user, Key: \"aaa\". Value of x-amz-id-2: yMah1cwPhqTH267QLPhTKeVPKJB8BO5ndBHzOmWtxLTM6uAvwYYuqieAKyb6qRPTxP1tHXCoR4Y="
    }
  ]
}
```

ruleName

The name of the rule that triggered the error action.

topic

The topic in which the original message was received.

cloudwatchTraceId

A unique identity referring to the error logs in CloudWatch.

clientId

The client ID of the message publisher.

base64OriginalPayload

The original message payload Base64-encoded.

failures

failedAction

The name of the action that failed to complete (for
example, "S3Action").

failedResource

The name of the resource (for example, the name of an S3
bucket).

errorMessage

The description and explanation of the error.

## Error action example

Here is an example of a rule with an added error action. The following rule has an
action that writes message data to a DynamoDB table and an error action that writes
data to an Amazon S3 bucket:

```
{
    "sql" : "SELECT * FROM ..."
    "actions" : [{
        "dynamoDB" : {
            "table" : "PoorlyConfiguredTable",
            "hashKeyField" : "AConstantString",
            "hashKeyValue" : "AHashKey"}}
    ],
    "errorAction" : {
        "s3" : {
            "roleArn": "arn:aws:iam::123456789012:role/aws_iot_s3",
            "bucketName" : "message-processing-errors",
            "key" : "${replace(topic(), '/', '-') + '-' + timestamp() + '-' + newuuid()}"
        }
    }
}
```

You can use any [function](iot-sql-functions.md "iot-sql-functions.md") or [substitution
template](iot-substitution-templates.md "iot-substitution-templates.md") in an error action's SQL statement including the external
functions: [`aws_lambda()`](iot-sql-functions.md#iot-func-aws-lambda "iot-sql-functions.md#iot-func-aws-lambda"), [`get_dynamodb()`](iot-sql-functions.md#iot-sql-function-get-dynamodb "iot-sql-functions.md#iot-sql-function-get-dynamodb"), [`get_thing_shadow()`](iot-sql-functions.md#iot-sql-function-get-thing-shadow "iot-sql-functions.md#iot-sql-function-get-thing-shadow"), [`get_secret()`](iot-sql-functions.md#iot-sql-function-get-secret "iot-sql-functions.md#iot-sql-function-get-secret"), [`machinelearning_predict()`](iot-sql-functions.md#iot-sql-function-machine-learning "iot-sql-functions.md#iot-sql-function-machine-learning"), and [`decode()`](iot-sql-functions.md#iot-sql-decode-base64 "iot-sql-functions.md#iot-sql-decode-base64"). If an error action requires to call an
external function, then invoking the error action can result in additional bill for
the external function.

The following external functions are billed equivalent to that of a rule action:
[`aws_lambda`](iot-sql-functions.md#iot-func-aws-lambda "iot-sql-functions.md#iot-func-aws-lambda"), [`get_dynamodb()`](iot-sql-functions.md#iot-sql-function-get-dynamodb "iot-sql-functions.md#iot-sql-function-get-dynamodb"), and [`get_thing_shadow()`](iot-sql-functions.md#iot-sql-function-get-thing-shadow "iot-sql-functions.md#iot-sql-function-get-thing-shadow"). You also get billed for the [`decode()`](iot-sql-functions.md#iot-sql-decode-base64 "iot-sql-functions.md#iot-sql-decode-base64") function only when you are [decoding a Protobuf message to JSON](binary-payloads.md#binary-payloads-protobuf "binary-payloads.md#binary-payloads-protobuf"). For more details, refer to the
[AWS IoT Core pricing
page](https://aws.amazon.com/iot-core/pricing/ "https://aws.amazon.com/iot-core/pricing/").

For more information about rules and how to specify an error action, see [Creating an AWS IoT Rule](iot-create-rule.md "iot-create-rule.md").

For more information about using CloudWatch to monitor the success or failure of rules,
see [AWS IoT metrics and dimensions](metrics_dimensions.md "metrics_dimensions.md").
