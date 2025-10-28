# Creating data protection

policies in Amazon SNS using the API

The number and size of Amazon SNS resources in an AWS account are limited. For more
information, see [Amazon Simple Notification Service
endpoints and quotas](../../../general/latest/gr/sns.md "../../../general/latest/gr/sns.md").

## Creating a data protection policy using API

Create an Amazon SNS data protection policy using the AWS API.

###### To create a data protection policy together with an Amazon SNS topic (AWS

API)

Use the `DataProtectionPolicy` property of a standard Amazon SNS
topic:

- [`CreateTopic`](../api/API_CreateTopic.md "../api/API_CreateTopic.md")

###### To retrieve or create a data protection policy for an existing Amazon SNS topic (AWS

API)

Call one of the following operations:

- [GetDataProtectionPolicy](../api/API_GetDataProtectionPolicy.md "../api/API_GetDataProtectionPolicy.md")
- [PutDataProtectionPolicy](../api/API_PutDataProtectionPolicy.md "../api/API_PutDataProtectionPolicy.md")
