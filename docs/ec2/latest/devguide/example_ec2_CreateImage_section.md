

# Use `CreateImage` with a CLI
<a name="example_ec2_CreateImage_section"></a>

The following code examples show how to use `CreateImage`.

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To create an AMI from an Amazon EBS-backed instance**  
The following `create-image` example creates an AMI from the specified instance.  

```
aws ec2 create-image \
    --instance-id {{i-1234567890abcdef0}} \
    --name {{"My server"}} \
    --description {{"An AMI for my server"}}
```
Output:  

```
{
    "ImageId": "ami-abcdef01234567890"
}
```
For more information about specifying a block device mapping for your AMI, see [Specifying a block device mapping for an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html#create-ami-bdm) in the *Amazon EC2 User Guide*.  
**Example 2: To create an AMI from an Amazon EBS-backed instance without reboot**  
The following `create-image` example creates an AMI and sets the --no-reboot parameter, so that the instance is not rebooted before the image is created.  

```
aws ec2 create-image \
    --instance-id {{i-1234567890abcdef0}} \
    --name {{"My server"}} \
    --no-reboot
```
Output:  

```
{
    "ImageId": "ami-abcdef01234567890"
}
```
For more information about specifying a block device mapping for your AMI, see [Specifying a block device mapping for an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html#create-ami-bdm) in the *Amazon EC2 User Guide*.  
**Example 3: To tag an AMI and snapshots on creation**  
The following `create-image` example creates an AMI, and tags the AMI and the snapshots with the same tag `cost-center=cc123`  

```
aws ec2 create-image \
    --instance-id {{i-1234567890abcdef0}} \
    --name {{"My server"}} \
    --tag-specifications {{"ResourceType=image,Tags=[{Key=cost-center,Value=cc123}]"}} {{"ResourceType=snapshot,Tags=[{Key=cost-center,Value=cc123}]"}}
```
Output:  

```
{
    "ImageId": "ami-abcdef01234567890"
}
```
For more information about tagging your resources on creation, see [Add tags on resource creation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-on-create-examples) in the *Amazon EC2 User Guide*.  
+  For API details, see [CreateImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-image.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example creates an AMI with the specified name and description, from the specified instance. Amazon EC2 attempts to cleanly shut down the instance before creating the image, and restarts the instance on completion.**  

```
New-EC2Image -InstanceId i-12345678 -Name "my-web-server" -Description "My web server AMI"
```
**Example 2: This example creates an AMI with the specified name and description, from the specified instance. Amazon EC2 creates the image without shutting down and restarting the instance; therefore, file system integrity on the created image can't be guaranteed.**  

```
New-EC2Image -InstanceId i-12345678 -Name "my-web-server" -Description "My web server AMI" -NoReboot $true
```
**Example 3: This example creates an AMI with three volumes. The first volume is based on an Amazon EBS snapshot. The second volume is an empty 100 GiB Amazon EBS volume. The third volume is an instance store volume. The syntax used by this example requires PowerShell version 3 or higher.**  

```
$ebsBlock1 = @{SnapshotId="snap-1a2b3c4d"}
$ebsBlock2 = @{VolumeSize=100}

New-EC2Image -InstanceId i-12345678 -Name "my-web-server" -Description "My web server AMI" -BlockDeviceMapping @( @{DeviceName="/dev/sdf";Ebs=$ebsBlock1}, @{DeviceName="/dev/sdg";Ebs=$ebsBlock2}, @{DeviceName="/dev/sdc";VirtualName="ephemeral0"})
```
+  For API details, see [CreateImage](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example creates an AMI with the specified name and description, from the specified instance. Amazon EC2 attempts to cleanly shut down the instance before creating the image, and restarts the instance on completion.**  

```
New-EC2Image -InstanceId i-12345678 -Name "my-web-server" -Description "My web server AMI"
```
**Example 2: This example creates an AMI with the specified name and description, from the specified instance. Amazon EC2 creates the image without shutting down and restarting the instance; therefore, file system integrity on the created image can't be guaranteed.**  

```
New-EC2Image -InstanceId i-12345678 -Name "my-web-server" -Description "My web server AMI" -NoReboot $true
```
**Example 3: This example creates an AMI with three volumes. The first volume is based on an Amazon EBS snapshot. The second volume is an empty 100 GiB Amazon EBS volume. The third volume is an instance store volume. The syntax used by this example requires PowerShell version 3 or higher.**  

```
$ebsBlock1 = @{SnapshotId="snap-1a2b3c4d"}
$ebsBlock2 = @{VolumeSize=100}

New-EC2Image -InstanceId i-12345678 -Name "my-web-server" -Description "My web server AMI" -BlockDeviceMapping @( @{DeviceName="/dev/sdf";Ebs=$ebsBlock1}, @{DeviceName="/dev/sdg";Ebs=$ebsBlock2}, @{DeviceName="/dev/sdc";VirtualName="ephemeral0"})
```
+  For API details, see [CreateImage](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.