

AWS FinOps Agent is in preview release and is subject to change.

# Setting up organization-wide access and a delegated administrator

Use organization-wide access to give an agent access to cost and usage data across the accounts in your AWS organization. The organization management account enables this access. You can then create organization-wide agents in a registered delegated administrator account or in the management account.

Enabling organization-wide access creates the AWS FinOps Agent service-linked role, `AWSServiceRoleForFinOpsAgent`, and enables trusted access with AWS Organizations. AWS FinOps Agent uses the role to read data across your organization and includes new accounts as they are added. Organization-wide agents use this role instead of a customer-created agent role. They still need an operator role for web application operations.

The service-linked role primarily reads cost, usage, and resource data in each member account, including AWS CloudTrail events, Amazon CloudWatch metrics, and CloudWatch Logs configuration. It can't read CloudWatch log events. The role can also start cost analyses, run or cancel read-only Data Hub queries, and create and manage the EventBridge rules that AWS FinOps Agent owns. It can't change your other resources.

Owners of member accounts don't need to do anything. New accounts are included automatically as they join the organization. An organization-wide agent can read data for every account in the organization; you can't exclude individual accounts. To limit an agent to one account, create an account-scoped agent instead.

**Note**  
Service-linked roles are not restricted by service control policies (SCPs). Review the service-linked role permissions described in the setup wizard before enabling organization-wide access. For more information, see [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the AWS Organizations User Guide.

**Note**  
Everyone who can use an organization-wide agent can read data for every member account in the organization. This includes organization-wide cost and billing data and each member account's operational data.

## What you see in each account
<a name="setting-up-organization-account-scenarios"></a>

The signed-in account determines the organization controls and create actions available in the console. Delegated administrator registration applies only to AWS FinOps Agent; registering as a delegated administrator for another service doesn't grant this access. The following table describes the organization setup and agent creation actions available in each account.


**Organization setup and agent creation by account**  

| Signed-in account | Organization setup | Agent creation | 
| --- | --- | --- | 
| Management account | Enable organization-wide access and register, move, or deregister the delegated administrator from Settings, AWS Organizations enablement. | Before setup, create an account-scoped agent or choose Set up organization-wide access. After setup, if no delegated administrator is registered, choose Create org-wide agent. If one is registered, choose Create agent via delegated administrator account to switch accounts. | 
| Registered delegated administrator account | View the organization's access status. The management account controls organization-wide enablement and delegated administrator registration. | When organization-wide access is enabled, choose Create org-wide agent. The create menu also offers Create agent for this account for an account-scoped agent. | 
| Member account that is not the delegated administrator | The AWS Organizations enablement tab and organization scope controls are not shown. | Choose Create agent to create an account-scoped agent. Ask the management account administrator to register this account if it should host organization-wide agents. | 

Registration does not grant a person permission to sign in to the delegated administrator account. Your IAM administrator must separately grant access to an appropriate role in that account.

## Prerequisites
<a name="setting-up-organization-prerequisites"></a>
+ Access to the AWS FinOps Agent console in the US East (N. Virginia) Region, where organization setup and organization-wide agents run.
+ An AWS organization with all features enabled. An organization that uses only consolidated billing must enable all features before enabling trusted access.
+ A signed-in IAM identity in the management account with the permissions in [Permissions for organization setup](#setting-up-organization-permissions).
+ If you use a delegated administrator, an active member account in the same organization and a role you can use to sign in to it. AWS FinOps Agent supports one delegated administrator at a time.
+ Permissions to create and manage agents in the account that hosts them. Organization setup supplements the [administrator setup policy](setting-up.md#setting-up-administrator-policy); it does not replace agent creation permissions or the [operator role permissions](setting-up.md#setting-up-operator-policy).

## Permissions for organization setup
<a name="setting-up-organization-permissions"></a>

Attach the following supplemental policy to the management account administrator's IAM identity. With this policy, you can use the console to read organization status, enable AWS FinOps Agent organization-wide access, create its service-linked role, and manage its delegated administrator. Replace {{111122223333}} with your management account ID, {{o-exampleorgid}} with your organization ID, and {{444455556666}} with the member account you intend to register.

```json
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "FinOpsAgentOrganizationAccess",
      "Effect": "Allow",
      "Action": [
        "finops-agent:GetOrganizationAccess",
        "finops-agent:UpdateOrganizationAccess"
      ],
      "Resource": "*"
    },
    {
      "Sid": "ReadOrganizationSetup",
      "Effect": "Allow",
      "Action": [
        "organizations:ListAccounts",
        "organizations:ListAWSServiceAccessForOrganization",
        "organizations:ListDelegatedAdministrators"
      ],
      "Resource": "*"
    },
    {
      "Sid": "EnableFinOpsAgentTrustedAccess",
      "Effect": "Allow",
      "Action": "organizations:EnableAWSServiceAccess",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "organizations:ServicePrincipal": "finops-agent.amazonaws.com"
        }
      }
    },
    {
      "Sid": "ManageFinOpsAgentDelegatedAdministrator",
      "Effect": "Allow",
      "Action": [
        "organizations:RegisterDelegatedAdministrator",
        "organizations:DeregisterDelegatedAdministrator"
      ],
      "Resource": "arn:aws:organizations::111122223333:account/o-exampleorgid/444455556666",
      "Condition": {
        "StringEquals": {
          "organizations:ServicePrincipal": "finops-agent.amazonaws.com"
        }
      }
    },
    {
      "Sid": "CreateFinOpsAgentServiceLinkedRole",
      "Effect": "Allow",
      "Action": "iam:CreateServiceLinkedRole",
      "Resource": "arn:aws:iam::111122223333:role/aws-service-role/finops-agent.amazonaws.com/AWSServiceRoleForFinOpsAgent",
      "Condition": {
        "StringEquals": {
          "iam:AWSServiceName": "finops-agent.amazonaws.com"
        }
      }
    }
  ]
}
```

The organization status and list operations use `Resource: "*"` because they apply to organization-wide configuration or return a list. The delegated administrator statement limits registration changes to the specified member account. To move a registration, include both the current and replacement member account ARNs in that statement's `Resource` array.

Console users in delegated administrator and ordinary member accounts need `finops-agent:GetOrganizationAccess` with `Resource: "*"` for the console's organization status check. A delegated administrator also needs `organizations:ListAWSServiceAccessForOrganization` to display trusted access. Grant agent administration permissions separately. Organization enablement is available only in the management account.

For more information about creating service-linked roles, see [Create a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html) in the IAM User Guide.

## Enabling access from the management account
<a name="setting-up-organization-enable"></a>

1. Sign in to the management account, open the AWS FinOps Agent console, and select the US East (N. Virginia) Region.

1. On the **Agents** page, choose **Set up organization-wide access**. You can also open **Settings**, choose **AWS Organizations enablement**, and choose **Enable organization-wide access**.

1. In **Enable organization-wide access**, review the service-linked role permissions and the notice about SCPs. Choose **Next**.

1. In **Choose a delegated administrator**, select **Delegated administrator account** and choose a member account. This is the recommended option, because it keeps day-to-day FinOps work out of the management account, the most sensitive account in your organization. To host organization-wide agents in the management account instead, select **Management account**. Choose **Next**.

1. In **Review and finish**, review the trusted access and service-linked role status and the account where the agent runs. Choose **Finish setup**.

1. Wait for the success notification. Deploying the role usually takes several minutes and can take up to 24 hours for a large organization. If setup fails, resolve the displayed permission or organization configuration error and choose **Finish setup** again to resume.

**Note**  
Enable organization-wide access through the AWS FinOps Agent console. Turning on trusted access directly in AWS Organizations does not complete AWS FinOps Agent organization setup.

## Creating an organization-wide agent
<a name="setting-up-organization-create-agent"></a>

1. Sign in to the registered delegated administrator account. If you are still in the management account, choose **Create agent via delegated administrator account**, then **Continue to switch role**. The AWS Switch Role page opens in a new tab. Check the target account and role name, then choose **Switch Role**.

1. On the **Agents** page in the delegated administrator account, choose **Create org-wide agent**. If you chose the management account during setup and have not registered a delegated administrator, this action is available in the management account.

1. Name the agent and configure its operator role in **Give the web app access to your agent**. The organization-wide creation flow skips the customer agent role step because data access uses `AWSServiceRoleForFinOpsAgent`. Do not pass the service-linked role as an agent role.

1. Optionally select **Use Data Hub for this agent**. An organization-wide agent reads a Data Hub dataset created in the management account, which covers every account in the organization. For the management account steps, see [Set up the management account for organization-wide agents](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/setup-trusted.html) in the *AWS Billing User Guide*.

1. Optionally connect Jira and Slack in **Third-party integrations**. Review the settings and create the agent.

1. Confirm that the agent has organization scope in the console. Open its web application and ask a cost question that covers the organization.

To create an account-scoped agent in a management or delegated administrator account, open the menu beside **Create org-wide agent** and choose **Create agent for this account**. This flow uses a customer-created agent role.

## Changing organization access
<a name="setting-up-organization-change-access"></a>

From the management account, open **Settings**, **AWS Organizations enablement** to register a delegated administrator later, move the registration to another member account, or deregister the current account. Moving registration removes the old account's delegated administrator privileges before registering the replacement. Existing agents and their data are not moved or deleted.

Disabling organization-wide access or removing an account's delegated administrator status makes its organization-wide agents inactive. You can still open their past conversations, context files, and artifacts. Their automations are canceled, and they can't start new conversations in the web application until organization access is restored. The agents keep their organization scope and don't fall back to account scope.

The console action **Disable trusted access** disables AWS FinOps Agent organization-wide access. It leaves the AWS Organizations trusted access configuration and service-linked roles in place. Re-enable access from the management account to restore eligible organization-wide agents.