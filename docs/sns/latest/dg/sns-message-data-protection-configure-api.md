

# Creating data protection policies in Amazon SNS using the API
<a name="sns-message-data-protection-configure-api"></a>

**Important**  
Amazon SNS message data protection is no longer available to new customers. For more information and guidance on alternatives, see [Amazon SNS message data protection availability change](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-availability-change.html).

The number and size of Amazon SNS resources in an AWS account are limited. For more information, see [Amazon Simple Notification Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sns.html).

## Creating a data protection policy using API
<a name="create-policies-api"></a>

Create an Amazon SNS data protection policy using the AWS API.

**To create a data protection policy together with an Amazon SNS topic (AWS API)**  
Use the `DataProtectionPolicy` property of a standard Amazon SNS topic:
+ [`CreateTopic`](https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html)

**To retrieve or create a data protection policy for an existing Amazon SNS topic (AWS API)**  
Call one of the following operations:
+ [GetDataProtectionPolicy](https://docs.aws.amazon.com/sns/latest/api/API_GetDataProtectionPolicy.html)
+ [PutDataProtectionPolicy](https://docs.aws.amazon.com/sns/latest/api/API_PutDataProtectionPolicy.html)