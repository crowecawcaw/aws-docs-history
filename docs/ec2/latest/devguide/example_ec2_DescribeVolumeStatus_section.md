# Use `DescribeVolumeStatus` with a CLI

The following code examples show how to use `DescribeVolumeStatus`.

CLI

**AWS CLI**

**To describe the status of a single volume**

This example command describes the status for the volume `vol-1234567890abcdef0`.

Command:

```
`aws ec2 describe-volume-status --volume-ids `vol-1234567890abcdef0``

```

Output:

```
{
    "VolumeStatuses": [
        {
            "VolumeStatus": {
                "Status": "ok",
                "Details": [
                    {
                        "Status": "passed",
                        "Name": "io-enabled"
                    },
                    {
                        "Status": "not-applicable",
                        "Name": "io-performance"
                    }
                ]
            },
            "AvailabilityZone": "us-east-1a",
            "VolumeId": "vol-1234567890abcdef0",
            "Actions": [],
            "Events": []
        }
    ]
}
```

**To describe the status of impaired volumes**

This example command describes the status for all volumes that are impaired. In this example output, there are no impaired volumes.

Command:

```
`aws ec2 describe-volume-status --filters `Name=volume-status.status,Values=impaired``

```

Output:

```
{
    "VolumeStatuses": []
}
```

If you have a volume with a failed status check (status is impaired), see Working with an Impaired Volume in the _Amazon EC2 User Guide_.

- For API details, see
  [DescribeVolumeStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-volume-status.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-volume-status.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example describes the status of the specified volume.**

```
Get-EC2VolumeStatus -VolumeId vol-12345678

```

**Output:**

```
Actions          : {}
AvailabilityZone : us-west-2a
Events           : {}
VolumeId         : vol-12345678
VolumeStatus     : Amazon.EC2.Model.VolumeStatusInfo
```

```
(Get-EC2VolumeStatus -VolumeId vol-12345678).VolumeStatus

```

**Output:**

```
Details                         Status
-------                         ------
{io-enabled, io-performance}    ok
```

```
(Get-EC2VolumeStatus -VolumeId vol-12345678).VolumeStatus.Details

```

**Output:**

```
Name                            Status
----                            ------
io-enabled                      passed
io-performance                  not-applicable
```

- For API details, see
  [DescribeVolumeStatus](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example describes the status of the specified volume.**

```
Get-EC2VolumeStatus -VolumeId vol-12345678

```

**Output:**

```
Actions          : {}
AvailabilityZone : us-west-2a
Events           : {}
VolumeId         : vol-12345678
VolumeStatus     : Amazon.EC2.Model.VolumeStatusInfo
```

```
(Get-EC2VolumeStatus -VolumeId vol-12345678).VolumeStatus

```

**Output:**

```
Details                         Status
-------                         ------
{io-enabled, io-performance}    ok
```

```
(Get-EC2VolumeStatus -VolumeId vol-12345678).VolumeStatus.Details

```

**Output:**

```
Name                            Status
----                            ------
io-enabled                      passed
io-performance                  not-applicable
```

- For API details, see
  [DescribeVolumeStatus](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
