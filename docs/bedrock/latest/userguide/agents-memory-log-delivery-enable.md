# Enable memory summarization log delivery

To enable logging for your Amazon Bedrock agent alias, use the [PutDeliverySource](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md") CloudWatch API. Make sure to specify the following:

- For `resourceArn`, provide the Amazon Resource Name (ARN) of the agent alias that is generating and sending the logs
- For `logType`, specify `APPLICATION_LOGS` as the supprted log type.
  You will also need the add `bedrock:AllowVendedLogDeliveryForResource` permission for the user signed into the console. This permission allows logs to be delivered for the agent alias resource.

To view an example IAM role/permissions policy with all the required permissions for your specific logging destination, see [Vended logs permissions for different delivery destinations](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-vended-logs-permissions-V2 "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-vended-logs-permissions-V2"). Use the example to provide details for your logging destination, including allowing updates to your specific logging destination resource (CloudWatch Logs, Amazon S3, or Amazon Data Firehose).
