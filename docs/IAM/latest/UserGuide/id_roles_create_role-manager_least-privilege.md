# Apply least-privilege permissions to a role created automatically

When creating a resource in a service console, role manager provides the IAM role that
the resource needs. For some tasks, such as running your own code, AWS cannot determine in
advance what permissions are required. As a result, a role can allow more permissions than the
resource requires. After you know which permissions the resource needs, you can reduce the
role's permissions to match.

Disabling role manager does not affect roles previously created by role manager. You can
disable role manager without reducing any permissions, and you can reduce a role's permissions
without disabling role manager.

## When to apply least-privilege permissions

Granting a role only the permissions its resource requires is a security best practice in
line with the principle of least privilege. Most roles created by role manager are
over-permissive by default because they are intended to help you get started without
encountering IAM friction.

When you are ready to start scoping down roles created by role manager, we
recommend starting with the roles associated with your most sensitive workloads and resources,
such as anything handling PII or production data. To learn more, see [Prepare for least-privilege permissions](getting-started-reduce-permissions.md "getting-started-reduce-permissions.md").

## How to analyze unused access

Before disabling role manager, AWS recommends that you use [Using AWS Identity and Access Management Access Analyzer](what-is-access-analyzer.md "what-is-access-analyzer.md") to create an unused access analyzer in your account. The
analyzer compares the actions that a role is allowed to perform with the actions that it has performed,
and reports the unused permissions. The analyzer reviews the IAM
roles in your account, including roles that you created yourself. The analyzer reports what
it observes as
findings, which appear on the **Roles** page in the IAM console. For each
role, you can see the number of unused permissions and open a recommendation. For more
information, see [IAM Access Analyzer
findings](access-analyzer-findings.md "access-analyzer-findings.md").

## Prerequisites

To review Access Analyzer findings, you need permission to perform the
`access-analyzer:ListFindings` action. To apply a recommendation, you need
permission to perform `iam:CreatePolicy`, `iam:AttachRolePolicy`, and
`iam:DetachRolePolicy` on the role.

## To reduce a role's permissions in console

1. Sign in to the AWS Management Console and open the IAM console.
2. In the navigation pane, choose **Roles**.
3. Choose the name of the role whose permissions you want to reduce.
4. Review the unused permissions reported for the role, and then choose
   **Reduce permissions**.
5. Compare the recommended permissions with the role's current permissions, and review
   the actions that the recommendation removes.
6. Choose **Apply**.

## How recommended permissions work

Based on the unused access analyzer findings, IAM creates one or more customer-managed
policies that contain the recommended permissions. IAM attaches the new policies before it
detaches the old ones, so the role keeps its permissions throughout the change.

For example, consider an AWS Lambda execution role. IAM Access Analyzer reports which of the
role's permissions are unused and recommends a policy scoped to the actions that the role
performed, such as writing logs to Amazon CloudWatch Logs. You review the recommendation against what the
function does, confirm that it covers everything the function needs, and apply it. The role
then allows only the actions the function needs.

###### Important

The recommendation is based on the last 30 days of activity. A permission that the
resource uses infrequently on a longer time horizon, such as for a quarterly job, can appear
as unused. Review the recommendation against what your workload needs before you apply
it.

After you change a role's policies or trust policies, role manager no longer manages
that role. The role will not pick up any version changes to the role template that was
originally used to create the role.

IAM limits the number of managed policies that you can attach to a role. If applying
the recommendation would exceed that limit, the console notifies you and does not apply the
change. For information about this quota, see [IAM and AWS STS quotas](reference_iam-quotas.md "reference_iam-quotas.md").

## Related information

- [Create roles automatically with role manager](id_roles_create_role-manager.md "id_roles_create_role-manager.md")
- [Manage access to role manager](id_roles_create_role-manager_enable-use.md "id_roles_create_role-manager_enable-use.md")
- [Overview of role templates](id_roles_create_role-template.md "id_roles_create_role-template.md")
