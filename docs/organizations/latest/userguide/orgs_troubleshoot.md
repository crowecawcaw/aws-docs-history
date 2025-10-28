# Troubleshooting AWS Organizations

If you encounter issues when working with AWS Organizations, consult the topics in this
section.

## Troubleshooting general issues

Use the information here to help you diagnose and fix access-denied or other common issues
that you might encounter when working with AWS Organizations.

###### Topics

- [I get an "access denied"
  message when I make a request to AWS Organizations](#troubleshoot_general_access-denied-service "#troubleshoot_general_access-denied-service")
- [I get an "access denied"
  message when I make a request with temporary security credentials](#troubleshoot_general_access-denied-temp-creds "#troubleshoot_general_access-denied-temp-creds")
- [I get an "access denied"
  message when I try to leave an organization as a member account or remove a member
  account as the management account](#troubleshoot_general_error-leaving-org "#troubleshoot_general_error-leaving-org")
- [I get a "quota exceeded"
  message when I try to add an account to my organization](#troubleshoot_general_error-adding-account "#troubleshoot_general_error-adding-account")
- [I get a "this operation requires
  a wait period" message while adding or removing accounts](#troubleshoot_general_error-wait-req "#troubleshoot_general_error-wait-req")
- [I get an "organization is still
  initializing" message when I try to add an account to my organization](#troubleshoot_general_error-still-init "#troubleshoot_general_error-still-init")
- [I get an "Invitations
  are disabled" message when I try to invite an account to my organization.](#troubleshoot_general_error-changing-feature-set "#troubleshoot_general_error-changing-feature-set")
- [Changes that I make aren't
  always immediately visible](#troubleshoot_general_eventual-consistency "#troubleshoot_general_eventual-consistency")
- [I get a “Complete sign-up”
  message when I try to access an account that is already a part of an
  organization](#troubleshoot_general_complete-signup "#troubleshoot_general_complete-signup")

### I get an "access denied"

message when I make a request to AWS Organizations

- Verify that you have permissions to call the action and resource that you have
  requested. An administrator must grant permissions by attaching an IAM policy
  to your user, group, or role. If the policy statements that grant those
  permissions include any conditions, such as time-of-day or IP address
  restrictions, you also must meet those requirements when you send the request.
  For information about viewing or modifying policies for a user, group, or role,
  see [Working with
  Policies](../../../IAM/latest/UserGuide/access_policies_manage.md "../../../IAM/latest/UserGuide/access_policies_manage.md") in the _IAM User Guide_.
- If you are signing API requests manually (without using the [AWS SDKs](http://aws.amazon.com/tools/ "http://aws.amazon.com/tools/")), verify that you have
  correctly [signed the
  request](../../../general/latest/gr/signing_aws_api_requests.md "../../../general/latest/gr/signing_aws_api_requests.md").

### I get an "access denied"

message when I make a request with temporary security credentials

- Verify that the user or role that you are using to make the request has the
  correct permissions. Permissions for temporary security credentials are derived
  from an user or role, so the permissions are limited to those granted to the
  user or role. For more information about how permissions for temporary security
  credentials are determined, see [Controlling
  Permissions for Temporary Security Credentials](../../../IAM/latest/UserGuide/id_credentials_temp_control-access.md "../../../IAM/latest/UserGuide/id_credentials_temp_control-access.md") in the _IAM User Guide_.
- Verify that your requests are being signed correctly and that the request is
  well formed. For details, see the [toolkit](http://aws.amazon.com/tools/ "http://aws.amazon.com/tools/") documentation for your chosen SDK or [Using Temporary
  Security Credentials to Request Access to AWS Resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the
  _IAM User Guide_.
- Verify that your temporary security credentials haven't expired. For more
  information, see [Requesting Temporary Security Credentials](../../../IAM/latest/UserGuide/id_credentials_temp_request.md "../../../IAM/latest/UserGuide/id_credentials_temp_request.md") in the _IAM User Guide_.

### I get an "access denied"

message when I try to leave an organization as a member account or remove a member
account as the management account

- You can remove a member account only after you enable IAM user access to
  billing in the member account. For more information, see [Activating Access to the Billing and Cost Management Console](../../../awsaccountbilling/latest/aboutv2/grantaccess.md#ControllingAccessWebsite-Activate "../../../awsaccountbilling/latest/aboutv2/grantaccess.md#ControllingAccessWebsite-Activate") in the
  _AWS Billing User Guide_.
- You can remove an account from your organization only if the account has the
  information required for it to operate as a standalone account. When you create
  an account in an organization using the AWS Organizations console, API, or AWS CLI
  commands, that information isn't automatically collected. For an account that
  you want to make standalone, you must accept the AWS Customer Agreement,
  choose a support plan, provide and verify the required contact information, and
  provide a current payment method. AWS uses the payment method to charge for
  any billable (not AWS Free Tier) AWS activity that occurs while the account
  isn't attached to an organization. For more information, see [Leaving an organization from a
  member account with AWS Organizations](orgs_manage_accounts_leave-as-member.md "orgs_manage_accounts_leave-as-member.md").

### I get a "quota exceeded"

message when I try to add an account to my organization

There is a maximum number of accounts that you can have in an organization. Deleted or
closed accounts continue to count against this quota.

An invitation to join counts against the maximum number of accounts in your
organization. The count is returned if the invited account declines, the management
account cancels the invitation, or the invitation expires.

- Before you close or delete an AWS account, [remove it from your
  organization](orgs_manage_accounts_remove.md "orgs_manage_accounts_remove.md") so that it doesn't continue to count against your
  quota.
- See [Maximum and minimum values](orgs_reference_limits.md#min-max-values "orgs_reference_limits.md#min-max-values") for
  information about how to request a quota increase.

### I get a "this operation requires

a wait period" message while adding or removing accounts

Some actions require a wait period due to account quotas. For example, you can't
immediately remove newly created accounts. Try the action again in a few days.

For issues with adding accounts, see the quota [Default maximum number of
accounts](orgs_reference_limits.md#default-maximum-number-of-accounts "orgs_reference_limits.md#default-maximum-number-of-accounts"). For issues with removing accounts, see the quota [Number of accounts you can close within a
30-day period](orgs_reference_limits.md#number-of-accounts-you-can-close "orgs_reference_limits.md#number-of-accounts-you-can-close").

### I get an "organization is still

initializing" message when I try to add an account to my organization

If you receive this error and it's been over an hour since you created the
organization, contact [AWS Support](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

### I get an "Invitations

are disabled" message when I try to invite an account to my organization.

This happens when you [enable all
features in your organization](orgs_manage_org_support-all-features.md "orgs_manage_org_support-all-features.md"). This operation can take some time and requires
that all member accounts respond. Until the operation is completed, you can't invite new
accounts to join the organization.

### Changes that I make aren't

always immediately visible

As a service that is accessed through computers in data centers around the world,
AWS Organizations uses a distributed computing model called [eventual consistency](https://wikipedia.org/wiki/Eventual_consistency "https://wikipedia.org/wiki/Eventual_consistency").
Any change that you make in AWS Organizations takes time to become visible from all possible
endpoints. Some of the delay results from the time it takes to send the data from server
to server or from replication zone to replication zone. AWS Organizations also uses caching to
improve performance, but in some cases this can add time. The change might not be
visible until the previously cached data times out.

Design your global applications to account for these potential delays and ensure that
they work as expected, even when a change made in one location isn't instantly visible
at another.

For more information about how some other AWS services are affected by this, consult
the following resources:

- [Managing Data
  Consistency](../../../redshift/latest/dg/managing-data-consistency.md "../../../redshift/latest/dg/managing-data-consistency.md") in the _Amazon Redshift Database Developer Guide_
- [Amazon S3 Data
  Consistency Model](../../../AmazonS3/latest/userguide/Introduction.md#ConsistencyModel "../../../AmazonS3/latest/userguide/Introduction.md#ConsistencyModel") in the _Amazon Simple Storage Service User Guide_
- [Ensuring Consistency When Using Amazon S3 and Amazon Elastic MapReduce for ETL
  Workflows](https://aws.amazon.com/blogs/big-data/ensuring-consistency-when-using-amazon-s3-and-amazon-elastic-mapreduce-for-etl-workflows/ "https://aws.amazon.com/blogs/big-data/ensuring-consistency-when-using-amazon-s3-and-amazon-elastic-mapreduce-for-etl-workflows/") in the AWS Big Data Blog
- [EC2 Eventual Consistency](../../../AWSEC2/latest/APIReference/query-api-troubleshooting.md#eventual-consistency "../../../AWSEC2/latest/APIReference/query-api-troubleshooting.md#eventual-consistency") in the
  _Amazon EC2 API Reference_.

### I get a “Complete sign-up”

message when I try to access an account that is already a part of an
organization

- It may take up to 48 hours for the member account to inherit the management
  account’s billing details.
- If the issue persists after 48 hours, you can open a support case to the
  Account and Billing support team. For more information, see [Creating a support case](../../../awssupport/latest/user/case-management.md#creating-a-support-case "../../../awssupport/latest/user/case-management.md#creating-a-support-case").
