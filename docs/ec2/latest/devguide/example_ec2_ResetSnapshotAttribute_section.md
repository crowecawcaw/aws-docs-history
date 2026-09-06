

# Use `ResetSnapshotAttribute` with a CLI
<a name="example_ec2_ResetSnapshotAttribute_section"></a>

The following code examples show how to use `ResetSnapshotAttribute`.

------
#### [ CLI ]

**AWS CLI**  
**To reset a snapshot attribute**  
This example resets the create volume permissions for snapshot `snap-1234567890abcdef0`. If the command succeeds, no output is returned.  
Command:  

```
aws ec2 reset-snapshot-attribute --snapshot-id {{snap-1234567890abcdef0}} --attribute {{createVolumePermission}}
```
+  For API details, see [ResetSnapshotAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-snapshot-attribute.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example resets the specified attribute of the specified snapshot.**  

```
Reset-EC2SnapshotAttribute -SnapshotId snap-12345678 -Attribute CreateVolumePermission
```
+  For API details, see [ResetSnapshotAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example resets the specified attribute of the specified snapshot.**  

```
Reset-EC2SnapshotAttribute -SnapshotId snap-12345678 -Attribute CreateVolumePermission
```
+  For API details, see [ResetSnapshotAttribute](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.