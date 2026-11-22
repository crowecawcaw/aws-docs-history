

# Connecting your AWS Organization

An *organization association* gives AWS DevOps Agent access to the accounts in all or part of your organization in AWS Organizations. You don't connect accounts one at a time. Instead, you choose an organizational unit (OU) or your organization root, and AWS DevOps Agent deploys and maintains an access role in each covered account. When an account joins a covered OU later, AWS DevOps Agent covers it automatically if the association covers the whole OU. When an account moves out of a covered OU, AWS DevOps Agent stops using it and removes its role.

This topic describes the prerequisites, what AWS DevOps Agent deploys in your accounts, how deployment works, how to change or stop access, and the quotas that apply. For limitations that apply to organization mode, see [Limitations](configuring-integrations-and-knowledge-aws-devops-agent-and-aws-organizations.html#limitations).

## Prerequisites
<a name="prerequisites"></a>

### Organization setup
<a name="organization-setup"></a>

Before you start, make sure that your organization meets the following requirements. An administrator of the management account sets these up.
+ **All features are enabled in your organization.** Consolidated billing alone isn't sufficient. For more information, see [Enabling all features for an organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html) in the *AWS Organizations User Guide*.
+ **The Agent Space is in the management account or a delegated administrator account.** The account where you create the Agent Space is the *primary account*. If you use a delegated administrator, the account must be registered for both `aidevops.amazonaws.com` and `member.org.stacksets.cloudformation.amazonaws.com`. For instructions, see [Enabling a delegated administrator for AWS DevOps Agent](configuring-integrations-and-knowledge-aws-devops-agent-and-aws-organizations.html#enabling-a-delegated-administrator-for-aws-devops-agent).
+ **Trusted access is enabled for AWS DevOps Agent and activated for AWS CloudFormation StackSets.** For instructions, see [Enabling trusted access with AWS DevOps Agent](configuring-integrations-and-knowledge-aws-devops-agent-and-aws-organizations.html#enabling-trusted-access-with-aws-devops-agent).

### Agent Space and roles
<a name="agent-space-and-roles"></a>

The Agent Space must be in an AWS Region where AWS DevOps Agent is available. Organization mode isn't available in the AWS GovCloud (US) Regions or the China Regions. For the list of Regions, see [Supported Regions](about-aws-devops-agent-supported-regions.md).

You also need the following resources. If you don't have them yet, the procedure in [Creating an organization association](#creating-an-organization-association) creates them.
+ **An Agent Space in organization mode.** Set organization mode when you create the Agent Space. You can also switch an existing Agent Space to organization mode, but not while it has secondary accounts connected.
+ **A primary account role.** This role gives the agent access to AWS resources in the primary account. Its trust policy includes an `aws:SourceArn` or `aws:SourceAccount` condition. The primary account role doesn't need CloudFormation StackSets or AWS Organizations permissions.
+ **A service management role.** This role is in the primary account and has the `AIDevOpsOrganizationsAccessPolicy` AWS managed policy attached. Its trust policy needs an `aws:SourceAccount` or `aws:SourceArn` condition. AWS DevOps Agent uses this role for the AWS Organizations and CloudFormation StackSets operations that it runs on your behalf. The console can create the role for you, or you can create it yourself and register it as `serviceManagementRoleArn` on the association for the primary account.

Register this role before you create your first organization association, and keep it until removal of your organization associations is complete.

### Permissions for the caller
<a name="permissions-for-the-caller"></a>

The principal that creates the Agent Space in organization mode, or creates or updates an organization association, needs the following permissions:
+ AWS DevOps Agent permissions, and `iam:PassRole` for the primary account role and the service management role. The principal that makes the request, such as your console user or the role that runs your AWS CLI commands, needs this permission so that it can register those roles with the Agent Space. For the required policy, see [Required permissions in your primary account](configuring-integrations-and-knowledge-connecting-multiple-aws-accounts.html#required-permissions-in-your-primary-account).
+ The following AWS Organizations permissions. AWS DevOps Agent uses them to check the prerequisites when you make the request.
  + `organizations:DescribeOrganization`
  + `organizations:ListAWSServiceAccessForOrganization`
  + `organizations:DescribeOrganizationalUnit`, or `organizations:ListRoots` when you cover the root
  + `organizations:ListDelegatedServicesForAccount`, in a delegated administrator account only

### Verify your prerequisites
<a name="verify-your-prerequisites"></a>

Use the following commands to check the organization setup.

Most of these commands require credentials for the management account or a delegated administrator account. From a member account, the AWS Organizations commands return `AccessDeniedException` and the CloudFormation command returns a validation error. The exception is `describe-organization`, which any account in the organization can run. If you don't have access to the management account, send this checklist to your organization administrator.

```
# All features enabled: FeatureSet is ALL.
# Any account in the organization can run this command.
aws organizations describe-organization

# Trusted access for AWS DevOps Agent: the output lists aidevops.amazonaws.com.
aws organizations list-aws-service-access-for-organization

# Trusted access for CloudFormation StackSets: Status is ENABLED.
# In a delegated administrator account, add --call-as DELEGATED_ADMIN.
aws cloudformation describe-organizations-access

# Delegated administrator (if you use one): the output lists aidevops.amazonaws.com
# and member.org.stacksets.cloudformation.amazonaws.com.
# Replace <ACCOUNT_ID> with the ID of the primary account.
aws organizations list-delegated-services-for-account --account-id <ACCOUNT_ID>
```

If `describe-organizations-access` returns `Invalid choice`, your version of the AWS CLI doesn't support the command. Update the AWS CLI and try again.

## Organization association scope
<a name="organization-association-scope"></a>

Each organization association covers one OU or your organization root. Coverage includes the accounts in all nested child OUs. The OU must already exist, and an Agent Space can have only one association for each OU. In the console, you can select several OUs at once. The console creates one organization association for each OU and shows how many your selection uses.

An association can cover either of the following:
+ **Every account in the OU**, including accounts that join the OU later.
+ **A list of specific accounts in the OU**, up to 1,000 accounts per association. AWS DevOps Agent covers only the listed accounts that are under the OU.

## What AWS DevOps Agent deploys in your accounts
<a name="what-aws-devops-agent-deploys-in-your-accounts"></a>

For each organization association, AWS DevOps Agent creates a CloudFormation stack set named `AIDevOpsOrgSource-<ASSOCIATION_ID>`. The stack set deploys one AWS Identity and Access Management (IAM) role to each covered account. The role's name starts with `AIDevOpsAgentSpaceRole-`. The role has the following characteristics:
+ Its trust policy allows only AWS DevOps Agent to assume the role.
+ It has the `AIDevOpsAgentAccessPolicy` AWS managed policy attached. It also has an inline policy, `AllowCreateServiceLinkedRoles`, that allows creating the AWS Resource Explorer service-linked role in the account.
+ AWS CloudTrail logs the agent's API calls in each member account as sessions of this role.

The following accounts never receive the role, and they don't count against your quotas:
+ **The management account.** CloudFormation StackSets doesn't deploy stack instances to the management account.
+ **The primary account.** The agent accesses this account directly through the primary account role. If this account is in a covered OU, it gets an empty stack from the stack set, with no role in it.

An Agent Space in organization mode accesses only the primary account and the accounts that its organization associations cover. You can't also connect individual secondary accounts to it, as described in [Connecting multiple AWS Accounts](configuring-integrations-and-knowledge-connecting-multiple-aws-accounts.md). As a result, if your Agent Space is in a delegated administrator account, the agent can't investigate resources in your management account, because the management account never receives the role.

**Important**  
** AWS DevOps Agent manages the stack set, its stack instances, and the deployed roles. Don't modify or delete them. For more information, see [Actions to avoid during deployment](#actions-to-avoid-during-deployment).

## Creating an organization association
<a name="creating-an-organization-association"></a>

You can create an organization association by using the AWS DevOps Agent console or the AWS CLI.

### Using the AWS DevOps Agent console
<a name="using-the-aws-devops-agent-console"></a>

If trusted access isn't enabled yet, an administrator of the management account must enable it first. For instructions, see [Enabling trusted access with AWS DevOps Agent](configuring-integrations-and-knowledge-aws-devops-agent-and-aws-organizations.html#enabling-trusted-access-with-aws-devops-agent).

To create an organization association, do the following in the primary account, which is your management account or a delegated administrator account.

**Step 1.** In the AWS DevOps Agent console, choose **Agent spaces**, and then choose **Create agent space**.

**Step 2.** On the **Agent space properties** page, enter a name for the Agent Space. Optionally, add a description and tags. Then choose **Next**.

![Agent space details section with an Agent Space name and description entered.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/org-association-console-agent-space-details.png)


**Step 3.** On the **Agent scope** page, for **Account scope**, choose **Organization**.

![Account scope options with Organization selected.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/org-association-console-account-scope.png)


**Step 4.** Under **Organizational units and accounts**, select what the agent can access:
+ To cover every account in an OU, including accounts added later, select the OU.
+ To cover only specific accounts, select those accounts.

The console shows how many organization associations your selection uses.

![Organizational units and accounts table with two OUs and one account selected.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/org-association-console-organizational-units.png)


**Step 5.** Under **Service management role**, choose one of the following options:
+ **Auto-create a new DevOps Agent service management role** – The console creates the role and shows its name.
+ **Assign an existing role** – Choose a role that you created.
+ **Create a new DevOps Agent service management role using a policy template** – Create the role in the IAM console by using the details that the console provides.

![Service management role options with the auto-create option selected and the name of the role that the console creates.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/org-association-console-service-management-role.png)


**Step 6.** Under **AWS resource access**, for **Primary account role**, choose one of the same three options for the primary account role.

![Primary account role options with the auto-create option selected.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/org-association-console-primary-account-role.png)


**Step 7.** Choose **Next**. On the optional **Additional configuration** page, you can change the content safety guardrail and choose a customer managed key for encryption. For more information, see [Configuring the content safety guardrail](getting-started-with-aws-devops-agent-creating-an-agent-space.html#configuring-the-content-safety-guardrail-optional) and [Customer managed keys](aws-devops-agent-security-encryption-at-rest-for-devops-agent.html#customer-managed-keys). Then choose **Next**.

**Step 8.** On the **Review and create** page, check the **Agent scope** section, and then choose **Create agent space**.

![Agent scope section of the Review and create page, with the organization scope, service management role, and primary account role.](https://docs.aws.amazon.com/devopsagent/latest/userguide/images/org-association-console-review-agent-scope.png)


After the Agent Space is created, the console opens its page. On the **Capabilities** tab, in the **Cloud** section, the **Multi-account organizational units and accounts** table lists each organization association and its status. The status is **Pending** while deployment runs. For more information, see [Deployment timing and status](#deployment-timing-and-status). To change coverage later, choose **Edit scope**.

### Using the AWS CLI
<a name="using-the-aws-cli"></a>

Unless a step says otherwise, run the commands in the primary account, which is your management account or your delegated administrator account. Replace the following placeholders with your own values:
+ `<REGION>` – The Region of the Agent Space.
+ `<ACCOUNT_ID>` – The ID of the primary account.
+ `<AGENT_SPACE_ID>` – The ID of the Agent Space.
+ `<ASSOCIATION_ID>` – The ID of the association.
+ `<OU_ID>` – The ID of the OU to cover.
+ `<ROOT_ID>` – The ID of your organization root.
+ `<SUFFIX>` – A short random string that makes the service management role's name unique.

To create an organization association, run the following commands.

**Step 1.** Create an Agent Space in organization mode.

```
aws devops-agent create-agent-space \
    --name "MyOrgAgentSpace" \
    --aws-source-mode organization \
    --region <REGION>
```

Save the Agent Space ID, which is in the `agentSpace.agentSpaceId` field of the response. To print only the ID, add `--query 'agentSpace.agentSpaceId' --output text` to the command.

**Step 2.** Create the primary account role and the service management role in the primary account.

**Step 2a.** Save the following trust policy as `trust.json`. The service management role uses this trust policy.

```
{
  "Version": "2012-10-17",		 	 	 		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "Service": "aidevops.amazonaws.com" },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "<ACCOUNT_ID>",
          "aws:SourceArn": "arn:aws:aidevops:<REGION>:<ACCOUNT_ID>:agentspace/<AGENT_SPACE_ID>"
        }
      }
    }
  ]
}
```

The `aws:SourceArn` value is the ARN of the Agent Space. The `create-agent-space` response doesn't include the ARN, so build it from the Agent Space ID. This example uses both conditions for least privilege. You can use only `aws:SourceAccount` instead.

**Step 2b.** Create the primary account role, `DevOpsAgentRole-AgentSpace`, by following [Create the DevOps Agent space role](getting-started-with-aws-devops-agent-cli-onboarding-guide.html#1-create-the-devops-agent-space-role) in the CLI onboarding guide. That procedure attaches the `AIDevOpsAgentAccessPolicy` managed policy and the `AllowCreateServiceLinkedRoles` inline policy, which lets the agent create the AWS Resource Explorer service-linked role in the primary account.

**Step 2c.** Create the service management role and attach the `AIDevOpsOrganizationsAccessPolicy` managed policy. Don't attach any other policies to this role.

```
aws iam create-role \
    --role-name DevOpsAgentRole-ServiceManagement-<SUFFIX> \
    --assume-role-policy-document file://trust.json

aws iam attach-role-policy \
    --role-name DevOpsAgentRole-ServiceManagement-<SUFFIX> \
    --policy-arn arn:aws:iam::aws:policy/AIDevOpsOrganizationsAccessPolicy
```

**Step 3.** Associate the primary account and register both roles. In the configuration, `accountType` is `monitor`, which is the API value for the primary account.

The principal that runs this command needs AWS DevOps Agent permissions and `iam:PassRole` permission with the `iam:PassedToService` condition set to `aidevops.amazonaws.com`. For the required policy, see [Required permissions in your primary account](configuring-integrations-and-knowledge-connecting-multiple-aws-accounts.html#required-permissions-in-your-primary-account).

```
aws devops-agent associate-service \
    --agent-space-id <AGENT_SPACE_ID> \
    --service-id aws \
    --configuration '{
      "aws": {
        "accountId": "<ACCOUNT_ID>",
        "accountType": "monitor",
        "assumableRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/DevOpsAgentRole-AgentSpace",
        "serviceManagementRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/DevOpsAgentRole-ServiceManagement-<SUFFIX>"
      }
    }' \
    --region <REGION>
```

**Important**  
** `update-association` replaces the whole configuration. When you update this association later, include `serviceManagementRoleArn` every time.

**Step 4.** Find the ID of the OU or root that you want to cover. Run these commands in the management account or a delegated administrator account.

```
# Get the organization root ID (r-*).
aws organizations list-roots

# List the OUs directly under the root.
# To list nested OUs, run the command again with an OU ID as the parent.
aws organizations list-organizational-units-for-parent \
    --parent-id <ROOT_ID>
```

**Step 5.** Create the organization association. The following example covers every account in an OU.

```
aws devops-agent associate-service \
    --agent-space-id <AGENT_SPACE_ID> \
    --service-id aws \
    --configuration '{
      "sourceAwsOrg": {
        "accountType": "source",
        "organizationalUnit": {
          "organizationalUnitId": "<OU_ID>"
        }
      }
    }' \
    --region <REGION>
```

To change the scope, modify `organizationalUnit` as follows:
+ **To cover specific accounts**, add `accountIds` with 1–1,000 account IDs. For example: `"organizationalUnit": {"organizationalUnitId": "<OU_ID>", "accountIds": ["111111111111", "222222222222"]}`
+ **To cover your entire organization**, set `organizationalUnitId` to your root ID (`r-*`).

Save the `associationId` from the response.

**Step 6.** Track the deployment. The `status`, `statusReason`, and `deploymentState` fields in the response report progress. `deploymentState` is inside the association's `sourceAwsOrg` configuration. For more information, see [Deployment timing and status](#deployment-timing-and-status).

```
aws devops-agent get-association \
    --agent-space-id <AGENT_SPACE_ID> \
    --association-id <ASSOCIATION_ID> \
    --region <REGION>
```

## Deployment timing and status
<a name="deployment-timing-and-status"></a>

After you create an association, deployment runs in the background:
+ **Status** – The association has a status of `pending-confirmation` while it deploys. The status changes to `valid` when deployment finishes, even if some accounts failed. If deployment fails in every account, the status changes to `invalid`, and `statusReason` explains why. AWS DevOps Agent doesn't retry this on its own.
+ **Availability** – The agent can use your accounts when the association status is `valid`. AWS DevOps Agent automatically adds accounts that finish deploying after that point.
+ **Duration** – In large organizations, deployment can take many hours because CloudFormation deploys to accounts in batches.
+ **Failures** – If deployment fails in one account, it continues in the other accounts.
+ **New accounts** – When an account joins or moves into a covered OU, AWS DevOps Agent detects the change.

AWS DevOps Agent acts on change notifications from AWS Organizations, usually within minutes. If a notification is delayed, AWS DevOps Agent catches the change on its next periodic check, which runs every 6 to 9 hours, depending on how many accounts it checks.

Use the following fields to monitor an association:
+ `statusReason` – Explains why an association is pending or invalid, and how to fix it.
+ `deploymentState` – Shows how many accounts are deployed, the reason for each account that has a problem, and when the state was last checked. After you change an association's scope, this field reports only the new scope.

To retry after you fix a problem, run `update-association` with the association's current configuration. This retries accounts whose deployment failed. It also restarts deployment for an association that's `pending-confirmation` or that failed in every account. After an association is `valid`, AWS DevOps Agent doesn't retry a failed account until you do this. If an account is reported as `accountSuspended` or `stackInstanceInoperable`, delete its stack instance from the stack set first. For instructions, see [Suspended and closed accounts](#suspended-and-closed-accounts) and [Deleting an INOPERABLE stack instance](#deleting-an-inoperable-stack-instance).

## Actions to avoid during deployment
<a name="actions-to-avoid-during-deployment"></a>

The following actions slow down deployment or cut off access. None of them speeds up deployment.
+ **Don't delete and re-create an association to retry it.** Removing the association removes the roles that it already deployed, and the new association creates a new stack set and redeploys to every account. You also can't create a second association for the same OU while the first one exists. To retry, run `update-association` with the association's current configuration. For more information, see [Deployment timing and status](#deployment-timing-and-status).
+ **Don't edit or delete the roles, the stack set, or its stack instances.**
  + If you delete an account's stack instance from the stack set, AWS DevOps Agent redeploys it, usually within a day.
  + If you delete only the role, the agent can't use that account, and requests for it fail with an error that names the role. AWS DevOps Agent doesn't re-create the role.
  + Deleting resources isn't a reliable way to stop access. Instead, use one of the methods in [Stopping access](#stopping-access).
+ **Don't turn off automatic deployment or managed execution on the stack set, and don't run your own operations on it.** These actions block or delay deployment and repair. If you change automatic deployment, AWS DevOps Agent changes it back, usually within a day. If you turn off managed execution, CloudFormation can refuse AWS DevOps Agent's operations while another operation on the stack set is running. Turn managed execution back on. AWS DevOps Agent retries daily, or you can run `update-association` with the association's current configuration to retry now.
+ **Don't move accounts out of a covered OU and back in to retry deployment.** AWS DevOps Agent detects account moves on its own. When you move an account out, its role is removed. When you move it back in, the role is deployed again.

## Changing coverage
<a name="changing-coverage"></a>

To change coverage, update the association with the complete configuration that you want. You can switch between covering a whole OU and covering specific accounts, and you can add or remove accounts from the list. AWS DevOps Agent checks added coverage against your quotas. You can always reduce coverage. You can't change an association's OU. To cover a different OU, create a new association for it, and then remove this one.

The following example changes an association to cover a specific list of accounts. Replace `<MEMBER_ACCOUNT_ID_1>` and `<MEMBER_ACCOUNT_ID_2>` with the IDs of the accounts to cover.

```
aws devops-agent update-association \
    --agent-space-id <AGENT_SPACE_ID> \
    --association-id <ASSOCIATION_ID> \
    --configuration '{
      "sourceAwsOrg": {
        "accountType": "source",
        "organizationalUnit": {
          "organizationalUnitId": "<OU_ID>",
          "accountIds": ["<MEMBER_ACCOUNT_ID_1>", "<MEMBER_ACCOUNT_ID_2>"]
        }
      }
    }' \
    --region <REGION>
```

When you change coverage, the following applies:
+ While a scope change deploys, the association's status is `pending-confirmation`. Accounts that it already covered keep working.
+ When you remove an account from the list, AWS DevOps Agent refuses new access to that account starting with the next request. It then removes the account's role.
+ For an association that covers a whole OU, when an account moves out of the OU, its role is removed automatically.
+ For an association that lists specific accounts, when a listed account moves out of the OU, AWS DevOps Agent stops using it right away and then removes its role. If the account moves back, AWS DevOps Agent redeploys the role, usually within minutes. If you no longer want the account covered, remove it from the list.
+ When an account leaves your organization, see [When an account leaves your organization](#when-an-account-leaves-your-organization).

The agent's credentials for your accounts are valid for up to 1 hour. A coverage change prevents new credentials from being issued. Credentials that were already issued remain valid until they expire, unless a service control policy (SCP) blocks them.

## Stopping access
<a name="stopping-access"></a>

Choose a method based on the scope and how quickly you need access to stop.

### For your entire organization
<a name="for-your-entire-organization"></a>

Disable trusted access for `aidevops.amazonaws.com`. AWS DevOps Agent stops issuing new credentials within minutes. Credentials that were already issued remain valid until they expire, within 1 hour. The deployed roles remain in your accounts, but AWS DevOps Agent doesn't use them. Re-enabling trusted access restores access without redeploying anything.

Requests that AWS DevOps Agent refuses return an error that names the cause. Organization associations change to `invalid`, usually within minutes.

For more information, see [Disabling trusted access with AWS DevOps Agent](configuring-integrations-and-knowledge-aws-devops-agent-and-aws-organizations.html#disabling-trusted-access-with-aws-devops-agent).

### For one account
<a name="for-one-account"></a>

Use one of the following methods:
+ Remove the account from the association's account list. For instructions, see [Changing coverage](#changing-coverage). This change takes effect on the next request.
+ Move the account out of the covered OU.
+ Remove the association. For instructions, see [Removing an organization association](#removing-an-organization-association).

### Immediately, including sessions in progress
<a name="immediately-including-sessions-in-progress"></a>

Attach the following SCP to the accounts or OUs where you want to stop access. Because AWS Organizations evaluates SCPs on every request, the policy also blocks sessions that are already running. The policy denies all actions, but the `aws:PrincipalArn` condition limits it to the AWS DevOps Agent roles.

```
{
  "Version": "2012-10-17",		 	 	 		 	 	 
  "Statement": [
    {
      "Sid": "DenyAIDevOpsAgentSpaceRole",
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "ArnLike": {
          "aws:PrincipalArn": "arn:aws:iam::*:role/AIDevOpsAgentSpaceRole-*"
        }
      }
    }
  ]
}
```

The SCP blocks access only while it's attached. To stop access permanently, also use one of the methods in [For one account](#for-one-account) or [For your entire organization](#for-your-entire-organization).

## Removing an organization association
<a name="removing-an-organization-association"></a>

When you remove an association or delete the Agent Space, AWS DevOps Agent deletes the stacks and roles that it deployed, and then deletes the stack set. It doesn't delete any of your data or other resources.

AWS DevOps Agent doesn't remove the following:
+ **Stacks in suspended accounts.** You can delete them after the account is reinstated.
+ **Stacks and roles in listed accounts that already left your organization.** This applies only to associations that cover specific accounts. For more information, see [When an account leaves your organization](#when-an-account-leaves-your-organization).

Removal continues in the background after the command returns. Until removal is complete, keep the following in place:
+ The service management role, with its trust policy and `AIDevOpsOrganizationsAccessPolicy`
+ Trusted access for CloudFormation StackSets
+ Your delegated administrator registration, if you use one

Removal is complete when the stack set no longer exists. To check, run the following command. It returns `StackSetNotFoundException` when removal is complete. In a delegated administrator account, add `--call-as DELEGATED_ADMIN`.

```
aws cloudformation describe-stack-set \
    --stack-set-name AIDevOpsOrgSource-<ASSOCIATION_ID> \
    --region <REGION>
```

If removal stops, the stack set stays in place. For example, this happens if AWS DevOps Agent can't use the service management role, or if trusted access for CloudFormation StackSets is off. If trusted access for CloudFormation StackSets is off, turn it back on, because deleting the stack instances requires it. Then delete the stack instances and the stack set yourself.

`disassociate-service` and `delete-agent-space` fail if the association for the primary account has no service management role. You can't remove the association for the primary account while an organization association exists. If `disassociate-service` returns an error, fix the cause that it names and run it again. You can create a new association for the same OU as soon as `disassociate-service` returns.

To remove an association, run the following command:

```
aws devops-agent disassociate-service \
    --agent-space-id <AGENT_SPACE_ID> \
    --association-id <ASSOCIATION_ID> \
    --region <REGION>
```

## When an account leaves your organization
<a name="when-an-account-leaves-your-organization"></a>

AWS DevOps Agent stops issuing credentials for an account as soon as AWS Organizations reports that the account left your organization. What happens to the role depends on the association's scope:
+ **Whole OU** – CloudFormation removes the role automatically when the account leaves.
+ **Specific accounts** – AWS DevOps Agent removes the account's stack instance from the stack set, usually within minutes, and the account no longer counts against your quota. `deploymentState` reports the account as `accountNotInScope`. CloudFormation can't reach an account after it leaves your organization, so the stack and its `AIDevOpsAgentSpaceRole-*` role stay in the account.

### Removing the role from an account that left your organization
<a name="removing-the-role-from-an-account-that-left-your-organization"></a>

Sign in to the account and delete the CloudFormation stack whose name starts with `StackSet-AIDevOpsOrgSource-<ASSOCIATION_ID>-`. Deleting the stack also deletes the role.

**Note**  
** Delete the stack rather than only the role, so that nothing is left behind. The stack is no longer part of the stack set, so deleting it doesn't affect the association.

### Having AWS DevOps Agent remove roles before accounts leave
<a name="having-aws-devops-agent-remove-roles-before-accounts-leave"></a>

To have AWS DevOps Agent remove the roles before you remove accounts from your organization, do the following.

**Step 1.** Remove the accounts from the association's account list, or remove the association.

**Step 2.** Wait until the accounts' stack instances no longer appear in the stack set. To check, run the following command. In a delegated administrator account, add `--call-as DELEGATED_ADMIN`.

```
aws cloudformation list-stack-instances \
    --stack-set-name AIDevOpsOrgSource-<ASSOCIATION_ID> \
    --region <REGION>
```

**Step 3.** Remove the accounts from your organization.

### If an account rejoins your organization
<a name="if-an-account-rejoins-your-organization"></a>

When a listed account rejoins your organization and is back under the association's OU, AWS DevOps Agent redeploys the role automatically, usually within minutes. The new role has a different name from the one left behind, so you don't need to delete the old stack first. The old stack and role stay in the account and aren't used. You can delete the old stack at any time.

In rare cases, the new role's name matches the old one, and deployment to the account fails. `deploymentState` then reports `deploymentFailed` for the account, with a message that names the stack to delete. Delete that stack in the account. Then run `update-association` with the association's current configuration to retry. For more information, see [Changing coverage](#changing-coverage).

## Suspended and closed accounts
<a name="suspended-and-closed-accounts"></a>

AWS DevOps Agent doesn't use accounts that are suspended, pending closure, or closed, and it doesn't delete anything when an account is suspended. If a suspended account already has the role, it keeps the role, and access resumes when the account is reinstated. A closed account can't be used again.

If an account was suspended when the association was first deployed, CloudFormation skips the account. After the account is reinstated, redeploy to it as follows. Modify the stack set yourself only when this topic, `statusReason`, or `deploymentState` tells you to, as in this procedure.

To deploy to a reinstated account, do the following.

**Step 1.** Delete the account's stack instance from the stack set. Run the following command in the primary account. If it's a delegated administrator account, add `--call-as DELEGATED_ADMIN`. Replace `<MEMBER_ACCOUNT_ID>` with the ID of the reinstated account. For `<OU_ID>`, use the `OrganizationalUnitId` that `list-stack-instances` shows for the account.

```
aws cloudformation delete-stack-instances \
    --stack-set-name AIDevOpsOrgSource-<ASSOCIATION_ID> \
    --deployment-targets OrganizationalUnitIds=<OU_ID>,Accounts=<MEMBER_ACCOUNT_ID>,AccountFilterType=INTERSECTION \
    --regions <REGION> \
    --no-retain-stacks \
    --region <REGION>
```

**Step 2.** Run `update-association` with the association's current configuration to redeploy. For more information, see [Changing coverage](#changing-coverage).

### Deleting an INOPERABLE stack instance
<a name="deleting-an-inoperable-stack-instance"></a>

If `deploymentState` reports an account as `stackInstanceInoperable`, or `statusReason` says that stack instances are INOPERABLE, do the following.

1. Run the `delete-stack-instances` command from the previous procedure for that account, with `--retain-stacks` instead of `--no-retain-stacks`.

1. Sign in to the account and delete the CloudFormation stack whose name starts with `StackSet-AIDevOpsOrgSource-<ASSOCIATION_ID>-`. Deleting the stack also deletes the role.

1. Run `update-association` with the association's current configuration to redeploy. For more information, see [Changing coverage](#changing-coverage).

## Troubleshooting organization associations
<a name="troubleshooting-organization-associations"></a>

AWS DevOps Agent doesn't bypass your controls. If an SCP or a missing permission blocks a step, the step fails and `statusReason` describes what to fix.
+ **An association is pending and `statusReason` doesn't report a problem.** Deployment is still running. Wait, and check the status again later.
+ **`statusReason` reports a problem.** Fix the problem that it describes, such as a missing permission, an SCP, or a CloudFormation StackSets setting. If `statusReason` says that AWS DevOps Agent retries, it retries on its own, daily for most deployment problems. Otherwise, to retry, run `update-association` with the association's current configuration. AWS DevOps Agent doesn't retry an `invalid` association on its own. The exceptions are turning trusted access back on and registering the delegated administrator again, which restore the association automatically. For more information, see [Changing coverage](#changing-coverage).
+ **`deploymentState` reports problems in some accounts.** Fix the problem in those accounts. Then run `update-association` with the association's current configuration to retry them. The rest of the association continues to work.

## Organization association quotas
<a name="organization-association-quotas"></a>

The following quotas apply to organization associations. They are also listed in [Quotas](quotas.md).


| Quota | Value | Adjustable | Service Quotas name (code) | 
| --- | --- | --- | --- | 
| Organization associations per Agent Space | 20 | No | aws-orgs-associations-per-agent-space (L-0178C38B) | 
| Organization-covered accounts per Agent Space | 3,000 | No | aws-orgs-secondary-accounts-per-agent-space (L-10E2D25F) | 
| Accounts in an association's account list | 1,000 | No | – | 
| OUs per association | 1 (an OU or the root) | No | – | 

**Note**  
** The Service Quotas console might show some of these quotas as adjustable. Increase requests for these quotas aren't currently granted.

The following applies to the quotas:
+ **Invalid associations count.** An `invalid` association counts against the organization associations quota until you remove it.
+ **Coverage counts per association.** If two associations cover the same account (for example, an association for a nested OU and another for its parent), the account counts twice.
+ **Requests that exceed the covered-accounts quota are refused.** The error message shows the quota and your current coverage. If an association that covers a whole OU turns out to have too many accounts, the association stays `pending-confirmation`, and `statusReason` tells you to narrow the scope or reduce coverage elsewhere. AWS DevOps Agent doesn't retry until you update the association.
+ **Accounts beyond the quota aren't used.** If an OU grows beyond the quota, new accounts still receive the role, but the agent doesn't use them until coverage is available. AWS DevOps Agent adds waiting accounts in ascending order of account ID.