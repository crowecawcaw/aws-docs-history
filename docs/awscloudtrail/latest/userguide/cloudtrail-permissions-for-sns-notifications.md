# Amazon SNS topic policy for CloudTrail

To send notifications to an SNS topic, CloudTrail must have the required permissions. CloudTrail
automatically attaches the required permissions to the topic when you create an Amazon SNS topic
as part of creating or updating a trail in the CloudTrail console.

###### Important

As a security best practice, to restrict access to your SNS topic, we strongly
recommend that after you create or update a trail to send SNS notifications, you
manually edit the IAM policy that is attached to the SNS topic to add condition keys.
For more information, see [Security best practice for SNS topic policy](#cloudtrail-sns-notifications-policy-security "#cloudtrail-sns-notifications-policy-security")
in this topic.

CloudTrail adds the following statement to the policy for you with the following fields:

- The allowed SIDs.
- The service principal name for CloudTrail.
- The SNS topic, including Region, account ID, and topic name.
  The following policy allows CloudTrail to send notifications about log file delivery from
  supported Regions. For more information, see [CloudTrail supported Regions](cloudtrail-supported-regions.md "cloudtrail-supported-regions.md"). This is the default policy that is
  attached to a new or existing SNS topic policy when you create or update a trail, and choose
  to enable SNS notifications.

**SNS
topic policy**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AWSCloudTrailSNSPolicy20131101",
 "Effect": "Allow",
 "Principal": {
 "Service": "cloudtrail.amazonaws.com"
 },
 "Action": "SNS:Publish",
 "Resource": "arn:aws:sns:`us-east-1`:`111111111111`:`SNSTopicName`"
 }
 ]
}`

```

To use an AWS KMS-encrypted Amazon SNS topic to send notifications, you must also enable
compatibility between the event source (CloudTrail) and the encrypted topic by adding the
following statement to the policy of the AWS KMS key.

**KMS key policy**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "cloudtrail.amazonaws.com"
 },
 "Action": [
 "kms:GenerateDataKey*",
 "kms:Decrypt"
 ],
 "Resource": "*"
 }
 ]
}`

```

For more information, see [Enable Compatibility between Event Sources from AWS Services and Encrypted Topics](../../../sns/latest/dg/sns-key-management.md#compatibility-with-aws-services "../../../sns/latest/dg/sns-key-management.md#compatibility-with-aws-services").

###### Contents

- [Security best practice for SNS topic policy](cloudtrail-permissions-for-sns-notifications.md#cloudtrail-sns-notifications-policy-security "cloudtrail-permissions-for-sns-notifications.md#cloudtrail-sns-notifications-policy-security")
- [Specifying an existing topic for sending notifications](cloudtrail-permissions-for-sns-notifications.md#specifying-an-existing-topic-for-sns-notifications "cloudtrail-permissions-for-sns-notifications.md#specifying-an-existing-topic-for-sns-notifications")
- [Troubleshooting the SNS topic policy](cloudtrail-permissions-for-sns-notifications.md#troubleshooting-sns-topic-policy "cloudtrail-permissions-for-sns-notifications.md#troubleshooting-sns-topic-policy")
  - [CloudTrail is not sending notifications for a Region](cloudtrail-permissions-for-sns-notifications.md#sns-topic-policy-for-multiple-regions "cloudtrail-permissions-for-sns-notifications.md#sns-topic-policy-for-multiple-regions")
  - [CloudTrail is not sending notifications for a member account in an organization](cloudtrail-permissions-for-sns-notifications.md#sns-topic-policy-authorization-failure "cloudtrail-permissions-for-sns-notifications.md#sns-topic-policy-authorization-failure")

- [Additional resources](cloudtrail-permissions-for-sns-notifications.md#cloudtrail-notifications-more-info-5 "cloudtrail-permissions-for-sns-notifications.md#cloudtrail-notifications-more-info-5")

## Security best practice for SNS topic policy

By default, the IAM policy statement that CloudTrail attaches to your Amazon SNS topic allows
the CloudTrail service principal to publish to an SNS topic, identified by an ARN. To help
prevent an attacker from gaining access to your SNS topic, and sending notifications on
behalf of CloudTrail to topic recipients, manually edit your CloudTrail SNS topic policy to add an
`aws:SourceArn` condition key to the policy statement attached by CloudTrail.
The value of this key is the ARN of the trail, or an array of trail ARNs that are using
the SNS topic. Because it includes both the specific trail ID and the ID of the account
that owns the trail, it restricts SNS topic access to only those accounts that have
permission to manage the trail. Before you add condition keys to your SNS topic policy,
get the SNS topic name from your trail's settings in the CloudTrail console.

The `aws:SourceAccount` condition key is also supported, but is not
recommended.

###### To add the `aws:SourceArn` condition key to your SNS topic

policy

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation pane, choose **Topics**.
3. Choose the SNS topic that is shown in your trail settings, and then choose
   **Edit**.
4. Expand **Access policy**.
5. In the **Access policy** JSON editor, look for a block that
   resembles the following example.

```
    {
      "Sid": "AWSCloudTrailSNSPolicy20150319",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudtrail.amazonaws.com"
      },
      "Action": "SNS:Publish",
      "Resource": "arn:aws:sns:us-west-2:111122223333:aws-cloudtrail-logs-111122223333-61bbe496"
    }
```

6. Add a new block for a condition, `aws:SourceArn`, as shown in the
   following example. The value of `aws:SourceArn` is the ARN of the
   trail about which you are sending notifications to SNS.

```
    {
      "Sid": "AWSCloudTrailSNSPolicy20150319",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudtrail.amazonaws.com"
      },
      "Action": "SNS:Publish",
      "Resource": "arn:aws:sns:us-west-2:111122223333:aws-cloudtrail-logs-111122223333-61bbe496",
      "Condition": {
        "StringEquals": {
          "aws:SourceArn": "arn:aws:cloudtrail:us-west-2:123456789012:trail/Trail3"
        }
      }
    }
```

7. When you are finished editing the SNS topic policy, choose **Save
   changes**.

###### To add the `aws:SourceAccount` condition key to your SNS topic

policy

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation pane, choose **Topics**.
3. Choose the SNS topic that is shown in your trail settings, and then choose
   **Edit**.
4. Expand **Access policy**.
5. In the **Access policy** JSON editor, look for a block that
   resembles the following example.

```
    {
      "Sid": "AWSCloudTrailSNSPolicy20150319",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudtrail.amazonaws.com"
      },
      "Action": "SNS:Publish",
      "Resource": "arn:aws:sns:us-west-2:111122223333:aws-cloudtrail-logs-111122223333-61bbe496"
    }
```

6. Add a new block for a condition, `aws:SourceAccount`, as shown in
   the following example. The value of `aws:SourceAccount` is the ID of
   the account that owns the CloudTrail trail. This example restricts access to the SNS
   topic to only those users who can sign in to the AWS account
7.

```
    {
      "Sid": "AWSCloudTrailSNSPolicy20150319",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudtrail.amazonaws.com"
      },
      "Action": "SNS:Publish",
      "Resource": "arn:aws:sns:us-west-2:111122223333:aws-cloudtrail-logs-111122223333-61bbe496",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "123456789012"
        }
      }
    }
```

7. When you are finished editing the SNS topic policy, choose **Save
   changes**.

## Specifying an existing topic for sending notifications

You can manually add the permissions for an Amazon SNS topic to your topic policy in the
Amazon SNS console and then specify the topic in the CloudTrail console.

###### To manually update an SNS topic policy

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. Choose **Topics** and then choose the topic.
3. Choose **Edit** and then scroll down to **Access policy**.
4. Add the statement from [SNS topic policy](#sns-topic-policy "#sns-topic-policy") with the appropriate values for the Region,
   account ID, and topic name.
5. If your topic is an encrypted topic, you must allow CloudTrail to have
   `kms:GenerateDataKey*` and the `kms:Decrypt`
   permissions. For more information, see [Encrypted SNS topic KMS key policy](#kms-key-policy "#kms-key-policy").
6. Choose **Save changes**.
7. Return to the CloudTrail console and specify the topic for the trail.

## Troubleshooting the SNS topic policy

The following sections describe how to troubleshoot the SNS topic policy.

###### Scenarios:

- [CloudTrail is not sending notifications for a Region](#sns-topic-policy-for-multiple-regions "#sns-topic-policy-for-multiple-regions")
- [CloudTrail is not sending notifications for a member account in an organization](#sns-topic-policy-authorization-failure "#sns-topic-policy-authorization-failure")

### CloudTrail is not sending notifications for a Region

When you create a new topic as part of creating or updating a trail, CloudTrail attaches
the required permissions to your topic. The topic policy uses the service principal
name, `"cloudtrail.amazonaws.com"`, which allows CloudTrail to send
notifications for all Regions.

If CloudTrail is not sending notifications for a Region, it's possible that your topic
has an older policy that specifies CloudTrail account IDs for each Region. This type of policy
gives CloudTrail permission to send notifications only for the Regions specified.

As a best practice, update the policy to use a permission with the CloudTrail service
principal. To do this, replace the account ID ARNs with the service principal name:
`"cloudtrail.amazonaws.com"`.

The following example policy gives CloudTrail permission to send notifications for current and new Regions:

###### Example topic policy with service principal name

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "AWSCloudTrailSNSPolicy20131101",
 "Effect": "Allow",
 "Principal": {"Service": "cloudtrail.amazonaws.com"},
 "Action": "SNS:Publish",
 "Resource": "arn:aws:sns:us-west-2:123456789012:myTopic"
 }]
}`

```

Verify that the policy has the correct values:

- In the `Resource` field, specify the account number of the
  topic owner. For topics that you create, specify your account number.
- Specify the appropriate values for the Region and SNS topic name.

### CloudTrail is not sending notifications for a member account in an organization

When a member account with an AWS Organizations organization trail is not sending Amazon SNS notifications,
there could be an issue with the configuration of the SNS topic policy. CloudTrail creates organization trails
in member accounts even if a resource validation fails, for example, the organization trail's SNS topic
does not include all member account IDs. If the SNS topic policy is incorrect, an authorization failure occurs.

To check whether a trail's SNS topic policy has an authorization failure:

- From the CloudTrail console, check the trail's details page. If there's an authorization failure, the details page includes a warning
  `SNS authorization failed` and indicates to fix the SNS topic
  policy.
- From the AWS CLI, run the [get-trail-status](../../../cli/latest/reference/cloudtrail/get-trail-status.md "../../../cli/latest/reference/cloudtrail/get-trail-status.md") command. If there's an authorization failure,
  the command output includes the `LastNotificationError` field with a value of `AuthorizationError`.

## Additional resources

For more information about SNS topics and subscribing to them, see the
[Amazon Simple Notification Service Developer Guide](../../../sns/latest/dg.md "../../../sns/latest/dg.md").
