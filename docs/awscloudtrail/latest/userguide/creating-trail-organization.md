# Creating a trail for an organization

If you have created an organization in AWS Organizations, you can create a trail that logs all
events for all AWS accounts in that organization. This is sometimes called an
_organization trail_.

The management account for the organization can assign a [delegated administrator](cloudtrail-delegated-administrator.md "cloudtrail-delegated-administrator.md") to create
new organization trails or manage existing organization trails. For more information on
adding a delegated administrator, see [Add a CloudTrail delegated administrator](cloudtrail-add-delegated-administrator.md "cloudtrail-add-delegated-administrator.md").

The management account for the organization can edit an existing trail in their account,
and apply it to an organization, making it an organization trail. Organization trails log
events for the management account and all member accounts in the organization. For more
information about AWS Organizations, see [Organizations Terminology and Concepts](../../../organizations/latest/userguide/orgs_getting-started_concepts.md "../../../organizations/latest/userguide/orgs_getting-started_concepts.md").

###### Note

You must sign in with the management account or a delegated administrator account
associated with an organization to create an organization trail. You must also have
[sufficient permissions](creating-an-organizational-trail-prepare.md#org_trail_permissions "creating-an-organizational-trail-prepare.md#org_trail_permissions") for the user or role in the management or delegated administrator
account to create the trail. If you don't have sufficient permissions, you won't have
the option to apply the trail to an organization.

All organization trails created using the console are multi-Region organization trails
that log events from the [enabled](../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-organization "../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-organization") AWS Regions in each member account in the organization. To log events
in all AWS partitions in your organization, create a multi-Region organization trail in
each partition. You can create either a single-Region or multi-Region organization trail by
using the AWS CLI. If you create a single-Region trail, you log activity only in the trail's
AWS Region (also referred to as the _Home_ Region).

Although most AWS Regions are enabled by default for your AWS account, you must
manually enable certain Regions (also referred to as _opt-in Regions_).
For information about which Regions are enabled by default, see [Considerations before enabling and disabling Regions](../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-considerations "../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-considerations") in the
_AWS Account Management Reference Guide_. For the list of Regions CloudTrail supports,
see [CloudTrail supported Regions](cloudtrail-supported-regions.md "cloudtrail-supported-regions.md").

When you create an organization trail, a copy of the trail with the name that you give it
is created in the member accounts that belongs to your organization.

- If the organization trail is for a **single-Region**
  and the trail's home Region **is not an opt-in Region**, a
  copy of the trail is created in the organization trail's home Region in each member
  account.
- If the organization trail is for a **single-Region**
  and the trail's home Region **is an opt-in Region**, a
  copy of the trail is created in the organization trail's home Region in the member
  accounts that have enabled that Region.
- If the organization trail is **multi-Region** and the
  trail's home Region **is**
  **not an opt-in Region**, a copy of the trail is
  created in each enabled AWS Region in each member account. When a member account
  enables an opt-in Region, a copy of the multi-Region trail is created in the newly
  opted in Region for the member account after activation of that Region is
  complete.
- If the organization trail is **multi-Region** and the
  home Region **is**
  **an opt-in Region**, member accounts will not send
  activity to the organization trail unless they opt into the AWS Region where the
  multi-Region trail was created. For example, if you create a multi-Region trail and
  choose the Europe (Spain) Region as the home Region for the trail, only member
  accounts that enabled the Europe (Spain) Region for their account will send
  their account activity to the organization trail.

###### Note

CloudTrail creates organization trails in member accounts even if a resource validation
fails. Examples of validation failures include:

- an incorrect Amazon S3 bucket policy
- an incorrect Amazon SNS topic policy
- inability to deliver to a CloudWatch Logs log group
- insufficient permission to encrypt using a KMS key
  A member account with CloudTrail permissions can see any validation failures for an
  organization trail by viewing the trail's details page on the CloudTrail console, or by
  running the AWS CLI [get-trail-status](../../../cli/latest/reference/cloudtrail/get-trail-status.md "../../../cli/latest/reference/cloudtrail/get-trail-status.md") command.

Users with CloudTrail permissions in member accounts can see organization trails when they log
into the CloudTrail console from their AWS accounts, or when they run AWS CLI commands such as
`describe-trails`. However, users in member accounts do not have sufficient
permissions to delete organization trails, turn logging on or off, change what types of
events are logged, or otherwise change an organization trail in any way.

When you create an organization trail in the console,
CloudTrail creates a [service-linked role](using-service-linked-roles.md "using-service-linked-roles.md") to perform logging tasks in your organization's member accounts. This role is named
**AWSServiceRoleForCloudTrail**, and is required for
CloudTrail to log events for an organization. If an AWS account is added to an organization, the
organization trail and service-linked role are added to that AWS account, and logging
starts for that account automatically in the organization trail. If an AWS account is
removed from an organization, the organization trail and service-linked role are deleted
from the AWS account that is no longer part of the organization. However, log files for
the removed account that were created before the account's removal remain in the Amazon S3 bucket
where log files are stored for the trail.

If the management account for an AWS Organizations organization creates an organization trail, but
then is subsequently removed as the organization's management account, any organization trail
created using their account becomes a non-organization trail.

In the following example, the organization's management account 111111111111
creates a trail named `MyOrganizationTrail` for the organization
`o-exampleorgid`. The trail logs activity for all accounts in
the organization in the same Amazon S3 bucket. All accounts in the organization can see
`MyOrganizationTrail` in their list of trails, but member
accounts cannot remove or modify the organization trail. Only the management account or
delegated administrator account can change or delete the trail for the organization. Only
the management account can remove a member account from an organization. Similarly, by
default, only the management account has access to the Amazon S3 bucket
for the trail, and the logs contained
within it. The high-level bucket structure for log files contains a folder named with the
organization ID, and subfolders named with the account IDs for each account in the
organization. Events for each member account are logged in the folder that corresponds to
the member account ID. If member account 444444444444 is removed from the
organization, `MyOrganizationTrail` and the service-linked role no
longer appear in AWS account 444444444444, and no further events are logged for
that account by the organization trail. However, the 444444444444 folder remains
in the Amazon S3 bucket, with all logs created before the removal of the account from the
organization.

![A conceptual overview of a sample organization in Organizations.](images/organization-trail.png)
In this example, the ARN of the trail created in the management account is
`aws:cloudtrail:us-east-2:111111111111:trail/`MyOrganizationTrail``.
This ARN is the ARN for the trail in all member accounts as well.

Organization trails are similar to regular trails in many ways. You can create multiple
trails for your organization, and choose whether to create a multi-Region or single-Region
organization trail, and what kinds of events you want logged in your organization trail,
just as in any other trail. However, there are some differences. For example, when you
create a trail in the console and choose whether to log data events for Amazon S3 buckets or
AWS Lambda functions, the only resources listed in the CloudTrail console are those for the
management account, but you can add the ARNs for resources in member accounts. Data events
for specified member account resources are logged without having to manually configure
cross-account access to those resources. For more information about logging management
events, Insights events, and data events, see [Logging management events](logging-management-events-with-cloudtrail.md "logging-management-events-with-cloudtrail.md"), [Logging data events](logging-data-events-with-cloudtrail.md "logging-data-events-with-cloudtrail.md"), and [Working with CloudTrail Insights](logging-insights-events-with-cloudtrail.md "logging-insights-events-with-cloudtrail.md").

###### Note

In the console, you create a multi-Region trail. It's a recommended best practice to
log activity in all enabled Regions in your AWS account, because it helps you keep
your AWS environment more secure. To create a single-Region trail, [use the AWS CLI](cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-create-trail.md#cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-examples-single "cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-create-trail.md#cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-examples-single").

When you view events in **Event history** for an organization in
AWS Organizations, you can view the events only for the AWS account with which you are signed in.
For example, if you are signed in with the organization management account, **Event
history** shows the last 90 days of management events for the management
account. Organization member account events are not shown in **Event
history** for the management account. To view member account events in
**Event history**, sign in with the member account.

You can configure other AWS services to further analyze and act upon the event data
collected in CloudTrail logs for an organization trail the same way you would for any other trail.
For example, you can analyze the data in an organization trail using Amazon Athena. For more
information, see [AWS service integrations with CloudTrail logs](cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations").

###### Topics

- [Moving from member
  account trails to organization trails](creating-an-organizational-trail-best-practice.md "creating-an-organizational-trail-best-practice.md")
- [Prepare for creating a trail
  for your organization](creating-an-organizational-trail-prepare.md "creating-an-organizational-trail-prepare.md")
- [Creating a trail for
  your organization in the console](creating-an-organizational-trail-in-the-console.md "creating-an-organizational-trail-in-the-console.md")
- [Creating a trail for an organization with the AWS CLI](cloudtrail-create-and-update-an-organizational-trail-by-using-the-aws-cli.md "cloudtrail-create-and-update-an-organizational-trail-by-using-the-aws-cli.md")
- [Troubleshooting issues with an organization trail](cloudtrail-troubleshooting.md "cloudtrail-troubleshooting.md")
