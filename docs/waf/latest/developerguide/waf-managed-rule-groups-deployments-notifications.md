**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Notifications for AWS Managed Rules rule groups deployments

This section explains how Amazon SNS notifications work with AWS Managed Rules rule groups.

The versioned AWS Managed Rules rule groups all provide SNS update notifications for deployments
and they all use the same SNS topic Amazon Resource Name (ARN).
The only rule groups that aren't versioned are the IP reputation rule groups.

For deployments that affect your protections, such as changes to the default version, AWS
provides SNS notifications to inform you of planned deployments and to let you
know when a deployment is starting. For deployments that don't affect your
protections, such as release candidate and static version deployments, AWS
might notify you after the deployment has started or even after it's completed.
At the completion of the deployment of a new static version, AWS updates this
guide, in the changelog at [AWS Managed Rules changelog](aws-managed-rule-groups-changelog.md "aws-managed-rule-groups-changelog.md") and in the document
history page at [Document history](doc-history.md "doc-history.md").

To receive all updates that AWS provides for the AWS Managed Rules rule groups, subscribe to the RSS feed from
any HTML page of this guide, and subscribe to the SNS topic for the AWS Managed Rules rule groups.
For information about subscribing to the SNS notifications, see [Getting notified of new
versions and updates to a managed rule group](waf-using-managed-rule-groups-sns-topic.md "waf-using-managed-rule-groups-sns-topic.md").

###### Contents of the SNS notifications

The fields in the Amazon SNS notifications always include the Subject,
Message, and MessageAttributes. Additional fields
depend on the type of message and which managed rule group the notification is
for. The following shows an example notification listing for `AWSManagedRulesCommonRuleSet`.

```
{
    "Type": "Notification",
    "MessageId": "4286b830-a463-5e61-bd15-e1ae72303868",
    "TopicArn": "arn:aws:sns:us-west-2:123456789012:MyTopic",
    "Subject": "New version available for rule group AWSManagedRulesCommonRuleSet",
    "Message": "Welcome to AWSManagedRulesCommonRuleSet version 1.5! We've updated the regex specification in this version to improve protection coverage, adding protections against insecure deserialization. For details about this change, see http://updatedPublicDocs.html. Look for more exciting updates in the future! ",
    "Timestamp": "2021-08-24T11:12:19.810Z",
    "SignatureVersion": "1",
    "Signature": "EXAMPLEHXgJm...",
    "SigningCertURL": "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-f3ecfb7224c7233fe7bb5f59f96de52f.pem",
    "SubscribeURL": "https://sns.us-west-2.amazonaws.com/?Action=ConfirmSubscription&TopicArn=arn:aws:sns:us-west-2:123456789012:MyTopic&Token=2336412f37...",
    "MessageAttributes": {
        "major_version": {
            "Type": "String",
            "Value": "v1"
        },
        "managed_rule_group": {
            "Type": "String",
            "Value": "AWSManagedRulesCommonRuleSet"
        }
    }
}
```
