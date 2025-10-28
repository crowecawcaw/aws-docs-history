# Use `ModifyInstanceAttribute` with a CLI

The following code examples show how to use `ModifyInstanceAttribute`.

CLI

**AWS CLI**

**Example 1: To modify the instance type**

The following `modify-instance-attribute` example modifies the instance type of the specified instance. The instance must be in the `stopped` state.

```
`aws ec2 modify-instance-attribute \
 --instance-id `i-1234567890abcdef0` \
 --instance-type "{\"Value\": \"m1.small\"}"`

```

This command produces no output.

**Example 2: To enable enhanced networking on an instance**

The following `modify-instance-attribute` example enables enhanced networking for the specified instance. The instance must be in the `stopped` state.

```
`aws ec2 modify-instance-attribute \
 --instance-id `i-1234567890abcdef0` \
 --sriov-net-support `simple``

```

This command produces no output.

**Example 3: To modify the sourceDestCheck attribute**

The following `modify-instance-attribute` example sets the `sourceDestCheck` attribute of the specified instance to `true`. The instance must be in a VPC.

```
`aws ec2 modify-instance-attribute --instance-id `i-1234567890abcdef0` --source-dest-check "{\"Value\": true}"`

```

This command produces no output.

**Example 4: To modify the deleteOnTermination attribute of the root volume**

The following `modify-instance-attribute` example sets the `deleteOnTermination` attribute for the root volume of the specified Amazon EBS-backed instance to `false`. By default, this attribute is `true` for the root volume.

Command:

```
`aws ec2 modify-instance-attribute \
 --instance-id `i-1234567890abcdef0` \
 --block-device-mappings "[{\"DeviceName\": \"/dev/sda1\",\"Ebs\":{\"DeleteOnTermination\":false}}]"`

```

This command produces no output.

**Example 5: To modify the user data attached to an instance**

The following `modify-instance-attribute` example adds the contents of the file `UserData.txt` as the UserData for the specified instance.

Contents of original file `UserData.txt`:

```
#!/bin/bash
yum update -y
service httpd start
chkconfig httpd on
```

The contents of the file must be base64 encoded. The first command converts the text file to base64 and saves it as a new file.

Linux/macOS version of the command:

```
base64 UserData.txt > UserData.base64.txt
```

This command produces no output.

Windows version of the command:

```
certutil -encode UserData.txt tmp.b64 && findstr /v /c:- tmp.b64 > UserData.base64.txt
```

Output:

```
Input Length = 67
Output Length = 152
CertUtil: -encode command completed successfully.
```

Now you can reference that file in the CLI command that follows:

```
`aws ec2 modify-instance-attribute \
 --instance-id=i-09b5a14dbca622e76 \
 --attribute `userData` --value `file://UserData.base64.txt``

```

This command produces no output.

For more information, see [User Data and the AWS CLI](../../../AWSEC2/latest/UserGuide/user-data.md#user-data-api-cli "../../../AWSEC2/latest/UserGuide/user-data.md#user-data-api-cli") in the _EC2 User Guide_.

- For API details, see
  [ModifyInstanceAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-attribute.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-attribute.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example modifies the instance type of the specified instance.**

```
Edit-EC2InstanceAttribute -InstanceId i-12345678 -InstanceType m3.medium

```

**Example 2: This example enables enhanced networking for the specified instance, by specifying "simple" as the value of the single root I/O virtualization (SR-IOV) network support parameter, -SriovNetSupport..**

```
Edit-EC2InstanceAttribute -InstanceId i-12345678 -SriovNetSupport "simple"

```

**Example 3: This example modifies the security groups for the specified instance. The instance must be in a VPC. You must specify the ID of each security group, not the name.**

```
Edit-EC2InstanceAttribute -InstanceId i-12345678 -Group @( "sg-12345678", "sg-45678901" )

```

**Example 4: This example enables EBS I/O optimization for the specified instance. This feature isn't available with all instance types. Additional usage charges apply when using an EBS-optimized instance.**

```
Edit-EC2InstanceAttribute -InstanceId i-12345678 -EbsOptimized $true

```

**Example 5: This example enables source/destination checking for the specified instance. For a NAT instance to perform NAT, the value must be 'false'.**

```
Edit-EC2InstanceAttribute -InstanceId i-12345678 -SourceDestCheck $true

```

**Example 6: This example disables termination for the specified instance.**

```
Edit-EC2InstanceAttribute -InstanceId i-12345678 -DisableApiTermination $true

```

**Example 7: This example changes the specified instance so that it terminates when shutdown is initiated from the instance.**

```
Edit-EC2InstanceAttribute -InstanceId i-12345678 -InstanceInitiatedShutdownBehavior terminate

```

- For API details, see
  [ModifyInstanceAttribute](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example modifies the instance type of the specified instance.**

```
Edit-EC2InstanceAttribute -InstanceId i-12345678 -InstanceType m3.medium

```

**Example 2: This example enables enhanced networking for the specified instance, by specifying "simple" as the value of the single root I/O virtualization (SR-IOV) network support parameter, -SriovNetSupport..**

```
Edit-EC2InstanceAttribute -InstanceId i-12345678 -SriovNetSupport "simple"

```

**Example 3: This example modifies the security groups for the specified instance. The instance must be in a VPC. You must specify the ID of each security group, not the name.**

```
Edit-EC2InstanceAttribute -InstanceId i-12345678 -Group @( "sg-12345678", "sg-45678901" )

```

**Example 4: This example enables EBS I/O optimization for the specified instance. This feature isn't available with all instance types. Additional usage charges apply when using an EBS-optimized instance.**

```
Edit-EC2InstanceAttribute -InstanceId i-12345678 -EbsOptimized $true

```

**Example 5: This example enables source/destination checking for the specified instance. For a NAT instance to perform NAT, the value must be 'false'.**

```
Edit-EC2InstanceAttribute -InstanceId i-12345678 -SourceDestCheck $true

```

**Example 6: This example disables termination for the specified instance.**

```
Edit-EC2InstanceAttribute -InstanceId i-12345678 -DisableApiTermination $true

```

**Example 7: This example changes the specified instance so that it terminates when shutdown is initiated from the instance.**

```
Edit-EC2InstanceAttribute -InstanceId i-12345678 -InstanceInitiatedShutdownBehavior terminate

```

- For API details, see
  [ModifyInstanceAttribute](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
