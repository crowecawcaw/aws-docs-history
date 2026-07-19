# Sending capacity provider system logs to Amazon S3

You can send capacity provider system logs to Amazon Simple Storage Service. With Amazon S3, you can store logs cost-effectively for long-term retention and analyze them using services like Athena.

###### Note

You can configure capacity provider system logs to be sent to Amazon S3 using the AWS CLI, AWS CloudFormation, and all AWS SDKs.

## Pricing

For more information about pricing, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/#Vended_Logs "https://aws.amazon.com/cloudwatch/pricing/#Vended_Logs").

## Setting up Amazon S3 log delivery

To send capacity provider system logs to Amazon S3, create a CloudWatch Logs subscription filter on your capacity provider's log group. The subscription filter routes log events to your Amazon S3 bucket.

By default, your capacity provider's log group is named `/aws/lambda/capacity-provider/`<capacity-provider-name>``. Use this log group when creating the subscription filter.

For instructions on setting up a subscription filter for Amazon S3, including IAM role creation and bucket permissions, see [Sending Lambda function logs to Amazon S3](logging-with-s3.md "logging-with-s3.md").

## Cross-account logging

You can configure your capacity provider to send logs to an Amazon S3 bucket in a different AWS account. This requires setting up a destination and configuring appropriate permissions in both accounts.

For instructions on setting up cross-account logging, including required IAM roles and policies, see [Setting up a new cross-account subscription](../../../AmazonCloudWatch/latest/logs/CrossAccountSubscriptions.md "../../../AmazonCloudWatch/latest/logs/CrossAccountSubscriptions.md") in the _Amazon CloudWatch User Guide_.
