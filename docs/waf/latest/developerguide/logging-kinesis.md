**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Sending protection pack (web ACL) traffic logs to an Amazon Data Firehose delivery stream

This section provides information for sending your protection pack (web ACL) traffic logs to an
Amazon Data Firehose delivery stream.

###### Note

You are charged for logging in addition to the charges for using
AWS WAF. For information, see [Pricing for logging protection pack (web ACL) traffic information](logging-pricing.md "logging-pricing.md").

To send logs to Amazon Data Firehose, you send logs from your protection pack (web ACL) to an Amazon Data Firehose delivery stream
which you configure in Firehose. After you enable logging, AWS WAF delivers
logs to your storage destination through the HTTPS endpoint of Firehose.

One AWS WAF log is equivalent to one Firehose record. If you typically receive 10,000
requests per second and you enable full logs, you should have a 10,000 records per
second setting in Firehose. If you don't configure Firehose correctly, AWS WAF won't record
all logs. For more information, see [Amazon Kinesis
Data Firehose quotas](../../../firehose/latest/dev/limits.md "../../../firehose/latest/dev/limits.md").

For information about how to create an Amazon Data Firehose delivery stream and review your stored logs,
see [What is Amazon Data Firehose?](../../../firehose/latest/dev/what-is-this-service.md "../../../firehose/latest/dev/what-is-this-service.md")

For information about creating your delivery stream, see [Creating
an Amazon Data Firehose delivery stream](../../../firehose/latest/dev/basic-create.md "../../../firehose/latest/dev/basic-create.md").

## Configuring an Amazon Data Firehose delivery stream for your protection pack (web ACL)

Configure an Amazon Data Firehose delivery stream for your protection pack (web ACL) as follows.

- Create it using the same account as you use to manage the protection pack (web ACL).
- Create it in the same Region as the protection pack (web ACL). If you are capturing logs for
  Amazon CloudFront, create the firehose in US East (N. Virginia) Region,
  `us-east-1`.
- Give the data firehose a name that starts with the prefix
  `aws-waf-logs-`. For example,
  `aws-waf-logs-us-east-2-analytics`.
- Configure it for direct put, which allows applications to access the
  delivery stream directly. In the [Amazon Data Firehose console](https://console.aws.amazon.com/firehose "https://console.aws.amazon.com/firehose"),
  for the delivery
  stream **Source** setting, choose **Direct PUT
  or other sources**. Through the API, set the delivery
  stream property `DeliveryStreamType` to
  `DirectPut`.

###### Note

Do not use a `Kinesis stream` as your source.

## Permissions required to publish

logs to an Amazon Data Firehose delivery stream

To understand the permissions required for your Kinesis Data Firehose
configuration, see [Controlling Access with
Amazon Kinesis Data Firehose](../../../firehose/latest/dev/controlling-access.md "../../../firehose/latest/dev/controlling-access.md").

You must have the following permissions to successfully enable protection pack (web ACL) logging
with an Amazon Data Firehose delivery stream.

- `iam:CreateServiceLinkedRole`
- `firehose:ListDeliveryStreams`
- `wafv2:PutLoggingConfiguration`

For information about service-linked roles and the
`iam:CreateServiceLinkedRole` permission, see [Using service-linked roles for AWS WAF](using-service-linked-roles.md "using-service-linked-roles.md").
