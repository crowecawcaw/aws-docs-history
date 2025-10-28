# Use `GetFunctionConcurrency` with a CLI

The following code examples show how to use `GetFunctionConcurrency`.

CLI

**AWS CLI**

**To view the reserved concurrency setting for a function**

The following `get-function-concurrency` example retrieves the reserved concurrency setting for the specified function.

```
`aws lambda get-function-concurrency \
 --function-name `my-function``

```

Output:

```
{
    "ReservedConcurrentExecutions": 250
}
```

- For API details, see
  [GetFunctionConcurrency](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-concurrency.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-concurrency.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This examples gets the Reserved concurrency for the Lambda Function**

```
Get-LMFunctionConcurrency -FunctionName "MylambdaFunction123" -Select *

```

**Output:**

```
ReservedConcurrentExecutions
----------------------------
100
```

- For API details, see
  [GetFunctionConcurrency](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This examples gets the Reserved concurrency for the Lambda Function**

```
Get-LMFunctionConcurrency -FunctionName "MylambdaFunction123" -Select *

```

**Output:**

```
ReservedConcurrentExecutions
----------------------------
100
```

- For API details, see
  [GetFunctionConcurrency](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Lambda with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
