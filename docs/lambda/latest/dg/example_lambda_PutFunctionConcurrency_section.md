# Use `PutFunctionConcurrency` with a CLI

The following code examples show how to use `PutFunctionConcurrency`.

CLI

**AWS CLI**

**To configure a reserved concurrency limit for a function**

The following `put-function-concurrency` example configures 100 reserved concurrent executions for the `my-function` function.

```
`aws lambda put-function-concurrency \
 --function-name `my-function` \
 --reserved-concurrent-executions `100``

```

Output:

```
{
    "ReservedConcurrentExecutions": 100
}
```

For more information, see [Reserving Concurrency for a Lambda Function](per-function-concurrency.md "per-function-concurrency.md") in the _AWS Lambda Developer Guide_.

- For API details, see
  [PutFunctionConcurrency](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-function-concurrency.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-function-concurrency.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example applies the concurrency settings for the Function as a whole.**

```
Write-LMFunctionConcurrency -FunctionName "MylambdaFunction123" -ReservedConcurrentExecution 100

```

- For API details, see
  [PutFunctionConcurrency](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example applies the concurrency settings for the Function as a whole.**

```
Write-LMFunctionConcurrency -FunctionName "MylambdaFunction123" -ReservedConcurrentExecution 100

```

- For API details, see
  [PutFunctionConcurrency](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Lambda with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
