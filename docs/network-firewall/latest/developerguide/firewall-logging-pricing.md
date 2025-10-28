# Pricing for AWS Network Firewall logging

You are charged for Amazon CloudWatch _vended logs_, on top of the basic
charges for using Network Firewall. Additionally, you incur charges when querying logs,
whether through CloudWatch and or through Amazon Athena for logs stored in Amazon S3. Vended logs are specific AWS service logs published by AWS
on your behalf at volume discount pricing.

Your logging costs can vary depending on factors such as the destination type that you choose and the
amount of data that you log. For example, flow logging sends logs for all of the
network traffic that reaches your firewall's stateful rules, but alert logging sends
logs only for network traffic that your stateful rules drop or explicitly alert on.

Review the following resources to understand the pricing considerations for using firewall logs:

- For information about CloudWatch vended log pricing, see [Logs](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/") on the _Amazon CloudWatch
  pricing_ page.
- For information about Network Firewall pricing, see
  [Network Firewall pricing](https://aws.amazon.com/network-firewall/pricing/ "https://aws.amazon.com/network-firewall/pricing/").
- For information about Amazon S3 pricing, see
  [Amazon S3 pricing](https://aws.amazon.com/S3/pricing/ "https://aws.amazon.com/S3/pricing/").
- For information about Amazon Athena pricing, see [Amazon Athena pricing](https://aws.amazon.com/athena/pricing/ "https://aws.amazon.com/athena/pricing/").
