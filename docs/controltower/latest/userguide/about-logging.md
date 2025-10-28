# About logging in AWS Control Tower

AWS Control Tower accomplishes logging of actions and events automatically, through its integration
with AWS CloudTrail and AWS Config, and it records them in CloudWatch. All actions are logged, including actions
from the AWS Control Tower management account and from your organization's member accounts.
Management account actions and events are viewable on the **Activities** page in
the console. You can view member account actions and events in the log archive files.

**Organization-level trails**

AWS Control Tower sets up a new CloudTrail trail when you set up a landing zone. It is an _organization-level trail_, which means that it logs all events for
the management account and all member accounts in the organization. This feature relies on
_trusted access_ to give the management account permissions
to create a trail on every member account.

For more information about AWS Control Tower and CloudTrail organization trails, see [Creating a trail for an organization](../../../awscloudtrail/latest/userguide/creating-trail-organization.md "../../../awscloudtrail/latest/userguide/creating-trail-organization.md").

###### Note

In AWS Control Tower releases before landing zone version 3.0, AWS Control Tower created a member account
trail in each account. When you update to release 3.0, your CloudTrail trail becomes an
organization trail. For best practices when moving between trails, see [Best practices for changing trails](../../../awscloudtrail/latest/userguide/creating-trail-organization.md#creating-an-organizational-trail-best-practice "../../../awscloudtrail/latest/userguide/creating-trail-organization.md#creating-an-organizational-trail-best-practice") in the _CloudTrail User
Guide_.

When you enroll an account into AWS Control Tower, your account is governed by the AWS CloudTrail trail
for the AWS Control Tower organization. If you have an existing deployment of a CloudTrail trail in that
account, you may see duplicate charges unless you delete the existing trail for the account
before you enroll it in AWS Control Tower.

###### Note

When you update to landing zone version 3.0, AWS Control Tower deletes the account-level trails
(that AWS Control Tower has created) in your enrolled accounts on your behalf. Your existing,
account-level log files are preserved in their Amazon S3 bucket.
