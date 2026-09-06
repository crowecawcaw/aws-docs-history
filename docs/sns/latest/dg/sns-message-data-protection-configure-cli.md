

# Creating data protection policies in Amazon SNS using the CLI
<a name="sns-message-data-protection-configure-cli"></a>

**Important**  
Amazon SNS message data protection is no longer available to new customers. For more information and guidance on alternatives, see [Amazon SNS message data protection availability change](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-availability-change.html).

The number and size of Amazon SNS resources in an AWS account are limited. For more information, see [Amazon Simple Notification Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sns.html).

## Creating data protection policies using the AWS CLI
<a name="create-policies-cli"></a>

Create an Amazon SNS data protection policy using the AWS Command Line Interface. 

**To create a data protection policy together with an Amazon SNS topic (AWS CLI)**  
Use this option to create a new data protection policy together with a standard Amazon SNS topic:
+ [create-topic](https://docs.aws.amazon.com/cli/latest/reference/sns/create-topic.html)

**To create or retrieve a data protection policy for an existing Amazon SNS topic (AWS CLI)**  
Call one of the following operations:
+ [get-data-protection-policy](https://docs.aws.amazon.com/cli/latest/reference/sns/get-data-protection-policy.html)
+ [put-data-protection-policy](https://docs.aws.amazon.com/cli/latest/reference/sns/put-data-protection-policy.html)