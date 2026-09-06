

# Use `DetachVolume` with a CLI
<a name="example_ec2_DetachVolume_section"></a>

The following code examples show how to use `DetachVolume`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples: 
+  [Creating and managing block storage volumes](example_ec2_GettingStarted_020_section.md) 
+  [Working with block storage encryption, snapshots, and volume initialization](example_ec2_GettingStarted_022_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To detach a volume from an instance**  
This example command detaches the volume (`vol-049df61146c4d7901`) from the instance it is attached to.  
Command:  

```
aws ec2 detach-volume --volume-id {{vol-1234567890abcdef0}}
```
Output:  

```
{
    "AttachTime": "2014-02-27T19:23:06.000Z",
    "InstanceId": "i-1234567890abcdef0",
    "VolumeId": "vol-049df61146c4d7901",
    "State": "detaching",
    "Device": "/dev/sdb"
}
```
+  For API details, see [DetachVolume](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-volume.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example detaches the specified volume.**  

```
Dismount-EC2Volume -VolumeId vol-12345678
```
**Output:**  

```
AttachTime          : 12/22/2015 1:53:58 AM
DeleteOnTermination : False
Device              : /dev/sdh
InstanceId          : i-1a2b3c4d
State               : detaching
VolumeId            : vol-12345678
```
**Example 2: You can also specify the instance ID and device name to ensure that you are detaching the correct volume.**  

```
Dismount-EC2Volume -VolumeId vol-12345678 -InstanceId i-1a2b3c4d -Device /dev/sdh
```
+  For API details, see [DetachVolume](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example detaches the specified volume.**  

```
Dismount-EC2Volume -VolumeId vol-12345678
```
**Output:**  

```
AttachTime          : 12/22/2015 1:53:58 AM
DeleteOnTermination : False
Device              : /dev/sdh
InstanceId          : i-1a2b3c4d
State               : detaching
VolumeId            : vol-12345678
```
**Example 2: You can also specify the instance ID and device name to ensure that you are detaching the correct volume.**  

```
Dismount-EC2Volume -VolumeId vol-12345678 -InstanceId i-1a2b3c4d -Device /dev/sdh
```
+  For API details, see [DetachVolume](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.