

# Use `EnableVolumeIo` with a CLI
<a name="example_ec2_EnableVolumeIo_section"></a>

The following code examples show how to use `EnableVolumeIo`.

------
#### [ CLI ]

**AWS CLI**  
**To enable I/O for a volume**  
The following `enable-volume-io` example enables I/O on volume `vol-1234567890abcdef0`.  

```
aws ec2 enable-volume-io \
    --volume-id {{vol-1234567890abcdef0}}
```
This command produces no output.  
For more information, see [Work with an impaired Amazon EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/work_volumes_impaired.html) in the *Amazon EBS User Guide*.  
+  For API details, see [EnableVolumeIo](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-volume-io.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example enables I/O operations for the specified volume, if I/O operations were disabled.**  

```
Enable-EC2VolumeIO -VolumeId vol-12345678
```
+  For API details, see [EnableVolumeIo](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example enables I/O operations for the specified volume, if I/O operations were disabled.**  

```
Enable-EC2VolumeIO -VolumeId vol-12345678
```
+  For API details, see [EnableVolumeIo](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.