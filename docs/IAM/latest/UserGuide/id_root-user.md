# AWS account root user

When you first create an Amazon Web Services (AWS) account, you begin with a single sign-in identity
that has complete access to all AWS services and resources in the account. This identity is
called the AWS account _root user_. The email address and password that you
used to create your AWS account are the credentials you use to sign in as your root user.

- Use the root user only to perform the tasks that require root-level permissions.

For the complete list of tasks that require you to sign in as the root user, see [Tasks that require root user credentials](#root-user-tasks "#root-user-tasks").

- Follow the [root user best practices for your
  AWS account](root-user-best-practices.md "root-user-best-practices.md").
- If you're having trouble signing in, see [Sign in to the
  AWS Management Console](../../../signin/latest/userguide/console-sign-in-tutorials.md "../../../signin/latest/userguide/console-sign-in-tutorials.md").

###### Important

We strongly recommend that you don't use the root user for your everyday tasks and that
you follow the [root user best practices for your
AWS account](root-user-best-practices.md "root-user-best-practices.md"). Safeguard your root user credentials and use them to perform the tasks
that only the root user can perform.
For the complete list of tasks that require you to sign in as the root user, see [Tasks that require root user credentials](#root-user-tasks "#root-user-tasks").

While MFA is enforced for root users by default, it requires customer action to add MFA during
the initial account creation or as prompted during sign-in. For more information about using MFA
to protect the root user, see [Multi-factor authentication for AWS account root user](enable-mfa-for-root.md "enable-mfa-for-root.md").

## Centrally manage root access for member

accounts

To help you manage credentials at scale, you can centrally secure access to root user
credentials for member accounts in AWS Organizations. When you enable AWS Organizations, you combine all your
AWS accounts into an organization for central management. Centralizing root access lets you
remove root user credentials and perform the following privileged tasks on member
accounts.

**Remove member account root user credentials**

After you [centralize root access for
member accounts](id_root-enable-root-access.md "id_root-enable-root-access.md"), you can choose to delete root user credentials from member
accounts in your Organizations. You can remove the root user password, access keys, signing
certificates, and deactivate multi-factor authentication (MFA). New accounts you create
in Organizations have no root user credentials by default. Member accounts can't sign in to their
root user or perform password recovery for their root user unless account recovery is
enabled.

**Perform privileged tasks that require root user credentials**

Some tasks can only be performed when you sign in as the root user of an account. Some
of these [Tasks that require root user credentials](#root-user-tasks "#root-user-tasks") can be
performed by the management account or delegated administrator for IAM. To learn more
about taking privileged actions on member accounts, see [Perform a privileged
task](id_root-user-privileged-task.md "id_root-user-privileged-task.md").

**Enable account recovery of the root user**

If you need to recover root user credentials for a member account, the Organizations
management account or delegated administrator can perform the **Allow password
recovery** privileged task. The person with access to the root user email inbox
for the member account can [reset the root user password](reset-root-password.md "reset-root-password.md")
to recover root user credentials. We recommend deleting root user credentials once you
complete the task that requires access to the root user.

## Tasks that require root user credentials

We recommend that you [configure an
administrative user in AWS IAM Identity Center](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md") to perform daily tasks and access AWS resources.
However, you can perform the tasks listed below only when you sign in as the root user of an
account.

To simplify managing privileged root user credentials across member accounts in AWS Organizations, you
can enable centralized root access to help you centrally secure highly privileged access to
your AWS accounts. [Centrally manage root access for member
accounts](#id_root-user-access-management "#id_root-user-access-management") lets you centrally remove and prevent
long-term root user credential recovery, improving account security in your organization. After
you enable this feature, you can perform the following privileged tasks on member
accounts.

- Remove member account root user credentials to prevent account recovery of the root user.
  You can also allow password recovery to recover root user credentials for a member
  account.
- Remove a misconfigured bucket policy that denies all principals from accessing an Amazon S3
  bucket.
- Delete an Amazon Simple Queue Service resource-based policy that denies all principals from accessing an
  Amazon SQS queue.

###### Account Management Tasks

- [Change your
  AWS account settings.](../../../accounts/latest/reference/manage-acct-update-root-user.md "../../../accounts/latest/reference/manage-acct-update-root-user.md") Standalone AWS accounts that are not part of AWS Organizations
  require root credentials to update the email address, root user password, and root user access
  keys. Other account settings, such as account name, contact information, alternate
  contacts, payment currency preference, and AWS Regions, don't require root user
  credentials.

###### Note

AWS Organizations, with all features enabled, can be used to manage member account settings
centrally from the management account and delegated admin accounts. Authorized
IAM users or IAM roles in both the management account and delegated admin accounts
can close member accounts and update the root email addresses, account names, contact
information, alternate contacts, and AWS Regions of member accounts.

- [Close your AWS account.](../../../awsaccountbilling/latest/aboutv2/close-account.md "../../../awsaccountbilling/latest/aboutv2/close-account.md")
  Standalone AWS accounts that are not part of AWS Organizations require root credentials to close
  the account. With AWS Organizations, you can close the member accounts centrally from the
  management account and delegated admin accounts.
- [Restore IAM user
  permissions.](access_policies_manage-edit.md "access_policies_manage-edit.md") If the only IAM administrator accidentally revokes their own
  permissions, you can sign in as the root user to edit policies and restore those
  permissions.

###### Billing Tasks

- [Activate IAM access to the Billing and Cost Management console](../../../awsaccountbilling/latest/aboutv2/control-access-billing.md#ControllingAccessWebsite-Activate "../../../awsaccountbilling/latest/aboutv2/control-access-billing.md#ControllingAccessWebsite-Activate").
- Some Billing tasks are limited to the root user. See [Managing an
  AWS account](../../../awsaccountbilling/latest/aboutv2/manage-account-payment.md "../../../awsaccountbilling/latest/aboutv2/manage-account-payment.md") in AWS Billing User Guide for more information.
- View certain tax invoices. An IAM user with the [aws-portal:ViewBilling](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md#user-permissions "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md#user-permissions") permission can view and download VAT invoices from AWS
  Europe, but not AWS Inc. or Amazon Internet Services Private Limited (AISPL).

###### AWS GovCloud (US) Tasks

- [Sign up for
  AWS GovCloud (US)](../../../govcloud-us/latest/UserGuide/getting-started-sign-up.md "../../../govcloud-us/latest/UserGuide/getting-started-sign-up.md").
- Request AWS GovCloud (US) account root user access keys from AWS Support.

###### Amazon EC2 Task

- [Register as a seller](../../../AWSEC2/latest/UserGuide/ri-market-general.md "../../../AWSEC2/latest/UserGuide/ri-market-general.md") in the
  Reserved Instance Marketplace.

###### AWS KMS Task

- In the event that an AWS Key Management Service key becomes unmanageable, an administrator can recover
  it by contacting Support; however, Support responds to your root user's primary phone number for
  authorization by confirming the ticket OTP.

###### Amazon Mechanical Turk Task

- [Link Your AWS account to your MTurk Requester account](../../../AWSMechTurk/latest/AWSMechanicalTurkGettingStartedGuide/SetUp.md#accountlinking "../../../AWSMechTurk/latest/AWSMechanicalTurkGettingStartedGuide/SetUp.md#accountlinking").

###### Amazon Simple Storage Service Tasks

- [Configure an Amazon S3 bucket
  to enable MFA (multi-factor authentication)](../../../AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.md "../../../AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.md").
- [Edit or
  delete an Amazon S3 bucket policy that denies all principals](https://aws.amazon.com/premiumsupport/knowledge-center/change-vpc-endpoint-s3-bucket-policy/ "https://aws.amazon.com/premiumsupport/knowledge-center/change-vpc-endpoint-s3-bucket-policy/").

You can use privileged actions to unlock an Amazon S3 bucket with a misconfigured bucket
policy. For details, see [Perform a privileged task on an AWS Organizations
member account](id_root-user-privileged-task.md "id_root-user-privileged-task.md").

###### Amazon Simple Queue Service Task

- [Edit or delete
  an Amazon SQS resource-based policy that denies all principals](https://aws.amazon.com/premiumsupport/knowledge-center/sqs-queue-access-issues-deny-policy "https://aws.amazon.com/premiumsupport/knowledge-center/sqs-queue-access-issues-deny-policy").

You can use privileged actions to unlock an Amazon SQS queue with a misconfigured
resource-based policy. For details, see [Perform a privileged task on an AWS Organizations
member account](id_root-user-privileged-task.md "id_root-user-privileged-task.md").

## Additional resources

For more information about the AWS root user, see the following resources:

- For help with root user issues, see [Troubleshoot issues with the root user](troubleshooting_root-user.md "troubleshooting_root-user.md").
- To centrally manage root user email addresses in AWS Organizations, see [Updating the root user email address for a member account](../../../organizations/latest/userguide/orgs_manage_accounts_update_primary_email.md "../../../organizations/latest/userguide/orgs_manage_accounts_update_primary_email.md") in the
  _AWS Organizations User Guide_.

The following articles provide additional information about working with the
root user.

- [What are some
  best practices for securing my AWS account and its resources?](https://repost.aws/knowledge-center/security-best-practices "https://repost.aws/knowledge-center/security-best-practices")
- [How can I create an EventBridge event rule to notify me that my root user was used?](https://repost.aws/knowledge-center/root-user-account-eventbridge-rule "https://repost.aws/knowledge-center/root-user-account-eventbridge-rule")
- [Monitor and notify on AWS account root user activity](https://aws.amazon.com/blogs/mt/monitor-and-notify-on-aws-account-root-user-activity/ "https://aws.amazon.com/blogs/mt/monitor-and-notify-on-aws-account-root-user-activity/")
- [Monitor
  IAM root user activity](../../../prescriptive-guidance/latest/patterns/monitor-iam-root-user-activity.md "../../../prescriptive-guidance/latest/patterns/monitor-iam-root-user-activity.md")
