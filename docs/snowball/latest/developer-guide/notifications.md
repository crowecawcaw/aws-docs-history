

AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/). 

# Notifications for Snowball Edge
<a name="notifications"></a>

## How Snow uses Amazon SNS
<a name="how-snow-uses-sns"></a>

The Snow service is designed to take advantage of the robust notifications delivered by Amazon Simple Notification Service (Amazon SNS). While creating a job to order a Snow device, you can provide email addresses to receive notifications for your job status changes. When you do this, you choose an existing SNS topic or create a new one. If the SNS topic is encrypted, you need to enable customer-managed KMS encryption for the topic and set up customer-managed KMS key policy. See [Choose preferences for notifications about the Snowball Edge job](create-job-common.md#setup-notifications).

After you create your job, every email address that you specified to get Amazon SNS notifications receives an email message from AWS notifications asking for confirmation to the topic subscription. A user of the email account must confirm the subscription by choosing **Confirm subscription**. The Amazon SNS notification emails are tailored for each job status, and include a link to the [AWS Snow Family Management Console](https://console.aws.amazon.com/snowfamily/home).

You can also configure Amazon SNS to send text messages for status change notifications from the Amazon SNS console. For more information, see [Mobile text messaging (SMS)](https://docs.aws.amazon.com/sns/latest/dg/SMSMessages.html) in the *Amazon Simple Notification Service Developer Guide*.

## Encrypting SNS topics for AWS Snow job status changes
<a name="encrypt-sns-notifications"></a>

Enable customer-managed KMS encryption for the SNS topic for Snow job status change notifications. SNS topics encrypted with AWS-managed encryption cannot receive Snow job status changes because the Snow import IAM role does not have access to the AWS-managed KMS key to perform `Decrypt` and `GenerateDataKey` actions. Additionally, policies of AWS-managed KMS keys cannot be edited.

**To enable server-side encryption for an SNS topic using the Amazon SNS management console**

1. Sign in to the AWS Management Console and open the Amazon SNS console at [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home).

1. In the navigation pane, choose **Topics**.

1. In the Topics page, choose the topic used for job status change notifications, then choose **Edit**.

1. Expand the **Encryption** section and do the following:

   1. Choose **Enable encryption**.

   1. Specify the AWS KMS key. See 

   1. For each KMS type, the description, account, and KMS ARN are displayed.

1. To use a custom key from your AWS account, choose the **AWS KMS key** field and then choose the custom KMS kms from the list. For instructions on creating custom KMS, see [Creating keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the AWS Key Management Service Developer Guide.

   To use a custom KMS ARN from your AWS account or from another AWS account, enter the KMS key ARN in the **AWS KMS key** field.

1. Choose **Save changes**. Server side encryption is enabled for your topic and the topic page is displayed.

## Setting up a customer-managed KMS key policy for AWS Snow
<a name="update-customer-kms-policy"></a>

After enabling encryption for SNS topics that will receive notifications for Snow job status changes, update the KMS policy for the SNS topic encryption and allow the Snow service principal `"importexport.amazonaws.com"` for `"kms:Decrypt"` and `"kms:GenerateDataKey*"` actions.

**To allow the import export service role in the KMS key policy**

1. Sign in to the AWS Management Console and open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms).

1. To change the AWS Region, use the Region selector in the upper-right corner of the page.

1. At the top-right corner of the console, change the AWS Region of the console to the same region as the Snow device was ordered from.

1. In the navigation pane, choose **Customer managed keys**.

1. IN the list of KMS keys, choose the alias or key ID of the KMS key to update.

1. Choose the **Key policy** tab, in the key policy statements, you can see the principals that have been given access to the KMS key by the key policy, and you can see the actions they can perform.

1. For the Snow service principal `"importexport.amazonaws.com"`, add the following policy statement for `"kms:Decrypt"` and `"kms:GenerateDataKey*"` actions:

   ```
     {
   
       "Effect": "Allow",
       "Principal": {
       "Service": "service.amazonaws.com"
     },
     "Action": [
     "kms:Decrypt",
     "kms:GenerateDataKey"
       ],
       "Resource": "*",
       "Condition": {
       "ArnLike": {
       "aws:SourceArn": "arn:aws:service:region:customer-account-id:resource-type/customer-resource-id"
     },
     "StringEquals": {
     "kms:EncryptionContext:aws:sns:topicArn": "arn:aws:sns:your_region:customer-account-id:your_sns_topic_name"
     }
     }
     }
   ```

1. Choose **Save Changes** to apply the changes and exit the policy editor.

## Amazon SNS notification examples for AWS Snow
<a name="job-status-notification-examples"></a>

Amazon SNS notifications produce the following email messages when your job status changes. These messages are examples of the `Email-JSON` SNS topic protocol.


| Job status | SNS notification JSON | 
| --- | --- | 
| Job created |  <pre><br />  {<br />  "Type" : "Notification",<br />  "MessageId" : "dc1e94d9-56c5-5e96-808d-cc7f68faa162",<br />  "TopicArn" : "arn:aws:sns:us-east-2:111122223333:ExampleTopic1",<br />  "Message" : "Your job Job-name (JID8bca334a-6c2f-4cd0-97e2-3f5a4dc9bd6d) has been created. More info - https://console.aws.amazon.com/importexport",<br />  "Timestamp" : "2023-02-23T00:27:58.831Z",<br />  "SignatureVersion" : "1",<br />  "Signature" : "FMG5tlZhJNHLHUXvZgtZzlk24FzVa7oX0T4P03neeXw8ZEXZx6z35j2FOTuNYShn2h0bKNC/zLTnMyIxEzmi2X1shOBWsJHkrW2xkR58ABZF+4uWHEE73yDVR4SyYAikP9jstZzDRm+bcVs8+T0yaLiEGLrIIIL4esi1llhIkgErCuy5btPcWXBdio2fpCRD5x9oR6gmE/rd5O7lX1c1uvnv4r1Lkk4pqP2/iUfxFZva1xLSRvgyfm6D9hNklVyPfy+7TalMD0lzmJuOrExtnSIbZew3foxgx8GT+lbZkLd0ZdtdRJlIyPRP44eyq78sU0Eo/LsDr0Iak4ZDpg8dXg==",<br />  "SigningCertURL" : "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem",<br />  "UnsubscribeURL" : "https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:111122223333:ExampleTopic1:e1039402-24e7-40a3-a0d4-797da162b297"<br />  }                          <br />                    </pre>  | 
| Preparing appliance |  <pre><br />  {<br />  "Type" : "Notification",<br />  "MessageId" : "dc1e94d9-56c5-5e96-808d-cc7f68faa162",<br />  "TopicArn" : "arn:aws:sns:us-east-2:111122223333:ExampleTopic1",<br />  "Message" : "Your job Job-name (JID8bca334a-6c2f-4cd0-97e2-3f5a4dc9bd6d) is being prepared. More info - https://console.aws.amazon.com/importexport",<br />  "Timestamp" : "2023-02-23T00:27:58.831Z",<br />  "SignatureVersion" : "1",<br />  "Signature" : "FMG5tlZhJNHLHUXvZgtZzlk24FzVa7oX0T4P03neeXw8ZEXZx6z35j2FOTuNYShn2h0bKNC/zLTnMyIxEzmi2X1shOBWsJHkrW2xkR58ABZF+4uWHEE73yDVR4SyYAikP9jstZzDRm+bcVs8+T0yaLiEGLrIIIL4esi1llhIkgErCuy5btPcWXBdio2fpCRD5x9oR6gmE/rd5O7lX1c1uvnv4r1Lkk4pqP2/iUfxFZva1xLSRvgyfm6D9hNklVyPfy+7TalMD0lzmJuOrExtnSIbZew3foxgx8GT+lbZkLd0ZdtdRJlIyPRP44eyq78sU0Eo/LsDr0Iak4ZDpg8dXg==",<br />  "SigningCertURL" : "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem",<br />  "UnsubscribeURL" : "https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:111122223333:ExampleTopic1:e1039402-24e7-40a3-a0d4-797da162b297"<br />  }                        <br />                    </pre>  | 
| Exporting |  <pre><br />  {<br />  "Type" : "Notification",<br />  "MessageId" : "dc1e94d9-56c5-5e96-808d-cc7f68faa162",<br />  "TopicArn" : "arn:aws:sns:us-east-2:111122223333:ExampleTopic1",<br />  "Message" : "Your job Job-name (JID8bca334a-6c2f-4cd0-97e2-3f5a4dc9bd6d) is being Exported. More info - https://console.aws.amazon.com/importexport",<br />  "Timestamp" : "2023-02-23T00:27:58.831Z",<br />  "SignatureVersion" : "1",<br />  "Signature" : "FMG5tlZhJNHLHUXvZgtZzlk24FzVa7oX0T4P03neeXw8ZEXZx6z35j2FOTuNYShn2h0bKNC/zLTnMyIxEzmi2X1shOBWsJHkrW2xkR58ABZF+4uWHEE73yDVR4SyYAikP9jstZzDRm+bcVs8+T0yaLiEGLrIIIL4esi1llhIkgErCuy5btPcWXBdio2fpCRD5x9oR6gmE/rd5O7lX1c1uvnv4r1Lkk4pqP2/iUfxFZva1xLSRvgyfm6D9hNklVyPfy+7TalMD0lzmJuOrExtnSIbZew3foxgx8GT+lbZkLd0ZdtdRJlIyPRP44eyq78sU0Eo/LsDr0Iak4ZDpg8dXg==",<br />  "SigningCertURL" : "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem",<br />  "UnsubscribeURL" : "https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:111122223333:ExampleTopic1:e1039402-24e7-40a3-a0d4-797da162b297"<br />  }                        <br />                    </pre>  | 
| In transit to you |  <pre><br />  {<br />  "Type" : "Notification",<br />  "MessageId" : "dc1e94d9-56c5-5e96-808d-cc7f68faa162",<br />  "TopicArn" : "arn:aws:sns:us-east-2:111122223333:ExampleTopic1",<br />  "Message" : "Your job Job-name (JID8bca334a-6c2f-4cd0-97e2-3f5a4dc9bd6d) is in transit to you. More info - https://console.aws.amazon.com/importexport",<br />  "Timestamp" : "2023-02-23T00:27:58.831Z",<br />  "SignatureVersion" : "1",<br />  "Signature" : "FMG5tlZhJNHLHUXvZgtZzlk24FzVa7oX0T4P03neeXw8ZEXZx6z35j2FOTuNYShn2h0bKNC/zLTnMyIxEzmi2X1shOBWsJHkrW2xkR58ABZF+4uWHEE73yDVR4SyYAikP9jstZzDRm+bcVs8+T0yaLiEGLrIIIL4esi1llhIkgErCuy5btPcWXBdio2fpCRD5x9oR6gmE/rd5O7lX1c1uvnv4r1Lkk4pqP2/iUfxFZva1xLSRvgyfm6D9hNklVyPfy+7TalMD0lzmJuOrExtnSIbZew3foxgx8GT+lbZkLd0ZdtdRJlIyPRP44eyq78sU0Eo/LsDr0Iak4ZDpg8dXg==",<br />  "SigningCertURL" : "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem",<br />  "UnsubscribeURL" : "https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:111122223333:ExampleTopic1:e1039402-24e7-40a3-a0d4-797da162b297"<br />  }                        <br />                    </pre>  | 
| Delivered to you |  <pre><br />  {<br />  "Type" : "Notification",<br />  "MessageId" : "dc1e94d9-56c5-5e96-808d-cc7f68faa162",<br />  "TopicArn" : "arn:aws:sns:us-east-2:111122223333:ExampleTopic1",<br />  "Message" : "Your job Job-name (JID8bca334a-6c2f-4cd0-97e2-3f5a4dc9bd6d) was delivered to you. More info - https://console.aws.amazon.com/importexport",<br />  "Timestamp" : "2023-02-23T00:27:58.831Z",<br />  "SignatureVersion" : "1",<br />  "Signature" : "FMG5tlZhJNHLHUXvZgtZzlk24FzVa7oX0T4P03neeXw8ZEXZx6z35j2FOTuNYShn2h0bKNC/zLTnMyIxEzmi2X1shOBWsJHkrW2xkR58ABZF+4uWHEE73yDVR4SyYAikP9jstZzDRm+bcVs8+T0yaLiEGLrIIIL4esi1llhIkgErCuy5btPcWXBdio2fpCRD5x9oR6gmE/rd5O7lX1c1uvnv4r1Lkk4pqP2/iUfxFZva1xLSRvgyfm6D9hNklVyPfy+7TalMD0lzmJuOrExtnSIbZew3foxgx8GT+lbZkLd0ZdtdRJlIyPRP44eyq78sU0Eo/LsDr0Iak4ZDpg8dXg==",<br />  "SigningCertURL" : "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem",<br />  "UnsubscribeURL" : "https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:111122223333:ExampleTopic1:e1039402-24e7-40a3-a0d4-797da162b297"<br />  }                        <br />                    </pre>  | 
| In transit to AWS | <pre><br />  {<br />  "Type" : "Notification",<br />  "MessageId" : "dc1e94d9-56c5-5e96-808d-cc7f68faa162",<br />  "TopicArn" : "arn:aws:sns:us-east-2:111122223333:ExampleTopic1",<br />  "Message" : "Your job Job-name (JID8bca334a-6c2f-4cd0-97e2-3f5a4dc9bd6d) is in transit to AWS. More info - https://console.aws.amazon.com/importexport",<br />  "Timestamp" : "2023-02-23T00:27:58.831Z",<br />  "SignatureVersion" : "1",<br />  "Signature" : "FMG5tlZhJNHLHUXvZgtZzlk24FzVa7oX0T4P03neeXw8ZEXZx6z35j2FOTuNYShn2h0bKNC/zLTnMyIxEzmi2X1shOBWsJHkrW2xkR58ABZF+4uWHEE73yDVR4SyYAikP9jstZzDRm+bcVs8+T0yaLiEGLrIIIL4esi1llhIkgErCuy5btPcWXBdio2fpCRD5x9oR6gmE/rd5O7lX1c1uvnv4r1Lkk4pqP2/iUfxFZva1xLSRvgyfm6D9hNklVyPfy+7TalMD0lzmJuOrExtnSIbZew3foxgx8GT+lbZkLd0ZdtdRJlIyPRP44eyq78sU0Eo/LsDr0Iak4ZDpg8dXg==",<br />  "SigningCertURL" : "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem",<br />  "UnsubscribeURL" : "https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:111122223333:ExampleTopic1:e1039402-24e7-40a3-a0d4-797da162b297"<br />  }                    <br />                </pre> | 
| At sorting facility |  <pre><br />  {<br />  "Type" : "Notification",<br />  "MessageId" : "dc1e94d9-56c5-5e96-808d-cc7f68faa162",<br />  "TopicArn" : "arn:aws:sns:us-east-2:111122223333:ExampleTopic1",<br />  "Message" : "Your job Job-name (JID8bca334a-6c2f-4cd0-97e2-3f5a4dc9bd6d) is at AWS sorting facility. More info - https://console.aws.amazon.com/importexport",<br />  "Timestamp" : "2023-02-23T00:27:58.831Z",<br />  "SignatureVersion" : "1",<br />  "Signature" : "FMG5tlZhJNHLHUXvZgtZzlk24FzVa7oX0T4P03neeXw8ZEXZx6z35j2FOTuNYShn2h0bKNC/zLTnMyIxEzmi2X1shOBWsJHkrW2xkR58ABZF+4uWHEE73yDVR4SyYAikP9jstZzDRm+bcVs8+T0yaLiEGLrIIIL4esi1llhIkgErCuy5btPcWXBdio2fpCRD5x9oR6gmE/rd5O7lX1c1uvnv4r1Lkk4pqP2/iUfxFZva1xLSRvgyfm6D9hNklVyPfy+7TalMD0lzmJuOrExtnSIbZew3foxgx8GT+lbZkLd0ZdtdRJlIyPRP44eyq78sU0Eo/LsDr0Iak4ZDpg8dXg==",<br />  "SigningCertURL" : "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem",<br />  "UnsubscribeURL" : "https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:111122223333:ExampleTopic1:e1039402-24e7-40a3-a0d4-797da162b297"<br />  }                        <br />                    </pre>  | 
| At AWS |  <pre><br />  {<br />  "Type" : "Notification",<br />  "MessageId" : "dc1e94d9-56c5-5e96-808d-cc7f68faa162",<br />  "TopicArn" : "arn:aws:sns:us-east-2:111122223333:ExampleTopic1",<br />  "Message" : "Your job Job-name (JID8bca334a-6c2f-4cd0-97e2-3f5a4dc9bd6d) is at AWS. More info - https://console.aws.amazon.com/importexport",<br />  "Timestamp" : "2023-02-23T00:27:58.831Z",<br />  "SignatureVersion" : "1",<br />  "Signature" : "FMG5tlZhJNHLHUXvZgtZzlk24FzVa7oX0T4P03neeXw8ZEXZx6z35j2FOTuNYShn2h0bKNC/zLTnMyIxEzmi2X1shOBWsJHkrW2xkR58ABZF+4uWHEE73yDVR4SyYAikP9jstZzDRm+bcVs8+T0yaLiEGLrIIIL4esi1llhIkgErCuy5btPcWXBdio2fpCRD5x9oR6gmE/rd5O7lX1c1uvnv4r1Lkk4pqP2/iUfxFZva1xLSRvgyfm6D9hNklVyPfy+7TalMD0lzmJuOrExtnSIbZew3foxgx8GT+lbZkLd0ZdtdRJlIyPRP44eyq78sU0Eo/LsDr0Iak4ZDpg8dXg==",<br />  "SigningCertURL" : "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem",<br />  "UnsubscribeURL" : "https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:111122223333:ExampleTopic1:e1039402-24e7-40a3-a0d4-797da162b297"<br />  }                        <br />                    </pre>  | 
| Importing | <pre><br />  {<br />  "Type" : "Notification",<br />  "MessageId" : "dc1e94d9-56c5-5e96-808d-cc7f68faa162",<br />  "TopicArn" : "arn:aws:sns:us-east-2:111122223333:ExampleTopic1",<br />  "Message" : "Your job Job-name (JID8bca334a-6c2f-4cd0-97e2-3f5a4dc9bd6d) is being imported. More info - https://console.aws.amazon.com/importexport",<br />  "Timestamp" : "2023-02-23T00:27:58.831Z",<br />  "SignatureVersion" : "1",<br />  "Signature" : "FMG5tlZhJNHLHUXvZgtZzlk24FzVa7oX0T4P03neeXw8ZEXZx6z35j2FOTuNYShn2h0bKNC/zLTnMyIxEzmi2X1shOBWsJHkrW2xkR58ABZF+4uWHEE73yDVR4SyYAikP9jstZzDRm+bcVs8+T0yaLiEGLrIIIL4esi1llhIkgErCuy5btPcWXBdio2fpCRD5x9oR6gmE/rd5O7lX1c1uvnv4r1Lkk4pqP2/iUfxFZva1xLSRvgyfm6D9hNklVyPfy+7TalMD0lzmJuOrExtnSIbZew3foxgx8GT+lbZkLd0ZdtdRJlIyPRP44eyq78sU0Eo/LsDr0Iak4ZDpg8dXg==",<br />  "SigningCertURL" : "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem",<br />  "UnsubscribeURL" : "https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:111122223333:ExampleTopic1:e1039402-24e7-40a3-a0d4-797da162b297"<br />  }                      <br />                </pre> | 
| Completed |  <pre><br />  {<br />  "Type" : "Notification",<br />  "MessageId" : "dc1e94d9-56c5-5e96-808d-cc7f68faa162",<br />  "TopicArn" : "arn:aws:sns:us-east-2:111122223333:ExampleTopic1",<br />  "Message" : "Your job Job-name (JID8bca334a-6c2f-4cd0-97e2-3f5a4dc9bd6d) complete.\nThanks for using AWS Snowball Edge.\nCan you take a quick survey on your experience? Survey here: http://bit.ly/1pLQJMY. More info - https://console.aws.amazon.com/importexport",<br />  "Timestamp" : "2023-02-23T00:27:58.831Z",<br />  "SignatureVersion" : "1",<br />  "Signature" : "FMG5tlZhJNHLHUXvZgtZzlk24FzVa7oX0T4P03neeXw8ZEXZx6z35j2FOTuNYShn2h0bKNC/zLTnMyIxEzmi2X1shOBWsJHkrW2xkR58ABZF+4uWHEE73yDVR4SyYAikP9jstZzDRm+bcVs8+T0yaLiEGLrIIIL4esi1llhIkgErCuy5btPcWXBdio2fpCRD5x9oR6gmE/rd5O7lX1c1uvnv4r1Lkk4pqP2/iUfxFZva1xLSRvgyfm6D9hNklVyPfy+7TalMD0lzmJuOrExtnSIbZew3foxgx8GT+lbZkLd0ZdtdRJlIyPRP44eyq78sU0Eo/LsDr0Iak4ZDpg8dXg==",<br />  "SigningCertURL" : "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem",<br />  "UnsubscribeURL" : "https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:111122223333:ExampleTopic1:e1039402-24e7-40a3-a0d4-797da162b297"<br />  }                        <br />                    </pre>  | 
| Cancelled | <pre><br />  {<br />  "Type" : "Notification",<br />  "MessageId" : "dc1e94d9-56c5-5e96-808d-cc7f68faa162",<br />  "TopicArn" : "arn:aws:sns:us-east-2:111122223333:ExampleTopic1",<br />  "Message" : "Your job Job-name (JID8bca334a-6c2f-4cd0-97e2-3f5a4dc9bd6d) was canceled. More info - https://console.aws.amazon.com/importexport",<br />  "Timestamp" : "2023-02-23T00:27:58.831Z",<br />  "SignatureVersion" : "1",<br />  "Signature" : "FMG5tlZhJNHLHUXvZgtZzlk24FzVa7oX0T4P03neeXw8ZEXZx6z35j2FOTuNYShn2h0bKNC/zLTnMyIxEzmi2X1shOBWsJHkrW2xkR58ABZF+4uWHEE73yDVR4SyYAikP9jstZzDRm+bcVs8+T0yaLiEGLrIIIL4esi1llhIkgErCuy5btPcWXBdio2fpCRD5x9oR6gmE/rd5O7lX1c1uvnv4r1Lkk4pqP2/iUfxFZva1xLSRvgyfm6D9hNklVyPfy+7TalMD0lzmJuOrExtnSIbZew3foxgx8GT+lbZkLd0ZdtdRJlIyPRP44eyq78sU0Eo/LsDr0Iak4ZDpg8dXg==",<br />  "SigningCertURL" : "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem",<br />  "UnsubscribeURL" : "https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:111122223333:ExampleTopic1:e1039402-24e7-40a3-a0d4-797da162b297"<br />  }                    <br />                </pre> | 