# Use `ReleaseHosts` with a CLI

The following code examples show how to use `ReleaseHosts`.

CLI

**AWS CLI**

**To release a Dedicated host from your account**

To release a Dedicated host from your account. Instances that are on the host must be stopped or terminated before the host can be released.

Command:

```
`aws ec2 release-hosts --host-id=h-0029d6e3cacf1b3da`

```

Output:

```
{
    "Successful":  [
        "h-0029d6e3cacf1b3da"
         ],
  "Unsuccessful": []

 }
```

- For API details, see
  [ReleaseHosts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/release-hosts.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/release-hosts.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example releases the given host ID h-0badafd1dcb2f3456**

```
Remove-EC2Host -HostId h-0badafd1dcb2f3456

```

**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EC2Host (ReleaseHosts)" on target "h-0badafd1dcb2f3456".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y

Successful            Unsuccessful
----------            ------------
{h-0badafd1dcb2f3456} {}
```

- For API details, see
  [ReleaseHosts](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example releases the given host ID h-0badafd1dcb2f3456**

```
Remove-EC2Host -HostId h-0badafd1dcb2f3456

```

**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EC2Host (ReleaseHosts)" on target "h-0badafd1dcb2f3456".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y

Successful            Unsuccessful
----------            ------------
{h-0badafd1dcb2f3456} {}
```

- For API details, see
  [ReleaseHosts](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
