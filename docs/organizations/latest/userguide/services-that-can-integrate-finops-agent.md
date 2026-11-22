

# AWS FinOps Agent and AWS Organizations

AWS FinOps Agent is an AI agent that answers cost questions, investigates cost anomalies, finds savings opportunities, and creates recurring cost reports.

When you use AWS FinOps Agent with AWS Organizations, one agent can analyze cost, usage, and resource data across the accounts in your organization through a read-only service-linked role. You can run the agent from a member account that you register as the delegated administrator.

For more information, see [Setting up organization-wide access and a delegated administrator](https://docs.aws.amazon.com/finops-agent/latest/userguide/setting-up-organization-access.html) in the *AWS FinOps Agent User Guide*.

Use the following information to help you integrate AWS FinOps Agent with AWS Organizations.



## Service-linked roles created when you enable integration
<a name="integrate-enable-slr-finops-agent"></a>

The following [service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) is automatically created in your organization's management account when you enable trusted access. This role allows AWS FinOps Agent to perform supported operations within your organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between AWS FinOps Agent and Organizations, or if you remove the member account from the organization.

For more information, see [Setting up organization-wide access and a delegated administrator](https://docs.aws.amazon.com/finops-agent/latest/userguide/setting-up-organization-access.html) in the *AWS FinOps Agent User Guide*.
+ `AWSServiceRoleForFinOpsAgent` – Allows AWS FinOps Agent to read cost, usage, and resource data in the accounts in your organization on your behalf.

## Service principals used by AWS FinOps Agent
<a name="integrate-enable-svcprin-finops-agent"></a>

The service-linked role in the previous section can be assumed only by the service principals authorized by the trust relationships defined for the role. The service-linked roles used by AWS FinOps Agent grant access to the following service principals:
+ `finops-agent.amazonaws.com`

## Enabling trusted access with AWS FinOps Agent
<a name="integrate-enable-ta-finops-agent"></a>

For information about the permissions needed to enable trusted access, see [Permissions required to enable trusted access](orgs_integrate_services.md#orgs_trusted_access_perms).

Granting trusted access lets AWS FinOps Agent create its service-linked role, `AWSServiceRoleForFinOpsAgent`, in the accounts in your organization and assume it to read data on your behalf. Through that role, the agent reads cost and usage data, AWS CloudTrail events, and Amazon CloudWatch metrics in each member account. It can't read CloudWatch Logs, and it can't create, change, or delete resources, apart from the Amazon EventBridge rules that AWS FinOps Agent manages for your configured workflows.

An organization-wide agent can read data for every account in the organization. You can't exclude individual accounts. Service-linked roles are not restricted by service control policies (SCPs).

You can only enable trusted access using AWS FinOps Agent.

**Important**  
You must enable organization-wide access from the AWS FinOps Agent console. Turning on trusted access directly in AWS Organizations, from the console, the AWS CLI, or an SDK, does not create the `AWSServiceRoleForFinOpsAgent` service-linked role and does not complete AWS FinOps Agent organization setup, so no organization-wide agent works.

Only an administrator in the Organizations management account can enable trusted access with AWS FinOps Agent. To enable trusted access from the AWS FinOps Agent console, see [Setting up organization-wide access and a delegated administrator](https://docs.aws.amazon.com/finops-agent/latest/userguide/setting-up-organization-access.html) in the *AWS FinOps Agent User Guide*.

## Disabling trusted access
<a name="integrate-disable-ta-finops-agent"></a>

For information about the permissions needed to disable trusted access, see [Permissions required to disable trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms).

You can only disable trusted access using the AWS FinOps Agent tools.

Only an administrator in the Organizations management account can disable AWS FinOps Agent organization-wide access, using the AWS FinOps Agent console. Disabling leaves the AWS Organizations trusted access configuration and the service-linked roles in place, and makes the organization's organization-wide agents inactive until access is restored. To disable organization-wide access, see [Setting up organization-wide access and a delegated administrator](https://docs.aws.amazon.com/finops-agent/latest/userguide/setting-up-organization-access.html) in the *AWS FinOps Agent User Guide*.

## Enabling a delegated administrator account for AWS FinOps Agent
<a name="integrate-enable-da-finops-agent"></a>

A registered delegated administrator account hosts organization-wide agents that read cost and usage data across the organization. This is the recommended setup, because it keeps day-to-day FinOps work out of the management account. AWS FinOps Agent supports one delegated administrator at a time. Organization-wide enablement and delegated administrator registration stay in the management account. For more information, see [Setting up organization-wide access and a delegated administrator](https://docs.aws.amazon.com/finops-agent/latest/userguide/setting-up-organization-access.html) in the *AWS FinOps Agent User Guide*.

**Minimum permissions**  
Only an administrator in the Organizations management account can configure a delegated administrator for AWS FinOps Agent.

You can register a delegated administrator account using the AWS FinOps Agent console, or by using the Organizations `RegisterDelegatedAdministrator` CLI or SDK operation.

------
#### [ AWS CLI, AWS API ]

You can register a delegated administrator account using the AWS CLI or one of the AWS SDKs:
+ AWS CLI: [register-delegated-administrator](https://docs.aws.amazon.com/cli/latest/reference/organizations/register-delegated-administrator.html)

  ```bash
  $ aws organizations register-delegated-administrator \
      --account-id {{ACCOUNT_ID}} \
      --service-principal finops-agent.amazonaws.com
  ```
+ AWS API: [RegisterDelegatedAdministrator](https://docs.aws.amazon.com/organizations/latest/APIReference/API_RegisterDelegatedAdministrator.html)

------

## Disabling a delegated administrator account for AWS FinOps Agent
<a name="integrate-disable-da-finops-agent"></a>

Only an administrator in the Organizations management account can remove a delegated administrator account for AWS FinOps Agent. You can remove a delegated administrator using the AWS FinOps Agent console, or by using the Organizations `DeregisterDelegatedAdministrator` CLI or SDK operation. Removing a delegated administrator makes its organization-wide agents inactive. To remove a delegated administrator using the AWS FinOps Agent console, see [Setting up organization-wide access and a delegated administrator](https://docs.aws.amazon.com/finops-agent/latest/userguide/setting-up-organization-access.html) in the *AWS FinOps Agent User Guide*.

------
#### [ AWS CLI, AWS API ]

You can remove a delegated administrator account using the AWS CLI or one of the AWS SDKs:
+ AWS CLI: [deregister-delegated-administrator](https://docs.aws.amazon.com/cli/latest/reference/organizations/deregister-delegated-administrator.html)

  ```bash
  $ aws organizations deregister-delegated-administrator \
      --account-id {{ACCOUNT_ID}} \
      --service-principal finops-agent.amazonaws.com
  ```
+ AWS API: [DeregisterDelegatedAdministrator](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.html)

------