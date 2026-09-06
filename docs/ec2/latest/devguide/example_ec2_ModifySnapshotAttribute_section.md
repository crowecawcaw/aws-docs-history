

# Use `ModifySnapshotAttribute` with a CLI
<a name="example_ec2_ModifySnapshotAttribute_section"></a>

The following code examples show how to use `ModifySnapshotAttribute`.

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To modify a snapshot attribute**  
The following `modify-snapshot-attribute` example updates the `createVolumePermission` attribute for the specified snapshot, removing volume permissions for the specified user.  

```
aws ec2 modify-snapshot-attribute \
    --snapshot-id {{snap-1234567890abcdef0}} \
    --attribute {{createVolumePermission}} \
    --operation-type {{remove}} \
    --user-ids {{123456789012}}
```
**Example 2: To make a snapshot public**  
The following `modify-snapshot-attribute` example makes the specified snapshot public.  

```
aws ec2 modify-snapshot-attribute \
    --snapshot-id {{snap-1234567890abcdef0}} \
    --attribute {{createVolumePermission}} \
    --operation-type {{add}} \
    --group-names {{all}}
```
+  For API details, see [ModifySnapshotAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-snapshot-attribute.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example makes the specified snapshot public by setting its CreateVolumePermission attribute.**  

```
Edit-EC2SnapshotAttribute -SnapshotId snap-12345678 -Attribute CreateVolumePermission -OperationType Add -GroupName all
```
+  For API details, see [ModifySnapshotAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example makes the specified snapshot public by setting its CreateVolumePermission attribute.**  

```
Edit-EC2SnapshotAttribute -SnapshotId snap-12345678 -Attribute CreateVolumePermission -OperationType Add -GroupName all
```
+  For API details, see [ModifySnapshotAttribute](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.