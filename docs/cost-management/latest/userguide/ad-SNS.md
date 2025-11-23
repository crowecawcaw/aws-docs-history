# Creating an Amazon SNS topic for anomaly notifications

To create an anomaly detection monitor that sends notifications to an Amazon Simple Notification Service
(Amazon SNS) topic, you must already have Amazon SNS topic or create a new one. You can use Amazon SNS
topics to send notifications over Amazon SNS in addition to email. AWS Cost Anomaly Detection must have
permissions to send a notification to your topic.

###### To create an Amazon SNS notification topic and grant permissions

1. Sign in to the AWS Management Console and open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation pane, choose **Topics**.
3. Choose **Create topic**.
4. For **Name**, enter the name for your notification
   topic.
5. (Optional) For **Display name**, enter the name that you want
   displayed when you receive a notification.
6. In **Access policy**, choose
   **Advanced**.
7. In the policy text field, after **"Statement": [**, enter
   one of the following statements:

To allow the AWS Cost Anomaly Detection service to publish to the Amazon SNS topic, use the following
statement.

```
{
  "Sid": `"E.g., AWSAnomalyDetectionSNSPublishingPermissions"`,
  "Effect": "Allow",
  "Principal": {
    "Service": "costalerts.amazonaws.com"
  },
  "Action": "SNS:Publish",
  "Resource": `"your topic ARN"`
}

```

To allow the AWS Cost Anomaly Detection service to publish to the Amazon SNS topic only on behalf of
a certain account, use the following statement.

```
{
  "Sid": `"E.g., AWSAnomalyDetectionSNSPublishingPermissions"`,
  "Effect": "Allow",
  "Principal": {
    "Service": "costalerts.amazonaws.com"
  },
  "Action": "SNS:Publish",
  "Resource": `"your topic ARN"`,
  "Condition": {
        "StringEquals": {
          "aws:SourceAccount": [
            `"account-ID"`
          ]
        }
  }
}
```

###### Note

In this topic policy, you enter the subscription’s account ID as the value
for the `aws:SourceAccount` condition. This condition has
AWS Cost Anomaly Detection interact with the Amazon SNS topic only when performing operations for
the account that owns the subscription.

You can restrict AWS Cost Anomaly Detection to interact with the topic only when performing
operations on behalf of a specific subscription. To do this, use the
`aws:SourceArn` condition in the topic policy.

For more information about these conditions, see [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") and [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") in the
_IAM User Guide_. 8. In the topic policy statement that you select, replace the following
values:

    * Replace (for example,
     `AWSAnomalyDetectionSNSPublishingPermissions`)
     with a string. The `Sid` must be unique within the
     policy.
    * Replace `your topic ARN` with the Amazon SNS topic
     Amazon Resource Name (ARN).
    * If you're using the statement with the `aws:SourceAccount`
     condition, replace `account-ID` with the
     account ID that owns the subscription. If the Amazon SNS topic has multiple
     subscriptions from different accounts, add multiple account IDs to the
     `aws:SourceAccount` condition.

9. Choose **Create topic**.

Your topic now appears in the list of topics on the
**Topics** page.

## Checking or resending notification

confirmation email messages

When you create an anomaly detection monitor with notifications, you also create
Amazon SNS notifications. For notifications to be sent, you must accept the subscription
to the Amazon SNS notification topic.

To confirm that your notification subscriptions are accepted or to resend a
subscription confirmation email, use the Amazon SNS console.

###### To check your notification status or to resend a notification confirmation

email message

1. Sign in to the AWS Management Console and open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation pane, choose **Subscriptions**.
3. Check the status of your notification. Under **Status**,
   `PendingConfirmation` appears if a subscription isn't
   accepted and confirmed.
4. (Optional) To resend a confirmation request, select the subscription with
   a pending confirmation and choose **Request confirmation**.
   Amazon SNS sends a confirmation request to the endpoints that are subscribed to
   the notification.

When each owner of an endpoint receives the email, they must choose the
**Confirm subscription** link to activate the
notification.

## Protecting your Amazon SNS anomaly detection alerts

data with SSE and AWS KMS

You can use server-side encryption (SSE) to transfer sensitive data in encrypted
topics. SSE protects Amazon SNS messages by using keys managed in AWS Key Management Service
(AWS KMS).

To manage SSE using AWS Management Console or the AWS SDK, see [Enabling
Server-Side Encryption (SSE) for an Amazon SNS Topic](../../../sns/latest/dg/sns-tutorial-enable-encryption-for-topic.md "../../../sns/latest/dg/sns-tutorial-enable-encryption-for-topic.md") in the _Amazon Simple Notification Service Getting Started Guide_.

To create encrypted topics using AWS CloudFormation, see the [AWS CloudFormation User
Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md").

SSE encrypts messages as soon as Amazon SNS receives them. The messages are stored
encrypted and are decrypted using Amazon SNS only when they're sent.

### Configuring AWS KMS permissions

You must configure your AWS KMS key policies before you can use server-side
encryption (SSE). You can use this configuration to encrypt topics, in addition
to encrypting and decrypting messages. For information about AWS KMS permissions,
see [AWS KMS API
Permissions: Actions and Resources Reference](../../../kms/latest/developerguide/kms-api-permissions-reference.md "../../../kms/latest/developerguide/kms-api-permissions-reference.md") in the _AWS Key Management Service Developer Guide_.

You can also use IAM policies to manage AWS KMS key permissions. For more
information, see [Using IAM Policies with
AWS KMS](../../../kms/latest/developerguide/iam-policies.md "../../../kms/latest/developerguide/iam-policies.md").

###### Note

You can configure global permissions to send and receive message from
Amazon SNS. However, AWS KMS requires that you name the full Amazon Resource Name
(ARN) of the AWS KMS keys (KMS keys) in the specific AWS Regions. You
can find this in the **Resource** section of an IAM
policy.

Ensure that the key policies of the KMS key allow the necessary
permissions. To do this, name the principals that produce and consume
encrypted messages in Amazon SNS as users in the KMS key policy.

###### To enable compatibility between AWS Cost Anomaly Detection

and encrypted Amazon SNS topics

1. [Create a KMS key](../../../kms/latest/developerguide/create-keys.md#create-keys-console "../../../kms/latest/developerguide/create-keys.md#create-keys-console").
2. Add one of the following policies as the KMS key policy:

To grant the AWS Cost Anomaly Detection service access to the KMS key, use the
following statement.

JSON

```
`{
 "Version": "`2012-10-17`",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "costalerts.amazonaws.com"
 },
 "Action": [
 "kms:GenerateDataKey*",
 "kms:Decrypt"
 ],
 "Resource": "`*`"
 }
 ]
}`

```

To grant the AWS Cost Anomaly Detection service access to the KMS key only when
performing operations on behalf of a certain account, use the following
statement.

JSON

```
`{
 "Version": "`2012-10-17`",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "costalerts.amazonaws.com"
 },
 "Action": [
 "kms:GenerateDataKey*",
 "kms:Decrypt"
 ],
 "Resource": "`*`",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": [
 "`account-ID`"
 ]
 }
 }
 }
 ]
}`

```

###### Note

In this KMS key policy, you enter the subscription’s account ID
as the value for the `aws:SourceAccount` condition. This
condition has AWS Cost Anomaly Detection interact with the KMS key only when
performing operations for the account that owns the
subscription.

To have AWS Cost Anomaly Detection interact with the KMS key only when performing
operations on behalf of a specific subscription, use the
`aws:SourceArn` condition in the KMS key
policy.

For more information about these conditions, see [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") and [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") in the
_IAM User Guide_. 3. If you're using the KMS key policy with the
`aws:SourceAccount` condition, replace
`account-ID` with the account ID that owns
the subscription. If the Amazon SNS topic has multiple subscriptions from
different accounts, add multiple account IDs to the
`aws:SourceAccount` condition. 4. [Enable SSE for your Amazon SNS topic](../../../sns/latest/dg/sns-tutorial-enable-encryption-for-topic.md "../../../sns/latest/dg/sns-tutorial-enable-encryption-for-topic.md").

###### Note

Make sure that you're using the same KMS key that grants
AWS Cost Anomaly Detection the permissions to publish to encrypted Amazon SNS
topics. 5. Choose **Save Changes**.
