# Centralize root access for member

accounts

Root user credentials are the initial credentials assigned to each AWS account
that has complete access to all AWS services and resources in the account. When you enable
AWS Organizations, you combine all your AWS accounts into an organization for central management.
Each member account has its own root user with default permissions to perform any action in the
member account. We recommend you centrally secure the root user credentials of AWS accounts
managed using AWS Organizations to prevent root user credential recovery and access at scale.

After you centralize root access, you can choose to delete root user credentials from member
accounts in your organization. You can remove the root user password, access keys, signing
certificates, and deactivate multi-factor authentication (MFA). New accounts you create in
AWS Organizations have no root user credentials by default. Member accounts can't sign in to their
root user or perform password recovery for their root user.

###### Note

While some [Tasks that require root user credentials](id_root-user.md#root-user-tasks "id_root-user.md#root-user-tasks") can be
performed by the management account or delegated administrator for IAM, some tasks can
only be performed when you sign in as the root user of an account.

If you need to recover root user credentials for a member account to perform one of these
tasks, follow the steps in [Perform a privileged
task](id_root-user-privileged-task.md "id_root-user-privileged-task.md") and select **Allow
password recovery**. The person with access to the root user email inbox for
the member account can then follow the steps to [reset the root user
password](reset-root-password.md "reset-root-password.md") and sign in to the member account root user.

We recommend deleting root user credentials once you complete the task that requires
access to the root user.

## Prerequisites

Before you centralize root access, you must have an account configured with the
following settings:

- You must have the following IAM permissions:
  - `iam:GetAccessKeyLastUsed`
  - `iam:GetAccountSummary`
  - `iam:GetLoginProfile`
  - `iam:GetUser`
  - `iam:ListAccessKeys`
  - `iam:ListMFADevices`
  - `iam:ListSigningCertificates`
  - `sts:AssumeRoot`

###### Note

To audit the root user credential status of a member account, you can use the
[IAMAuditRootUserCredentials](security-iam-awsmanpol.md#security-iam-awsmanpol-IAMAuditRootUserCredentials "security-iam-awsmanpol.md#security-iam-awsmanpol-IAMAuditRootUserCredentials")
AWS managed policy to scope down permissions when you perform a privileged
task on an AWS Organizations member account, or use any policy with access to
`iam:GetAccountSummary`.

To generate the root user credential
information report, other policies only need the
`iam:GetAccountSummary` action to produce the same output.
You can also list or get individual root user credential information,
including:

    + Whether a root user password is present
    + Whether a root user access key is present and when it was last
     used
    + Whether the root user has associated signing certificates
    + Root user associated MFA devices
    + List of the consolidated root user credential status

- You must manage your AWS accounts in [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md").
- You must have the following permissions to enable this feature in your
  organization:
  - `iam:EnableOrganizationsRootCredentialsManagement`
  - `iam:EnableOrganizationsRootSessions`
  - `iam:ListOrganizationsFeatures`
  - `organizations:EnableAwsServiceAccess`
  - `organizations:ListAccountsForParent`
  - `organizations:RegisterDelegatedAdministrator`

- To ensure optimal console functionality, we recommend enabling the following
  additional permissions:
  - `organizations:DescribeAccount`
  - `organizations:DescribeOrganization`
  - `organizations:ListAWSServiceAccessForOrganization`
  - `organizations:ListDelegatedAdministrators`
  - `organizations:ListOrganizationalUnitsForParent`
  - `organizations:ListParents`
  - `organizations:ListTagsForResource`

## Enabling centralized root access

(console)

###### To enable this feature for member accounts in the AWS Management Console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the console, choose **Root access
   management**, and then select **Enable**.

###### Note

If you see **Root access management is disabled**, enable
trusted access for AWS Identity and Access Management in AWS Organizations. For details, see [AWS IAM and AWS Organizations](../../../organizations/latest/userguide/services-that-can-integrate-iam.md "../../../organizations/latest/userguide/services-that-can-integrate-iam.md") in the _AWS Organizations User
Guide_. 3. In the Capabilities to enable section, choose which features to enable.

    * Select **Root credentials management** to allow the
     management account and the delegated administrator for IAM to delete
     root user credentials for member accounts. You must enable Privileged root
     actions in member accounts to allow member accounts to recover their
     root user credentials after they have been deleted.
    * Select **Privileged root actions in member accounts**
     to allow the management account and the delegated administrator for
     IAM to perform certain tasks that require root user credentials.

4. (Optional) Enter the account ID of the **Delegated
   administrator** that is authorized to manage root user access and take
   privileged actions on member accounts. We recommend an account that is intended
   for security or management purposes.
5. Choose **Enable**.

## Enabling centralized root access

(AWS CLI)

###### To enable centralized root access from the AWS Command Line Interface (AWS CLI)

1. If you haven't already enabled trusted access for AWS Identity and Access Management in AWS Organizations, use
   the following command: [aws organizations enable-aws-service-access](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/enable-aws-service-access.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/enable-aws-service-access.html").
2. Use the following command to allow the management account and the delegated
   administrator to delete root user credentials for member accounts: [aws iam enable-organizations-root-credentials-management](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/enable-organizations-root-credentials-management.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/enable-organizations-root-credentials-management.html").
3. Use the following command to allow the management account and the delegated
   administrator to perform certain tasks that require root user credentials: [aws iam enable-organizations-root-sessions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/enable-organizations-root-sessions.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/enable-organizations-root-sessions.html").
4. (Optional) Use the following command to register a delegated administrator:
   [aws organizations register-delegated-administrator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/register-delegated-administrator.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/register-delegated-administrator.html").

The following example assigns account 111111111111 as the delegated
administrator for the IAM service.

```
aws organizations register-delegated-administrator
--service-principal iam.amazonaws.com
--account-id `111111111111`

```

## Enabling centralized root access (AWS

API)

###### To enable centralized root access from the AWS API

1. If you haven't already enabled trusted access for AWS Identity and Access Management in AWS Organizations, use
   the following command: [EnableAWSServiceAccess](../../../organizations/latest/APIReference/API_EnableAWSServiceAccess.md "../../../organizations/latest/APIReference/API_EnableAWSServiceAccess.md").
2. Use the following command to allow the management account and the delegated
   administrator to delete root user credentials for member accounts: [EnableOrganizationsRootCredentialsManagement](../APIReference/API_EnableOrganizationsRootCredentialsManagement.md "../APIReference/API_EnableOrganizationsRootCredentialsManagement.md").
3. Use the following command to allow the management account and the delegated
   administrator to perform certain tasks that require root user credentials: [EnableOrganizationsRootSessions](../APIReference/API_EnableOrganizationsRootSessions.md "../APIReference/API_EnableOrganizationsRootSessions.md").
4. (Optional) Use the following command to register a delegated administrator:
   [RegisterDelegatedAdministrator](../../../organizations/latest/APIReference/API_RegisterDelegatedAdministrator.md "../../../organizations/latest/APIReference/API_RegisterDelegatedAdministrator.md").

## Next steps

Once you've centrally secured privileged credentials for the member accounts in your
organization, see [Perform a privileged
task](id_root-user-privileged-task.md "id_root-user-privileged-task.md") to take privileged actions on a member
account.
