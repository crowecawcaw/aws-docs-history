# Use `DeregisterImage` with a CLI

The following code examples show how to use `DeregisterImage`.

CLI

**AWS CLI**

**To deregister an AMI**

This example deregisters the specified AMI. If the command succeeds, no output is returned.

Command:

```
`aws ec2 deregister-image --image-id `ami-4fa54026``

```

- For API details, see
  [DeregisterImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/deregister-image.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/deregister-image.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example deregisters the specified AMI.**

```
Unregister-EC2Image -ImageId ami-12345678

```

- For API details, see
  [DeregisterImage](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example deregisters the specified AMI.**

```
Unregister-EC2Image -ImageId ami-12345678

```

- For API details, see
  [DeregisterImage](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
