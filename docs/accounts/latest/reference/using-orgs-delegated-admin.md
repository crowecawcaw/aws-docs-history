# Enable a delegated admin account for

AWS Account Management

You enable a delegated admin account so you can call the AWS Account Management API operations for
other member accounts in AWS Organizations. After you register a delegated admin account for your
organization, users and roles in that account can call the AWS CLI and AWS SDK operations in
the `account` namespace that can work in the Organizations mode by supporting an optional
`AccountId` parameter.

To register a member account in your organization as a delegated admin account, use the
following procedure.

AWS CLI & SDKs

###### To register a delegated admin account for the Account Management service

You can use the following commands to enable a delegated admin for the
Account Management service.

###### Minimum permissions

To perform these tasks, you must meet the following requirements:

- You can perform this only from the organization's
  management account.
- Your organization must have [all features enabled](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md").
- You must have [enabled
  trusted access for Account Management in your organization](using-orgs-trusted-access.md "using-orgs-trusted-access.md").

You must specify the following service principal:

```
account.amazonaws.com
```

- AWS CLI: [register-delegated-administrator](../../../cli/latest/reference/organizations/register-delegated-administrator.md "../../../cli/latest/reference/organizations/register-delegated-administrator.md")

The following example registers a member account of the organization
as a delegated admin for the Account Management service.

```
`$` `aws organizations register-delegated-administrator \
 --account-id 123456789012 \
 --service-principal account.amazonaws.com`
```

This command produces no output if it's successful.

After you run this command, you can use credentials from account
123456789012 to call Account Management AWS CLI and SDK API operations that
use the `--account-id` parameter to reference member accounts
in an organization.

AWS Management ConsoleThis task isn't supported in the AWS Account Management management console. You
can perform this task only by using the AWS CLI or an API operation from one of the AWS SDKs.
