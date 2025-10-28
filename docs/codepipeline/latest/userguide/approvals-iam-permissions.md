# Grant approval permissions to an IAM user

in CodePipeline

Before IAM users in your organization can approve or reject approval actions, they
must be granted permissions to access pipelines and to update the status of approval
actions. You can grant permission to access all pipelines and approval actions in your
account by attaching the `AWSCodePipelineApproverAccess` managed policy to an
IAM user, role, or group; or you can to grant limited permissions by specifying the
individual resources that can be accessed by an IAM user, role, or group.

###### Note

The permissions described in this topic grant very limited access. To enable a
user, role, or group to do more than approve or reject approval actions, you can
attach other managed policies. For information about the managed policies available
for CodePipeline, see [AWS managed policies for AWS CodePipeline](managed-policies.md "managed-policies.md").

## Grant approval permission to all

pipelines and approval actions

For users who need to perform approval actions in CodePipeline, use the
`AWSCodePipelineApproverAccess` managed policy.

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

## Specify approval permission for

specific pipelines and approval actions

For users who need to perform approval actions in CodePipeline, use the following custom
policy. In the policy below, specify the individual resources a user can access. For
example, the following policy grants users the authority to approve or reject only
the action named `MyApprovalAction` in the `MyFirstPipeline`
pipeline in the US East (Ohio) Region (us-east-2):

###### Note

The `codepipeline:ListPipelines` permission is required only if
IAM users need to access the CodePipeline dashboard to view this list of pipelines.
If console access is not required, you can omit
`codepipeline:ListPipelines`.

###### To use the JSON policy editor to create a policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left, choose **Policies**.

If this is your first time choosing **Policies**, the
**Welcome to Managed Policies** page appears. Choose **Get
Started**. 3. At the top of the page, choose **Create policy**. 4. In the **Policy editor** section, choose the
**JSON** option. 5. Enter the following JSON policy document:

```
 {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "codepipeline:ListPipelines"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "codepipeline:GetPipeline",
                "codepipeline:GetPipelineState",
                "codepipeline:GetPipelineExecution"
            ],
            "Resource": "arn:aws:codepipeline:us-east-2:80398EXAMPLE:MyFirstPipeline"
        },
        {
            "Effect": "Allow",
            "Action": [
                "codepipeline:PutApprovalResult"
            ],
            "Resource": "arn:aws:codepipeline:us-east-2:80398EXAMPLE:MyFirstPipeline/MyApprovalStage/MyApprovalAction"
        }
    ]
}
```

6. Choose **Next**.

###### Note

You can switch between the **Visual** and **JSON**
editor options anytime. However, if you make changes or choose **Next**
in the **Visual** editor, IAM might restructure your policy to
optimize it for the visual editor. For more information, see [Policy restructuring](../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure "../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure")
in the _IAM User Guide_. 7. On the **Review and create** page, enter a **Policy
name** and a **Description** (optional) for the policy that
you are creating. Review **Permissions defined in this policy** to see
the permissions that are granted by your policy. 8. Choose **Create policy** to save your new policy.
