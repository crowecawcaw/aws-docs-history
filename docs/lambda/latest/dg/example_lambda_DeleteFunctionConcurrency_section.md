# Use `DeleteFunctionConcurrency` with a CLI

The following code examples show how to use `DeleteFunctionConcurrency`.

CLI

**AWS CLI**

**To remove the reserved concurrent execution limit from a function**

The following `delete-function-concurrency` example deletes the reserved concurrent execution limit from the `my-function` function.

```
`aws lambda delete-function-concurrency \
 --function-name `my-function``

```

This command produces no output.

For more information, see [Reserving Concurrency for a Lambda Function](per-function-concurrency.md "per-function-concurrency.md") in the _AWS Lambda Developer Guide_.

- For API details, see
  [DeleteFunctionConcurrency](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-function-concurrency.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-function-concurrency.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This examples removes the Function Concurrency of the Lambda Function.**

```
Remove-LMFunctionConcurrency -FunctionName "MylambdaFunction123"

```

- For API details, see
  [DeleteFunctionConcurrency](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This examples removes the Function Concurrency of the Lambda Function.**

```
Remove-LMFunctionConcurrency -FunctionName "MylambdaFunction123"

```

- For API details, see
  [DeleteFunctionConcurrency](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Lambda with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
