# Use `DeleteParameter` with a CLI

The following code examples show how to use `DeleteParameter`.

CLI

**AWS CLI**

**To delete a parameter**

The following `delete-parameter` example deletes the specified single parameter.

```
`aws ssm delete-parameter \
 --name `"MyParameter"``

```

This command produces no output.

For more information, see [Working with Parameter Store](parameter-store-working-with.md "parameter-store-working-with.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [DeleteParameter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-parameter.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-parameter.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example deletes a parameter. There is no output if the command succeeds.**

```
Remove-SSMParameter -Name "helloWorld"

```

- For API details, see
  [DeleteParameter](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example deletes a parameter. There is no output if the command succeeds.**

```
Remove-SSMParameter -Name "helloWorld"

```

- For API details, see
  [DeleteParameter](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
