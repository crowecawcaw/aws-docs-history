# Use `GetDefaultPatchBaseline` with a CLI

The following code examples show how to use `GetDefaultPatchBaseline`.

CLI

**AWS CLI**

**Example 1: To display the default Windows patch baseline**

The following `get-default-patch-baseline` example retrieves details for the default patch baseline for Windows Server.

```
`aws ssm get-default-patch-baseline`

```

Output:

```
{
  "BaselineId": "pb-0713accee01612345",
  "OperatingSystem": "WINDOWS"
}
```

**Example 2: To display the default patch baseline for Amazon Linux**

The following `get-default-patch-baseline` example retrieves details for the default patch baseline for Amazon Linux.

```
`aws ssm get-default-patch-baseline \
 --operating-system `AMAZON_LINUX``

```

Output:

```
{
    "BaselineId": "pb-047c6eb9c8fc12345",
    "OperatingSystem": "AMAZON_LINUX"
}
```

For more information, see About Predefined and Custom Patch Baselines <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-baselines.html>\_\_ and [Set an Existing Patch Baseline as the Default](set-default-patch-baseline.md "set-default-patch-baseline.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [GetDefaultPatchBaseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-default-patch-baseline.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-default-patch-baseline.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example displays the default patch baseline.**

```
Get-SSMDefaultPatchBaseline

```

**Output:**

```
arn:aws:ssm:us-west-2:123456789012:patchbaseline/pb-04fb4ae6142167966
```

- For API details, see
  [GetDefaultPatchBaseline](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example displays the default patch baseline.**

```
Get-SSMDefaultPatchBaseline

```

**Output:**

```
arn:aws:ssm:us-west-2:123456789012:patchbaseline/pb-04fb4ae6142167966
```

- For API details, see
  [GetDefaultPatchBaseline](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
