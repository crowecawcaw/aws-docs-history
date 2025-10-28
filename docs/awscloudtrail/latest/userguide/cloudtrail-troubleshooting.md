# Troubleshooting issues with an organization trail

This section provides information on how to troubleshoot issues with an organization
trail.

###### Topics

- [CloudTrail is not delivering events](#event-delivery-failure-optin "#event-delivery-failure-optin")
- [CloudTrail is not sending Amazon SNS notifications
  for a member account in an organization](#sns-topic-policy-failure "#sns-topic-policy-failure")

## CloudTrail is not delivering events

**If CloudTrail is not delivering CloudTrail log files to the Amazon S3
bucket**

Check if there is an issue with the S3 bucket.

- From the CloudTrail console, check the trail's details page. If there's an issue
  with the S3 bucket, the details page includes a warning that delivery to the
  S3 bucket failed.
- From the AWS CLI, run the [get-trail-status](../../../cli/latest/reference/cloudtrail/get-trail-status.md "../../../cli/latest/reference/cloudtrail/get-trail-status.md") command. If there's a
  failure, the command output includes the `LatestDeliveryError`
  field, which displays any Amazon S3 error that CloudTrail encountered when attempting
  to deliver log files to the designated bucket. This error occurs only when
  there is a problem with the destination S3 bucket, and does not occur for
  requests that time out. To resolve the issue, fix the bucket policy so that
  CloudTrail can write to the bucket; or create a new bucket, and then call
  `update-trail` to specify the new bucket. For information
  about the organization bucket policy, see [Create or update an Amazon S3 bucket to use to store the log files for an
  organization trail](create-s3-bucket-policy-for-cloudtrail.md#org-trail-bucket-policy "create-s3-bucket-policy-for-cloudtrail.md#org-trail-bucket-policy").

###### Note

If you misconfigure your trail (for example, the S3 bucket is unreachable),
CloudTrail will attempt to redeliver the log files to your S3 bucket for 30 days, and
these attempted-to-deliver events will be subject to standard CloudTrail charges.
To avoid charges on a misconfigured trail, you need to delete the trail.

**If CloudTrail is not delivering logs to CloudWatch Logs**

Check if there is an issue with the configuration of the CloudWatch Logs role policy.

- From the CloudTrail console, check the trail's details page. If there's an issue
  with CloudWatch Logs, the details page includes a warning that indicates CloudWatch Logs
  delivery failed.
- From the AWS CLI, run the [get-trail-status](../../../cli/latest/reference/cloudtrail/get-trail-status.md "../../../cli/latest/reference/cloudtrail/get-trail-status.md") command. If there's a
  failure, the command output includes the
  `LatestCloudWatchLogsDeliveryError` field, which displays any
  CloudWatch Logs error that CloudTrail encountered when attempting to deliver logs to CloudWatch Logs.
  To resolve the issue, fix the CloudWatch Logs role policy. For information about the
  CloudWatch Logs role policy, see [Role policy document for CloudTrail to use CloudWatch Logs for monitoring](cloudtrail-required-policy-for-cloudwatch-logs.md "cloudtrail-required-policy-for-cloudwatch-logs.md").

**If you're not seeing activity for a member account in an
organization trail**

If you're not seeing activity for a member account in an organization trail, check
the following:

- **Check the home Region for the trail to see if it is
  an opt-in Region**

Although most AWS Regions are enabled by default for your AWS account,
you must manually enable certain Regions (also referred to as
_opt-in Regions_). For information about which
Regions are enabled by default, see [Considerations before enabling and disabling Regions](../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-considerations "../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-considerations") in the
_AWS Account Management Reference Guide_. For the list of Regions
CloudTrail supports, see [CloudTrail supported Regions](cloudtrail-supported-regions.md "cloudtrail-supported-regions.md").

If the organization trail is multi-Region and the home Region is an opt-in
Region, member accounts will not send activity to the organization trail
unless they opt into the AWS Region where the multi-Region trail was
created. For example, if you create a multi-Region trail and choose the
Europe (Spain) Region as the home Region for the trail, only member
accounts that enabled the Europe (Spain) Region for their account will
send their account activity to the organization trail. To resolve the issue,
enable the opt-in Region in each member account in your organization. For
information about enabling an opt-in Region, see [Enable or disable a Region in your organization](../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-organization "../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-organization") in the
_AWS Account Management Reference Guide_.

- **Check if the organization resource-based policy
  conflicts with the CloudTrail service-linked role policy**

CloudTrail uses the service-linked role named [AWSServiceRoleForCloudTrail](using-service-linked-roles-create-slr-for-org-trails.md#service-linked-role-permissions-create-slr-for-org-trails "using-service-linked-roles-create-slr-for-org-trails.md#service-linked-role-permissions-create-slr-for-org-trails") to support
organization trails. This service-linked role allows CloudTrail to perform actions
on organization resources, such as
`organizations:DescribeOrganization`. If the organization's
resource-based policy denies an action that is allowed in the service-linked
role policy, CloudTrail will not be able to perform the action even though it is
allowed in the service-linked role policy. To resolve the issue, fix the
organization's resource-based policy so that it doesn't deny actions that
are allowed in the service-linked role policy.

## CloudTrail is not sending Amazon SNS notifications

for a member account in an organization

When a member account with an AWS Organizations organization trail is not sending Amazon SNS
notifications, there could be an issue with the configuration of the SNS topic
policy. CloudTrail creates organization trails in member accounts even if a resource
validation fails, for example, the organization trail's SNS topic does not include
all member account IDs. If the SNS topic policy is incorrect, an authorization
failure occurs.

To check whether a trail's SNS topic policy has an authorization failure:

- From the CloudTrail console, check the trail's details page. If there's an
  authorization failure, the details page includes a warning `SNS
authorization failed` and indicates to fix the SNS topic
  policy.
- From the AWS CLI, run the [get-trail-status](../../../cli/latest/reference/cloudtrail/get-trail-status.md "../../../cli/latest/reference/cloudtrail/get-trail-status.md") command. If there's an
  authorization failure, the command output includes the
  `LastNotificationError` field with a value of
  `AuthorizationError`. To resolve the issue, fix the Amazon SNS
  topic policy. For information about the Amazon SNS topic policy, see [Amazon SNS topic policy for CloudTrail](cloudtrail-permissions-for-sns-notifications.md "cloudtrail-permissions-for-sns-notifications.md").

For more information about SNS topics and subscribing to them, see [Getting started
with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md "../../../sns/latest/dg/sns-getting-started.md") in the _Amazon Simple Notification Service Developer Guide_.
