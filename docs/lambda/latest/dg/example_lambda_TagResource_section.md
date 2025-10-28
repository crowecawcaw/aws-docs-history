# Use `TagResource` with a CLI

The following code examples show how to use `TagResource`.

CLI

**AWS CLI**

**To add tags to an existing Lambda function**

The following `tag-resource` example adds a tag with the key name `DEPARTMENT` and a value of `Department A` to the specified Lambda function.

```
`aws lambda tag-resource \
 --resource `arn:aws:lambda:us-west-2:123456789012:function:my-function` \
 --tags `"DEPARTMENT=Department A"``

```

This command produces no output.

For more information, see [Tagging Lambda Functions](tagging.md "tagging.md") in the _AWS Lambda Developer Guide_.

- For API details, see
  [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/tag-resource.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/tag-resource.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: Adds the three tags (Washington, Oregon and California) and their associated values to the specified function identified by its ARN.**

```
Add-LMResourceTag -Resource "arn:aws:lambda:us-west-2:123456789012:function:MyFunction" -Tag @{ "Washington" = "Olympia"; "Oregon" = "Salem"; "California" = "Sacramento" }

```

- For API details, see
  [TagResource](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: Adds the three tags (Washington, Oregon and California) and their associated values to the specified function identified by its ARN.**

```
Add-LMResourceTag -Resource "arn:aws:lambda:us-west-2:123456789012:function:MyFunction" -Tag @{ "Washington" = "Olympia"; "Oregon" = "Salem"; "California" = "Sacramento" }

```

- For API details, see
  [TagResource](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Lambda with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
