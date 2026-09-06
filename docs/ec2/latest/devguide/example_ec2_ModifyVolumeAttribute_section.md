

# Use `ModifyVolumeAttribute` with a CLI
<a name="example_ec2_ModifyVolumeAttribute_section"></a>

The following code examples show how to use `ModifyVolumeAttribute`.

------
#### [ CLI ]

**AWS CLI**  
**To modify a volume attribute**  
This example sets the `autoEnableIo` attribute of the volume with the ID `vol-1234567890abcdef0` to `true`. If the command succeeds, no output is returned.  
Command:  

```
aws ec2 modify-volume-attribute --volume-id {{vol-1234567890abcdef0}} --auto-enable-io
```
+  For API details, see [ModifyVolumeAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-volume-attribute.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example modifies the specified attribute of the specified volume. I/O operations for the volume are automatically resumed after being suspended due to potentially inconsistent data.**  

```
Edit-EC2VolumeAttribute -VolumeId vol-12345678 -AutoEnableIO $true
```
+  For API details, see [ModifyVolumeAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example modifies the specified attribute of the specified volume. I/O operations for the volume are automatically resumed after being suspended due to potentially inconsistent data.**  

```
Edit-EC2VolumeAttribute -VolumeId vol-12345678 -AutoEnableIO $true
```
+  For API details, see [ModifyVolumeAttribute](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.