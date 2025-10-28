# Use `ResetInstanceAttribute` with a CLI

The following code examples show how to use `ResetInstanceAttribute`.

CLI

**AWS CLI**

**To reset the sourceDestCheck attribute**

This example resets the `sourceDestCheck` attribute of the specified instance. The instance must be in a VPC. If the command succeeds, no output is returned.

Command:

```
`aws ec2 reset-instance-attribute --instance-id `i-1234567890abcdef0` --attribute `sourceDestCheck``

```

**To reset the kernel attribute**

This example resets the `kernel` attribute of the specified instance. The instance must be in the `stopped` state. If the command succeeds, no output is returned.

Command:

```
`aws ec2 reset-instance-attribute --instance-id `i-1234567890abcdef0` --attribute `kernel``

```

**To reset the ramdisk attribute**

This example resets the `ramdisk` attribute of the specified instance. The instance must be in the `stopped` state. If the command succeeds, no output is returned.

Command:

```
`aws ec2 reset-instance-attribute --instance-id `i-1234567890abcdef0` --attribute `ramdisk``

```

- For API details, see
  [ResetInstanceAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-instance-attribute.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-instance-attribute.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example resets the 'sriovNetSupport' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute sriovNetSupport

```

**Example 2: This example resets the 'ebsOptimized' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute ebsOptimized

```

**Example 3: This example resets the 'sourceDestCheck' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute sourceDestCheck

```

**Example 4: This example resets the 'disableApiTermination' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute disableApiTermination

```

**Example 5: This example resets the 'instanceInitiatedShutdownBehavior' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute instanceInitiatedShutdownBehavior

```

- For API details, see
  [ResetInstanceAttribute](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example resets the 'sriovNetSupport' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute sriovNetSupport

```

**Example 2: This example resets the 'ebsOptimized' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute ebsOptimized

```

**Example 3: This example resets the 'sourceDestCheck' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute sourceDestCheck

```

**Example 4: This example resets the 'disableApiTermination' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute disableApiTermination

```

**Example 5: This example resets the 'instanceInitiatedShutdownBehavior' attribute for the specified instance.**

```
Reset-EC2InstanceAttribute -InstanceId i-12345678 -Attribute instanceInitiatedShutdownBehavior

```

- For API details, see
  [ResetInstanceAttribute](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
