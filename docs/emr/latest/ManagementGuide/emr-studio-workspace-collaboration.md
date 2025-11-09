# Configure Workspace

collaboration in EMR Studio

Workspace collaboration lets you write and run notebook code simultaneously with
other members of your team. When you work in the same notebook file, you'll see changes as
your collaborators make them. You can enable collaboration when you create a
Workspace, or switch collaboration on and off in an existing Workspace.

###### Note

EMR Studio Workspace collaboration isn't supported with [EMR Serverless
interactive applications](../EMR-Serverless-UserGuide/interactive-workloads.md "../EMR-Serverless-UserGuide/interactive-workloads.md") or if trusted identity propagation is enabled.

###### Prerequisites

Before you configure collaboration for a Workspace, make sure you complete the
following tasks:

- Ensure that your EMR Studio admin has given you the necessary permissions. For
  example, the following statement allows a user to configure collaboration for any
  Workspace with the tag key `creatorUserId` whose value matches the user's ID
  (indicated by the policy variable `aws:userId`).

```
{
    "Sid": "UserRolePermissionsForCollaboration",
    "Action": [
        "elasticmapreduce:UpdateEditor",
        "elasticmapreduce:PutWorkspaceAccess",
        "elasticmapreduce:DeleteWorkspaceAccess",
        "elasticmapreduce:ListWorkspaceAccessIdentities"
    ],
    "Resource": "*",
    "Effect": "Allow",
    "Condition": {
        "StringEquals": {
            "elasticmapreduce:ResourceTag/creatorUserId": "${aws:userid}"
        }
    }
}
```

- Ensure that the service role associated with your EMR Studio has the permissions
  required to enable and configure Workspace collaboration, as in the following example
  statement.

```
{
    "Sid": "AllowWorkspaceCollaboration",
    "Effect": "Allow",
    "Action": [
        "iam:GetUser",
        "iam:GetRole",
        "iam:ListUsers",
        "iam:ListRoles",
        "sso:GetManagedApplicationInstance",
        "sso-directory:SearchUsers"
    ],
    "Resource": "*"
}
```

For more information, see [Create an EMR Studio service role](emr-studio-service-role.md "emr-studio-service-role.md").

###### To enable Workspace collaboration and add collaborators

1. In your Workspace, choose the **Collaboration** icon from
   the Launcher screen or the bottom of the left panel.

###### Note

You won't see the **Collaboration** panel unless your
Studio administator has given you permission to configure collaboration for the
Workspace. For more information, see [Set ownership for
Workspace collaboration](emr-studio-user-permissions.md#emr-studio-workspace-collaboration-permissions "emr-studio-user-permissions.md#emr-studio-workspace-collaboration-permissions"). 2. Make sure the **Allow Workspace collaboration** toggle is in
the on position. When you enable collaboration, only you and the collaborators that you
add can see the Workspace in the list on the Studio
**Workspaces** page. 3. Enter a **Collaborator name**. Your Workspace can have a
maximum of five collaborators including yourself. A collaborator can be any user with
access to your EMR Studio. If you don't enter a collaborator, the Workspace
is a private Workspace that is only accessible to you.

The following table specifies the applicable collaborator values to enter based on the
identity type of the owner.

###### Note

An owner can only invite collaborators with the same identity type. For example, a
user can only add other a users, and an IAM Identity Center user can only add other IAM Identity Center
users.

| Authentication mode | Value to enter for **Collaborator name**                                                                                                                                                                                                                                                            |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IAM authentication  | a username. This is the name that a user sees when logged in to the<br>AWS Management Console.                                                                                                                                                                                                      |
| IAM federation      | The name of an IAM role and an optional session name.<br>To add all of the federated users who assume the same IAM role, specify the<br>name of an IAM role for federation.<br>To add a single user as a collaborator, specify a role and session name. For<br>example, `MyRoleName:MySessionName`. |
| SSO                 | An IAM Identity Center user name like `user@example.com.`                                                                                                                                                                                                                                           |

4. Choose **Add**. The collaborator can now see the Workspace
   on their EMR Studio **Workspaces** page, and launch the
   Workspace to use it in real time with you.

###### Note

If you disable Workspace collaboration, the Workspace returns to its
shared state and can be seen by all Studio users. In the shared state, only one
Studio user can open and work in the Workspace at a time.
