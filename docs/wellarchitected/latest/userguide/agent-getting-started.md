

AWS Well-Architected Agent is in preview release and is subject to change.

# Getting started with AWS Well-Architected Agent

To use AWS Well-Architected Agent, you create an agent profile that defines the scope of your infrastructure analysis. You need an agent profile before you can generate and view application-level recommendations, run architecture reviews, or use any other AWS WA Agent feature. To receive personalized, goal-aligned recommendations with cross-pillar trade-off analysis, complete the following setup steps.

**Tip**  
You don't have to create a profile to receive resource-level recommendations. The first time you open the AWS WA Agent agent profile screen without any profiles, the agent automatically creates a basic profile for you and returns resource-level recommendations without any setup. For more information, see [Basic profiles](agent-basic-profile.md).

This page describes the console-based setup. To set up AWS WA Agent using the AWS CLI instead, see [API quickstart](agent-api-quickstart.md).

 Once a profile is created and properly configured, AWS WA Agent begins the process of generating scheduled recommendations within 24 hours. For more information on scheduled recommendations and recommendation types, see [Recommendations](agent-rec-management.md). 

## Prerequisites
<a name="agent-prerequisites"></a>

All agent profiles require the following prerequisites:
+ You have an active AWS Support plan at the Business\+ tier or higher (Business\+, Enterprise On-Ramp, Enterprise Support, or Unified Operations). Developer and Business tier customers do not have access to AWS WA Agent. For tier-specific entitlements, see [AWS Well-Architected Agent Quotas and limits](agent-quotas.md).
+ You have the IAM permissions required to create a AWS WA Agent profile, including permissions to create IAM roles (`iam:CreateRole`, `iam:AttachRolePolicy`, `iam:PassRole`) and AWS WA Agent actions (`wellarchitected:CreateAgentProfile`). For more information about the AWS WA Agent access model, see [AWS Well-Architected Agent access model](security-iam-agent.md).
+ You have identified the AWS accounts that you want AWS WA Agent to analyze.
+ For all member (linked) accounts in AWS Organizations that you wish to monitor in AWS WA Agent, confirm that any [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) attached to the account or its parent organizational units (OUs) allow both the AWS WA Agent actions in the `wellarchitected:*` namespace and the actions in the [`WellArchitectedAgentResourceScanning`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/WellArchitectedAgentResourceScanning.html) managed policy. The access roles use this policy to scan resources in your workload accounts.

   SCPs are organization-level guardrails that can block access even when your IAM permissions allow it. An SCP must allow these actions at every level between your account and the organization root.

  If the SCP does not allow the `wellarchitected:*` actions, you cannot create an agent profile or use the agent from the account. If the SCP does not allow the resource-scanning actions, you can create a profile, but AWS WA Agent cannot view your resources, which returns empty recommendations.

**Important**  
AWS WA Agent requires an active AWS Support plan at Business\+ or higher in every account within the monitoring boundary, not just the account that owns the profile. If a monitored account has only a Basic or Developer plan, AWS WA Agent cannot call AWS Trusted Advisor APIs for that account.   
 As a result, AWS WA Agent limits that account's recommendations to application-level recommendations (beta). This often affects customers who do not use AWS Organizations, or who subscribe to Business\+ without auto-enrollment, so their other accounts do not receive the plan automatically.

### Organizational profile prerequisites
<a name="agent-prerequisites-orgs"></a>

Organizational profiles also require the following additional prerequisites:
+  The account that creates an organizational profile must be the management account of an AWS Organization. 
+ You have enabled [Trusted Access](agent-preferences.md#agent-preferences-trusted-access) in the **Preferences** page of AWS WA Agent.
**Important**  
 Trusted Access must be enabled prior to creating the organizational profile. For more detail, see [Preferences](agent-preferences.md). 

### (Optional) AWS Cost Explorer prerequisites
<a name="agent-prerequisites-cost"></a>

Accurate cost data relies on the following optional prerequisites:
+ **(Optional)** You have enabled AWS Cost Explorer in your account for accurate cost data. There are two separate features to check to fully enable Cost Explorer for AWS WA Agent:
  +  Enable the main AWS Cost Explorer service. 
  +  In **Cost Management Preferences** in the Cost Explorer sidebar, under **Granular data**, select the **Resource-level data at daily granularity** checkbox. 

   For more detail, see [(Optional) Enable AWS Cost Explorer](#agent-cost-explorer) 
**Note**  
 Without Cost Explorer enabled, AWS WA Agent estimates costs from public AWS pricing. 

## Step 1: Enter profile details
<a name="agent-create-profile"></a>

Name the profile, choose the accounts and AWS Regions it monitors, and set up service access. This step has three parts: **Profile**, **Monitoring scope**, and **Configure service access**.

**To enter profile details**

1. Open the AWS Management Console and navigate to AWS Well-Architected.

1. Open the AWS WA Agent console.

1. Choose **Agent profiles** in the left-hand navigation.

1. In the top right corner, choose **Add profile**.

1. Under **Profile**, enter a **Profile name**. Use only letters, numbers, hyphens (-), and underscores (\_). For example, `product-backend-team`.

1. (Optional) Enter a **Profile description** (maximum 512 characters).

1. Under **Monitoring scope**, for **Regions to monitor**, select the AWS Regions this profile monitors and analyzes.

1. For account selection, choose one of the following options:
   + **The current account:** AWS WA Agent monitors only the account you are signed in to and creates the required roles automatically. You don't need to create any roles manually.
   + **Use AWS Organizations:** Select accounts from your organization. AWS WA Agent creates the required roles automatically for the accounts you select. You can use the organiational dialog to select multiple accounts at once, and you can select a folder or OU to include all accounts within it. Alternatively, you can enter account names in the search field. For more information, see [Selecting accounts from your organization](agent-preferences.md#agent-select-org-accounts).
**Note**  
Unlike delegated administrator registration, which registers accounts one at a time, profile creation lets you select multiple accounts at once. This option requires trusted access with AWS Organizations to be enabled. For more information, see [Trusted access with AWS Organizations](agent-preferences.md#agent-preferences-trusted-access).
   + **Manually add accounts:** Add the accounts yourself. Complete the following steps:

     1. Under **Accounts to monitor**, enter AWS account IDs separated by commas (up to 100 accounts).

     1. Under **Common access role name**, enter the access role name to use across all accounts in the profile. The recommended name is `AccessRoleForWellArchitectedAgent`.
**Note**  
Whether you create your own access role name or use the recommended one, you must use that exact same access role name across all accounts in the profile. This only applies to the console onboarding experience.

### Configure service access
<a name="agent-permissions-integrations"></a>

What you configure under **Configure service access** depends on the account selection option you chose for **Monitoring scope**.

If you chose **The current account** or **Use AWS Organizations**, no action is needed. Two read-only roles are created in this account to grant the service access to AWS resources. Both roles are read-only and can't modify your resources. The following table describes each role.


| Role name | What it does | 
| --- | --- | 
| `ExecutionRoleForWellArchitectedAgent` | Orchestrates resource discovery. Assumes the access role to read resources. | 
| `AccessRoleForWellArchitectedAgent` | Grants read-only access to the resources in this account. | 

If you chose **Manually add accounts**, you select an existing execution role or create a new one. The execution role is an IAM role in your profile account that AWS WA Agent assumes to orchestrate resource discovery. The execution role chains to the access roles in your workload accounts. When you choose **Create new role**, the console creates the IAM execution role for you automatically, applying the required trust policy and permissions policy. You don't need to navigate to the IAM console separately.

**To create a new execution role**

1. Choose **Create new role**.

1. The console pre-populates the **Role name** field with `ExecutionRoleForWellArchitectedAgent`. We recommend using this default name.

1. (Optional) To review the trust policy and permissions policy the console will apply, choose **View trust policy**.

1. Choose **Create role**.

For the manually added accounts path, you must also create access roles in each workload account after the profile is created. For more information, see [(Optional) Create access roles in your workload accounts](#agent-access-roles). To use real-time, accurate cost data in your recommendations, you can optionally enable AWS Cost Explorer. For more information, see [(Optional) Enable AWS Cost Explorer](#agent-cost-explorer).

## Step 2: Add application context
<a name="agent-app-context"></a>

Tell the agent about the application this profile covers. Better context leads to recommendations tailored to this application. Only the name is required. Add what you know now, then fill in details or add applications after setup.

**Important**  
You must define at least one application context during profile creation. Without application context, your profile is flagged as invalid and scheduled recommendation generation does not run.

**To add application context**

1. Under **Application details**, for **Application name**, enter the name of the workload or microservice. Use letters, numbers, spaces, hyphens, and underscores.

1. Under **Application boundary**, select one of the following options:
   + **Use everything the profile monitors:** Covers every account and Region you selected in [Step 1: Enter profile details](#agent-create-profile).
   + **Limit to specific accounts and regions:** Select particular AWS accounts and AWS Regions. Leave out shared services or sandbox accounts.

   The application boundary is required and defaults to **Use everything the profile monitors**.

The following optional details improve the relevance of your recommendations:
+ **Application overview:** What this application does for the business.
+ **Tags:** Key-value pairs that narrow the scope to specific resources. Choose **Add new tag** to add more.
+ **Narrow by service or resource:** Expand this setting to scope the application to specific AWS services or individual resources. Selecting a service automatically selects all of its resources.
+ **Architecture overview:** The pattern it uses, how components interact, and what runs in each account.
+ **Criticality:** How critical the workload is. Influences how recommendations are prioritized.
+ **Classify this application:** Expand this setting to add the following:
  + **Type:** The type of application.
  + **Industry:** The industry the application serves, for domain-specific recommendations.
  + **Additional context:** Any constraints, migrations, known trade-offs, or other context you want AWS WA Agent to consider.

For full per-field detail, see [Updating application context](agent-update-app-context.md).

## Step 3: Configure optimization goals and settings
<a name="agent-goals-pillars"></a>

Set the pillars and goals that matter most to your business, and termination protection.

**To configure optimization goals and settings**

1. Under **Optimization pillars**, select at least one optimization pillar for AWS WA Agent to analyze: Cost optimization, Security, Resilience, or Performance. To add another pillar, choose **Add optimization pillar**.

1. For each pillar, enter a goal statement. At least one goal is required for AWS WA Agent to generate prioritized recommendations, and goals are editable after creation. For guidance on writing effective goals, see [Goals and personalization in AWS Well-Architected Agent](agent-goals.md).

1. For **Termination protection**, choose whether to enable it. Enabling it is recommended to prevent accidental profile deletion from the console, API, or CLI. To delete a profile, you must first disable it.

## Step 4: Review and create
<a name="agent-review-create"></a>

Check your configuration before creating the profile. The review screen summarizes each of the previous steps, with an **Edit** option next to each section so you can jump back and make changes.

**To review and create the profile**

1. Review the summary of each step:
   + **Step 1: Specify profile details.** The **Profile details** (profile name and description), the **Monitoring scope** (regions to monitor, account selection method, and accounts to monitor), and **Configure service access** (for example, roles created automatically, or the selected execution role).
   + **Step 2: Add application context.** The application details and the application boundary.
   + **Step 3: Configure optimization goals and settings.** The optimization pillars, goal statements, and termination protection setting.

1. To change a section, choose **Edit** next to it.

1. When the configuration is correct, choose **Create profile**.

## (Optional) Create access roles in your workload accounts
<a name="agent-access-roles"></a>

**Important**  
This procedure applies only if you chose **Manually add accounts** in [Step 1: Enter profile details](#agent-create-profile). If you chose **The current account** or **Use AWS Organizations**, the console already created both the execution role and the access roles automatically during profile creation, and you can skip this step.

After you create your profile, create an IAM access role in each AWS account that you selected to monitor. Access roles allow AWS WA Agent to discover and analyze resources in those accounts.

When profile creation finishes, the create-profile page shows an **Action required** prompt indicating that the selected accounts still need an access role. Creating these roles is a separate task that you perform manually in the IAM console. The console does not create the roles for you, and it does not open the IAM console automatically. AWS WA Agent does not monitor or analyze an account until that account's access role exists.

The role name must match the **Common access role name** that you entered during profile creation. The recommended name is `AccessRoleForWellArchitectedAgent`.

The execution role's permissions policy grants `sts:AssumeRole` on the access roles, and each access role's trust policy allows the execution role to assume it. Use the same role name in every workload account.

Use the following trust policy template for your access roles. {{ProfileOwningAccountId}} is the account where you created the agent profile. {{ExecutionRoleName}} is the name of the execution role in the agent profile. By default, this is usually `ExecutionRoleForWellArchitectedAgent`.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::{{ProfileOwningAccountId}}:role/service-role/{{ExecutionRoleName}}"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

**Important**  
The execution role ARN format depends on how the role was created:  
If you used the **Create new role** button in [Configure service access](#agent-permissions-integrations), the console places the role under the `service-role/` path: `arn:aws:iam::{{111122223333}}:role/service-role/ExecutionRoleForWellArchitectedAgent`
If you created the execution role manually in IAM beforehand and selected it during profile creation, use the ARN without the `service-role/` prefix: `arn:aws:iam::{{111122223333}}:role/ExecutionRoleForWellArchitectedAgent`

**To create an access role**

1. Open the IAM console in the workload account.

1. In the left-hand navigation, choose **Roles**, then choose **Create role**.

1. For **Trusted entity type**, choose **Custom trust policy**.

1. Paste the trust policy shown in the preceding template, and substitute the required information.

1. Choose **Next**. On the **Add permissions** page, search for and attach the [`WellArchitectedAgentResourceScanning` managed policy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/WellArchitectedAgentResourceScanning.html). This grants read-only access to resource metadata and configuration.

1. Choose **Next**. Enter the role name (it must match the **Common access role name** from profile creation - we recommend `AccessRoleForWellArchitectedAgent`) and choose **Create role**. Use the same name in every workload account.

**Note**  
If you already created access roles with a broader trust policy, edit each role's **Trust relationships** tab to use the trust policy shown in the preceding template.

Repeat this procedure in each workload account you want AWS WA Agent to analyze. For more information about the AWS WA Agent access model and role chain, see [AWS Well-Architected Agent access model](security-iam-agent.md).

## (Optional) Enable AWS Cost Explorer
<a name="agent-cost-explorer"></a>

**Note**  
Enabling AWS Cost Explorer is an optional step to enhance the specificity of cost data. Cost Explorer is enabled at the AWS account level, not per AWS WA Agent profile. If you enable Cost Explorer in your organization's management account, all member accounts are also granted access. 

**Important**  
 After you enable Cost Explorer, it cannot be disabled, though the optional granular data preferences (resource-level data) can be changed at any time.

To use real-time, accurate cost data and resources from your accounts, you can choose to enable AWS Cost Explorer.

 With Cost Explorer and hourly and [resource-level data at daily granularity](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-resource-daily.html) both enabled, AWS WA Agent can provide recommendations and optimizations with your exact cost data.

Without Cost Explorer enabled, AWS WA Agent estimates costs based on public AWS pricing.

There is no charge for using the Cost Explorer console. Charges apply for Cost Explorer API requests and for the resource-level granular data preferences. Resource-level cost attribution in AWS WA Agent recommendations requires the granular data preferences. To estimate these charges, see [AWS Cost Explorer pricing](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/pricing/).

**To enable AWS Cost Explorer**

1. Open Cost Explorer in the AWS Management Console.

1. Configure Cost Explorer for your AWS account. For more detail, see [Getting started with Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-getting-started.html).

 After enabling Cost Explorer, it can take up to 24 hours for the data to be available to AWS WA Agent, and resource-level data at daily granularity can take up to 48 hours to propogate. 

## Next steps
<a name="agent-next-steps"></a>

After you complete your profile setup, you can:
+ View your personalized recommendations in the AWS WA Agent dashboard ([Recommendations](agent-rec-management.md)). Initial scheduled recommendations become available 24 hours after completing profile setup.
+ Conduct an architecture review by uploading your IaC files ([Conducting architecture reviews](agent-architecture-reviews.md)).
+ Manage your profile settings at any time ([Agent profiles](agent-manage-profiles.md)).