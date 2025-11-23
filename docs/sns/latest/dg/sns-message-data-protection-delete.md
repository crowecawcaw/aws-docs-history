# Deleting data protection policies in

Amazon SNS

You can **delete** Amazon SNS data protection policies using the
AWS API, AWS CLI, CloudFormation, or AWS Management Console.

For general information about Amazon SNS data protection policies, see [Understanding Amazon SNS data protection
policies](sns-message-data-protection-policies.md "sns-message-data-protection-policies.md").

The number and size of Amazon SNS data protection policy resources in an AWS
account are limited. For more information, see [Amazon SNS API throttling](../../../general/latest/gr/sns.md "../../../general/latest/gr/sns.md") in AWS General Reference.

## Deleting data protection policies

using the console

###### To delete a managed data protection policy using the console

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. Choose the topic that contains the data protection policy that you want to
   delete.
3. Choose **Edit**.
4. Expand the **Data protection policy** section.
5. Choose **Remove** next to the data protection policy
   statement that you want to remove.
6. Choose **Save changes**.

## Deleting a data

protection policy using an empty JSON string

You can delete a data protection policy by updating it to an empty JSON string.

## Deleting a data

protection policy using the AWS CLI

You can delete a data protection policy using the AWS CLI.

`//aws sns put-data-protection-policy --resource-arn
 `topic-arn` --data-protection-policy ""`
