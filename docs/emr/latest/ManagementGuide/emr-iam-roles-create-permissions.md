# Allow users and groups to create and

modify roles

IAM principals (users and groups) who create, modify, and specify roles for a
cluster, including default roles, must be allowed to perform the following actions. For
details about each action, see [Actions](../../../IAM/latest/APIReference/API_Operations.md "../../../IAM/latest/APIReference/API_Operations.md") in the _IAM API Reference_.

- `iam:CreateRole`
- `iam:PutRolePolicy`
- `iam:CreateInstanceProfile`
- `iam:AddRoleToInstanceProfile`
- `iam:ListRoles`
- `iam:GetPolicy`
- `iam:GetInstanceProfile`
- `iam:GetPolicyVersion`
- `iam:AttachRolePolicy`
- `iam:PassRole`
  The `iam:PassRole` permission allows cluster creation. The remaining
  permissions allow the creation of the default roles.

For information about assigning permissions to a user, see [Changing
permissions for a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md "../../../IAM/latest/UserGuide/id_users_change-permissions.md") in the _IAM User Guide_.
