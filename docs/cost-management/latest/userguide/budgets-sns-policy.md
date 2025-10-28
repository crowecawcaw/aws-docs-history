# Creating an Amazon SNS topic for budget

notifications

When you create a budget that sends notifications to an Amazon Simple Notification Service (Amazon SNS) topic, you need to
either have a preexisting Amazon SNS topic or create one. Amazon SNS topics allow you to send
notifications over SNS in addition to email. Your budget must have permissions to send a
notification to your topic.

To create an Amazon SNS topic and grant permissions to your budget, use the Amazon SNS console.

###### Note

Amazon SNS topics must be in the same account as the Budgets you're configuring. Cross-account Amazon SNS isn't supported.

###### To create an Amazon SNS notification topic and grant permissions

1. Sign in to the AWS Management Console and open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. On the navigation pane, choose **Topics**.
3. Choose **Create topic**.
4. For **Name**, enter the name for your notification topic.
5. (Optional) For **Display name**, enter the name that you want displayed when you receive
   a notification.
6. In **Access policy**, choose **Advanced**.
7. In the policy text field, after **"Statement": [**, add the
   following text:

```
{
  "Sid": "`E.g., AWSBudgetsSNSPublishingPermissions`",
  "Effect": "Allow",
  "Principal": {
    "Service": "budgets.amazonaws.com"
  },
  "Action": "SNS:Publish",
  "Resource": "`your topic ARN`",
   "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "`<account-id>`"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:budgets::`<account-id>`:*"
        }
      }
}
```

8. Replace **E.g., AWSBudgetsSNSPublishingPermissions** with a string. The
   `Sid` must be unique within the policy.
9. Choose **Create topic**.
10. Under **Details**, save your ARN.
11. Choose **Edit**.
12. Under **Access policy**, replace `your topic ARN` with the Amazon SNS topic ARN from step 10.
13. Choose **Save changes**.

Your topic now appears in the list of topics on the **Topics** page.

## Troubleshooting

You might encounter the following error messages when you’re creating your Amazon SNS topic for budget notifications.

**Please comply with SNS ARN format**

There’s a syntax error in the ARN you replaced (step 9). Confirm the ARN for proper syntax and formatting.

**Invalid SNS topic**

AWS Budgets doesn’t have access to the SNS topic. Confirm that you’ve allowed budgets.amazonaws.com the ability to publish messages to this SNS topic, in the SNS topic’s resource based policy.

**The SNS topic is encrypted**

You have **encryption** enabled on the SNS topic. The SNS topic won’t work without additional permissions. Disable encryption on the topic, and refresh the **Budget edit** page.

## Checking or resending notification confirmation emails

When you create a budget with notifications, you also create Amazon SNS notifications. For
notifications to be sent, you must accept the subscription to the Amazon SNS notification
topic.

To confirm that your notification subscriptions have been accepted or to resend a
subscription confirmation email, use the Amazon SNS console.

###### To check your notification status or to resend a notification confirmation email

1. Sign in to the AWS Management Console and open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. On the navigation pane, choose **Subscriptions**.
3. On the **Subscriptions** page, for **Filter**, enter `budget`. A list of your budget notifications appears.
4. Check the status of your notification. Under **Status**, `PendingConfirmation` appears if a subscription hasn't been
   accepted and confirmed.
5. (Optional) To resend a confirmation request, select the subscription with a pending
   confirmation and choose **Request confirmation**. Amazon SNS sends a
   confirmation request to the endpoints that are subscribed to the
   notification.

When each owner of an endpoint receives the email, they must choose the **Confirm
subscription** link to activate the notification.

## Protecting your Amazon SNS budget alerts data with SSE and

AWS KMS

You can use server-side encryption (SSE) to transfer sensitive data in encrypted topics. SSE
protects Amazon SNS messages by using keys managed in AWS Key Management Service (AWS KMS).

To manage SSE using AWS Management Console or the AWS Service Development Kit (SDK), see [Enabling
Server-Side Encryption (SSE) for an Amazon SNS Topic](../../../sns/latest/dg/sns-tutorial-enable-encryption-for-topic.md "../../../sns/latest/dg/sns-tutorial-enable-encryption-for-topic.md") in the _Amazon Simple Notification Service Getting Started Guide_.

To create encrypted topics using AWS CloudFormation, see the [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md").

SSE encrypts messages as soon as Amazon SNS receives them. The messages are stored encrypted and
are decrypted using Amazon SNS only when they're sent.

### Configuring AWS KMS permissions

You must configure your AWS KMS key policies before you can use SSE. The configuration
enables you to encrypt topics, as well as encrypt and decrypt messages. For details
about AWS KMS permissions, see [AWS KMS API
Permissions: Actions and Resources Reference](../../../kms/latest/developerguide/kms-api-permissions-reference.md "../../../kms/latest/developerguide/kms-api-permissions-reference.md") in the _AWS Key Management Service Developer Guide_.

You can also use IAM policies to manage AWS KMS key permissions. For more information, see
[Using IAM Policies with AWS KMS](../../../kms/latest/developerguide/iam-policies.md "../../../kms/latest/developerguide/iam-policies.md").

###### Note

Although you can configure global permissions to send and receive message from Amazon SNS, AWS KMS requires you to name the full ARN of AWS KMS keys (KMS key) in the specific Regions. You can find this in the **Resource** section of an IAM policy.

You must ensure that the key policies of the KMS keys allow the necessary permissions. To do this, name the principals that produce and consume encrypted messages in Amazon SNS as users in the KMS key policy.

###### To enable compatibility between AWS Budgets and

encrypted Amazon SNS topics

1. [Create a KMS key](../../../kms/latest/developerguide/create-keys.md#create-keys-console "../../../kms/latest/developerguide/create-keys.md#create-keys-console").
2. Add the following text to the KMS key policy.
3. [Enable SSE for your SNS topic](../../../sns/latest/dg/sns-tutorial-enable-encryption-for-topic.md "../../../sns/latest/dg/sns-tutorial-enable-encryption-for-topic.md").

###### Note

Be sure that you're using the same KMS key that grants AWS Budgets the permissions to publish to
encrypted Amazon SNS topics. 4. Choose **Save Changes**.
