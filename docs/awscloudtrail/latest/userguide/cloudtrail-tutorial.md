# Getting started with AWS CloudTrail tutorials

If you're new to AWS CloudTrail, these tutorials can help you learn how to use its features. To use CloudTrail features, you need to have adequate permissions. This page describes the managed policies available for CloudTrail 
 and provides information about how you can grant permissions.

###### Examples:

* [Grant permissions to use CloudTrail](#tutorial-grant-permissions "#tutorial-grant-permissions")
* [View event history](tutorial-event-history.md "tutorial-event-history.md")
* [Create a trail to log management events](tutorial-trail.md "tutorial-trail.md")
* [Create an event data store for S3 data
 events](tutorial-lake-S3.md "tutorial-lake-S3.md")

## Grant permissions to use CloudTrail


To create, update, and manage CloudTrail resources like trails, event data stores, and channels,
 you need to grant permissions to use CloudTrail. This section provides information about the managed policies available for CloudTrail.


###### Note

The permissions you grant to users to perform CloudTrail administration tasks aren't the same as
 the permissions that CloudTrail requires to deliver log files to Amazon S3 buckets or send notifications
 to Amazon SNS topics. For more information about those permissions, see [Amazon S3 bucket policy for CloudTrail](create-s3-bucket-policy-for-cloudtrail.md "create-s3-bucket-policy-for-cloudtrail.md").

If you configure integration with Amazon CloudWatch Logs, CloudTrail also requires a role that it can assume
 to deliver events to an Amazon CloudWatch Logs log group. You must create the role that CloudTrail uses. For more
 information, see [Granting permission to view and configure Amazon CloudWatch Logs information on the CloudTrail console](security_iam_id-based-policy-examples.md#grant-cloudwatch-permissions-for-cloudtrail-users "security_iam_id-based-policy-examples.md#grant-cloudwatch-permissions-for-cloudtrail-users") and [Sending events to CloudWatch Logs](send-cloudtrail-events-to-cloudwatch-logs.md "send-cloudtrail-events-to-cloudwatch-logs.md").


The following AWS managed policies are available for CloudTrail:



* [**AWSCloudTrail\_FullAccess**](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudTrail_FullAccess.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudTrail_FullAccess.html") – This policy
 provides full access to CloudTrail actions on CloudTrail resources, such as trails, event data stores, and
 channels. This policy provides the required permissions to create, update, and delete CloudTrail
 trails, event data stores, and channels. 


 This policy also provides permissions to manage the Amazon S3 bucket, the log group for
 CloudWatch Logs, and an Amazon SNS topic for a trail. However, the `AWSCloudTrail_FullAccess`
 managed policy doesn't provide permissions to delete the Amazon S3 bucket, the log group for CloudWatch Logs,
 or an Amazon SNS topic. For information about managed policies for other AWS services, see the
 [*AWS
 Managed Policy Reference Guide*](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/about-managed-policy-reference.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/about-managed-policy-reference.html").


###### Note

The **AWSCloudTrail\_FullAccess** policy
 isn't intended to be shared broadly across your AWS account. Users with this role can turn
 off or reconfigure the most sensitive and important auditing functions in their
 AWS accounts. For this reason, you must only apply this policy to account administrators.
 You must closely control and monitor use of this policy.
* [**AWSCloudTrail\_ReadOnlyAccess**](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudTrail_ReadOnlyAccess.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudTrail_ReadOnlyAccess.html") – This
 policy grants permissions to view the CloudTrail console, including recent events and event history.
 This policy also allows you to view existing trails, event data stores, and channels. Roles
 and users with this policy can [download the event history](view-cloudtrail-events-console.md#downloading-events "view-cloudtrail-events-console.md#downloading-events"), but they can't create or update trails, event data
 stores, or channels.

To provide access, add permissions to your users, groups, or roles:



* Users and groups in AWS IAM Identity Center:


Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html "https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html") in the *AWS IAM Identity Center User Guide*.
* Users managed in IAM through an identity provider:


Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html")
 in the *IAM User Guide*.
* IAM users:




	+ Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html") in the *IAM User Guide*.
	+ (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console") in the *IAM User Guide*.
