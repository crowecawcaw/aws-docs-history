

# Amazon SNS message data protection availability change
<a name="sns-message-data-protection-availability-change"></a>

**Important**  
Amazon SNS message data protection is no longer available to new customers. For more information and guidance on alternatives, see [Amazon SNS message data protection availability change](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-availability-change.html).

After careful consideration, the Amazon SNS message data protection feature will no longer be available to new customers effective on April 30, 2026. If you are an existing customer with SNS message data protection policies configured, you may continue to use the feature within those accounts. While we will not be introducing enhancements to the feature, we remain committed to providing security updates.

## Alternative architecture
<a name="sns-mdp-alternative-architecture"></a>

An AWS Lambda-based architecture using Amazon Bedrock Guardrails is the recommended approach for customers seeking an alternative solution. This solution enables real-time sensitive data detection and protection with the flexibility to customize data protection to meet your specific requirements.

An example demonstrating this recommended architecture is available in the AWS Samples repository on GitHub: [Protect Sensitive Data in SNS Messages using Amazon Bedrock Guardrails](https://github.com/aws-samples/sample-sns-sensitive-data-protection-bedrock). The example shows how to leverage Amazon Bedrock Guardrails and custom pattern matching for sensitive data detection.  

**Architecture overview**  
The recommended Lambda-based architecture works as follows:

1. Publishers send messages to an inbound Amazon SNS topic.

1. A Lambda function subscribed to the inbound topic inspects message content.

1. The Lambda function leverages Amazon Bedrock Guardrails to detect sensitive data in the message and apply your policies:
   + **LOG** – Log sensitive detection and publish the original message.
   + **BLOCK** – Drop the message entirely.
   + **REDACT** – Redact sensitive data and publish the redacted message.

1. Processed messages are published to your destination Amazon SNS topic for delivery to your topic subscribers.

For further guidance and sample code, see [Protect Sensitive Data in SNS Messages using Amazon Bedrock Guardrails](https://github.com/aws-samples/sample-sns-sensitive-data-protection-bedrock).  

## Viewing existing message data protection policies
<a name="sns-mdp-view-existing-policies"></a>

If you currently use Amazon SNS message data protection, you can review your configured policies through the AWS Management Console or AWS CLI.

**Using the AWS Management Console**

1. Navigate to the [Amazon SNS console](https://console.aws.amazon.com/sns/).

1. Select **Topics** from the navigation panel.

1. Choose a topic to view its details.

1. Check if a data protection policy is configured on the **Data protection policy** tab.

**Using the AWS CLI**  
To check if a specific topic has message data protection enabled, run the following command. Replace {{topic-arn}} with your Amazon SNS topic ARN.

```
aws sns get-data-protection-policy --resource-arn {{topic-arn}}
```

## Disabling Amazon SNS message data protection
<a name="sns-mdp-disable"></a>

You can remove data protection policies from your Amazon SNS topics at any time, whether you're migrating to a Lambda-based alternative or no longer require data protection. The policy removal process can be completed through the AWS Management Console, AWS CLI, or your infrastructure as code (IaC) tools.

**Using the AWS Management Console**

1. Navigate to the [Amazon SNS console](https://console.aws.amazon.com/sns/).

1. Select **Topics** from the navigation panel.

1. Choose the topic you want to modify.

1. Select **Edit**.

1. Go to the **Data protection policy** section.

1. Remove the data protection policy configuration associated with the topic.

**Using the AWS CLI**  
To disable message data protection, delete the data protection policy from your topic. Replace {{topic-arn}} with your Amazon SNS topic ARN.

```
aws sns put-data-protection-policy --resource-arn {{topic-arn}} --data-protection-policy ""
```

If you have additional questions, contact [AWS Support](https://console.aws.amazon.com/support/home#/).