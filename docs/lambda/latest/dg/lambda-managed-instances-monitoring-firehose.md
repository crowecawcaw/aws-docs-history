# Sending capacity provider system logs to Firehose

You can send capacity provider system logs to Amazon Data Firehose. With Firehose, you can stream logs in real time to various destinations, including third-party analytics tools and custom endpoints.

###### Note

You can configure capacity provider system logs to be sent to Firehose using the AWS CLI, AWS CloudFormation, and all AWS SDKs.

## Pricing

For more information about pricing, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/#Vended_Logs "https://aws.amazon.com/cloudwatch/pricing/#Vended_Logs").

## Setting up Firehose log delivery

To send capacity provider system logs to Firehose, create a CloudWatch Logs subscription filter on your capacity provider's log group. The subscription filter routes log events to your Firehose delivery stream.

By default, your capacity provider's log group is named `/aws/lambda/capacity-provider/`<capacity-provider-name>``. Use this log group when creating the subscription filter.

For instructions on setting up a subscription filter for Firehose, including IAM role creation and permissions, see [Subscription filters with Firehose](../../../AmazonCloudWatch/latest/logs/SubscriptionFilters.md#FirehoseExample "../../../AmazonCloudWatch/latest/logs/SubscriptionFilters.md#FirehoseExample") in the _Amazon CloudWatch User Guide_.

## Cross-account logging

You can configure your capacity provider to send logs to a Firehose delivery stream in a different AWS account. This requires setting up a destination and configuring appropriate permissions in both accounts.

For instructions on setting up cross-account logging, including required IAM roles and policies, see [Setting up a new cross-account subscription](../../../AmazonCloudWatch/latest/logs/CrossAccountSubscriptions.md "../../../AmazonCloudWatch/latest/logs/CrossAccountSubscriptions.md") in the _Amazon CloudWatch User Guide_.
