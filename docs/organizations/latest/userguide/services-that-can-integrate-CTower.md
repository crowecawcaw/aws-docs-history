# AWS Control Tower and

AWS Organizations

AWS Control Tower offers a straightforward way to set up and govern an AWS multi-account environment, following prescriptive best practices.
AWS Control Tower orchestration extends the capabilities of AWS Organizations. AWS Control Tower applies preventive and detective controls (guardrails) to help keep your organizations and accounts from divergence from best practices (drift).

AWS Control Tower orchestration extends the capabilities of AWS Organizations.

For more information, see [the _AWS Control Tower user guide_](../../../controltower/latest/userguide.md "../../../controltower/latest/userguide.md").

Use the following information to help you integrate
AWS Control Tower with AWS Organizations.

## Roles needed for integration

The `AWSControlTowerExecution` role must be present in all enrolled accounts. It allows AWS Control Tower to manage your individual accounts and report
information about them to your Audit and Log Archive accounts.

To learn more about roles used by AWS Control Tower, see [How AWS Control Tower works with roles to create and manage accounts](../../../controltower/latest/userguide/roles-how.md "../../../controltower/latest/userguide/roles-how.md")
and [Using Identity-Based Policies (IAM Policies) for AWS Control Tower](../../../controltower/latest/userguide/access-control-managing-permissions.md "../../../controltower/latest/userguide/access-control-managing-permissions.md").

## Service principals used by AWS Control Tower

AWS Control Tower uses the `controltower.amazonaws.com` service principal.

## Enabling trusted access with

AWS Control Tower

AWS Control Tower uses trusted access to detect drift for preventive controls, and to track account and OU changes that cause drift.

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

You can only enable trusted access using the Organizations
tools.

To enable trusted access from the Organizations console, choose `Enable access` next to **AWS Control Tower**.

You can enable trusted access by running a Organizations AWS CLI command, or by
calling an Organizations API operation in one of the AWS SDKs.

AWS CLI, AWS API

###### To enable trusted service access using the Organizations CLI/SDK

Use the following AWS CLI commands or API operations to enable
trusted service access:

- AWS CLI: [enable-aws-service-access](../../../cli/latest/reference/organizations/enable-aws-service-access.md "../../../cli/latest/reference/organizations/enable-aws-service-access.md")

Run the following command to enable AWS Control Tower as a
trusted service with Organizations.

```
`$` **aws organizations enable-aws-service-access \
 --service-principal controltower.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md")

## Disabling trusted access with

AWS Control Tower

For information about the permissions needed to disable trusted
access, see [Permissions required to disable
trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms "orgs_integrate_services.md#orgs_trusted_access_disable_perms").

You can only disable trusted access using the Organizations
tools.

###### Important

Disabling AWS Control Tower's trusted access causes drift in
your AWS Control Tower Landing Zone. The only way to fix the drift is to use
AWS Control Tower's Landing Zone repair. Re-enabling trusted access in Organizations does not fix the drift. [Learn more about drift](../../../controltower/latest/userguide/drift.md "../../../controltower/latest/userguide/drift.md") in the _AWS Control Tower user guide_.

You can disable trusted access by running a Organizations AWS CLI command, or by
calling an Organizations API operation in one of the AWS SDKs.

AWS CLI, AWS API

###### To disable trusted service access using the Organizations CLI/SDK

Use the following AWS CLI commands or API operations to disable
trusted service access:

- AWS CLI: [disable-aws-service-access](../../../cli/latest/reference/organizations/disable-aws-service-access.md "../../../cli/latest/reference/organizations/disable-aws-service-access.md")

Run the following command to disable AWS Control Tower as a
trusted service with Organizations.

```
`$` **aws organizations disable-aws-service-access \
 --service-principal controltower.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [DisableAWSServiceAccess](../APIReference/API_DisableAWSServiceAccess.md "../APIReference/API_DisableAWSServiceAccess.md")
