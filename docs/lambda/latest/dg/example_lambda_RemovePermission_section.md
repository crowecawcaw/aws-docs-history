# Use `RemovePermission` with a CLI

The following code examples show how to use `RemovePermission`.

CLI

**AWS CLI**

**To remove permissions from an existing Lambda function**

The following `remove-permission` example removes permission to invoke a function named `my-function`.

```
`aws lambda remove-permission \
 --function-name `my-function` \
 --statement-id `sns``

```

This command produces no output.

For more information, see [Using Resource-based Policies for AWS Lambda](access-control-resource-based.md "access-control-resource-based.md") in the _AWS Lambda Developer Guide_.

- For API details, see
  [RemovePermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/remove-permission.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/remove-permission.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example removes the function policy for the specified StatementId of a Lambda Function.**

```
$policy =  Get-LMPolicy -FunctionName "MylambdaFunction123" -Select Policy | ConvertFrom-Json| Select-Object -ExpandProperty Statement
Remove-LMPermission -FunctionName "MylambdaFunction123" -StatementId $policy[0].Sid

```

- For API details, see
  [RemovePermission](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example removes the function policy for the specified StatementId of a Lambda Function.**

```
$policy =  Get-LMPolicy -FunctionName "MylambdaFunction123" -Select Policy | ConvertFrom-Json| Select-Object -ExpandProperty Statement
Remove-LMPermission -FunctionName "MylambdaFunction123" -StatementId $policy[0].Sid

```

- For API details, see
  [RemovePermission](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Lambda with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
