AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Configuring Amazon SNS topics for Change Manager

notifications

###### Change Manager availability change

AWS Systems Manager Change Manager will no longer be open to new customers
starting November 7, 2025. If you would like to use Change Manager, sign up prior to that
date. Existing customers can continue to use the service as normal. For more
information, see [AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

You can configure Change Manager, a tool in AWS Systems Manager, to send notifications to an
Amazon Simple Notification Service (Amazon SNS) topic for events related to change requests and
change templates. Complete the following tasks to receive notifications for the
Change Manager events you add a topic to.

###### Topics

- [Task 1: Create and
  subscribe to an Amazon SNS topic](#change-manager-sns-setup-create-topic "#change-manager-sns-setup-create-topic")
- [Task 2: Update
  the Amazon SNS access policy](#change-manager-sns-setup-encryption-policy "#change-manager-sns-setup-encryption-policy")
- [Task 3: (Optional)
  Update the AWS Key Management Service access policy](#change-manager-sns-setup-KMS-policy "#change-manager-sns-setup-KMS-policy")

## Task 1: Create and

subscribe to an Amazon SNS topic

First, you must create and subscribe to an Amazon SNS topic. For more
information, see [Creating a Amazon SNS topic](../../../sns/latest/dg/sns-create-topic.md "../../../sns/latest/dg/sns-create-topic.md")
and [Subscribing to an Amazon SNS topic](../../../sns/latest/dg/sns-tutorial-create-subscribe-endpoint-to-topic.md "../../../sns/latest/dg/sns-tutorial-create-subscribe-endpoint-to-topic.md") in the
_Amazon Simple Notification Service Developer Guide_.

###### Note

To receive notifications, you must specify the Amazon Resource Name
(ARN) of an Amazon SNS topic that is in the same AWS Region and
AWS account as the delegated administrator account.

## Task 2: Update

the Amazon SNS access policy

Use the following procedure to update the Amazon SNS access policy so that
Systems Manager can publish Change Manager notifications to the Amazon SNS topic you created in
Task 1. Without completing this task, Change Manager doesn't have permission to
send notifications for the events you add the topic for.

1. Sign in to the AWS Management Console and open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation pane, choose **Topics**.
3. Choose the topic you created in Task 1, and then choose
   **Edit**.
4. Expand **Access policy**.
5. Add and update the following `Sid` block to the
   existing policy and replace each `user input
placeholder` with your own information .

```
{
    "Sid": "Allow Change Manager to publish to this topic",
    "Effect": "Allow",
    "Principal": {
        "Service": "ssm.amazonaws.com"
    },
    "Action": "sns:Publish",
    "Resource": "arn:aws:sns:`region`:`account-id`:`topic-name`",
    "Condition": {
        "StringEquals": {
            "aws:SourceAccount": [
                "`account-id`"
            ]
        }
    }
}
```

Enter this block after the existing `Sid` block, and
replace `region`,
`account-id`, and
`topic-name` with the appropriate
values for the topic you created. 6. Choose **Save changes**.

The system now sends notifications to the Amazon SNS topic when the event type
you add to topic for occurs.

###### Important

If you configured the Amazon SNS topic with an AWS Key Management Service (AWS KMS)
server-side encryption key, then you must complete Task 3.

## Task 3: (Optional)

Update the AWS Key Management Service access policy

If you turned on AWS Key Management Service (AWS KMS) server-side encryption for your Amazon SNS
topic, then you must also update the access policy of the AWS KMS key you
chose when you configured the topic. Use the following procedure to update
the access policy so that Systems Manager can publish Change Manager approval notifications
to the Amazon SNS topic you created in Task 1.

1. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. In the navigation pane, choose **Customer managed keys**.
3. Choose the ID of the customer managed key you chose when you created the
   topic.
4. In the **Key policy** section, choose
   **Switch to policy view**.
5. Choose **Edit**.
6. Enter the following `Sid` block after one of the
   existing `Sid` blocks in the existing policy. Replace
   each `user input placeholder` with your own
   information.

```
{
    "Sid": "Allow Change Manager to decrypt the key",
    "Effect": "Allow",
    "Principal": {
        "Service": "ssm.amazonaws.com"
    },
    "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey*"
    ],
    "Resource": "arn:aws:kms:`region`:`account-id`:key/`key-id`",
    "Condition": {
        "StringEquals": {
            "aws:SourceAccount": [
                "`account-id`"
            ]
        }
    }
}
```

7. Now enter the following `Sid` block after one of the
   existing `Sid` blocks in the resource policy to help
   prevent the [cross-service
   confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md").

This block uses the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition
context keys to limit the permissions that Systems Manager gives another
service to the resource.

Replace each `user input placeholder`
with your own information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Configure confused deputy protection for AWS KMS keys used in Amazon SNS topic when called from Systems Manager",
 "Effect": "Allow",
 "Principal": {
 "Service": "ssm.amazonaws.com"
 },
 "Action": [
 "sns:Publish"
 ],
 "Resource": "arn:aws:sns:`us-east-1`:`111122223333`:`topic-name`",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:ssm:`us-east-1`:`111122223333`:*"
 },
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 }
 }
 }
 ]
}`

```

8. Choose **Save changes**.
