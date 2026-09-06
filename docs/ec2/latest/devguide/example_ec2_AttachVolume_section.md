

# Use `AttachVolume` with a CLI
<a name="example_ec2_AttachVolume_section"></a>

The following code examples show how to use `AttachVolume`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Creating and managing block storage volumes](example_ec2_GettingStarted_020_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To attach a volume to an instance**  
This example command attaches a volume (`vol-1234567890abcdef0`) to an instance (`i-01474ef662b89480`) as `/dev/sdf`.  
Command:  

```
aws ec2 attach-volume --volume-id {{vol-1234567890abcdef0}} --instance-id {{i-01474ef662b89480}} --device {{/dev/sdf}}
```
Output:  

```
{
    "AttachTime": "YYYY-MM-DDTHH:MM:SS.000Z",
    "InstanceId": "i-01474ef662b89480",
    "VolumeId": "vol-1234567890abcdef0",
    "State": "attaching",
    "Device": "/dev/sdf"
}
```
+  For API details, see [AttachVolume](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-volume.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example attaches the specified volume to the specified instance and exposes it with the specified device name.**  

```
Add-EC2Volume -VolumeId vol-12345678 -InstanceId i-1a2b3c4d -Device /dev/sdh
```
**Output:**  

```
AttachTime          : 12/22/2015 1:53:58 AM
DeleteOnTermination : False
Device              : /dev/sdh
InstanceId          : i-1a2b3c4d
State               : attaching
VolumeId            : vol-12345678
```
+  For API details, see [AttachVolume](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example attaches the specified volume to the specified instance and exposes it with the specified device name.**  

```
Add-EC2Volume -VolumeId vol-12345678 -InstanceId i-1a2b3c4d -Device /dev/sdh
```
**Output:**  

```
AttachTime          : 12/22/2015 1:53:58 AM
DeleteOnTermination : False
Device              : /dev/sdh
InstanceId          : i-1a2b3c4d
State               : attaching
VolumeId            : vol-12345678
```
+  For API details, see [AttachVolume](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.