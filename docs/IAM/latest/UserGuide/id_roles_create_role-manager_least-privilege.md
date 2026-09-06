

# Apply least-privilege permissions to a role created automatically
<a name="id_roles_create_role-manager_least-privilege"></a>

When creating a resource in a service console, role manager provides the IAM role that the resource needs. For some tasks, such as running your own code, AWS cannot determine in advance what permissions are required. As a result, a role can allow more permissions than the resource requires. After you know which permissions the resource needs, you can reduce the role's permissions to match.

Disabling role manager does not affect roles previously created by role manager. You can disable role manager without reducing any permissions, and you can reduce a role's permissions without disabling role manager.

## When to apply least-privilege permissions
<a name="id_roles_create_role-manager_least-privilege_when"></a>

Granting a role only the permissions its resource requires is a security best practice in line with the principle of least privilege. For most roles, role manager creates roles with well scoped permissions. For some roles, such as those for compute resources or cloud infrastructure management, it creates roles with broad permissions.

When you are ready to start scoping down roles created by role manager, we recommend starting with the roles associated with your most sensitive workloads and resources, such as anything handling PII or production data. To learn more, see [Prepare for least-privilege permissions](getting-started-reduce-permissions.md).

## How to analyze unused access
<a name="id_roles_create_role-manager_least-privilege_how-analysis-works"></a>

Before disabling role manager, AWS recommends that you use [IAM Access Analyzer](what-is-access-analyzer.md) to create an unused access analyzer in your account. The analyzer compares the actions that a role is allowed to perform with the actions that it has performed, and reports the unused permissions. The analyzer reviews the IAM roles in your account, including roles that you created yourself.

Where the findings appear depends on how the analyzer was provided:
+ **Analyzer provided by role manager:** When AWS provides the unused access analyzer for your account (see the note in this section), the findings appear on the **Roles** page in the IAM console. For each role, you can see the number of unused permissions and open a recommendation. Use the following procedure to reduce a role's permissions from the **Roles** page. After you disable role manager, the **Account settings** page provides a **View roles** button that opens the **Roles** page, where each role's findings appear.
+ **Analyzer created by yourself:** When you create your own unused access analyzer, the findings and recommendations appear in the IAM Access Analyzer console. That experience is unchanged by role manager. To review and act on unused access findings, see [IAM Access Analyzer findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings.html).

**Note**  
If AWS enabled role manager for your account created using the new AWS experience, you don't need to create an analyzer the first time you disable role manager. After you activate advanced features and disable role manager, AWS provides an unused access analyzer at no additional cost for 90 days. The analyzer gives you visibility into unused role permissions and policy scope-down recommendations so you can update the roles in your account, including those that role manager created, toward least privilege.

## Prerequisites
<a name="id_roles_create_role-manager_least-privilege_prereqs"></a>

To review Access Analyzer findings, you need permission to perform the `access-analyzer:ListFindings` action. To apply a recommendation, you need permission to perform `iam:CreatePolicy`, `iam:AttachRolePolicy`, and `iam:DetachRolePolicy` on the role.

## To reduce a role's permissions in the console (analyzer provided by role manager)
<a name="id_roles_create_role-manager_least-privilege_console"></a>

These steps apply when AWS provided the unused access analyzer for your account. If you created your own analyzer, review and apply recommendations in the IAM Access Analyzer console instead. See [IAM Access Analyzer findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings.html).

1. Sign in to the AWS Management Console and open the IAM console.

1. In the navigation pane, choose **Roles**.

1. On the **Roles** page, in the **Findings** column, choose the **Unused permissions** link for the role whose permissions you want to reduce.

1. On the **Reduce role permissions** page, review the unused permissions reported for the role.

1. Compare the recommended permissions with the role's current permissions, and review the actions that the recommendation removes.

1. Choose **Make changes**.

## How recommended permissions work
<a name="id_roles_create_role-manager_least-privilege_what-happens"></a>

Based on the unused access analyzer findings, IAM creates one or more customer-managed policies that contain the recommended permissions. IAM attaches the new policies before it detaches the old ones, so the role keeps its permissions throughout the change.

For example, consider an AWS Lambda execution role. IAM Access Analyzer reports which of the role's permissions are unused and recommends a policy scoped to the actions that the role performed, such as writing logs to Amazon CloudWatch Logs. You review the recommendation against what the function does, confirm that it covers everything the function needs, and apply it. The role then allows only the actions the function needs.

**Important**  
The recommendation is based on the last 30 days of activity. A permission that the resource uses infrequently on a longer time horizon, such as for a quarterly job, can appear as unused. Review the recommendation against what your workload needs before you apply it.  
After you change a role's policies or trust policies, role manager no longer manages that role. The role will not pick up any version changes to the role template that was originally used to create the role.

IAM limits the number of managed policies that you can attach to a role. If applying the recommendation would exceed that limit, the console notifies you and does not apply the change. For information about this quota, see [IAM and AWS STS quotas](reference_iam-quotas.md).

## Related information
<a name="id_roles_create_role-manager_least-privilege_related"></a>
+ [Create roles automatically with role manager](id_roles_create_role-manager.md)
+ [Manage access to role manager](id_roles_create_role-manager_enable-use.md)
+ [Overview of role templates](id_roles_create_role-template.md)