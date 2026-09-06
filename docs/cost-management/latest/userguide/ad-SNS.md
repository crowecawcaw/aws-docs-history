

# Creating an Amazon SNS topic for anomaly notifications
<a name="ad-SNS"></a>

To create an anomaly detection monitor that sends notifications to an Amazon Simple Notification Service (Amazon SNS) topic, you must already have Amazon SNS topic or create a new one. You can use Amazon SNS topics to send notifications over Amazon SNS in addition to email. AWS Cost Anomaly Detection must have permissions to send a notification to your topic. 

**To create an Amazon SNS notification topic and grant permissions**

1. Sign in to the AWS Management Console and open the Amazon SNS console at [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home).

1. In the navigation pane, choose **Topics**.

1. Choose **Create topic**.

1. For **Name**, enter the name for your notification topic.

1. (Optional) For **Display name**, enter the name that you want displayed when you receive a notification.

1. In **Access policy**, choose **Advanced**.

1. In the policy text field, after ** "Statement": [**, enter one of the following statements:

   To allow the AWS Cost Anomaly Detection service to publish to the Amazon SNS topic, use the following statement.

   ```
   {
     "Sid": {{"E.g., AWSAnomalyDetectionSNSPublishingPermissions"}},
     "Effect": "Allow",
     "Principal": {
       "Service": "costalerts.amazonaws.com"
     },
     "Action": "SNS:Publish",
     "Resource": {{"your topic ARN"}}
   }
   ```

   To allow the AWS Cost Anomaly Detection service to publish to the Amazon SNS topic only on behalf of a certain account, use the following statement.

   ```
   {
     "Sid": {{"E.g., AWSAnomalyDetectionSNSPublishingPermissions"}},
     "Effect": "Allow",
     "Principal": {
       "Service": "costalerts.amazonaws.com"
     },
     "Action": "SNS:Publish",
     "Resource": {{"your topic ARN"}},
     "Condition": {
           "StringEquals": {
             "aws:SourceAccount": [
               {{"account-ID"}}
             ]
           }
     }
   }
   ```
**Note**  
In this topic policy, you enter the subscription’s account ID as the value for the `aws:SourceAccount` condition. This condition has AWS Cost Anomaly Detection interact with the Amazon SNS topic only when performing operations for the account that owns the subscription.  
You can restrict AWS Cost Anomaly Detection to interact with the topic only when performing operations on behalf of a specific subscription. To do this, use the `aws:SourceArn` condition in the topic policy.  
For more information about these conditions, see [`aws:SourceAccount`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount) and [`aws:SourceArn`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn) in the *IAM User Guide*.

1. In the topic policy statement that you select, replace the following values:
   + Replace (for example, {{AWSAnomalyDetectionSNSPublishingPermissions}}) with a string. The `Sid` must be unique within the policy.
   + Replace {{your topic ARN}} with the Amazon SNS topic Amazon Resource Name (ARN).
   + If you're using the statement with the `aws:SourceAccount` condition, replace {{account-ID}} with the account ID that owns the subscription. If the Amazon SNS topic has multiple subscriptions from different accounts, add multiple account IDs to the `aws:SourceAccount` condition.

1. Choose **Create topic**.

   Your topic now appears in the list of topics on the **Topics** page.

## Checking or resending notification confirmation email messages
<a name="ad-confirm-subscription"></a>

When you create an anomaly detection monitor with notifications, you also create Amazon SNS notifications. For notifications to be sent, you must accept the subscription to the Amazon SNS notification topic.

To confirm that your notification subscriptions are accepted or to resend a subscription confirmation email, use the Amazon SNS console.

**To check your notification status or to resend a notification confirmation email message**

1. Sign in to the AWS Management Console and open the Amazon SNS console at [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home).

1. In the navigation pane, choose **Subscriptions**.

1. Check the status of your notification. Under **Status**, `PendingConfirmation` appears if a subscription isn't accepted and confirmed.

1. (Optional) To resend a confirmation request, select the subscription with a pending confirmation and choose **Request confirmation**. Amazon SNS sends a confirmation request to the endpoints that are subscribed to the notification.

   When each owner of an endpoint receives the email, they must choose the **Confirm subscription** link to activate the notification.

## Protecting your Amazon SNS anomaly detection alerts data with SSE and AWS KMS
<a name="protect-sns-sse"></a>

You can use server-side encryption (SSE) to transfer sensitive data in encrypted topics. SSE protects Amazon SNS messages by using keys managed in AWS Key Management Service (AWS KMS).

To manage SSE using AWS Management Console or the AWS SDK, see [Enabling Server-Side Encryption (SSE) for an Amazon SNS Topic](https://docs.aws.amazon.com/sns/latest/dg/sns-tutorial-enable-encryption-for-topic.html) in the *Amazon Simple Notification Service Getting Started Guide*.

To create encrypted topics using AWS CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

SSE encrypts messages as soon as Amazon SNS receives them. The messages are stored encrypted and are decrypted using Amazon SNS only when they're sent.

### Configuring AWS KMS permissions
<a name="configure-kms-perm"></a>

You must configure your AWS KMS key policies before you can use server-side encryption (SSE). You can use this configuration to encrypt topics, in addition to encrypting and decrypting messages. For information about AWS KMS permissions, see [AWS KMS API Permissions: Actions and Resources Reference](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) in the *AWS Key Management Service Developer Guide*.

You can also use IAM policies to manage AWS KMS key permissions. For more information, see [Using IAM Policies with AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies.html).

**Note**  
You can configure global permissions to send and receive message from Amazon SNS. However, AWS KMS requires that you name the full Amazon Resource Name (ARN) of the AWS KMS keys (KMS keys) in the specific AWS Regions. You can find this in the **Resource** section of an IAM policy.  
Ensure that the key policies of the KMS key allow the necessary permissions. To do this, name the principals that produce and consume encrypted messages in Amazon SNS as users in the KMS key policy.<a name="enable-compatiblility"></a>

**To enable compatibility between AWS Cost Anomaly Detection and encrypted Amazon SNS topics**

1. [Create a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-keys-console).

1. Add one of the following policies as the KMS key policy:

   To grant the AWS Cost Anomaly Detection service access to the KMS key, use the following statement.

------
#### [ JSON ]

****  

   ```
   {
       "Version": "{{2012-10-17}}",
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
               "Resource": "{{*}}"
           }
       ]
   }
   ```

------

   To grant the AWS Cost Anomaly Detection service access to the KMS key only when performing operations on behalf of a certain account, use the following statement.

------
#### [ JSON ]

****  

   ```
   {
       "Version": "{{2012-10-17}}",
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
               "Resource": "{{*}}",
               "Condition": {
                   "StringEquals": {
                       "aws:SourceAccount": [
                           "{{account-ID}}"
                       ]
                   }
               }
           }
       ]
   }
   ```

------
**Note**  
In this KMS key policy, you enter the subscription’s account ID as the value for the `aws:SourceAccount` condition. This condition has AWS Cost Anomaly Detection interact with the KMS key only when performing operations for the account that owns the subscription.  
To have AWS Cost Anomaly Detection interact with the KMS key only when performing operations on behalf of a specific subscription, use the `aws:SourceArn` condition in the KMS key policy.  
For more information about these conditions, see [`aws:SourceAccount`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount) and [`aws:SourceArn`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn) in the *IAM User Guide*.

1. If you're using the KMS key policy with the `aws:SourceAccount` condition, replace {{account-ID}} with the account ID that owns the subscription. If the Amazon SNS topic has multiple subscriptions from different accounts, add multiple account IDs to the `aws:SourceAccount` condition.

1. [Enable SSE for your Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-tutorial-enable-encryption-for-topic.html).
**Note**  
Make sure that you're using the same KMS key that grants AWS Cost Anomaly Detection the permissions to publish to encrypted Amazon SNS topics.

1. Choose **Save Changes**.