

# AWS DevOps Agent and AWS Organizations

AWS DevOps Agent integrates with AWS Organizations so that a single Agent Space can investigate resources across multiple accounts in your organization. You choose an organizational unit (OU) or your organization root, and AWS DevOps Agent deploys an access role to each covered member account and adds it to the Agent Space as a secondary account, so the agent can investigate it.

To use the integration, you enable trusted access for both AWS DevOps Agent and AWS CloudFormation StackSets. Trusted access lets an AWS service perform tasks in your organization and its accounts on your behalf. For more information, see [Using AWS Organizations with other AWS services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) in the *AWS Organizations User Guide*. For setup instructions, see [Connecting your AWS Organization](configuring-integrations-and-knowledge-connecting-your-aws-organization.md).

## Roles that the integration uses
<a name="roles-that-the-integration-uses"></a>

Enabling trusted access doesn't create a service-linked role for AWS DevOps Agent. The integration uses the following IAM roles in your accounts.
+ **Service management role** – A role in the primary account, which is the account where you create the Agent Space. The primary account must be your management account or a delegated administrator account. We recommend using a delegated administrator account, following AWS Organizations best practices for minimizing use of the management account. The role has the `AIDevOpsOrganizationsAccessPolicy` AWS managed policy attached. AWS DevOps Agent uses it to read your organization structure and to manage its AWS CloudFormation stack sets. You create this role, or the AWS DevOps Agent console creates it for you. For the permissions in this policy, see [AIDevOpsOrganizationsAccessPolicy](aws-devops-agent-security-devops-agent-iam-permissions.html#aidevopsorganizationsaccesspolicy).
+ **Member account role** – For each organization association, AWS DevOps Agent uses CloudFormation StackSets to deploy one role to each covered member account. The role's name starts with `AIDevOpsAgentSpaceRole-`, and it has the `AIDevOpsAgentAccessPolicy` AWS managed policy attached. Your management account and the primary account don't get this role.

**Note**  
** Because the integration deploys roles through CloudFormation StackSets with service-managed permissions, CloudFormation StackSets creates its own service-linked roles in your organization: `AWSServiceRoleForCloudFormationStackSetsOrgAdmin` in the management account and `AWSServiceRoleForCloudFormationStackSetsOrgMember` in member accounts. CloudFormation StackSets owns and manages these roles. For more information, see [AWS CloudFormation StackSets and AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudformation.html) in the *AWS Organizations User Guide*.

## Service principals used by the integration
<a name="service-principals-used-by-the-integration"></a>
+ `aidevops.amazonaws.com` – The service principal for AWS DevOps Agent. You enable trusted access for this principal, and it's the only principal that the AWS DevOps Agent roles trust.
+ `member.org.stacksets.cloudformation.amazonaws.com` – The service principal for the integration between CloudFormation StackSets and AWS Organizations. Activating trusted access for CloudFormation StackSets enables it. If you use a delegated administrator, you also register that account with this principal. For more information, see [Enabling a delegated administrator for AWS DevOps Agent](#enabling-a-delegated-administrator-for-aws-devops-agent).

## Enabling trusted access with AWS DevOps Agent
<a name="enabling-trusted-access-with-aws-devops-agent"></a>

Only an administrator in the organization's management account can enable trusted access. For information about the permissions needed to enable trusted access, see [Permissions required to enable trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html#orgs_trusted_access_perms) in the *AWS Organizations User Guide*.

### Using the AWS DevOps Agent console
<a name="using-the-aws-devops-agent-console"></a>

To enable trusted access, do the following in the management account.

1. Open the AWS DevOps Agent console, and then choose **Agent spaces settings**.

1. In **Organizations trusted access and delegated admins**, select **AWS DevOps Agent**, and then choose **Enable**.

1. (Optional) Under **Delegated administrators**, choose the member accounts that you want to register as delegated administrators.

1. Choose **Enable trusted access**.

The console enables trusted access for both AWS DevOps Agent and AWS CloudFormation StackSets. It also registers each delegated administrator that you choose for both services.

### Using the AWS CLI
<a name="using-the-aws-cli"></a>

If `activate-organizations-access` or `describe-organizations-access` returns `Invalid choice`, your version of the AWS CLI doesn't support the command. Update the AWS CLI and try again.

To enable trusted access, run the following commands in the management account.

**Step 1.** Enable trusted access for AWS DevOps Agent.

```
aws organizations enable-aws-service-access \
    --service-principal aidevops.amazonaws.com
```

**Step 2.** Activate trusted access for CloudFormation StackSets. Use this command, not `enable-aws-service-access`, which doesn't create the service-linked roles that CloudFormation StackSets needs.

```
aws cloudformation activate-organizations-access
```

**Step 3.** Verify that both are enabled.

```
aws organizations list-aws-service-access-for-organization

aws cloudformation describe-organizations-access
```

The first command's output includes `aidevops.amazonaws.com` and `member.org.stacksets.cloudformation.amazonaws.com`. The second command returns a `Status` of `ENABLED`.

If you use an AWS SDK instead of the AWS CLI, steps 1 and 2 use the `EnableAWSServiceAccess` and `ActivateOrganizationsAccess` API operations.

## Disabling trusted access with AWS DevOps Agent
<a name="disabling-trusted-access-with-aws-devops-agent"></a>

Disabling trusted access stops AWS DevOps Agent from accessing the member accounts that your organization associations cover. It doesn't delete the roles or stack sets that were deployed. For information about the permissions needed to disable trusted access, see [Permissions required to disable trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html#orgs_trusted_access_disable_perms) in the *AWS Organizations User Guide*.

In the management account, run the following commands. If you registered a delegated administrator for AWS DevOps Agent, deregister it first. Otherwise, skip the first command. Replace `<DELEGATED_ADMIN_ACCOUNT_ID>` with the account ID of your delegated administrator account.

```
aws organizations deregister-delegated-administrator \
    --account-id <DELEGATED_ADMIN_ACCOUNT_ID> \
    --service-principal aidevops.amazonaws.com

aws organizations disable-aws-service-access \
    --service-principal aidevops.amazonaws.com
```

After you disable trusted access, the following happens:
+ **Access ends within 1 hour.** AWS DevOps Agent stops issuing new credentials within minutes. Credentials that it already issued stay valid until they expire, within 1 hour.
+ **Deployed resources stay.** The roles and stack sets remain in place, but AWS DevOps Agent doesn't use them.
+ **Re-enabling restores access.** If you enable trusted access again, and register your delegated administrator again if you use one, your organization associations recover on their own. You don't need to redeploy anything.

**Important**  
** Don't run `aws cloudformation deactivate-organizations-access` to stop AWS DevOps Agent. That command deactivates trusted access for CloudFormation StackSets across your entire organization and affects every stack set that uses service-managed permissions, not only the ones that AWS DevOps Agent uses.

To stop access immediately, or to remove the roles and stack sets that AWS DevOps Agent deployed, see [Stopping access](configuring-integrations-and-knowledge-connecting-your-aws-organization.html#stopping-access) and [Removing an organization association](configuring-integrations-and-knowledge-connecting-your-aws-organization.html#removing-an-organization-association). AWS DevOps Agent doesn't delete the service management role. You can delete it after removal is complete.

## Enabling a delegated administrator for AWS DevOps Agent
<a name="enabling-a-delegated-administrator-for-aws-devops-agent"></a>

You can create an Agent Space that uses your organization in the management account or in a delegated administrator account. Using a delegated administrator separates management of your organization from operation of AWS DevOps Agent.

The delegated administrator account must be registered for both AWS DevOps Agent and CloudFormation StackSets. First enable trusted access as described in [Enabling trusted access with AWS DevOps Agent](#enabling-trusted-access-with-aws-devops-agent). If you enabled trusted access in the console and chose delegated administrators there, they're already registered for both services, and you can skip the following commands.

**Important**  
** A CloudFormation StackSets delegated administrator has full permissions to deploy to every account in your organization. The management account can't limit those permissions to specific OUs or operations. Grant this registration only to accounts that you trust with that level of access. For more information, see [Register a delegated administrator member account](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html) in the *AWS CloudFormation User Guide*.

In the management account, run the following commands. Replace `<DELEGATED_ADMIN_ACCOUNT_ID>` with the account ID of your delegated administrator account.

```
aws organizations register-delegated-administrator \
    --account-id <DELEGATED_ADMIN_ACCOUNT_ID> \
    --service-principal aidevops.amazonaws.com

aws organizations register-delegated-administrator \
    --account-id <DELEGATED_ADMIN_ACCOUNT_ID> \
    --service-principal member.org.stacksets.cloudformation.amazonaws.com
```

**Note**  
** Stack sets that a delegated administrator creates are stored in the management account. CloudFormation StackSets and AWS DevOps Agent each support up to five delegated administrators per organization.

## Disabling a delegated administrator for AWS DevOps Agent
<a name="disabling-a-delegated-administrator-for-aws-devops-agent"></a>

To deregister the delegated administrator for AWS DevOps Agent, run the following command in the management account. Replace `<DELEGATED_ADMIN_ACCOUNT_ID>` with the account ID of your delegated administrator account.

```
aws organizations deregister-delegated-administrator \
    --account-id <DELEGATED_ADMIN_ACCOUNT_ID> \
    --service-principal aidevops.amazonaws.com
```

After you deregister the account, Agent Spaces in that account can no longer access your member accounts, and their organization associations change to `invalid`. If you register the account again, the associations recover on their own.

**Note**  
** This command doesn't deregister the account for CloudFormation StackSets. Other stack sets that this account manages might depend on that registration, and AWS DevOps Agent needs it to remove its stack sets. If you no longer need the registration, deregister it after removal of your organization associations is complete. For more information, see [Removing an organization association](configuring-integrations-and-knowledge-connecting-your-aws-organization.html#removing-an-organization-association). For deregistration instructions, see [Register a delegated administrator member account](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html) in the *AWS CloudFormation User Guide*.

## Limitations
<a name="limitations"></a>

The following limitations apply to organization mode:
+ You can't use [directed actions](working-with-devops-agent-working-with-directed-actions.html) in accounts that an organization association covers, because you can't register an elevated role for them. In those accounts, the agent uses read-only actions. Directed actions remain available in the primary account and for supported third-party integrations.
+ An Agent Space in organization mode can't also have individually connected secondary accounts. To switch it back to standalone mode, first remove all of its organization associations, including invalid ones.
+ If your Agent Space is in a delegated administrator account, the agent can't investigate resources in the management account.
+ Organization mode isn't available in the AWS GovCloud (US) Regions or the China Regions.
+ For quotas that apply to organization associations, see [Organization association quotas](configuring-integrations-and-knowledge-connecting-your-aws-organization.html#organization-association-quotas).