

# Deleting data protection policies in Amazon SNS
<a name="sns-message-data-protection-delete"></a>

**Important**  
Amazon SNS message data protection is no longer available to new customers. For more information and guidance on alternatives, see [Amazon SNS message data protection availability change](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-availability-change.html).

You can **delete** Amazon SNS data protection policies using the AWS API, AWS CLI, CloudFormation, or AWS Management Console.

For general information about Amazon SNS data protection policies, see [Understanding Amazon SNS data protection policies](sns-message-data-protection-policies.md).

The number and size of Amazon SNS data protection policy resources in an AWS account are limited. For more information, see [ Amazon SNS API throttling](https://docs.aws.amazon.com/general/latest/gr/sns.html) in AWS General Reference.

## Deleting data protection policies using the console
<a name="sns-delete-data-protection-policy"></a>

**To delete a managed data protection policy using the console**

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home).

1. Choose the topic that contains the data protection policy that you want to delete.

1. Choose **Edit**.

1. Expand the **Data protection policy** section.

1. Choose **Remove** next to the data protection policy statement that you want to remove.

1. Choose **Save changes**.

## Deleting a data protection policy using an empty JSON string
<a name="sns-message-data-protection-remove-example-json"></a>

You can delete a data protection policy by updating it to an empty JSON string.

## Deleting a data protection policy using the AWS CLI
<a name="sns-message-data-protection-remove-example-cli"></a>

You can delete a data protection policy using the AWS CLI.

`//aws sns put-data-protection-policy --resource-arn {{topic-arn}} --data-protection-policy ""`