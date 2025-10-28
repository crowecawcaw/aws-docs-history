# Managing Amazon SNS encryption keys and costs

The following sections provide information about working with keys managed in AWS Key Management Service
(AWS KMS).

###### Note

Amazon SNS only supports symmetric encryption KMS keys. You cannot use any other type of
KMS key to encrypt your service resources. For help determining whether a KMS key is a
symmetric encryption key, see [Identifying asymmetric
KMS keys](../../../kms/latest/developerguide/find-symm-asymm.md "../../../kms/latest/developerguide/find-symm-asymm.md").

## Estimating AWS KMS costs

To predict costs and better understand your AWS bill, you might want to
know how often Amazon SNS uses your AWS KMS key.

###### Note

Although the following formula can give you a very good idea of expected costs, actual
costs might be higher because of the distributed nature of Amazon SNS.

To calculate the number of API requests (`R`) _per topic_,
use the following formula:

```
R = B / D * (2 * P)
```

`B` is the billing period (in seconds).

`D` is the data key reuse period (in seconds—Amazon SNS reuses a data key for
up to 5 minutes).

`P` is the number of publishing [principals](../../../IAM/latest/UserGuide/reference_policies_elements.md#Principal "../../../IAM/latest/UserGuide/reference_policies_elements.md#Principal") that send
to the Amazon SNS topic.

The following are example calculations. For exact pricing information, see [AWS Key Management Service Pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

### Example 1: Calculating the number of AWS KMS API

calls for 1 publisher and 1 topic

This example assumes the following:

- The billing period is January 1-31 (2,678,400 seconds).
- The data key reuse period is 5 minutes (300 seconds).
- There is 1 topic.
- There is 1 publishing principal.

```
2,678,400 / 300 * (2 * 1) = 17,856
```

### Example 2: Calculating the number of

AWS KMS API calls for multiple publishers and 2 topics

This example assumes the following:

- The billing period is February 1-28 (2,419,200 seconds).
- The data key reuse period is 5 minutes (300 seconds).
- There are 2 topics.
- The first topic has 3 publishing principals.
- The second topic has 5 publishing principals.

```
(2,419,200 / 300 * (2 * 3)) + (2,419,200 / 300 * (2 * 5)) = 129,024
```

## Configuring AWS KMS permissions

Before you can use SSE, you must configure AWS KMS key policies to allow encryption of
topics and encryption and decryption of messages. For examples and more information about
AWS KMS permissions, see [AWS KMS API
Permissions: Actions and Resources Reference](../../../kms/latest/developerguide/kms-api-permissions-reference.md "../../../kms/latest/developerguide/kms-api-permissions-reference.md") in the
_AWS Key Management Service Developer Guide_. For details on how to set up an Amazon SNS topic with
server-side encryption, see [Additional information](sns-enable-encryption-for-topic.md#set-up-topic-with-sse "sns-enable-encryption-for-topic.md#set-up-topic-with-sse").

###### Note

You can also manage permissions for symmetric encryption KMS keys using IAM
policies. For more information, see [Using IAM
Policies with AWS KMS](../../../kms/latest/developerguide/iam-policies.md "../../../kms/latest/developerguide/iam-policies.md").

While you can configure global permissions to send to and receive from Amazon SNS, AWS KMS
requires explicitly naming the full ARN of KMSs in specific regions in the
`Resource` section of an IAM policy.

You must also ensure that the key policies of the AWS KMS key allow the necessary
permissions. To do this, name the principals that produce and consume encrypted messages in
Amazon SNS as users in the KMS key policy.

Alternatively, you can specify the required AWS KMS actions and KMS ARN in an IAM policy
assigned to the principals that publish and subscribe to receive encrypted messages in Amazon SNS.
For more information, see [Managing Access to AWS KMS](../../../kms/latest/developerguide/control-access-overview.md#managing-access "../../../kms/latest/developerguide/control-access-overview.md#managing-access") in the _AWS Key Management Service Developer Guide_.

If selecting a customer-managed key for your Amazon SNS topic and you are using aliases to
control access to KMS keys using IAM policies or KMS key policies with the condition key
`kms:ResourceAliases`, ensure that the customer-managed key that is selected also
has an alias associated. For more information on using alias to control access to KMS keys,
see [Using
aliases to control access to KMS keys](../../../kms/latest/developerguide/alias-authorization.md "../../../kms/latest/developerguide/alias-authorization.md") in the _AWS Key Management Service
Developer Guide_.

### Allow a user to send messages to a topic with

SSE

The publisher must have the `kms:GenerateDataKey*` and
`kms:Decrypt` permissions for the AWS KMS key.

```
{
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "kms:GenerateDataKey*",
      "kms:Decrypt"
    ],
    "Resource": "arn:aws:kms:us-east-2:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"
  }, {
    "Effect": "Allow",
    "Action": [
      "sns:Publish"
    ],
    "Resource": "arn:aws:sns:*:123456789012:MyTopic"
  }]
}
```

### Enable compatibility between event sources

from AWS services and encrypted topics

Several AWS services publish events to Amazon SNS topics. To allow these event
sources to work with encrypted topics, you must perform the following steps.

1. Use a customer managed key. For more information, see [Creating Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
   _AWS Key Management Service Developer Guide_.
2. To allow the AWS service to have the
   `kms:GenerateDataKey*` and `kms:Decrypt` permissions, add the
   following statement to the KMS policy.

```
{
  "Statement": [{
    "Effect": "Allow",
    "Principal": {
      "Service": "`service`.amazonaws.com"
    },
    "Action": [
      "kms:GenerateDataKey*",
      "kms:Decrypt"
    ],
    "Resource": "*"
  }]
}
```

| Event source                                                                                                                                                                                                 | Service principal                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Amazon CloudWatch](../../../AmazonCloudWatch/latest/DeveloperGuide.md "../../../AmazonCloudWatch/latest/DeveloperGuide.md")                                                                                 | `cloudwatch.amazonaws.com`                                                                                                           |
| [Amazon CloudWatch Events](../../../AmazonCloudWatch/latest/events.md "../../../AmazonCloudWatch/latest/events.md")                                                                                          | `events.amazonaws.com`                                                                                                               |
| [AWS CodeCommit](../../../codecommit/latest/userguide/how-to-notify-sns.md "../../../codecommit/latest/userguide/how-to-notify-sns.md")                                                                      | `codecommit.amazonaws.com`                                                                                                           |
| [AWS Database Migration Service](../../../dms/latest/userguide/CHAP_Events.md "../../../dms/latest/userguide/CHAP_Events.md")                                                                                | `dms.amazonaws.com`                                                                                                                  |
| [AWS Directory Service](../../../directoryservice/latest/admin-guide/ms_ad_enable_notifications.md "../../../directoryservice/latest/admin-guide/ms_ad_enable_notifications.md")                             | `ds.amazonaws.com`                                                                                                                   |
| [Amazon DynamoDB](../../../amazondynamodb/latest/developerguide/DAX.md#DAX.cluster-management.custom-settings "../../../amazondynamodb/latest/developerguide/DAX.md#DAX.cluster-management.custom-settings") | `dynamodb.amazonaws.com`                                                                                                             |
| [Amazon Inspector](../../../inspector/latest/userguide/inspector_introduction.md "../../../inspector/latest/userguide/inspector_introduction.md")                                                            | `inspector.amazonaws.com`                                                                                                            |
| [Amazon Redshift](../../../redshift/latest/mgmt/working-with-event-notifications.md "../../../redshift/latest/mgmt/working-with-event-notifications.md")                                                     | `redshift.amazonaws.com`                                                                                                             |
| [Amazon RDS](../../../AmazonRDS/latest/DeveloperGuide/USER_Events.md "../../../AmazonRDS/latest/DeveloperGuide/USER_Events.md")                                                                              | `events.rds.amazonaws.com`                                                                                                           |
| [Amazon Glacier](../../../amazonglacier/latest/dev/configuring-notifications.md "../../../amazonglacier/latest/dev/configuring-notifications.md")                                                            | `glacier.amazonaws.com`                                                                                                              |
| [Amazon Simple Email Service](../../../ses/latest/DeveloperGuide/configure-sns-notifications.md "../../../ses/latest/DeveloperGuide/configure-sns-notifications.md")                                         | `ses.amazonaws.com`                                                                                                                  |
| [Amazon Simple Storage Service](../../../AmazonS3/latest/userguide/ways-to-add-notification-config-to-bucket.md "../../../AmazonS3/latest/userguide/ways-to-add-notification-config-to-bucket.md")           | `s3.amazonaws.com`                                                                                                                   |
| [AWS Snowball Edge](../../../snowball/latest/api-reference/API_Notification.md "../../../snowball/latest/api-reference/API_Notification.md")                                                                 | `importexport.amazonaws.com`                                                                                                         |
| [AWS Systems Manager Incident Manager](../../../incident-manager/latest/userguide/chat.md "../../../incident-manager/latest/userguide/chat.md")                                                              | AWS Systems Manager Incident Manager consists of two service principles: `ssm-incidents.amazonaws.com`; `ssm-contacts.amazonaws.com` | ###### Note Some Amazon SNS event sources require you to provide an IAM role (rather than the service principal) in the AWS KMS key policy: <br>• [Amazon EC2 Auto Scaling](../../../autoscaling/ec2/userguide/ASGettingNotifications.md "../../../autoscaling/ec2/userguide/ASGettingNotifications.md") <br>• [Amazon Elastic Transcoder](../../../elastictranscoder/latest/developerguide/notifications.md "../../../elastictranscoder/latest/developerguide/notifications.md") <br>• [AWS CodePipeline](../../../codepipeline/latest/userguide/approvals.md#approvals-configuration-options "../../../codepipeline/latest/userguide/approvals.md#approvals-configuration-options") <br>• [AWS Config](../../../config/latest/developerguide/notifications-for-AWS-Config.md "../../../config/latest/developerguide/notifications-for-AWS-Config.md") <br>• [AWS Elastic Beanstalk](../../../elasticbeanstalk/latest/dg/using-features.managing.md "../../../elasticbeanstalk/latest/dg/using-features.managing.md") <br>• [AWS IoT](../../../iot/latest/developerguide/iot-sns-rule.md "../../../iot/latest/developerguide/iot-sns-rule.md") <br>• [EC2 Image Builder](../../../imagebuilder/latest/userguide/ibhow-integrations.md#integ-sns-encrypted "../../../imagebuilder/latest/userguide/ibhow-integrations.md#integ-sns-encrypted") 3. Add the `aws:SourceAccount` and `aws:SourceArn` condition keys to the KMS resource policy to further protect the KMS key from [confused deputy](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") attacks. Refer to service specific documentation list (above) for exact details in each case. ###### Important Adding the `aws:SourceAccount`, `aws:SourceArn`, and `aws:SourceOrgID` to a AWS KMS policy is not supported for EventBridge-to-encrypted topics. ``{ "Effect": "Allow", "Principal": { "Service": "service.amazonaws.com" }, "Action": [ "kms:GenerateDataKey*", "kms:Decrypt" ], "Resource": "*", "Condition": { "StringEquals": { "aws:SourceAccount": "`customer-account-id`" }, "ArnLike": { "aws:SourceArn": "arn:aws:service:region:`customer-account-id`:resource-type:`customer-resource-id`" } } }`` 4. [Enable SSE for your topic](sns-enable-encryption-for-topic.md "sns-enable-encryption-for-topic.md") using your KMS. 5. Provide the ARN of the encrypted topic to the event source. ## AWS KMS errors When you work with Amazon SNS and AWS KMS, you might encounter errors. The following list describes the errors and possible troubleshooting solutions. **KMSAccessDeniedException** The ciphertext references a key that doesn't exist or that you don't have access to. HTTP Status Code: 400 **KMSDisabledException** The request was rejected because the specified KMS isn't enabled. HTTP Status Code: 400 **KMSInvalidStateException** The request was rejected because the state of the specified resource isn't valid for this request. For more information, see [Key states of AWS KMS keys](../../../kms/latest/developerguide/key-state.md "../../../kms/latest/developerguide/key-state.md") in the _AWS Key Management Service Developer Guide_. HTTP Status Code: 400 **KMSNotFoundException** The request was rejected because the specified entity or resource can't be found. HTTP Status Code: 400 **KMSOptInRequired** The AWS access key ID needs a subscription for the service. HTTP Status Code: 403 **KMSThrottlingException** The request was denied due to request throttling. For more information about throttling, see [Quotas](../../../kms/latest/developerguide/limits.md#requests-per-second "../../../kms/latest/developerguide/limits.md#requests-per-second") in the _AWS Key Management Service Developer Guide_. HTTP Status Code: 400 |
