# Use `DeleteAlias` with a CLI

The following code examples show how to use `DeleteAlias`.

CLI

**AWS CLI**

**To delete an alias of a Lambda function**

The following `delete-alias` example deletes the alias named `LIVE` from the `my-function` Lambda function.

```
`aws lambda delete-alias \
 --function-name `my-function` \
 --name `LIVE``

```

This command produces no output.

For more information, see [Configuring AWS Lambda Function Aliases](aliases-intro.md "aliases-intro.md") in the _AWS Lambda Developer Guide_.

- For API details, see
  [DeleteAlias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-alias.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-alias.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example deletes the Lambda function Alias mentioned in the command.**

```
Remove-LMAlias -FunctionName "MylambdaFunction123" -Name "NewAlias"

```

- For API details, see
  [DeleteAlias](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example deletes the Lambda function Alias mentioned in the command.**

```
Remove-LMAlias -FunctionName "MylambdaFunction123" -Name "NewAlias"

```

- For API details, see
  [DeleteAlias](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Lambda with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
