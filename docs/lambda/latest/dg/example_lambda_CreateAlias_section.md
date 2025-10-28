# Use `CreateAlias` with a CLI

The following code examples show how to use `CreateAlias`.

CLI

**AWS CLI**

**To create an alias for a Lambda function**

The following `create-alias` example creates an alias named `LIVE` that points to version 1 of the `my-function` Lambda function.

```
`aws lambda create-alias \
 --function-name `my-function` \
 --description `"alias for live version of function"` \
 --function-version `1` \
 --name `LIVE``

```

Output:

```
{
    "FunctionVersion": "1",
    "Name": "LIVE",
    "AliasArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function:LIVE",
    "RevisionId": "873282ed-4cd3-4dc8-a069-d0c647e470c6",
    "Description": "alias for live version of function"
}
```

For more information, see [Configuring AWS Lambda Function Aliases](aliases-intro.md "aliases-intro.md") in the _AWS Lambda Developer Guide_.

- For API details, see
  [CreateAlias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-alias.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-alias.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example creates a New Lambda Alias for specified version and routing configuration to specify the percentage of invocation requests that it receives.**

```
New-LMAlias -FunctionName "MylambdaFunction123" -RoutingConfig_AdditionalVersionWeight @{Name="1";Value="0.6} -Description "Alias for version 4" -FunctionVersion 4 -Name "PowershellAlias"

```

- For API details, see
  [CreateAlias](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example creates a New Lambda Alias for specified version and routing configuration to specify the percentage of invocation requests that it receives.**

```
New-LMAlias -FunctionName "MylambdaFunction123" -RoutingConfig_AdditionalVersionWeight @{Name="1";Value="0.6} -Description "Alias for version 4" -FunctionVersion 4 -Name "PowershellAlias"

```

- For API details, see
  [CreateAlias](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Lambda with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
