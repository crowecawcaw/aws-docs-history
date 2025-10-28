# AWS Backup and

AWS Organizations

AWS Backup is a service that allows you to manage and monitor the AWS Backup jobs in your
organization. Using AWS Backup, if you sign-in as a user in the organization's management
account, you can enable organization-wide backup protection and monitoring. It helps you to
achieve compliance by using [backup
policies](orgs_manage_policies_backup.md "orgs_manage_policies_backup.md") to centrally apply AWS Backup plans to resources across all of the accounts
in your organization. When you use both AWS Backup and AWS Organizations together, you can get the
following benefits:

**Protection**

You can [enable the backup
policy type](enable-policy-type.md "enable-policy-type.md") in your organization and then [create backup policies](orgs_policies_create.md "orgs_policies_create.md")
to attach to the organization's root, OUs, or accounts. A backup policy combines
an AWS Backup plan with the other details required to apply the plan automatically to
your accounts.Policies that are directly attached to an account are merged with
policies [inherited](orgs_manage_policies_inheritance_mgmt.md "orgs_manage_policies_inheritance_mgmt.md")
from the organization's root and any parent OUs to create an _[effective
policy](orgs_manage_policies_effective.md "orgs_manage_policies_effective.md")_ that applies to the account. The policy includes
the ID of an IAM role that has permissions to run AWS Backup on the resources in
your accounts. AWS Backup uses the IAM role to perform the backup on your behalf as
specified by the backup plan in the effective policy.

**Monitoring**

When you [enable
trusted access for AWS Backup](orgs_integrate_services.md#orgs_how-to-enable-disable-trusted-access "orgs_integrate_services.md#orgs_how-to-enable-disable-trusted-access") in your organization, you can use the AWS Backup
console to view details about the backup, restore, and copy jobs in any of the
accounts in your organization. For more information, see [Monitor your backup jobs](../../../aws-backup/latest/devguide/monitor-and-verify-protected-resources.md "../../../aws-backup/latest/devguide/monitor-and-verify-protected-resources.md") in the _AWS Backup Developer Guide_.

For more information about AWS Backup, see the _[AWS Backup Developer Guide](../../../aws-backup/latest/devguide.md "../../../aws-backup/latest/devguide.md")_.

Use the following information to help you integrate
AWS Backup with AWS Organizations.

## Enabling trusted access with

AWS Backup

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

You can enable trusted access using either the AWS Backup console or the AWS Organizations
console.

###### Important

We strongly recommend that whenever possible, you use the AWS Backup console or
tools to enable integration with Organizations. This lets AWS Backup perform any
configuration that it requires, such as creating resources needed by the service.
Proceed with these steps only if you can’t enable integration using the tools
provided by AWS Backup. For more information, see [this note](orgs_integrate_services.md#important-note-about-integration "orgs_integrate_services.md#important-note-about-integration").

If you enable trusted access by using the AWS Backup console or tools then you
don’t need to complete these steps.

To enabled trusted access using AWS Backup, see [Enabling backup in multiple AWS accounts](../../../aws-backup/latest/devguide/manage-cross-account.md#enable-xaccount-management "../../../aws-backup/latest/devguide/manage-cross-account.md#enable-xaccount-management") in the _AWS Backup Developer Guide_.

## Disabling trusted access with

AWS Backup

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

AWS Backup requires trusted access with AWS Organizations to enable monitoring of backup, restore,
and copy jobs across your organization's accounts. If you disable trusted access AWS Backup,
you lose the ability to view jobs outside of the current account. The AWS Backup role that
AWS Backup creates remains. If you later re-enable trusted access, AWS Backup continues to operate
as before, without the need for you to reconfigure the service.

You can only disable trusted access using the Organizations
tools.

You can disable trusted access by running a Organizations AWS CLI command, or by
calling an Organizations API operation in one of the AWS SDKs.

AWS CLI, AWS API

###### To disable trusted service access using the Organizations CLI/SDK

Use the following AWS CLI commands or API operations to disable
trusted service access:

- AWS CLI: [disable-aws-service-access](../../../cli/latest/reference/organizations/disable-aws-service-access.md "../../../cli/latest/reference/organizations/disable-aws-service-access.md")

Run the following command to disable AWS Backup as a
trusted service with Organizations.

```
`$` **aws organizations disable-aws-service-access \
 --service-principal backup.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [DisableAWSServiceAccess](../APIReference/API_DisableAWSServiceAccess.md "../APIReference/API_DisableAWSServiceAccess.md")

## Enabling a delegated administrator

account for AWS Backup

See [Delegated administrator](../../../aws-backup/latest/devguide/manage-cross-account.md#backup-delegatedadmin "../../../aws-backup/latest/devguide/manage-cross-account.md#backup-delegatedadmin") in the _AWS Backup Developer Guide_.
