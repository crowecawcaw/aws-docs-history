# Use `PublishVersion` with a CLI

The following code examples show how to use `PublishVersion`.

CLI

**AWS CLI**

**To publish a new version of a function**

The following `publish-version` example publishes a new version of the `my-function` Lambda function.

```
`aws lambda publish-version \
 --function-name `my-function``

```

Output:

```
{
    "TracingConfig": {
        "Mode": "PassThrough"
    },
    "CodeSha256": "dBG9m8SGdmlEjw/JYXlhhvCrAv5TxvXsbL/RMr0fT/I=",
    "FunctionName": "my-function",
    "CodeSize": 294,
    "RevisionId": "f31d3d39-cc63-4520-97d4-43cd44c94c20",
    "MemorySize": 128,
    "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function:3",
    "Version": "2",
    "Role": "arn:aws:iam::123456789012:role/service-role/MyTestFunction-role-zgur6bf4",
    "Timeout": 3,
    "LastModified": "2019-09-23T18:32:33.857+0000",
    "Handler": "my-function.handler",
    "Runtime": "nodejs10.x",
    "Description": ""
}
```

For more information, see [Configuring AWS Lambda Function Aliases](aliases-intro.md "aliases-intro.md") in the _AWS Lambda Developer Guide_.

- For API details, see
  [PublishVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/publish-version.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/publish-version.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example creates a version for the existing snapshot of Lambda Function Code**

```
Publish-LMVersion -FunctionName "MylambdaFunction123" -Description "Publishing Existing Snapshot of function code as a  new version through Powershell"

```

- For API details, see
  [PublishVersion](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example creates a version for the existing snapshot of Lambda Function Code**

```
Publish-LMVersion -FunctionName "MylambdaFunction123" -Description "Publishing Existing Snapshot of function code as a  new version through Powershell"

```

- For API details, see
  [PublishVersion](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Lambda with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
