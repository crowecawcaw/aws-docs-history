

AWS Well-Architected Agent is in preview release and is subject to change.

# Getting started with AWS Well-Architected Agent
<a name="agent-getting-started"></a>

To use AWS Well-Architected Agent, you create an agent profile that defines the scope of your infrastructure analysis. Creating an agent profile is the onboarding step. You need a profile before you can view recommendations, conduct architecture reviews, or use any other AWS WA Agent feature.

**Tip**  
Baseline recommendations from AWS Trusted Advisor are available without creating a profile. To receive personalized, goal-aligned recommendations with cross-pillar trade-off analysis, complete the following setup steps.

The setup process uses two AWS services:
+ **AWS Well-Architected** (Well-Architected console): Create your agent profile, configure accounts, pillars, goals, and application context.
+ **IAM**: Create access roles in your workload accounts and update trust policies to establish cross-account access.

This page describes the console-based setup. To set up AWS WA Agent using the AWS CLI instead, see [API quickstart](agent-api-quickstart.md).

 Once a profile is created and properly configured, AWS WA Agent begins generating scheduled recommendations within 48 hours. For more information on scheduled recommendations and recommendation types, see [Recommendations](agent-rec-management.md). 

## Prerequisites
<a name="agent-prerequisites"></a>
+ You have an active AWS Support plan at the Business\+ tier or higher (Business\+, Enterprise On-Ramp, Enterprise Support, or Unified Operations). Developer and Business tier customers do not have access to AWS WA Agent. For tier-specific entitlements, see [AWS Well-Architected Agent Quotas and limits](agent-quotas.md).
+ **(Optional)** You have enabled AWS Cost Explorer in your account for accurate cost data. There are two separate features to check to fully enable Cost Explorer for AWS WA Agent:
  +  Enable the main AWS Cost Explorer service. 
  +  In **Cost Management Preferences** in the Cost Explorer sidebar, under **Granular data**, select the **Resource-level data at daily granularity** checkbox. 
**Note**  
 Without Cost Explorer enabled, AWS WA Agent estimates costs from public AWS pricing. 
+ You have the IAM permissions required to create a AWS WA Agent profile, including permissions to create IAM roles (`iam:CreateRole`, `iam:AttachRolePolicy`, `iam:PassRole`) and AWS WA Agent actions (`wellarchitected:CreateAgentProfile`). For more information about the AWS WA Agent access model, see [AWS Well-Architected Agent access model](security-iam-agent.md).
+ You have identified the AWS account IDs that you want AWS WA Agent to analyze (maximum 100 accounts).
+ You have defined your business goals and selected the optimization pillars you want to focus on.

## Step 1: Create an agent profile
<a name="agent-create-profile"></a>

Create an agent profile from the AWS WA Agent console. During profile creation, you can create an execution role or select an existing one.

**To create an agent profile**

1. Open the AWS Management Console and navigate to AWS Well-Architected.

1. Open the AWS WA Agent console.

1. Choose **Agent profiles** in the left-hand navigation.

1. In the top right corner, choose **Add profile**.

1. Enter a profile name between 3 and 128 characters. Use only letters, numbers, hyphens (-), and underscores (\_). For example, `product-backend-team`.

1. Enter a description for the profile.

1. Under **Select accounts & regions**, select AWS Regions to monitor and analyze.

1. Under **Accounts to monitor**, enter account IDs separated by commas (up to 100 accounts).

1.  Then, under **Common access role name**, enter the access role name to use across all accounts in the profile. The recommended name is `AccessRoleForWellArchitectedAgent`. 
**Note**  
 Whether you create your own access role name or use the recommended one, you must use that exact same access role name across all accounts in the profile. This only applies to the console onboarding experience. 

## Step 2: Add goals and optimization pillars
<a name="agent-goals-pillars"></a>

During profile creation, configure the following in **Optimization pillars**:
+ **Optimization pillar:** Select at least one pillar for AWS WA Agent to analyze: Cost optimization, Security, Resilience, or Performance.
+ **Goal statement:** Enter at least one plain-text goal statement. Each profile requires a minimum of one goal for AWS WA Agent to generate prioritized recommendations. Goals are editable at any time after creation. For guidance on writing effective goals, see [Goals and personalization in AWS Well-Architected Agent](agent-goals.md).

## Step 3: Configure permissions and integrations
<a name="agent-permissions-integrations"></a>

After configuring pillars, under **Permissions and Integrations**, you can either select an existing execution role or create a new one.

The execution role is an IAM role in your profile account that AWS WA Agent assumes to orchestrate resource discovery. The execution role chains to the access roles in your workload accounts. When you choose **Create new role**, the console creates the IAM execution role for you automatically, applying the required trust policy and permissions policy. You do not need to navigate to the IAM console separately.

**To create a new execution role**

1. Choose **Create new role**.

1. The console pre-populates the **Role name** field with `ExecutionRoleForWellArchitectedAgent`. We recommend using this default name.

1. (Optional) To review the trust policy and permissions policy the console will apply, choose **View trust policy**.

1. Choose **Create role**.

1. Determine whether to enable or disable Termination protection. It is recommended to enable this feature to avoid accidental profile deletion.

If you do not want to enable AWS Cost Explorer, choose **Get started** to finish creating your profile. After the profile is created, complete the remaining setup. To enable cross-account discovery, you must create access roles in your workload accounts, as described in [Step 6: Create access roles in your workload accounts](#agent-access-roles).

If you want to enable Cost Explorer, go to [(Optional) Step 4: Enable AWS Cost Explorer](#agent-cost-explorer) before finishing profile creation.

## (Optional) Step 4: Enable AWS Cost Explorer
<a name="agent-cost-explorer"></a>

**Note**  
Enabling AWS Cost Explorer is an optional step to enhance the specificity of cost data. Cost Explorer is enabled at the AWS account level, not per AWS WA Agent profile. If you enable Cost Explorer in your organization's management account, all member accounts are also granted access.   
 After you enable Cost Explorer, it cannot be disabled, though the optional granular data preferences (resource-level data) can be changed at any time.

To use real-time, accurate cost data and resources from your accounts, you can enable AWS Cost Explorer.

 With Cost Explorer and hourly and [resource-level data at daily granularity](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-resource-daily.html) both enabled, AWS WA Agent can provide recommendations and optimizations with your exact cost data.

Without Cost Explorer enabled, AWS WA Agent estimates costs based on public AWS pricing.

There is no charge for using the Cost Explorer console. Charges apply for Cost Explorer API requests and for the resource-level granular data preferences. Resource-level cost attribution in AWS WA Agent recommendations requires the granular data preferences. To estimate these charges, see [AWS Cost Explorer pricing](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/pricing/).

To get started with Cost Explorer in your AWS WA Agent profile, choose **Open Cost Explorer**, then configure Cost Explorer for your AWS account. For more detail, see [Getting started with Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-getting-started.html).

 After enabling Cost Explorer, it can take up to 24 hours for the data to be available to AWS WA Agent, and resource-level data at daily granularity can take up to 48 hours to propogate. 

## Step 5: Add application context
<a name="agent-app-context"></a>

After your profile is created, add application context to help AWS WA Agent generate more relevant recommendations. Application context provides details about your workloads that AWS WA Agent cannot discover automatically.

**Important**  
At least one application context is required per profile for AWS WA Agent to generate scheduled recommendations. Without application context, your profile is flagged as invalid and scheduled recommendation generation does not run.

**To add application context to a profile**

1.  In the left-hand navigation, choose **Agent profiles**. 

1.  In the profile you already created, choose **Profile Details**. 

1.  Select the **Application context** tab. 

1.  Choose **Add application context**. 

1.  Enter details on your application context, including Application name, overview, accounts in the application, AWS Regions, and tags. For a full overview of adding or updating application context, see [Updating application context](agent-update-app-context.md). 

1. After filling in your application context, choose **Add application**.

## Step 6: Create access roles in your workload accounts
<a name="agent-access-roles"></a>

After you create your profile, create an IAM access role in each AWS account that you selected to monitor. Access roles allow AWS WA Agent to discover and analyze resources in those accounts.

When profile creation finishes, the create-profile page shows an **Action required** prompt indicating that the selected accounts still need an access role. Creating these roles is a separate task that you perform manually in the IAM console. The console does not create the roles for you, and it does not open the IAM console automatically. AWS WA Agent does not monitor or analyze an account until that account's access role exists.

The role name must match the **Common access role name** that you entered during profile creation. The recommended name is `AccessRoleForWellArchitectedAgent`.

The execution role's permissions policy grants `sts:AssumeRole` on the access roles, and each access role's trust policy allows the execution role to assume it. Use the same role name in every workload account.

Use the following trust policy template for your access roles. {{ProfileOwningAccountId}} is the account where you created the agent profile. {{ExecutionRoleName}} is the name of the execution role in the agent profile. By default, this is usually `ExecutionRoleForWellArchitectedAgent`.

```
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
If you used the **Create new role** button in [Step 3: Configure permissions and integrations](#agent-permissions-integrations), the console places the role under the `service-role/` path: `arn:aws:iam::{{111122223333}}:role/service-role/ExecutionRoleForWellArchitectedAgent`
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

## Next steps
<a name="agent-next-steps"></a>

After you complete your profile setup, you can:
+ View your personalized recommendations in the AWS WA Agent dashboard ([Recommendations](agent-rec-management.md)). Scheduled recommendations typically become available within 24 hours of completing profile setup.
+ Conduct an architecture review by uploading your IaC files ([Conducting architecture reviews](agent-architecture-reviews.md)).
+ Manage your profile settings at any time ([Agent profiles](agent-manage-profiles.md)).