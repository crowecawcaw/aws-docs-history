# Creating data protection policies in Amazon SNS using the CLI

###### Important

Amazon SNS message data protection will no longer be available to new customers starting April 30, 2026.
For more information and guidance on alternatives, see
[Amazon SNS message data protection availability change](sns-message-data-protection-availability-change.md "sns-message-data-protection-availability-change.md").

The number and size of Amazon SNS resources in an AWS account are limited. For more
information, see [Amazon Simple Notification Service
endpoints and quotas](../../../general/latest/gr/sns.md "../../../general/latest/gr/sns.md").

## Creating data protection policies using the AWS CLI

Create an Amazon SNS data protection policy using the AWS Command Line Interface.

###### To create a data protection policy together with an Amazon SNS topic (AWS CLI)

Use this option to create a new data protection policy together with a standard
Amazon SNS topic:

- [create-topic](../../../cli/latest/reference/sns/create-topic.md "../../../cli/latest/reference/sns/create-topic.md")

###### To create or retrieve a data protection policy for an existing Amazon SNS topic (AWS CLI)

Call one of the following operations:

- [get-data-protection-policy](../../../cli/latest/reference/sns/get-data-protection-policy.md "../../../cli/latest/reference/sns/get-data-protection-policy.md")
- [put-data-protection-policy](../../../cli/latest/reference/sns/put-data-protection-policy.md "../../../cli/latest/reference/sns/put-data-protection-policy.md")
