# Handle failure in data

transformation

If your Lambda function invocation fails because of a network timeout or because you've
reached the Lambda invocation limit, Amazon Data Firehose retries the invocation three times by default.
If the invocation does not succeed, Amazon Data Firehose then skips that batch of records. The skipped
records are treated as unsuccessfully processed records. You can specify or override the
retry options using the [CreateDeliveryStream](../APIReference/API_CreateDeliveryStream.md "../APIReference/API_CreateDeliveryStream.md") or `UpdateDestination`
API. For this type of failure, you can log invocation errors to Amazon CloudWatch Logs. For more
information, see [Monitor Amazon Data Firehose Using
CloudWatch Logs](monitoring-with-cloudwatch-logs.md "monitoring-with-cloudwatch-logs.md").

If the status of the data transformation of a record is `ProcessingFailed`,
Amazon Data Firehose treats the record as unsuccessfully processed. For this type of failure, you can
emit error logs to Amazon CloudWatch Logs from your Lambda function. For more information, see [Accessing Amazon CloudWatch Logs for
AWS Lambda](../../../lambda/latest/dg/monitoring-functions-logs.md "../../../lambda/latest/dg/monitoring-functions-logs.md") in the _AWS Lambda Developer Guide_.

If a data transformation fails, the unsuccessfully processed records are delivered to
your S3 bucket in the `processing-failed` folder. The records have
the following format:

```
{
    "attemptsMade": "`count`",
    "arrivalTimestamp": "`timestamp`",
    "errorCode": "`code`",
    "errorMessage": "`message`",
    "attemptEndingTimestamp": "`timestamp`",
    "rawData": "`data`",
    "lambdaArn": "`arn`"
}
```

`attemptsMade`

The number of invocation requests attempted.

`arrivalTimestamp`

The time that the record was received by Amazon Data Firehose.

`errorCode`

The HTTP error code returned by Lambda.

`errorMessage`

The error message returned by Lambda.

`attemptEndingTimestamp`

The time that Amazon Data Firehose stopped attempting Lambda invocations.

`rawData`

The base64-encoded record data.

`lambdaArn`

The Amazon Resource Name (ARN) of the Lambda function.
