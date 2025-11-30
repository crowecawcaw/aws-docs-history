# AWS IoT rule actions

AWS IoT rule actions specify what to do when a rule is invoked. You can define actions
to send data to an Amazon DynamoDB database, send data to Amazon Kinesis Data Streams, invoke an AWS Lambda
function, and so on. AWS IoT supports the following actions in AWS Regions where the
action's service is available.

| Rule action                                                                                 | Description                                                                                     | Name in API        |
| ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------ |
| [Apache Kafka](apache-kafka-rule-action.md "apache-kafka-rule-action.md")                   | Sends a message to an Apache Kafka cluster.                                                     | `kafka`            |
| [CloudWatch alarms](cloudwatch-alarms-rule-action.md "cloudwatch-alarms-rule-action.md")    | Changes the state of an Amazon CloudWatch alarm.                                                | `cloudwatchAlarm`  |
| [CloudWatch Logs](cloudwatch-logs-rule-action.md "cloudwatch-logs-rule-action.md")          | Sends a message to Amazon CloudWatch Logs.                                                      | `cloudwatchLogs`   |
| [CloudWatch metrics](cloudwatch-metrics-rule-action.md "cloudwatch-metrics-rule-action.md") | Sends a message to a CloudWatch metric.                                                         | `cloudwatchMetric` |
| [DynamoDB](dynamodb-rule-action.md "dynamodb-rule-action.md")                               | Sends a message to a DynamoDB table.                                                            | `dynamoDB`         |
| [DynamoDBv2](dynamodb-v2-rule-action.md "dynamodb-v2-rule-action.md")                       | Sends message data to multiple columns in a DynamoDB table.                                     | `dynamoDBv2`       |
| [Elasticsearch](elasticsearch-rule-action.md "elasticsearch-rule-action.md")                | Sends a message to an OpenSearch endpoint.                                                      | `OpenSearch`       |
| [HTTP](https-rule-action.md "https-rule-action.md")                                         | Posts a message to an HTTPS endpoint.                                                           | `http`             |
| [IoT Analytics](iotanalytics-rule-action.md "iotanalytics-rule-action.md")                  | Sends a message to an AWS IoT Analytics channel.                                                | `iotAnalytics`     |
| [AWS IoT Events](iotevents-rule-action.md "iotevents-rule-action.md")                       | Sends a message to an AWS IoT Events input.                                                     | `iotEvents`        |
| [AWS IoT SiteWise](iotsitewise-rule-action.md "iotsitewise-rule-action.md")                 | Sends message data to AWS IoT SiteWise asset properties.                                        | `iotSiteWise`      |
| [Firehose](kinesis-firehose-rule-action.md "kinesis-firehose-rule-action.md")               | Sends a message to a Firehose delivery stream.                                                  | `firehose`         |
| [Kinesis Data Streams](kinesis-rule-action.md "kinesis-rule-action.md")                     | Sends a message to a Kinesis data stream.                                                       | `kinesis`          |
| [Lambda](lambda-rule-action.md "lambda-rule-action.md")                                     | Invokes a Lambda function with message data as input.                                           | `lambda`           |
| [Location](location-rule-action.md "location-rule-action.md")                               | Sends location data to Amazon Location Service.                                                 | `location`         |
| [OpenSearch](opensearch-rule-action.md "opensearch-rule-action.md")                         | Sends a message to an Amazon OpenSearch Service endpoint.                                       | `OpenSearch`       |
| [Republish](republish-rule-action.md "republish-rule-action.md")                            | Republishes a message to another MQTT topic.                                                    | `republish`        |
| [S3](s3-rule-action.md "s3-rule-action.md")                                                 | Stores a message in an Amazon Simple Storage Service (Amazon S3) bucket.                        | `s3`               |
| [Salesforce IoT](salesforce-iot-rule-action.md "salesforce-iot-rule-action.md")             | Sends a message to a Salesforce IoT input stream.                                               | `salesforce`       |
| [SNS](sns-rule-action.md "sns-rule-action.md")                                              | Publishes a message as an Amazon Simple Notification Service (Amazon SNS) push<br>notification. | `sns`              |
| [SQS](sqs-rule-action.md "sqs-rule-action.md")                                              | Sends a message to an Amazon Simple Queue Service (Amazon SQS) queue.                           | `sqs`              |
| [Step Functions](stepfunctions-rule-action.md "stepfunctions-rule-action.md")               | Starts an AWS Step Functions state machine.                                                     | `stepFunctions`    |
| [Timestream](timestream-rule-action.md "timestream-rule-action.md")                         | Sends a message to an Amazon Timestream database table.                                         | `timestream`       |

###### Notes

- Define the rule in the same AWS Region as another service's resource so
  that the rule action can interact with that resource.
- The AWS IoT rules engine might make multiple attempts to perform an action
  if intermittent errors occur. If all attempts fail, the message is discarded
  and the error is available in your CloudWatch Logs. You can specify an error action
  for each rule that is invoked after a failure occurs. For more information,
  see [Error handling (error action)](rule-error-handling.md "rule-error-handling.md").
- Some rule actions activate actions in services that integrate with
  AWS Key Management Service (AWS KMS) to support data encryption at rest. If you use a
  customer-managed AWS KMS key (KMS key) to encrypt data at rest, the
  service must have permission to use the KMS key on the caller's behalf. To
  learn how to manage permissions for your customer managed KMS key, see the
  data encryption topics in the appropriate service guide. For more
  information about customer managed KMS keys, see [AWS Key Management Service concepts](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md") in the
  _AWS Key Management Service Developer Guide_.

You can use any [function](iot-sql-functions.md "iot-sql-functions.md") or [substitution
template](iot-substitution-templates.md "iot-substitution-templates.md") in an error action's SQL statement including the external
functions: [`aws_lambda()`](iot-sql-functions.md#iot-func-aws-lambda "iot-sql-functions.md#iot-func-aws-lambda"), [`get_dynamodb()`](iot-sql-functions.md#iot-sql-function-get-dynamodb "iot-sql-functions.md#iot-sql-function-get-dynamodb"), [`get_registry_data()`](iot-sql-functions.md#iot-sql-function-get-registry_data "iot-sql-functions.md#iot-sql-function-get-registry_data"), [`get_thing_shadow()`](iot-sql-functions.md#iot-sql-function-get-thing-shadow "iot-sql-functions.md#iot-sql-function-get-thing-shadow"), [`get_secret()`](iot-sql-functions.md#iot-sql-function-get-secret "iot-sql-functions.md#iot-sql-function-get-secret"), [`machinelearning_predict()`](iot-sql-functions.md#iot-sql-function-machine-learning "iot-sql-functions.md#iot-sql-function-machine-learning"), and [`decode()`](iot-sql-functions.md#iot-sql-decode-base64 "iot-sql-functions.md#iot-sql-decode-base64"). If an error action requires to call an
external function, then invoking the error action can result in additional bill for
the external function.
