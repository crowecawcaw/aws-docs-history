# Best practices for member accounts

Follow these recommendations to help protect the security of the member accounts in your
organization. These recommendations assume that you also adhere to the [best practice of using the root user only for
those tasks that truly require it](../../../IAM/latest/UserGuide/root-user-best-practices.md "../../../IAM/latest/UserGuide/root-user-best-practices.md").

###### Topics

- [Define account name and attributes](#bp_member-acct_define-acct "#bp_member-acct_define-acct")
- [Efficiently scale your environment
  and account usage](#bp_member-acct_efficiently-scale "#bp_member-acct_efficiently-scale")
- [Enable root access management to simplify managing root user credentials for member accounts](#bp_member-acct_root-access-management "#bp_member-acct_root-access-management")

## Define account name and attributes

For your member accounts, use a naming structure and email address that reflects the
account usage. For example, `Workloads+fooA+dev@domain.com` for
`WorkloadsFooADev`, `Workloads+fooB+dev@domain.com` for
`WorkloadsFooBDev`. If you have custom tags defined for your
organization, we recommend that you assign those tags on accounts that reflect account
usage, cost center, environment, and project. This makes it easier to identify,
organize, and search for accounts.

## Efficiently scale your environment

and account usage

As you scale, before creating new accounts, make sure accounts for similar needs do
not already exist, to avoid unnecessary duplication. AWS accounts should be based on
common access requirements. If you are planning to reuse the accounts, such as a sandbox
account or equivalent, we recommend that you clean up unneeded resources or workloads
from the accounts, but save the accounts for a future use.

Before closing accounts, note that they are subject to close account quota limits. For
more information, see [Quotas and service limits for AWS Organizations](orgs_reference_limits.md "orgs_reference_limits.md"). Consider implementing a cleanup process to
reuse accounts instead of closing them and creating new ones when possible. This way,
you will avoid running into incurring costs from running resources, and reaching [CloseAccount API](../APIReference/API_CloseAccount.md "../APIReference/API_CloseAccount.md") limits.

## Enable root access management to simplify managing root user credentials for member accounts

We recommend you enable root access management to help you monitor and remove root user credentials for member accounts.
Root access management prevents recovery of root user credentials, improving account security in your organization.

- Remove root user credentials for member accounts to prevent sign in to the root user. This also prevents member accounts from recovery of the root user.
- Assume a privileged session to perform the following tasks on member accounts:
  - Remove a misconfigured bucket policy that denies all principals from accessing an Amazon S3 bucket.
  - Delete an Amazon Simple Queue Service resource-based policy that denies all principals from accessing an Amazon SQS queue.
  - Allow a member account to recover their root user credentials.
    The person with access to the root user email inbox for the member account
    can reset the root user password and sign in as the member account root user.

After root access management is enabled, newly created member accounts are secure-by-default,
having no root user credentials, which eliminates the need for additional security, such as MFA after provisioning.

For more information, see [Centralize root user credentials for member accounts](../../../IAM/latest/UserGuide/id_root-user.md#id_root-user-access-management "../../../IAM/latest/UserGuide/id_root-user.md#id_root-user-access-management") in the _AWS Identity and Access Management User Guide_.

### Use an SCP to restrict what the root user in your

member accounts can do

We recommend that you create a service control policy (SCP) in the organization and
attach it to the organization's root so that it applies to all member accounts. For more
information, see [Secure your
Organizations account root user credentials](../../../IAM/latest/UserGuide/root-user-best-practices.md#ru-bp-organizations "../../../IAM/latest/UserGuide/root-user-best-practices.md#ru-bp-organizations").

You can deny all root actions except a specific root only action that you must perform
in your member account. For example, the following SCP prevents the root user in any
member account from making any AWS service API calls except “Updating a S3 bucket
policy that was misconfigured and denies access to all principals” (one of the actions
that requires root credentials). For more information, see [Tasks that require root user credentials](../../../IAM/latest/UserGuide/root-user-tasks.md "../../../IAM/latest/UserGuide/root-user-tasks.md") in the _IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "NotAction":[
 "s3:GetBucketPolicy",
 "s3:PutBucketPolicy",
 "s3:DeleteBucketPolicy"
 ],
 "Resource": "*",
 "Condition": {
 "ArnLike": { "aws:PrincipalArn": "arn:aws:iam::*:root" }
 }
 }
 ]
 }`

```

In the majority of circumstances, any administrative tasks can be performed by an
AWS Identity and Access Management (IAM) role in the member account that has relevant administrator
permissions. Any such roles should have suitable controls applied to limit, log, and
monitor activities.
