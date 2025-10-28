# Use `PutUserPermissionsBoundary` with a CLI

The following code examples show how to use `PutUserPermissionsBoundary`.

CLI

**AWS CLI**

**Example 1: To apply a permissions boundary based on a custom policy to an IAM user**

The following `put-user-permissions-boundary` example applies a custom policy named `intern-boundary` as the permissions boundary for the specified IAM user.

```
`aws iam put-user-permissions-boundary \
 --permissions-boundary `arn:aws:iam::123456789012:policy/intern-boundary` \
 --user-name `intern``

```

This command produces no output.

**Example 2: To apply a permissions boundary based on an AWS managed policy to an IAM user**

The following `put-user-permissions-boundary` example applies the AWS managed pollicy named `PowerUserAccess` as the permissions boundary for the specified IAM user.

```
`aws iam put-user-permissions-boundary \
 --permissions-boundary `arn:aws:iam::aws:policy/PowerUserAccess` \
 --user-name `developer``

```

This command produces no output.

For more information, see [Adding and removing IAM identity permissions](access_policies_manage-attach-detach.md "access_policies_manage-attach-detach.md") in the _AWS IAM User Guide_.

- For API details, see
  [PutUserPermissionsBoundary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-user-permissions-boundary.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-user-permissions-boundary.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example shows how to set the Permission boundary for the user. You can set AWS Managed policies or Custom policies as permission boundary.**

```
Set-IAMUserPermissionsBoundary -UserName joe -PermissionsBoundary arn:aws:iam::123456789012:policy/intern-boundary

```

- For API details, see
  [PutUserPermissionsBoundary](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example shows how to set the Permission boundary for the user. You can set AWS Managed policies or Custom policies as permission boundary.**

```
Set-IAMUserPermissionsBoundary -UserName joe -PermissionsBoundary arn:aws:iam::123456789012:policy/intern-boundary

```

- For API details, see
  [PutUserPermissionsBoundary](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
