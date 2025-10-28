# Getting notified of updates to a threat signature rule group in AWS Network Firewall

You can subscribe to Amazon Simple Notification Service (Amazon SNS) notifications for updates to a
managed threat signature rule group, such as updates made
for urgent security updates. AWS updates managed threat signature rule
groups for Network Firewall as often as once a day to once a week.

The AWS threat signature managed rule groups use a single SNS subscription
topic ARN, so you subscribe once for all the rule groups.

###### How to subscribe

To subscribe to notifications for a rule group, create an Amazon SNS
subscription for the rule group's Amazon SNS topic
ARN.

For information about how to subscribe to an Amazon SNS topic, see [Configuring Amazon Simple Notification Service](../../../sns/latest/dg/sns-configuring.md "../../../sns/latest/dg/sns-configuring.md") in the _[Amazon Simple Notification Service Developer Guide](../../../sns/latest/dg.md "../../../sns/latest/dg.md")_.

###### Where to find the Amazon SNS topic ARN for a threat signature managed rule group

The AWS managed rule groups use a single SNS topic ARN, so you can retrieve the topic
ARN from one of the rule groups and subscribe to it to get notifications for
all of the managed rule groups.

- **Console**
  - On
    the
    Network Firewall rule groups page, in the **AWS
    managed rule group** tab, in the
    **Threat signature rule groups**
    section, select a rule group to view the rule
    group's details. The details include the rule
    group's Amazon SNS topic ARN.
  - (Option) After you've added the managed rule group into your firewall policy, choose
    **Edit** on the firewall policy, and then select
    and edit the rule group rule to view the rule group's Amazon SNS topic
    ARN.

- **API** – The [DescribeRuleGroup](../APIReference/API_DescribeRuleGroup.md "../APIReference/API_DescribeRuleGroup.md") response includes `SnsTopic`. The value for `SnsTopic` is the Amazon SNS topic ARN.
- **CLI** – The [describe-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/describe-rule-group.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/describe-rule-group.html") response includes `SnsTopic`. The value for `SnsTopic` is the Amazon SNS topic ARN.

###### The notification format for AWS managed rule group

The Amazon SNS notifications for AWS managed rule groups always contain the fields
`Subject`, `Message`, and
`MessageAttributes`. Other fields are included according to
the type of message and which managed rule group the notification is for.

The following shows an example notification listing for the
`AWS-Managed-Threat-Signatures`.

```
{
  "Type" : "Notification",
  "MessageId" : "82a03348-5419-5945-9a82-699adada25e3",
  "TopicArn" : "arn:aws:sns:us-west-2:696851677263:AWS-Managed-Threat-Signatures",
  "Subject" : "New version available for: StatefulRG2",
  "Message" : "The following Network Firewall managed resource has a new version: arn:aws:network-firewall:us-west-2:aws-managed:stateful-rulegroup/StatefulRG2. To view the new version, either call DescribeRuleGroup or view the resource in the Network Firewall console.",
  "Timestamp" : "2022-04-14T21:05:07.002Z",
  "SignatureVersion" : "1",
  "Signature" : "ZoDQM5iIhp6E7u84qnip14RTQo/5Vi+fpQ7/tYuqwk28o+7uXuHz9TygI6otycw6Dz5Pw+VOLu0PDuIK4xrGwFYrJypbsaZ1cbNRnM9upkzwGH8w/VORCDZ1QwKYKNP4Ep/mSKVyigh9qe+CHSW/jD2HNE9LY96li5D0h7a2594A12MH5koAXucnYUcHkclBAzwwxbbca2fCkI4PaT24SYyHem1COw86hLt1mDZYE8o7crIX7OUN19+/3vAtsJ2NJ4pLbbR7xufWQmQJks90irG9xRk9K5ky+/1xEv33RYPushZIYjf+H3EW7jX6fAc7+Dz/KLCX5Jeft2pheVMomQ==",
  "SigningCertURL" : "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-7ff5318490ec183fbaddaa2a969abfda.pem",
  "UnsubscribeURL" : "https://sns.us-west-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-west-2:123456789012:AWS-Managed-Threat-Signatures:f2b28278-6d26-4d05-8332-1a96687c850f",
  "MessageAttributes" : {
    "source_revision_token" : {"Type":"String","Value":"14a7e0f5-e050-40d0-a0b1-001f690d44b9"},
    "managed_arn" : {"Type":"String","Value":"arn:aws:network-firewall:us-west-2:aws-managed:stateful-rulegroup/StatefulRG2"}
  }
}
```

The notification contains `source_revision_token`. The value for `source_revision_token` is the `UpdateToken` that you can view when you call [DescribeRuleGroup](../APIReference/API_DescribeRuleGroup.md "../APIReference/API_DescribeRuleGroup.md") in the _AWS Network Firewall API Reference_.

For general information about Amazon SNS notification formats and how to filter the
notifications that you receive, see
[Parsing message formats](../../../sns/latest/dg/sns-message-and-json-formats.md "../../../sns/latest/dg/sns-message-and-json-formats.md") and
[Amazon SNS subscription filter policies](../../../sns/latest/dg/sns-subscription-filter-policies.md "../../../sns/latest/dg/sns-subscription-filter-policies.md")
in the Amazon Simple Notification Service Developer Guide.
