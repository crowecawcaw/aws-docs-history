# Use `DescribeInstanceAttribute` with a CLI

The following code examples show how to use `DescribeInstanceAttribute`.

CLI

**AWS CLI**

**To describe the instance type**

This example describes the instance type of the specified instance.

Command:

```
`aws ec2 describe-instance-attribute --instance-id `i-1234567890abcdef0` --attribute `instanceType``

```

Output:

```
{
    "InstanceId": "i-1234567890abcdef0"
    "InstanceType": {
        "Value": "t1.micro"
    }
}
```

**To describe the disableApiTermination attribute**

This example describes the `disableApiTermination` attribute of the specified instance.

Command:

```
`aws ec2 describe-instance-attribute --instance-id `i-1234567890abcdef0` --attribute `disableApiTermination``

```

Output:

```
{
"InstanceId": "i-1234567890abcdef0"
    "DisableApiTermination": {
        "Value": "false"
    }
}
```

**To describe the block device mapping for an instance**

This example describes the `blockDeviceMapping` attribute of the specified instance.

Command:

```
`aws ec2 describe-instance-attribute --instance-id `i-1234567890abcdef0` --attribute `blockDeviceMapping``

```

Output:

```
{
    "InstanceId": "i-1234567890abcdef0"
    "BlockDeviceMappings": [
        {
            "DeviceName": "/dev/sda1",
            "Ebs": {
                "Status": "attached",
                "DeleteOnTermination": true,
                "VolumeId": "vol-049df61146c4d7901",
                "AttachTime": "2013-05-17T22:42:34.000Z"
            }
        },
        {
            "DeviceName": "/dev/sdf",
            "Ebs": {
                "Status": "attached",
                "DeleteOnTermination": false,
                "VolumeId": "vol-049df61146c4d7901",
                "AttachTime": "2013-09-10T23:07:00.000Z"
            }
        }
    ],
}
```

- For API details, see
  [DescribeInstanceAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-attribute.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-attribute.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example describes the instance type of the specified instance.**

```
Get-EC2InstanceAttribute -InstanceId i-12345678 -Attribute instanceType

```

**Output:**

```
InstanceType                      : t2.micro
```

**Example 2: This example describes whether enhanced networking is enabled for the specified instance.**

```
Get-EC2InstanceAttribute -InstanceId i-12345678 -Attribute sriovNetSupport

```

**Output:**

```
SriovNetSupport                   : simple
```

**Example 3: This example describes the security groups for the specified instance.**

```
(Get-EC2InstanceAttribute -InstanceId i-12345678 -Attribute groupSet).Groups

```

**Output:**

```
GroupId
-------
sg-12345678
sg-45678901
```

**Example 4: This example describes whether EBS optimization is enabled for the specified instance.**

```
Get-EC2InstanceAttribute -InstanceId i-12345678 -Attribute ebsOptimized

```

**Output:**

```
EbsOptimized                      : False
```

**Example 5: This example describes the 'disableApiTermination' attribute of the specified instance.**

```
Get-EC2InstanceAttribute -InstanceId i-12345678 -Attribute disableApiTermination

```

**Output:**

```
DisableApiTermination             : False
```

**Example 6: This example describes the 'instanceInitiatedShutdownBehavior' attribute of the specified instance.**

```
Get-EC2InstanceAttribute -InstanceId i-12345678 -Attribute instanceInitiatedShutdownBehavior

```

**Output:**

```
InstanceInitiatedShutdownBehavior : stop
```

- For API details, see
  [DescribeInstanceAttribute](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example describes the instance type of the specified instance.**

```
Get-EC2InstanceAttribute -InstanceId i-12345678 -Attribute instanceType

```

**Output:**

```
InstanceType                      : t2.micro
```

**Example 2: This example describes whether enhanced networking is enabled for the specified instance.**

```
Get-EC2InstanceAttribute -InstanceId i-12345678 -Attribute sriovNetSupport

```

**Output:**

```
SriovNetSupport                   : simple
```

**Example 3: This example describes the security groups for the specified instance.**

```
(Get-EC2InstanceAttribute -InstanceId i-12345678 -Attribute groupSet).Groups

```

**Output:**

```
GroupId
-------
sg-12345678
sg-45678901
```

**Example 4: This example describes whether EBS optimization is enabled for the specified instance.**

```
Get-EC2InstanceAttribute -InstanceId i-12345678 -Attribute ebsOptimized

```

**Output:**

```
EbsOptimized                      : False
```

**Example 5: This example describes the 'disableApiTermination' attribute of the specified instance.**

```
Get-EC2InstanceAttribute -InstanceId i-12345678 -Attribute disableApiTermination

```

**Output:**

```
DisableApiTermination             : False
```

**Example 6: This example describes the 'instanceInitiatedShutdownBehavior' attribute of the specified instance.**

```
Get-EC2InstanceAttribute -InstanceId i-12345678 -Attribute instanceInitiatedShutdownBehavior

```

**Output:**

```
InstanceInitiatedShutdownBehavior : stop
```

- For API details, see
  [DescribeInstanceAttribute](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
