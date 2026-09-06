

# Protect sensitive data
<a name="mask-sensitive-data"></a>

Amazon CloudWatch Logs uses data protection policies to identify sensitive data and define actions to protect that data. You use data identifiers to select the sensitive data of interest. Amazon CloudWatch Logs then detects the sensitive data using machine learning and pattern matching. You can define audit and masking operations to log sensitive data findings and mask sensitive data when viewing log events.

For more information, see [Protecting sensitive log data with masking](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch-logs-data-protection-policies.html).

You can configure data protection for Amazon Bedrock AgentCore at the **account level** or at the **log group level**. With account level data protection, data protection rules are applied to all logs in your account. With log level data protection, data protection rules are can be applied to specific log groups in your account. This gives you granular control over how PII data is masked in your in your account.

**To configure data protection at the account level**

1. Open the Amazon CloudWatch console.

1. In the navigation pane, choose **Settings**.

1. Choose the **Logs** tab.

1. Choose **Configure the Data protection account policy**.

1. Specify the data identifiers that are relevant to your data.
   + To use a a predefined data identifier, in the **Managed data identifiers** drop-down, select the data identifiers that are relevant to your data.
   + To use a custom data identifier, choose **Add custom data identifier**, and then specify a name for the identifier and a Regex pattern for the data to protect.

1. (*Optional*) Choose a destination for the audit findings.
   + To send audit findings to a CloudWatch log, choose **Amazon CloudWatch Logs** and then select the destination log group.
   + To send audit findings to a Firehose stream, choose **Amazon Data Firehose** and then select the destination firehose stream.
   + To send audit findings to an Amazon S3 bucket, choose **Amazon S3** and then select the destination Amazon S3 bucket.

1. Choose **Activate data protection**.

**To configure data protection at the log group level**

1. Open the Amazon CloudWatch console.

1. In the navigation panel, choose **Logs**, **Log Management**.

1. Choose the **Log groups** tab, select the log group you want to enable data protection on, and then choose **Create data protection policy**.

1. Specify the data identifiers that are relevant to your data.
   + To use a a predefined data identifier, in the **Managed data identifiers** drop-down, select the data identifiers that are relevant to your data.
   + To use a custom data identifier, choose **Add custom data identifier**, and then specify a name for the identifier and a Regex pattern for the data to protect.

1. (*Optional*) Choose a destination for the audit findings.
   + To send audit findings to a CloudWatch log, choose **Amazon CloudWatch Logs** and then select the destination log group.
   + To send audit findings to a Firehose stream, choose **Amazon Data Firehose** and then select the destination firehose stream.
   + To send audit findings to an Amazon S3 bucket, choose **Amazon S3** and then select the destination Amazon S3 bucket.

1. Choose **Activate data protection**.